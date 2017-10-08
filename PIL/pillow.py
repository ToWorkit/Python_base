# https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014320027235877860c87af5544f25a8deeb55141d60c5000

from PIL import Image

# 打开一个jpg图像文件
im = Image.open('test.jpg')
# 获取图像尺寸
w, h = im.size
print(type(w))
print('width: %s, height: %s' % (w, h))
# 缩放到50%
im.thumbnail((w//2, h//2))
print('resize width: %s, height；%s' % (w//2, h//2))
# 保存缩放图
im.save('test_thumbnail.jpg', 'jpeg')
