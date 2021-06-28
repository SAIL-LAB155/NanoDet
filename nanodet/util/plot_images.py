import cv2

def verify_bbox(meta):
    img = meta['img'].squeeze().numpy().transpose(1,2,0)
    target = meta['gt_bboxes'][0].tolist()[0]
    img = cv2.rectangle(img, (target[0],target[1]), (target[2], target[3]), thickness=1, )
    cv2.imshow('img',img)
    cv2.waitKey(0)