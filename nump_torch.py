import torch
import numpy as np

# tensor与numpy_array转换
np_data = np.arange(6).reshape((2, 3))
torch_data = torch.from_numpy(np_data)
tensor2array = torch_data.numpy()
print(
    '\nnumpy:', np_data,
    '\ntorch_data:', torch_data,
    '\ntensor2array', tensor2array,
    '\n'
)

# abs
data = [-1, - 2, -3]
tensor = torch.Tensor(data)  # 32bit
print(tensor)
print(tensor.abs())
print(tensor.sin())
# 返回一个2维张量，对角线位置全1，其它位置全0
print(torch.eye(3, 2))