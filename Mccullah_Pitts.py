w1=1
w2=1

x1=[0,0,1,1]
x2=[0,1,0,1]
# Assuming theta to vary from -3 to 3 to determine for keep firing

def mccullah(x1,x2,w1,w2,theta,target_outputs):
  cnt=0;
  outputs=[]
  for i in range(4):
    Yin=x1[i]*w1+x2[i]*w2;
    Yhat = 1 if Yin >= theta else 0
    outputs.append(Yhat)
  return outputs == target_outputs



gates = {
    "OR":    [0, 1, 1, 1],
    "AND":   [0, 0, 0, 1],
    "NAND":  [1, 1, 1, 0],
    "NOR":   [1, 0, 0, 0],
    "XOR":   [0, 1, 1, 0],
    "XNOR":  [1, 0, 0, 1]
}

for gate in gates:
  found=False
  for theta in [t * 0.5 for t in range(-100,100)]:
    target_outputs = gates[gate]
    if(mccullah(x1,x2,w1,w2,theta,target_outputs)):
      plot_gate(gate, target_outputs, theta)
      print(gate," ",theta)
      found=True
      break
  if(not found):
    print(gate," Not Found for theta in range")
    




    
#####################################################################################################################################################

import matplotlib.pyplot as plt
import numpy as np

def plot_gate(gate_name, outputs, theta):
    plt.figure()
    for i in range(4):
        color = 'red' if outputs[i] == 1 else 'blue'
        plt.scatter(x1[i], x2[i], c=color, s=100)
    plt.xlabel("x1")
    plt.ylabel("x2")
    plt.title(f"{gate_name} Gate (theta={theta})")
    
    # Plot separating line: x1 + x2 = theta
    x_vals = np.linspace(-0.5, 1.5, 100)
    y_vals = theta - x_vals
    plt.plot(x_vals, y_vals, 'k--')
    plt.grid(True)
    plt.show()




##################################################################################################################################################
w1=-0.1
w2=-0.1

x1=[0,0,1,1]
x2=[0,1,0,1]
# Assuming theta to vary from -3 to 3 to determine for keep firing

def mccullah(x1,x2,w1,w2,theta,target_outputs):
  cnt=0;
  outputs=[]
  for i in range(4):
    Yin=x1[i]*w1+x2[i]*w2;
    Yhat = 1 if Yin >= theta else 0
    outputs.append(Yhat)
  return outputs == target_outputs



gates = {
    "OR":    [0, 1, 1, 1],
    "AND":   [0, 0, 0, 1],
    "NAND":  [1, 1, 1, 0],
    "NOR":   [1, 0, 0, 0],
    "XOR":   [0, 1, 1, 0],
    "XNOR":  [1, 0, 0, 1]
}

for gate in gates:
  found=False
  for theta in [t * 0.5 for t in range(-100,100)]:
    target_outputs = gates[gate]
    if(mccullah(x1,x2,w1,w2,theta,target_outputs)):
      plot_gate(gate, target_outputs, theta)
      print(gate," ",theta)
      found=True
      break
  if(not found):
    print(gate," Not Found for theta in range")
    




    
#####################################################################################################################################################

import matplotlib.pyplot as plt
import numpy as np

def plot_gate(gate_name, outputs, theta):
    plt.figure()
    for i in range(4):
        color = 'red' if outputs[i] == 1 else 'blue'
        plt.scatter(x1[i], x2[i], c=color, s=100)
    plt.xlabel("x1")
    plt.ylabel("x2")
    plt.title(f"{gate_name} Gate (theta={theta})")
    
    # Plot separating line: x1 + x2 = theta
    x_vals = np.linspace(-0.5, 1.5, 100)
    y_vals = theta - x_vals
    plt.plot(x_vals, y_vals, 'k--')
    plt.grid(True)
    plt.show()




