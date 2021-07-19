from gapp import dgp
from numpy import exp
from scipy.special import gamma
X=[6.04,0.86,2.11,9.54,8.58]
Y=[2.29,0.39,-0.56,-3.12,-2.12]
Sigma=[0.28,0.36,0.22,0.19,0.23]
def invgamma(theta,a,b):
    s=theta[0]
    p=b**a/gamma(a)*s**(-1-a)*exp(-b/s)
    return p
g=dgp.DGaussianProcess(X,Y,Sigma,theta=[1,1],prior=invgamma,priorargs=(0.2,1),grad='False')
