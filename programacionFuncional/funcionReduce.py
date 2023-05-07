##funcionReduce


from functools import reduce

l = range(1,3)


resultado = reduce(lambda a,b: a*b,l)


print(resultado)