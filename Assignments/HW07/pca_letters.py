"""
This module is for homework -07 and it prepares images of the english alphabet by cropping the unnecessary images for
Principle component analysis. The program re-samples the images onto a coarser grid so that each image has 16x16 pixels.
The program also creates a 2d-array, and performs PCA on it, resulting in a PCA constructed letter from
n_comp eigen-images.
"""
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from scipy.interpolate import interp2d
from sklearn.decomposition import PCA


def make_let_im(let_file, dim=16, ylo=70, yhi=220, xlo=10, xhi=200, edge_pix=150, plot_let=False):
    """

    :param let_file: file argument
    :param dim: dimension
    :param ylo: keyword argument
    :param yhi: keyword argument
    :param xlo: keyword argument
    :param xhi: keyword argument
    :param edge_pix: edge pixel
    :param plot_let: for plotting
    :return: let_im, let_im_flat for the processed image and cleaned up image
    """
    letter = mpimg.imread(let_file)

    letter = letter[ylo:yhi, xlo:xhi, 0]

    for i in range(letter.shape[1]):
        if letter[0:edge_pix, i].any() == 0:
            letter[0:edge_pix, i] = 1

    plt.imshow(letter, cmap='gray')
    plt.grid('off')
    plt.show()

    x = np.arange(letter.shape[1])
    y = np.arange(letter.shape[0])

    f2d = interp2d(x, y, letter)

    x_new = np.linspace(0, letter.shape[1], dim)
    y_new = np.linspace(0, letter.shape[0], dim)

    letter_new = f2d(x_new, y_new)
    letter_new -= np.mean(letter_new)

    letter_flat = letter_new.flatten()

    if plot_let:
        plt.imshow(letter_new, cmap='gray')
        plt.grid('off')
        plt.show()

    return letter_new, letter_flat


def alphabet_pca(X, n_comp=5):
    """

    :param X: perform PCA on X
    :param n_comp: number of PCA components
    :return: pca, Xproj, pca_comps
    """
    pca = PCA(n_comp)
    Xproj = pca.fit_transform(X)
    pca_comps = pca.components_

    return pca, Xproj, pca_comps


def show_pca_im(Xproj, pca_comps, dim=16, let_idx=0):
    """

    :param Xproj: x projection
    :param pca_comps: PCA components
    :param dim: dimension
    :param let_idx: reconstructed image of a single letter
    :return: NA
    """
    n_comp = pca_comps.shape[0]
    f, axes = plt.subplots(1, n_comp, figsize=(10, 2), subplot_kw=dict(xticks=[], yticks=[]))
    for i in range(n_comp):
        axes[i].imshow(pca_comps[i].reshape((dim, dim)), cmap='binary')

    dig_im = np.zeros((dim, dim))
    coeffs = Xproj[let_idx]
    for i in range(n_comp):
        dig_im += coeffs[i] * pca_comps[i].reshape((dim, dim))

    fig, ax = plt.subplots(1, 1, figsize=(2, 2))
    ax.imshow(dig_im, cmap='binary')
    ax.grid(False)
    ax.axis('off')
    plt.show()


if __name__ == "__main__":
    import doctest
    import argparse

    parser = argparse.ArgumentParser()
    # To read the command line arguments
    parser.add_argument('-let_idx', type=int)
    parser.add_argument('-n_comp', type=int)
    args = parser.parse_args()

    let_idx = args.let_idx
    n_comp = args.n_comp

    i = 0
    X = np.zeros((26, 256))
    while i < 26:
        filename = 'letter' + chr(65 + i) + '.png'
        # data array for all 26 letter
        letter, letter_flat = make_let_im(filename)
        X[i,] = letter_flat
        i += 1

    pca, Xproj, pca_comps = alphabet_pca(X, n_comp=n_comp)
    show_pca_im(Xproj, pca_comps, let_idx=let_idx)

    '''
    name this file with 'python pca_letters_[your Canvas login ID].py'          -5
    '''