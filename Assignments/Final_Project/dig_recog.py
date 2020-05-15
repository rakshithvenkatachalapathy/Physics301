"""
This module is for the final project which calls the programs in the paatern_recog_func.py to train,validate and test
the digits provided
"""
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from pattern_recog_func import interpol_im
from pattern_recog_func import rescale_pixel
from pattern_recog_func import svm_train
from sklearn.datasets import load_digits

# loading the digits
dig_data = load_digits()
# getting the digits data
X = dig_data.data
y = dig_data.target
# using the first 60 images in X to train
md_clf = svm_train(X[0:60], y[0:60])
perc = 0
mis = 0
tot_start = 60
tot_end = 80
# applying md_clf for the next 20 images
for i in range(tot_start, tot_end):
    ans = y[i]
    pre = md_clf.predict(X[i].reshape(1, -1))[0]
    if ans != pre:
        mis += 1
        plt.imshow(X[i].reshape((8, 8)), cmap='binary')
        plt.show()
        print("--------> index, actual digit, svm_prediction: {:d}, {:d}, {:d}".format(i, ans, pre))
    if ans == pre:
        perc += 1.

percentage = (perc / (tot_end - tot_start))
print("Total number of mis-identifications: {:d}".format(mis))
print("Success rate: {:1.2f}".format(percentage))
# Testing the unseen_dig
unseen = mpimg.imread('unseen_dig.png')
unseen_flat = interpol_im(unseen, plot_new_im=True)
# reshaping the image
plt.imshow(X[15].reshape((8, 8)), cmap='binary')
plt.show()

unseen_scaled = rescale_pixel(X, unseen_flat, ind=15)
# predictions for scaled and unscaled images
unseen_pre = md_clf.predict(unseen_flat.reshape(1, -1))
unseen_scaled_pre = md_clf.predict(unseen_scaled.reshape(1, -1))
print("Predictions for unscaled and scaled unseen image: {:d}, {:d}".format(unseen_pre[0], unseen_scaled_pre[0]))
