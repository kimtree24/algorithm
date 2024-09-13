import numpy
def solution(arr1, arr2):
    a = numpy.array(arr1)
    b = numpy.array(arr2)
    ans = a @ b
    return ans.tolist()