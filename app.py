import torch
from torch import nn
import torch.nn.functional as F
from torch.utils.data import Dataset
import torchvision.transforms as transforms
from torchvision.utils import save_image, make_grid
from torch.utils.data import DataLoader
from torch.autograd import Variable

from torchvision.models import vgg19

from ECV_Generator import *
from util import *

from flask import Flask
from flask_cors import CORS


app = Flask(__name__)
CORS(app)



@app.route("/", methods=["GET"])
def predict():
    return __name__

if __name__ == "__main__":
    app.run(debug=True)