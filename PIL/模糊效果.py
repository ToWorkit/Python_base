from PIL import Image, ImageFilter
# 先打开
im = Image.open('test.jpg')
# 模糊滤镜
im2 = im.filter(ImageFilter.BLUR)
im2.save('test_blur.jpg', 'jpeg')
