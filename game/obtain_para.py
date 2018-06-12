#将处理好的图片进行预测，返回一个代表不同表情的数
from model import test_model as t
import PIL.Image as Image
import numpy as np

def number():
    p = []
    for x in range(15):
        image = Image.open("C:\\Users\\huang\\Desktop\\project\\image\\60.jpg")
        image = np.array(image)
        a = t.evaluate(image)
        p.append(a)
    a = np.array(p)
    count = np.bincount(a)
    c = np.argmax(count)
    return c


