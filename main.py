import matplotlib.pyplot as plt
import numpy as np

left = -1
right = 1
step = 0.1

def get_func(x):
    return (x+1) * np.cos(x)

def get_answer():
    return 2*np.sin(1)

def get_integral_by_rectangle(arr_x, step):
    res = 0
    for i in range(1,len(arr_x)):
        res += get_func((arr_x[i-1] + arr_x[i]) / 2) * step
    return res

def get_integral_by_trapeze(arr_x, step):
    res = 0
    for i in range(1,len(arr_x)):
        res += (get_func(arr_x[i-1]) + get_func(arr_x[i])) / 2 * step
    return res

def get_integral_by_simpson(arr_x, step):
    res = 0
    for i in range(1,len(arr_x)):
        res += (get_func(arr_x[i-1]) + 4*get_func((arr_x[i-1]+arr_x[i])/2) + get_func(arr_x[i])) / 6 * step
    return res

err_rect = []
err_trap = []
err_simpson = []
arr_step = np.arange(0.001,0.2,0.001)

for step in arr_step:
    arr_x = np.arange(left,right,step)
    int_rect = get_integral_by_rectangle(arr_x, step)
    int_trap = get_integral_by_trapeze(arr_x, step)
    int_simpson = get_integral_by_simpson(arr_x, step)
    answer = get_answer()
    err_rect.append(np.abs(int_rect - answer))
    err_trap.append(abs(int_trap - answer))
    err_simpson.append(abs(int_simpson - answer))
    plt.plot()
    print(f"------------{step}------------------")
    print(int_rect)
    print(int_trap)
    print(int_simpson)
    print(answer)

plt.plot(arr_step,err_rect,color="r",label="rectangle error")
plt.plot(arr_step, err_trap, color="g", label="trapeze error")
plt.plot(arr_step, err_simpson, color='b', label='simpson error')
plt.legend()
plt.show()