import cv2
import numpy as np

# 读取原图像
img = cv2.imread('game.png', 0)

# # 显示原图像
# cv2.namedWindow('img', 0)
# cv2.resizeWindow('img', 400, 600)
# cv2.imshow('img', img)

# 高斯模糊
img_rgb = cv2.GaussianBlur(img, (5, 5), 0)
canny_img = cv2.Canny(img_rgb, 1, 10)

# 显示边缘检测图像
cv2.namedWindow('canny', 0)
cv2.resizeWindow('canny', 400, 600)
cv2.imshow('canny', canny_img)

# 输出边缘检测图像的高和宽
H, W = canny_img.shape
print(H, W)

y_top = np.nonzero([max(row) for row in canny_img[500:]])[0][0] + 500
x_top = int(np.mean(np.nonzero(canny_img[y_top])))
# 跳过小白圈,然后遍历
y_bottom = y_top + 80
for row in range(y_bottom, H):
    if canny_img[row, x_top] != 0:
        y_bottom = row
        break

# 得到方块的中心点
x_center, y_center = x_top, (y_top + y_bottom) // 2
print(x_center,y_center)

# 绘制以方块中心点为圆心的圆
cv2.circle(canny_img, (x_center, y_center), 33, (255, 0, 255), 2)

# 显示得到的图像
cv2.namedWindow('result', 0)
cv2.resizeWindow('result', 400, 600)
cv2.imshow('result', canny_img)

# 结束
cv2.waitKey(0)
cv2.destroyAllWindows()