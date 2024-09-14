a=int(input('solicitte primer numeros '))
b=int(input('solicitte segundo numeros '))

def multiplicacion(a,b):
    if a== 0:
     return 0
    return b + multiplicacion(a-1,b)

print(multiplicacion (a,b))

  