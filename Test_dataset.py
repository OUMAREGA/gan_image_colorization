import glob
from util import preprocess_img
from PIL import Image
import numpy as np
from torch.utils.data import Dataset

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