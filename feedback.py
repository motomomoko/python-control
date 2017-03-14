import numpy as np
from control import matlab
from matplotlib import pyplot as plt
#from matplotlib import pylab as plt

# PID controller
Kp = 0.5
Ki = 0.01
Kd = 0.01
num = [Kd, Kp, Ki]
den = [1, 0]
K = matlab.tf(num, den)

# control target
Kt = 1
J = 0.01
C = 0.1
num = [Kt]
den = [J, C, 0]
G = matlab.tf(num, den)

# feedback loop
sys = matlab.feedback(K*G, 1)

# step response
t = np.linspace(0, 3, 1000)
yout, T = matlab.step(sys, t)
plt.plot(T, yout)
plt.axhline(1, color="b", linestyle="--")
plt.xlim(0, 3)
plt.show()

# impulse response
yout, T = matlab.impulse(sys, t)
plt.plot(T, yout)
plt.axhline(0, color="b", linestyle="--")
plt.xlim(0, 3)
#plt.show()

# nyquist diagram
matlab.nyquist(sys)
#plt.show()

# bode diagram
matlab.bode(sys)
#plt.show()

# root locus
matlab.rlocus(sys)
#plt.show()

# pole
matlab.pole(sys)
#plt.show()

# margin
matlab.margin(sys)
#plt.show()
