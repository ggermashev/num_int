import matplotlib.pyplot as plt
import numpy as np

left = -1
right = 1

def get_func(x):
    return (x+1) * np.cos(x)

def get_answer():
    return 2.0*np.sin(1)

def get_integral_by_rectangle(arr_x, step):
    res = 0
    for i in range(1,len(arr_x)):
        res += get_func((arr_x[i-1] + arr_x[i]) / 2.0) * step
    return res

def get_integral_by_trapeze(arr_x, step):
    res = 0
    for i in range(1,len(arr_x)):
        res += (get_func(arr_x[i-1]) + get_func(arr_x[i])) / 2.0 * step
    return res

def get_integral_by_simpson(arr_x, step):
    res = 0
    for i in range(1,len(arr_x)):
        res += (get_func(arr_x[i-1]) + 4*get_func((arr_x[i-1]+arr_x[i])/2.0) + get_func(arr_x[i])) / 6.0 * step
    return res


err_rect = []
err_trap = []
err_simpson = []
nodes = 10
nodes_plus = 10
steps = []
for i in range(0, 10):
    nodes += nodes_plus
    step = 2.0 / (nodes - 1)
    steps.append(step)
    arr_x = np.linspace(left, right, nodes)
    int_rect = get_integral_by_rectangle(arr_x, step)
    int_trap = get_integral_by_trapeze(arr_x, step)
    int_simpson = get_integral_by_simpson(arr_x, step)
    answer = get_answer()
    err_rect.append(abs(int_rect - answer))
    err_trap.append(abs(int_trap - answer))
    err_simpson.append(abs(int_simpson - answer))
    plt.plot()
    print(f"------------{step}------------------")
    print(int_rect)
    print(int_trap)
    print(int_simpson)
    print(answer)

plt.loglog(steps, err_rect,color="r",label="rectangle error")
plt.loglog(steps, err_trap, color="g", label="trapeze error")
plt.loglog(steps, err_simpson, color='b', label='simpson error')
plt.xlabel("log(step)")
plt.ylabel("log(error)")
plt.legend()
plt.savefig("error.png")
plt.show()