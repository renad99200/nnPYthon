
import numpy as np

def tanh(x):
    return np.tanh(x)

i1 = 0.05
i2 = 0.10

np.random.seed(42)

w1 = np.random.uniform(-0.5, 0.5)
w2 = np.random.uniform(-0.5, 0.5)
w3 = np.random.uniform(-0.5, 0.5)
w4 = np.random.uniform(-0.5, 0.5)

w5 = np.random.uniform(-0.5, 0.5)
w6 = np.random.uniform(-0.5, 0.5)
w7 = np.random.uniform(-0.5, 0.5)
w8 = np.random.uniform(-0.5, 0.5)

b1 = 0.5
b2 = 0.7

net_h1 = w1*i1 + w2*i2 + b1
net_h2 = w3*i1 + w4*i2 + b1

out_h1 = tanh(net_h1)
out_h2 = tanh(net_h2)

net_o1 = w5*out_h1 + w6*out_h2 + b2
net_o2 = w7*out_h1 + w8*out_h2 + b2

out_o1 = tanh(net_o1)
out_o2 = tanh(net_o2)

print("Output o1:", out_o1)
print("Output o2:", out_o2)
