#coding: utf-8

from PIL import Image

filename = 'lenna.jpeg'

# グレースケール変換
image = Image.open(filename)
gray_image = image.convert('L')
gray_image.save('gray.jpeg')

# サムネイル
image = Image.open(filename)
image.thumbnail((128,128)) # 元の画像が変化する
image.save('thumbnail.jpeg')

# 領域のコピー、回転、貼り付け
box = (10,10,150,150)
image = Image.open(filename)
region = image.crop(box)
region = region.transpose(Image.ROTATE_180)
image.paste(region, box)
image.save("copy_rotate_paste.jpeg")

# 画像のサイズを変更する
image = Image.open(filename)
resized_image = image.resize((128, 128))
resized_image.save("resized.jpeg")

# 回転
image = Image.open(filename)
rotated_image = image.rotate(45)
rotated_image.save("rotated.jpeg")
