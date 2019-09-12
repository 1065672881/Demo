from PIL import Image, ImageFilter, ImageDraw, ImageFont
import random

# 打开一个jpg图像文件
im = Image.open('timg.jpg')
# 获得图像尺寸
x, y = im.size
# 缩放到50%
im.thumbnail((x//2, y//2))
x, y = im.size
print(x, y)
# 将缩放后的图片用jpeg保存
im.save('img.jpg', 'jpeg')

# 其他功能如切片、旋转、滤镜、输出文字、调色板等一应俱全。
# 比如，模糊效果也只需几行代码：
img = Image.open('timg.jpg')
img2 = img.filter(ImageFilter.BLUR)
img2.save('blur.jpg', 'jpeg')

# PIL的ImageDraw提供了一系列绘图方法，让我们可以直接绘图。比如要生成字母验证码图片
# 随机字母


def rndChar():
    return chr(random.randint(65, 90))


# 随机颜色
def rndColor ():
    return random.randint(64, 255), random.randint(64, 255), random.randint(64, 255)


# 随机颜色2
def rndColor2():
    return random.randint(32, 127), random.randint(32, 127), random.randint(32, 127)


width = 60*4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))
# 创建Font对象
font = ImageFont.truetype('C:/Windows/Fonts/Arial.ttf', 36)
# 创建Drow对象
draw = ImageDraw.Draw(image)
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())
# 输出文字
for t in range(4):
    draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())
image = image.filter(ImageFilter.BLUR)
image.save('code.jpg', 'jpeg')

