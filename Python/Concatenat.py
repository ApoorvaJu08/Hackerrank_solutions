import numpy

N, M, P = map(int, input().split())
array_1 = numpy.array([ map(int, input().split()) for i in range(N) ])
array_2 = numpy.array([ map(int, input().split()) for i in range(M) ])

y =  numpy.concatenate((array_1, array_2), axis = 0)
print(y)


