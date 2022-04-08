from  matplotlib import pyplot as plt

def cv2plt_show(img):
    im2 = img[:,:,::-1] 	# transform image to rgb
    plt.imshow(im2)
    plt.show()