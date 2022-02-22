class Pila:
    def __init__(self,tamanio):
        self.lista=[]
        self.tope=0
        self.size = tamanio

    def push_B(self,dato):
        if self.tope < self.size:
            self.lista.append(dato)
            self.tope += 1
        else:
            print("La Pila está Llena")

    def pop_B(self):
        if self.empty_B():
            return "Lista Vacia"
        else:
            top = self.lista[-1]
            self.tope -= 1
            self.lista = self.lista[:-1]
            return top

    def show_B(self):
        if self.empty_B():
            print("Lista vacia")
        else:                    
            for tope in range(self.tope-1,-1,-1):
                print("[{}]".format(self.lista[tope])) 

    def buscar_B(self,buscado):
        try:
            c=self.lista[::-1].index(buscado)
            print(c+1)
        except ValueError as e:
            print("Error: ",e)

    def longitud_B(self):
        return self.tope

    def empty_B(self):
        return self.tope == 0
   
# pila = Pila(3)
# pila.push_B("4")       
# pila.push_B("3")       
# pila.push_B("2")       
# pila.push_B("5")       
# pila.push_B("20")       
# pila.push_B("10")   
# pila.show_B()
# pila.buscar_B("10")    
# print(pila.pop_B())
# print(pila.pop_B())
# print(pila.pop_B())
# print(pila.pop_B())
# print(pila.pop_B())
# print(pila.pop_B())
