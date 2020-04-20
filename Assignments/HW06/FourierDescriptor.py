import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np


def extract_shape(im_file, blowup=1., plot_img=False, plot_contour=False, plot_contour_pts=False):
    im = mpimg.imread(im_file)

    if len(im.shape) > 2:
        im = im[:, :, 0]

    if plot_img:
        plt.figure()
        plt.title('Original Shape')
        plt.imshow(im, cmap=plt.cm.gray)

    x = np.arange(im.shape[1]) * blowup
    y = np.arange(im.shape[0]) * blowup

    y = y[::-1]
    X, Y = np.meshgrid(x, y)

    plt.figure()
    plt.title('Contours')

    CS = plt.contour(X, Y, im, 1)
    if not plot_contour:
        plt.close()
    cs_paths = CS.collections[0].get_paths()
    x_arr = []
    y_arr = []
    for i in range(len(cs_paths)):
        p = cs_paths[i]
        v = p.vertices
        x_arr.append(v[:, 0])
        y_arr.append(v[:, 1])

    if plot_contour_pts:
        plt.figure()
        plt.title("Verify the contour points are correct")
        for i in range(len(x_arr)):
            plt.scatter(x_arr[i], y_arr[i])

    return x_arr, y_arr


def FD(x, y, plot_FD=False, y_lim=None):
    N = len(x)
    n = np.arange(N)
    z = x + y * 1j
    Z = np.fft.fft(z)
    if plot_FD is True:
        plt.figure()
        plt.title('FD real and imag')
        plt.plot(Z.real, 'b-')
        plt.plot(Z.imag, 'g-')
        if y_lim is not None:
            plt.ylim([-y_lim, y_lim])
    return Z


def filt_FD(Z, n_keep, no_zeroth=True):
    N = len(Z)
    n = np.arange(len(Z))
    zeroth = 1
    if no_zeroth:
        zeroth = n > 0
    filt1 = zeroth * (n <= n_keep)
    filt2 = (n > ((N - 1) - n_keep))
    filt = filt1 + filt2
    Z *= filt
    return Z
