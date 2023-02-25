# PROGRAMA INVERTIR ENTEROS DE 3 CIFRAS

print("----------------------------")
print("--------INVERTIR------------")
print("----------------------------")

# INPUT
n= int(input("Digite el valor de n= "))

# PROCESING

X= n%10
Y= n//10%10
Z= n//100
ni= X*100 + Y*10 + Z

# OUTPUT

print("---------------------------------------")
print("-----------NUMERO INVERTIDO------------")
print("---------------------------------------")
print("Numero invertido: " +str(ni))


print("Exitos")