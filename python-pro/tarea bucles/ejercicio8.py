frase = input("Dame una frase: ")
letra = input("Ahora un letra: ")
n = 0 # contador coinciddencias
for i in range(0,len(frase),1):
    letra_concreto = frase[i]
    if letra == letra_concreto:
        n += 1
print(f"{n}")