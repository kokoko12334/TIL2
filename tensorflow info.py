import tensorflow as tf
from tensorflow.python.client import device_lib
device_lib.list_local_devices()
import sys
import tensorflow.keras
import pandas as pd
import sklearn as sk
import tensorflow as tf


###cpu, gpu 목록
device_lib.list_local_devices()

#tensorflow, kera외 기타 버전 정보
print(f"Tensor Flow Version: {tf.__version__}")
print(f"Keras Version: {tensorflow.keras.__version__}")
print()
print(f"Python {sys.version}")
print(f"Pandas {pd.__version__}")
print(f"Scikit-Learn {sk.__version__}")
gpu = len(tf.config.list_physical_devices('GPU'))>0
print("GPU is", "available" if gpu else "NOT AVAILABLE")


##cpu, gpu 정보2
tf.config.list_physical_devices()

tf.test.gpu_device_name()


##gpu 사용 맨 앞에 붙혀 놓으면 됨
import os
os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
os.environ["CUDA_VISIBLE_DEVICES"] = "0"
