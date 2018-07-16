from PIL import Image,ImageFilter,ImageDraw,ImageFont

import random

# 随机字母生成
def rndChar():
    return chr(random.randint(65,90))

# 随机颜色1生成
def rndColor():
    return (random.randint(64,255), random.randint(64,255), random.randint(64,255))

# 随机颜色2生成
def rndColor2():
    return (random.randint(32,127), random.randint(32,127), random.randint(32,127))

width = 60*4
height = 60

image = Image.new('RGB',(width,height),(255,255,255))

# 生成Font对象
font = ImageFont.truetype('C:\Windows\Fonts\Arial.ttf', 36)

# 生成Draw对象
draw = ImageDraw.Draw(image)

# 填充每个元素的颜色
for x in range(width):
    for y in range(height):
        draw.point((x,y),fill=rndColor())

# 输出字母
for t in range(4):
    draw.text((60 * t + 10, 10),rndChar(),font=font,fill=rndColor2())

# 模糊
image = image.filter(ImageFilter.BLUR)
image.save('code2.jpg','jpeg')