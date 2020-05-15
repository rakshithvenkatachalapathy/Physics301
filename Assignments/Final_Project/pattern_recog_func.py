""""
This module is for the final project which consists of Library of Python Functions which are being used in dig_recog.py
for part A of the final project.
"""
from scipy.interpolate import interp2d
from sklearn.decomposition import PCA
from sklearn import preprocessing
from sklearn import svm
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np


def interpol_im(im, dim1=8, dim2=8, plot_new_im=False, cmap='binary', grid_off=False):
    """
    This function interpolate the input image, im, onto a grid that is dim1 ⨉ dim2
    :param im: input image
    :param dim1: dimension
    :param dim2: dimension
    :param plot_new_im: boolean value used for plotting
    :param cmap: cmap - binary
    :param grid_off: used for plotting the grid
    :return: interpolated, flattened image array
    """
    im = im[:, :, 0]
    x = np.arange(im.shape[1])
    y = np.arange(im.shape[0])

    f2d = interp2d(x, y, im)

    x_new = np.linspace(0, im.shape[1], dim1)
    y_new = np.linspace(0, im.shape[0], dim2)
    im_new = -f2d(x_new, y_new)

    im_flat = im_new.flatten()

    if plot_new_im:
        plt.imshow(im_new, cmap=cmap, interpolation='nearest')
        if grid_off:
            plt.grid('off')
        plt.show()

    return im_flat


def pca_svm_pred(imfile, md_pca, md_clf, dim1=45, dim2=60):
    """
    This function loads the image contained in imfile and interpolates the image by calling interpol_im()
    :param imfile: image contained
    :param md_pca: md_pca
    :param md_clf:  md_clf
    :param dim1: dimension
    :param dim2: dimension
    :return: the prediction
    """
    im = mpimg.imread(imfile)
    # interpolates the image
    im_flat = interpol_im(im, dim1=dim1, dim2=dim2, plot_new_im=True)
    # projects the interpolated
    im_flat_proj = md_pca.transform(im_flat.reshape(1, -1))
    # makes a prediction
    pre = md_clf.predict(im_flat_proj.reshape(1, -1))
    # return the prediction
    return pre


def pca_X(X, n_comp=10):
    """
    This function returns md_pca and X_proj
    :param X: data array
    :param n_comp: n_comp
    :return: md_pca and X_proj
    """
    md_pca = PCA(n_components=n_comp, whiten=True)
    X_proj = md_pca.fit_transform(X)
    return md_pca, X_proj


def rescale_pixel(X, unseen, ind=0):
    """
    This function rescales the pixel values of the image unseen
    :param X: data array
    :param unseen: image
    :param ind: index
    :return: rescaled image
    """
    X_train = X[ind]
    min_max_scaler = preprocessing.MinMaxScaler(feature_range=(min(X_train), max(X_train)))
    unseen_scaled = min_max_scaler.fit_transform(X_train.reshape(1, -1), unseen.reshape(1, -1)).astype(int)
    return unseen_scaled


def svm_train(X, y, gamma=0.001, C=100):
    """

    :param X: data array
    :param y: y
    :param gamma: default values
    :param C: default values
    :return: md_clf
    """
    md_clf = svm.SVC(gamma=0.001, C=100.)
    # apply SVM to training data and draw boundaries.
    md_clf.fit(X, y)  # a prediction for the test data point.
    return md_clf
