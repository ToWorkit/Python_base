from PIL import Image
im = Image.open('叫兽.png')
print(im.format, im.size, im.mode)
import sys
# 默认情况下，Python解释器会搜索当前目录、所有已安装的内置模块和第三方模块，搜索路径存放在sys模块的path变量中：
print(sys.path)

# 添加自己的搜索目录
# 第一种  运行时修改，运行结束后失效
import sys
sys.path.append('/Users/hedy/Desktop/Python/模块')
