import shutil
import os

#输入原始图片和标签的地址
img_path = 'test/images/'
label_path = 'test/annotation/'
#输入目的图片和标签的地址
new_img_path = 'test/JGP/'
new_label_path = 'test/anno/'

#保存原始的图片和标签名字（带后缀名）
img_list = os.listdir(img_path)
label_list = os.listdir(label_path)
#保存原始的图片和标签名字（不带后缀名）
img_name = []
label_name = []

#获得不带后缀名的图片名字
for img in img_list:
    a, b = img.split('.')
    img_name.append(a)
#获得不带后缀名的标签名字
for label in label_list:
    a, b = label.split('.')
    label_name.append(a)

i = 0
for img in img_name:
    for label in label_name:
        #找到对应的图片和标签
        if img == label:
            n = 6 - len(str(i))
            #原始地址
            img_src = os.path.join(img_path, img+ '.jpg')
            label_src = os.path.join(label_path, label+ '.xml')
            #目的地址
            img_dst = os.path.join(new_img_path, n*str(0)+str(i)+".jpg")
            label_dst = os.path.join(new_label_path, n*str(0)+str(i)+".xml")
            #改名并保存倒新的地址
            shutil.move(img_src, img_dst)
            shutil.move(label_src, label_dst)
            i = i + 1
