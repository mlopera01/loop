# analiza si un número es o no primo
# un número es primo si es divisible por el mismo y por el 1
valor=0
numero=int(input("Enter your number\n"))
a=int(numero)

for i in range(1,a+1):
 if(a % i==0):
  #para saber cuántas veces ese número fue divisible
  #por cada uno de los numeros que evalua  
  valor=valor+1
# Si ese valor es diferente de dos es porque No es primo
if(valor!=2):
 print(str ("The number ") + str(a) + str(" is not a prime number"))
else:
 print(str ("The number ") + str(a) + str(" is a prime number"))
