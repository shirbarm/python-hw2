# -*- coding: utf-8 -*-
"""hw2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FZeOHbZLqacb-WV-GiR6iz1VzX6pfedm

install torchvision
"""

!pip install torch===1.7.1+cu110 torchvision===0.8.2+cu110 torchaudio===0.7.2 -f https://download.pytorch.org/whl/torch_stable.html

"""Clone & Install from source"""

!git clone https://github.com/PeizeSun/OneNet.git

cd OneNet

!python setup.py build develop

"""Link coco dataset path to OneNet/datasets/coco"""

! mkdir -p datasets/coco/
! ln -s /path_to_coco_dataset/annotations datasets/coco/annotations
! ln -s /path_to_coco_dataset/train2017 datasets/coco/train2017
! ln -s /path_to_coco_dataset/val2017 datasets/coco/val2017

import torch, torchvision
print(torch.__version__, torch.cuda.is_available())

"""Get the images"""

!wget http://images.cocodataset.org/zips/test2017.zip

!unzip test2017

"""Evaluate OneNet"""

!python projects/OneNet/train_net.py --num-gpus 1 \
    --config-file projects/OneNet/configs/onenet.res18.dcn.yaml \
    --eval-only MODEL.WEIGHTS /content/OneNet/configs/onenet_r18dcn.pth

"""Visualize OneNet"""

!python demo/demo.py\
    --config-file projects/OneNet/configs/onenet.res18.dcn.yaml \
    --input /content/OneNet/test2017/000000000057.jpg --output /content/OneNet/output_onenet_r18dcn --confidence-threshold 0.4 \
    --opts MODEL.WEIGHTS /content/OneNet/configs/onenet_r18dcn.pth