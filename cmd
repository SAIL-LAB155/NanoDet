demo.py
video
--model
/media/hkuit164/WD20EJRX/nanodet/workspace/nanodet_m_cocoall_steplr/model_best/model_best.pth
--config
/media/hkuit164/WD20EJRX/nanodet/config/nanodet-coco.yml
--path
/home/hkuit164/Downloads/out.mp4


train.py
../config/test.yml


test.py
--model
/media/hkuit164/WD20EJRX/nanodet/tools/workspace/3456-96/model_last.pth
--config
/media/hkuit164/WD20EJRX/nanodet/config/nanodet-mobilenet-3456-96.yml
--task
val