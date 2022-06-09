import numpy as np
import glob
import shutil

import mimetypes
from werkzeug.utils import secure_filename
from matplotlib import pyplot as plt

import torch
from torch import nn
import torch.nn.functional as F
from torch.utils.data import Dataset
from torch.utils.data import DataLoader
from torch.autograd import Variable

from ECV_Generator import *
from util import *

from flask import Flask, request
from flask_cors import CORS
from flask import send_file

app = Flask(__name__)
CORS(app)

model = color_ecv()
model.load_state_dict(torch.load("model/generator.pth", map_location ='cpu'))
model.eval()


class TestDataset(Dataset):
    def __init__(self, root, single_image):
        if single_image:
            self.files = [root]
        else:
            self.files = sorted(glob.glob(root + "/*.*"))

    def __getitem__(self, index):

        black_path = self.files[index % len(self.files)]
        img_black = np.asarray(Image.open(black_path))
        if (img_black.ndim == 2):
            img_black = np.tile(img_black[:, :, None], 3)
        (tens_l_orig, tens_l_rs) = preprocess_img(img_black, HW=(400, 400))

        return {"black": tens_l_rs.squeeze(0), 'orig': tens_l_orig.squeeze(0), 'path': black_path}

    def __len__(self):
        return len(self.files)

def predict_outputs(model, dataset):
    batch_size = 1
    dataloader = DataLoader(
        dataset,
        batch_size = batch_size,
        shuffle = False,
        num_workers = 0,
    )

    cuda = torch.cuda.is_available()
    if cuda:
        model = model.to('cuda')

    Tensor = torch.cuda.FloatTensor if cuda else torch.Tensor
    outputs = {}
    for i, imgs in enumerate(dataloader):
        imgs_black = Variable(imgs["black"].type(Tensor))
        imgs_black_orig = Variable(imgs["orig"].type(Tensor))
        gen_ab = model(imgs_black)
        gen_ab.detach_
        gen_color = postprocess_tens_new(imgs_black_orig, gen_ab)[0].transpose(1,2,0)
        outputs[imgs["path"][0]] = gen_color
    return outputs

def save_outputs(outputs, folder_path, single_image):
    os.makedirs(folder_path,  exist_ok=True)
    for i in outputs.keys():
        if single_image:
            name = i.split('/')[-1]
        else:
            name = i.split('\\')[-1]
        image = Image.fromarray((outputs[i] * 255).astype(np.uint8))
        image.save(folder_path + '/' + name)

        return name

def run():
    single_image = True
    filename = upload_file()
    path = 'sample/' + filename
    dataset = TestDataset(path, single_image)
    outputs = predict_outputs(model, dataset)
    image_name = save_outputs(outputs, folder_path='outputs', single_image=single_image)

    return image_name

def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file part'

        file = request.files['file']
        if file.filename == '':
            return 'No selected file'

        filename = secure_filename(file.filename)
        file.save(os.path.join('sample', filename))

        return file.filename

@app.route("/api/v1/save_predict", methods=["POST"])
def save_predict():
    files = glob.glob('outputs/*')
    for f in files:
        os.remove(f)
    image_name = run()
    folder = 'outputs/' + image_name
    mime_type = mimetypes.guess_type(folder)[0]

    return send_file('outputs/' + image_name, mimetype=mime_type)
    return 'hello'

@app.route("/api/v1/predict", methods=["GET"])
def predict():
    file = glob.glob("outputs/*")
    if len(file) > 0:
        mime_type = mimetypes.guess_type(file[0])[0]
        return send_file(file[0], mimetype=mime_type)

if __name__ == "__main__":
    app.run(debug=True)