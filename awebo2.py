lista=[]
import csv
encontrado=False   
def menu():
    print("")
    print(".-.-.- M E N U -.-.-.")
    print("")
    print("1.-Agregar producto")
    print("2.-Listar todos los productos")
    print("3.-Eliminar un producto po id")
    print("4.-Generar archivo csv")
    print("5.-Cargar archivo csv")
    print("6.-Estadisticas")
    print("0.-Salir")

def imprimir(lis):
    for x in lista:
        print("id     : ",x[0])
        print("Nombre : ",x[1])
        print("Valor  : ",x[2])
        print("_________")
while True:

    menu()
    op=int(input("Selecione una opcion : "))

    if op==1:
        print("")
        print(".-.-.- Agregar Producto -.-.-.")
        print("")
        di=int(input("Ingrese id del producto : "))
        nom=input("Ingrese nombre del producto : ")
        precio=int(input("Ingrese precio del producto : "))
        producto=[di,nom,precio]
        lista.append(producto)
        print("Producto agregado correctamente")
        print("\n"*4)
        
    elif op==2:
        print("")
        print(".-.-.- Listar todos los productos -.-.-.")
        print("")
        print("")
        imprimir(lista)
    elif op==3:
        print("")
        print(".-.-.- Eliminar por ID -.-.-.")
        print("")
        elim=int(input("Ingrese ID a eliminar : "))
        for lis in lista:
            if lis[0]==elim:
                lista.remove(lis)
                print("eliminado correctamente")
                encontrado=True
        if encontrado==False:
            print("No se a encontrado id...")
    elif op==4:
        print("")
        print(".-.-.- Generar archivo csv -.-.-.")
        print("")
        with open('producto.csv','w',newline="")as producto:
            escritor_csv=csv.writer(producto)
            escritor_csv.writerow(['ID','NOMBRE','PRECIO'])
            escritor_csv.writerows(lista)
            print("Archivo Generado correctamente")
    elif op==5:
        print("")
        print(".-.-.- Cargar archivo csv -.-.-.")
        print("")
        with open('producto.csv','r',newline='') as producto:
            lector_csv=csv.reader(producto)
            for lis in lector_csv:
                print(lis)
    elif op==6:
        print("")
    elif op==0:
        print("")
    else:
        print("")
