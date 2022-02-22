from menu import Menu
from lista import Lista
from pila import Pila
from cola import Cola
import os

a1 = Lista()
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
                a1.push_A(di)
                input("Presione una tecla para continuar")
            elif opc_1 == "2":
                a1.pop_A()
                input("Se eliminó un dato de la lista, presione cualquier tecla para continuar")
            elif opc_1 == "3":
                print("*"*10,"Mostrando la lista","*"*10)
                a1.show_A()
                input("Presione cualquier tecla para continuar")
            elif opc_1 == "4":
                pos1 = int(input("Ingrese la posición del dato a eliminar: "))
                print(a1.eliminarElemento_A(pos1))
                input("Pulse cualquier tecla para continuar")
            elif opc_1 ==  "5":
                pos2 = int(input("Ingrese la posición del dato a ingresar: "))
                dat = input("Dato a ingresar: ")
                print(a1.insertarElemento_A(pos2-1,dat))
                input("Pulse cualquier tecla para continuar")
            elif opc_1 == "6":
                bus = input("Ingrese el dato a buscar: ")
                a1.buscar_A(bus)
                input("Pulse cualquier tecla para continuar")
            elif opc_1 == "7":
                    break
    elif opcion_1 == "2":
        opc_1 = ""
        os.system("cls")
        b2 = int(input("Ingrese el tope máximo de la Pila: "))
        b1 = Pila(b2)
        os.system("cls")
        while True:
            os.system("cls")
            opc_1 = Menu.menu_principal("",["1. Push", "2. Pop", "3. Show","4. Buscar","5. Longitud","6. Salir"],"Menu pila")
            os.system("cls")
            if opc_1 == "1":
                di2 = input("Dato a ingresar: ")
                b1.push_B(di2)
                #print(Pila.lista)
                input("Presione una tecla para continuar")
            elif opc_1 == "2":
                #b4 = Pila(5)
                b1.pop_B()
                #print(Pila.pila)
                input("Se eliminó un dato de la lista, presione cualquier tecla para continuar")
            elif opc_1 == "3":
                print("*"*10,"Mostrando la lista","*"*10)
                b1.show_B()
                input("Presione cualquier tecla para continuar")
            elif opc_1 == "4":
                bus1 = input("Ingrese el dato a buscar: ")
                b1.buscar_B(bus1)
                input("Pulse cualquier tecla para continuar")
            elif opc_1 ==  "5":
                b1.longitud_B()
            elif opc_1 == "6":
                break
    elif opcion_1 == "3":
        opc_1 = ""
        os.system("cls")
        c2 = int(input("Ingrese el tope máximo de la Cola: "))
        c1 = Cola(c2)
        os.system("cls")
        while True:
            os.system("cls")
            opc_1 = Menu.menu_principal("",["1. Push", "2. Pop", "3. Show","4. Buscar","5. Longitud","6. Salir"],"Menu pila")
            os.system("cls")
            if opc_1 == "1":
                di3 = input("Dato a ingresar: ")
                c1.push_C(di3)
                #print(Pila.lista)
                input("Presione una tecla para continuar")
            elif opc_1 == "2":
                #b4 = Pila(5)
                c1.pop_C()
                #print(Pila.pila)
                input("Se eliminó un dato de la lista, presione cualquier tecla para continuar")
            elif opc_1 == "3":
                print("*"*10,"Mostrando la lista","*"*10)
                c1.show_C()
                input("Presione cualquier tecla para continuar")
            elif opc_1 == "4":
                bus2 = input("Ingrese el dato a buscar: ")
                c1.buscar_C(bus2)
                input("Pulse cualquier tecla para continuar")
            elif opc_1 ==  "5":
                c1.longitud_C()
            elif opc_1 == "6":
                break
    elif opcion_1 == "2":
        break
os.system("cls")