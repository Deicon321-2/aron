lista_numeros=[]
i=0
print("iniciando programa...")
for i in range (10):
    numero=int(input(f"Ingrese un numero para la lista numero N°{i+1} \n"))
    lista_numeros.append(numero)
while True:
    print("""
MENU PRINCIPAL
1-Ordenar menor a mayor
2-Ordenar mayor a menor
3-Salir""")
    op=int(input("Ingrese su opcion \n"))
    match op:
        case 1:
            print("1")
            input()
        case 2:
            lista_numeros.sort(reverse=True)
            print()
            print(lista_numeros)
            print("Lista Ordenada de mayor a menor")
            input()
        case 3:
            print("3")
            break
        
