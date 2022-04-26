import numpy as np

def calculate(list):

    if len(list)!=9:
        raise ValueError("List must contain nine numbers.")

    ls=np.array(list)
    print(ls)

    mean_axis1=[ls[[0,3,6]].mean(), ls[[1,4,7]].mean(), ls[[2,5,8]].mean()]
    mean_axis2=[ls[[0,1,2]].mean(), ls[[3,4,5]].mean(), ls[[6,7,8]].mean()]
    mean_flattened=ls.mean()

    var_axis1=[ls[[0,3,6]].var(), ls[[1,4,7]].var(), ls[[2,5,8]].var()]
    var_axis2=[ls[[0,1,2]].var(), ls[[3,4,5]].var(), ls[[6,7,8]].var()]
    var_flattened=ls.var()

    std_axis1=[ls[[0,3,6]].std(), ls[[1,4,7]].std(), ls[[2,5,8]].std()]
    std_axis2=[ls[[0,1,2]].std(), ls[[3,4,5]].std(), ls[[6,7,8]].std()]
    std_flattened=ls.std()

    max_axis1=[ls[[0,3,6]].max(), ls[[1,4,7]].max(), ls[[2,5,8]].max()]
    max_axis2=[ls[[0,1,2]].max(), ls[[3,4,5]].max(), ls[[6,7,8]].max()]
    max_flattened=ls.max()

    min_axis1=[ls[[0,3,6]].min(), ls[[1,4,7]].min(), ls[[2,5,8]].min()]
    min_axis2=[ls[[0,1,2]].min(), ls[[3,4,5]].min(), ls[[6,7,8]].min()]
    min_flattened=ls.min()

    sum_axis1=[ls[[0,3,6]].sum(), ls[[1,4,7]].sum(), ls[[2,5,8]].sum()]
    sum_axis2=[ls[[0,1,2]].sum(), ls[[3,4,5]].sum(), ls[[6,7,8]].sum()]
    sum_flattened=ls.sum()
    

    calculations = {
      'mean': [mean_axis1, mean_axis2, mean_flattened],
        'variance': [var_axis1, var_axis2, var_flattened],
        'standard deviation': [std_axis1, std_axis2, std_flattened],
        'max': [max_axis1, max_axis2, max_flattened],
        'min': [min_axis1, min_axis2, min_flattened],
        'sum': [sum_axis1, sum_axis2, sum_flattened]
    }

  
    return calculations