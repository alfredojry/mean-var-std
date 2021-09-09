import numpy as np

def calculate(lst):
    if len(lst) < 9:
        raise ValueError('List must contain nine numbers.')
    lst_2d = [[] for i in range(3)]
    for i in range(9):
        lst_2d[i // 3].append(lst[i])
    arr = np.array(lst_2d)
    # mean
    mean_axis1 = np.mean(arr, axis=0)
    mean_axis2 = np.mean(arr, axis=1)
    mean_flattened = np.mean(arr)
    mean = [mean_axis1.tolist(), mean_axis2.tolist(), mean_flattened]
    # variance
    var_axis1 = np.var(arr, axis=0)
    var_axis2 = np.var(arr, axis=1)
    var_flattened = np.var(arr)
    variance = [var_axis1.tolist(), var_axis2.tolist(), var_flattened]
    # standard desviation
    std_axis1 = np.std(arr, axis=0)
    std_axis2 = np.std(arr, axis=1)
    std_flattened = np.std(arr)
    std = [std_axis1.tolist(), std_axis2.tolist(), std_flattened]
    # max
    max_axis1 = np.amax(arr, axis=0)
    max_axis2 = np.amax(arr, axis=1)
    max_flattened = np.amax(arr)
    amax = [max_axis1.tolist(), max_axis2.tolist(), max_flattened]
    # min
    min_axis1 = np.amin(arr, axis=0)
    min_axis2 = np.amin(arr, axis=1)
    min_flattened = np.amin(arr)
    amin = [min_axis1.tolist(), min_axis2.tolist(), min_flattened]
    # sum
    sum_axis1 = np.sum(arr, axis=0)
    sum_axis2 = np.sum(arr, axis=1)
    sum_flattened = np.sum(arr)
    asum = [sum_axis1.tolist(), sum_axis2.tolist(), sum_flattened]
    # resume
    calculations = {
            'mean': mean,
            'variance': variance,
            'standard deviation': std,
            'max': amax,
            'min': amin,
            'sum': asum,
        }
    return calculations

