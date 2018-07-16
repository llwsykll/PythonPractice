from PIL import Image,ImageFilter

im = Image.open('C:\\Users\chengyangli\Pictures\\1.png')

w,h = im.size

# 缩小图片
print('Original image size: %sx%s' % (w, h))
im.thumbnail((w//2,h//2))
print('Resize image to: %sx%s' % (w//2, h//2))
# 把缩放后的图像用jpeg格式保存:
# im.save('thumbnail.jpg', 'jpeg')

# 模糊图片
im2 = im.filter(ImageFilter.BLUR)
# im2.save('blur.jpg','jpeg')

