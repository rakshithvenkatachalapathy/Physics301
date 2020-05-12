import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from pattern_recog_func import interpol_im
from pattern_recog_func import pca_X
from pattern_recog_func import rescale_pixel
from pattern_recog_func import svm_train
from pattern_recog_func import pca_svm_pred
from pdb import set_trace
from scipy.interpolate import interp2d
from skimage import transform, data, io
from sklearn.decomposition import PCA
from sklearn.svm import SVC
from sklearn.datasets import load_digits
from sklearn import preprocessing
from sklearn import svm


bohr = 10
ein = 11
flat_bohr = []
flat_ein = []
y = []
phys_dict = {0: 'Bohr', 1: 'Einstein'}