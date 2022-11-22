#pip install pillow 处理图片的工具
from PIL import Image
#打开文件
im = Image.open('./07合成女神图片/img_file/闭眼美女桌面壁纸.jpg')
#print(im.size)
w,h = im.size

img_row = 4
img_column = 4

import os #python 自带工具，专门处理文件
# for n in os.listdir('./07合成女神图片/img_file'):
#     print(n)
#储存所有的名字
names = os.listdir('./07合成女神图片/img_file')

#新的画布,RGB红色
new_img = Image.new('RGB',(img_column*w,img_row*h))

for y in range(img_row):#y=0,1,2,3
    for x in range(img_column):#x=0,1,2,3
        #打开要合成的图片
        o_img = Image.open('./07合成女神图片/img_file/'+names[img_column*y+x])
        new_img.paste(o_img,(x*w,y*h))
new_img.save('./07合成女神图片/img_file/new_img111.jpg')
