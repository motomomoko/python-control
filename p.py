from control.matlab import *
from matplotlib import pyplot as plt
import numpy as np

def main():
# PID parameter
    Kp = 0.6  # proportionality
    Ki = 0.03 # integration
    Kd = 0.03 # differential
    num = [Kd, Kp, Ki]
    den = [1, 0]
    K = tf(num, den)
    # control target
    Kt = 1
    J = 0.01
    C = 0.1
    num = [Kt]
    den = [J, C, 0]
    G = tf(num, den)
    # feedback loop
    sys = feedback(K*G, 1)
    t = np.linspace(0, 3, 1000)
    y, T = step(sys, t)
    plt.plot(T, y)
    plt.grid()
    plt.axhline(1, color="b", linestyle="--")
    plt.xlim(0, 3)
												  
if __name__ == "__main__":
    main()
