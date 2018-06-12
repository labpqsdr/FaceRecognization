import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
def process():
    img = tf.gfile.GFile('C:\\Users\\huang\\Desktop\\project\\image\\0.jpg', 'rb').read()
    with tf.Session() as sess:
        img_data = tf.image.decode_jpeg(img)
        #将图像编码转化为实数形式#
        resized = tf.image.resize_images(img_data, [48, 48], method=1)
        #将图像转化为灰度图像
        image_data = sess.run(tf.image.rgb_to_grayscale(resized))
        #将处理过的图像进行解码
        encoded_image = tf.image.encode_jpeg(image_data)
        #将处理好的图像进行保存
        with tf.gfile.GFile("C:\\Users\\huang\\Desktop\\project\\image\\60.jpg", "wb") as f:
            f.write(encoded_image.eval())








