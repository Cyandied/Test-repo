import matplotlib.pyplot as plt
import numpy as np

New = np.arange(1,9,0.01)
def func(x:list[float]) -> np.ndarray:
    return np.sin(x)



fig, (ax1,ax2) = plt.subplots(2,1)
ax1.scatter(New,func(New), label = "Hello world")
ax2.plot(New,New, label = "nr 2")

plt.legend()
plt.show();