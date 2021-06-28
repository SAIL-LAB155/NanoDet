
import torch
import cv2
import numpy as np
img_path = 'person.jpg'
img = cv2.imread(img_path)
img = cv2.resize(img,(416,416))
# img =torch.randn(1, 3, 416, 416, device="cpu")
ONNX = True
if ONNX:
    import onnxruntime as ort
    # img = img.numpy()
    img = img[np.newaxis, :].transpose(0, 3, 1, 2).astype(np.float32)
    ort_session = ort.InferenceSession('/media/hkuit164/TOSHIBA/nanodet/tools/nano_1cls_sim.onnx')
    boxes = ort_session.run(["817"], {'input.1': img})
    print(boxes)
    # boxes = boxes * 416
    # pred_onnx = torch.cat((torch.from_numpy(boxes), torch.from_numpy(obj), torch.ones([obj.shape[0], 1])), 1)
    # pred_onnx = pred_onnx[np.newaxis, :]
