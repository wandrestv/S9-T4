from menu import Menu
from lista import Lista
from pila import Pila
from cola import Cola
import os

menu_m = Menu()
list_men = ["1. Lista","2. Pila", "3. Cola", "4. Salir"]
opcion_1 = ""
while True:
    os.system("cls")
    opcion_1 = menu_m.menu_principal(list_men,"Menu Principal")
    if opcion_1 == "1":
        opc_1 = ""
        while True:
            os.system("cls")
            opc_1 = Menu.menu_principal("",["1. Push", "2. Pop", "3. Show","4. Eliminar","5. Insertar","6. Buscar","7. Salir"],"Menu lista")
            os.system("cls")
            if opc_1 == "1":
                di = input("Dato a ingresar: ")
                a1 = Lista()
                a1.push_A(di)
                print(Lista.lista)
                input("Presione una tecla para continuar")
            elif opc_1 == "2":
                a4 = Lista()
                a4.pop_A()
                print(Lista.lista)
                input("Se eliminó un dato de la lista, presione cualquier tecla para continuar")
            elif opc_1 == "3":
                print("*"*10,"Mostrando la lista","*"*10)
                a3 = Lista()
                a3.show_A()
                input("Presione cualquier tecla para continuar")
            elif opc_1 == "4":
                pos1 = int(input("Ingrese la posición del dato a eliminar: "))
                a5 = Lista()
                print(a5.eliminarElemento_A(pos1))
                input("Pulse cualquier tecla para continuar")
            elif opc_1 ==  "5":
                pos2 = int(input("Ingrese la posición del dato a ingresar: "))
                dat = input("Dato a ingresar: ")
                a6 = Lista()
                a6.insertarElemento_A(pos2-1,dat)
                print(Lista.lista)
                input("Pulse cualquier tecla para continuar")
            elif opc_1 == "6":
                bus = input("Ingrese el dato a buscar: ")
                a7 = Lista()
                a7.buscar(bus)
                input("Pulse cualquier tecla para continuar")
            elif opc_1 == "7":
                    break
    elif opcion_1 == "2":
        opc_1 = ""
        while True:
            os.system("cls")
            opc_1 = Menu.menu_principal("",["1. Push", "2. Pop", "3. Show","4. Buscar","5. Longitud","6. Salir"],"Menu pila")
            os.system("cls")
            if opc_1 == "1":
                di2 = input("Dato a ingresar: ")
                b1 = Pila(5)
                b1.push_B(di2)
                #print(Pila.lista)
                input("Presione una tecla para continuar")
            elif opc_1 == "2":
                b4 = Pila(5)
                b4.pop_B()
                #print(Pila.pila)
                input("Se eliminó un dato de la lista, presione cualquier tecla para continuar")
            elif opc_1 == "3":
                print("*"*10,"Mostrando la lista","*"*10)
                b3 = Pila(5)
                b3.show_B()
                input("Presione cualquier tecla para continuar")
            elif opc_1 == "4":
                pass
            elif opc_1 ==  "5":
                pass
            elif opc_1 == "6":
                bus = input("Ingrese el dato a buscar: ")
                a7 = Lista()
                a7.buscar(bus)
                input("Pulse cualquier tecla para continuar")
            elif opc_1 == "7":
                    break
        