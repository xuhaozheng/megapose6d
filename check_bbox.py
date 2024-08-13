# Third Party
import cv2

# img_path = '/home/deeplearner/Documents/haozheng_hdd/megapose6d/local_data/examples/barbecue-sauce/image_rgb.png'
img_path = '/home/deeplearner/Documents/haozheng_hdd/megapose6d/local_data/examples/tool_only_data/lnd1/rgb/000114.png'
img = cv2.imread(img_path)

cv2.imshow('test',img)
cv2.waitKey(0)