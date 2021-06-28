import os
cmds = [
    'python train.py ../config/nanodet-mobilenet-56-160.yml',
    # # 'python train.py ../config/nanodet-mobilenet-56-1280.yml',
    # 'python train.py ../config/nanodet-mobilenet-456-96.yml',
    # 'python train.py ../config/nanodet-mobilenet-456-160.yml',
    # 'python train.py ../config/nanodet-mobilenet-456-1280.yml',
    # 'python train.py ../config/nanodet-mobilenet-3456-96.yml',
    # 'python train.py ../config/nanodet-mobilenet-3456-160.yml',
    # 'python train.py ../config/nanodet-mobilenet-3456-1280.yml',
    # 'python train.py ../config/nanodet-mobilenet-256-1280.yml',
    # 'python train.py ../config/nanodet-mobilenet-356-1280.yml',
]
for cmd in cmds:
    os.system(cmd)