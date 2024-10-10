palabra = input("Dame una palabra: ")
for i in range(0,len(palabra),1):
    print(f"{palabra[len(palabra) - (i+1)]}")