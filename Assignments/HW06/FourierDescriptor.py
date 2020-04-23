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
    #
    # CS = plt.contour(X, Y, im, 1)
    # if not plot_contour:
    #     plt.close()
    # cs_paths = CS.collections[0].get_paths()

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
    # z = x + y * 1j
    z = x + 1j * y
    # z *= np.exp(1j * np.pi / 2.) 
    z *= np.exp(1j * np.pi / 2)  # To plot the image horizontally

    Z = np.fft.fft(z)

    d_complex = np.gradient(z)
    d = np.abs(d_complex).mean()
    k = np.fft.fftfreq(len(z), d=d)
    k_lo = np.abs(k[np.argsort(np.abs(k))][1])

    if plot_FD is True:
        plt.figure()
        plt.title('FD real and imag')
        plt.plot(Z.real, 'b-')
        plt.plot(Z.imag, 'g-')
        if y_lim is not None:
            plt.ylim([-y_lim, y_lim])
    return Z, k, k_lo
    # Z, k , k_low


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
    return Z, n_keep * filt


def get_FD_abs(x, y, order=10, norm=True, no_zeroth=True):
    x_reco = []
    y_reco = []
    fd_magn = []
    for i in range(len(x)):
        Z, k, k_lo = FD(x[i], y[i])
        Z_filt, k_filt = filt_FD(Z, order, no_zeroth)
        if norm:
            Z_filt = size_norm(Z_filt)
        x_rec, y_rec = recover_shape(Z_filt)
        tmp_mag = []
        for i in Z_filt:
            if i != 0:
                tmp_mag.append(i)  # k_kept
        fd_mag = np.abs(tmp_mag)
        x_reco.append(x_rec)
        y_reco.append(y_rec)
        fd_magn.append(fd_mag)

    k_kept = k[Z_filt != 0]
    return fd_magn, k_kept, x_reco, y_reco


def recover_shape(Z):
    z_rec = np.fft.ifft(Z)
    x_rec = z_rec.real
    y_rec = z_rec.imag
    return x_rec, y_rec


def size_norm(Z):
    return Z / np.sqrt(np.abs(Z[1]) * np.abs(Z[-1]))


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('-order', type=int)
    parser.add_argument('--no-norm', dest='norm', action='store_false')
    parser.add_argument('-zeroth', dest='no_zeroth', action='store_false')
    parser.set_defaults(no_zeroth=True, norm=True)
    args = parser.parse_args()

    order = args.order
    norm = args.norm
    no_zeroth = args.no_zeroth

    x1, y1 = extract_shape('number1.png')
    x2, y2 = extract_shape('number2.png')
    x6, y6 = extract_shape('number6.png')

    fd1_mag, k_kept1, x1_rec, y1_rec = get_FD_abs(x1, y1, order, norm, no_zeroth)
    fd2_mag, k_kept2, x2_rec, y2_rec = get_FD_abs(x2, y2, order, norm, no_zeroth)
    fd6_mag, k_kept6, x6_rec, y6_rec = get_FD_abs(x6, y6, order, norm, no_zeroth)

    plt.figure()
    plt.title("Numbers Recovered From FD's")
    for i in range(len(x1_rec)):
        plt.plot(x1_rec[i], y1_rec[i], 'b')
    for i in range(len(x2_rec)):
        plt.plot(x2_rec[i], y2_rec[i], 'g')
    for i in range(len(x6_rec)):
        plt.plot(x6_rec[i], y6_rec[i], 'r')
    plt.savefig('rec_numbers126.pdf')
    plt.show()

    plt.figure()
    plt.title("Magnitudes of FD's for 1, 2, and 6")

    for i in range(len(fd1_mag)):
        plt.plot(k_kept1, fd1_mag[i], 'bo')
    for i in range(len(fd2_mag)):
        plt.plot(k_kept2, fd2_mag[i], 'gx')
    for i in range(len(fd6_mag)):
        plt.plot(k_kept6, fd6_mag[i], 'r^')
    plt.savefig('FourierDescriptor_numbers126.pdf')
    plt.show()
    # FT
    # frequencies
    # index
