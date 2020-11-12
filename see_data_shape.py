import cv2

# 修改为你的图片地址
img_path = ' 修改为你的图片地址 '
img = cv2.imread(img_path)
size = img.shape
print(size)
print('width：',size[1])
print('height：',size[0])
