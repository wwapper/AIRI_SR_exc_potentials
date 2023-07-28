# -*- coding: utf-8 -*-
#!/usr/bin/env python
import numpy as np
from pyscf import gto, dft
from pyscf.dft import numint
import math
import torch 
from torch.autograd import Variable 
import torch.nn as nn 
import torch.nn.functional as F 
import pandas as pd



# definition of target molecule #

mol = gto.M(
    atom = '''
    O  0.   0.       0.
    H  0.   -0.757   0.587
    H  0.   0.757    0.587 ''',
    basis = '6-31G')

mf_orig = dft.RKS(mol)

mf_orig.kernel()

dm = mf_orig.make_rdm1()

coords = mf_orig.grids.coords
weights = mf_orig.grids.weights
ao_value = numint.eval_ao(mol, coords, deriv=0)

rho = numint.eval_rho(mol, ao_value, dm, xctype='LDA')



# definition of NN structure #
hidden=100
print("hidden nodes= "+str(hidden))

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(2, hidden)
        self.fc2 = nn.Linear(hidden, hidden)
        self.fc3 = nn.Linear(hidden, hidden)
        self.fc4 = nn.Linear(hidden, 1)


    def forward(self, x):
        t=torch.empty((x.shape[0],2))
        unif=(x[:,1]+x[:,0]+1e-7)**(1.0/3)
        t[:,0]=unif
        t[:,1]=((1+torch.div((x[:,0]-x[:,1]),(x[:,1]+x[:,0]+1e-7)))**(4.0/3)+(1-torch.div((x[:,0]-x[:,1]),(x[:,1]+x[:,0]+1e-7)))**(4.0/3))*0.5

        #print(t)
        logt=torch.log(t)#/scale.float()
        g1=F.elu(self.fc1(logt))
        g2=F.elu(self.fc2(g1))
        g3=F.elu(self.fc3(g2))
        #g4=F.elu(self.fc4(g3))
        eunif=(x[:,1]+x[:,0]).view(-1,1)**(1.0/3)
        spinscale=(((1+torch.div((x[:,0]-x[:,1]),(x[:,1]+x[:,0]+1e-7)))**(4.0/3)+(1-torch.div((x[:,0]-x[:,1]),(x[:,1]+x[:,0]+1e-7)))**(4.0/3))*0.5).view(-1,1)
        g4=-(F.elu(self.fc4(g3))+1)*eunif*spinscale
        return g4


#loading NN weights
model = Net()
model.load_state_dict(torch.load("NNLSDA",map_location='cpu'))

# definition of functional #

def eval_xc(xc_code, rho, spin, relativity=0, deriv=2, verbose=None):
    if spin!=0:
        rho01=rho[0]
        rho02=rho[1]
        
    else:
        rho01=rho02=rho*0.5

    rho0=np.concatenate((rho01.reshape((-1,1)),rho02.reshape((-1,1))),axis=1)
    N=rho0.shape[0]
    x=Variable(torch.Tensor(rho0),requires_grad=True)
#    pred_exc = 0.0027368415157811958 - 0.73869995621059249 * torch.pow(x, 1/3) #lda_x
#    pred_exc = - 0.0172 * torch.log(16.071131702086299 * torch.pow((- x - 0.54987870353745425), 2) - 0.08020000000000001) - 0.00463 #lda_c_chachiyo
    pred_exc=model(x) #NN
    exc=pred_exc.data[:,0].numpy()
    eneden=torch.dot(pred_exc[:,0],x[:,0]+x[:,1])
    eneden.backward()
    grad=x.grad.data.numpy()

    if spin!=0:
        vrho=np.hstack((grad[:,0].reshape((-1,1)),grad[:,1].reshape((-1,1))))

    else:
        vlapl=np.zeros(N)    
        vrho=(grad[:,0]+grad[:,1])/2
    vxc=(vrho, None, None, None)
    return exc, vxc, None, None


print('Массив значений электронной плотности (в электронах на кубический бор) - значения x_0')
print(rho)
print('Длина соответствующего массива')
print(len(rho))
print()
print('Массив значений плотности энергии - значения y')
print(eval_xc(xc_code='', rho=rho, spin=0)[0])
print('Длина соответствующего массива')
print(len(eval_xc(xc_code='', rho=rho, spin=0)[0]))

pd.DataFrame({'x_0': rho, 'y': eval_xc(xc_code='', rho=rho, spin=0)[0]}).to_csv('/content/NN_functional.csv', index=False)
