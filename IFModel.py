import numpy as np
import matplotlib.pyplot as plt

E = -65  # membrane potential
th = -50  # threshold
act = 20  # aciton potential
ref = 30  # refractory period
rest = 0  # rest of refractory period time
last = 0  # final refractory period finish time
tau = 15  # time constant


## calculate membrane potential
def v(weight, spikes, time):
    currents = []
    for sp in spikes:
        currents.append(current(sp, time))
    m = np.dot(weight, currents) + E
    global rest, last
    if rest > 0:  # won't accept input while refractory period
        rest -= 10
        if rest <= 0:
            last = time
        return E
    if m > th:  # generate spike
        m = act
        rest = ref
    return m


## spike response
def kernel(time):
    return time * np.exp(-time / tau)


## input current
def current(spikes, time):
    sum = 0
    for spike in spikes:
        if spike > time:
            break
        if spike > last:
            sum += kernel(time - spike)
    return sum


spike1 = np.array(np.arange(100, 1000, 300))
spike2 = np.array(np.arange(50, 1000, 200))
spike3 = np.array(np.arange(50, 1000, 100))
spike4 = np.array(np.arange(100, 1000, 150))
spikes = np.array([spike1, spike2, spike3, spike4])

weights = np.array([0.7, 1.2, 0.9, 0.8])
memV = []
for t in range(0, 1000):
    memV.append(v(weights, spikes, t))
plt.plot(memV)
plt.show()
