class Menu:
    def __init__(self):
        pass

    def menu_principal(self,opciones_A,titulo_A):
        print("*"*10,titulo_A,"*"*10)
        for opcion_A in opciones_A:
            print(opcion_A)
        print("*"*10,"*"*(len(titulo_A)),"*"*10)
        opc_A = input("Elija una de las opciones[1 - {}]: ".format(len(opciones_A)))
        return opc_A
