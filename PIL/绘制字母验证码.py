from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

# 随机字母
def rndChar():
  return chr(random.randint(65, 90))
# 随机颜色_1
def rndColor():
  return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))
# 随机颜色_2
def rndColor_2():
  return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

# 绘制尺寸
width = 60*4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))
# 创建Font对象
font = ImageFont.truetype('Arial.ttf', 36)
# 创建Draw对象
draw = ImageDraw.Draw(image)
# 填充每个像素
for x in range(width):
  for y in range(height):
    draw.point((x, y), fill = rndColor())
# 文字
for t in range(4):
  draw.text((60 * t + 10, 10), rndChar(), font = font, fill = rndColor_2())
# 模糊处理
image = image.filter(ImageFilter.BLUR)
image.save('code.png', 'png')
