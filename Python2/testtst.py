from random import shuffle
try:
    list_ord = list(range(10))
    print ("Lista de ordenada : " + str(list_ord))
    shuffle(list_ord)
    print ("A mesma lista desordenada : " +  str(list_ord))
except:
   print('Operação inválida')