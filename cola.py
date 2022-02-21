class Cola:                
    def __init__(self,tamanio):
        self.lista=[]
        self.tope=0
        self.size=tamanio

    def push_C(self,dato):
        if self.tope < self.size:
            self.lista += [dato]
            self.tope += 1
        else:
            print("La Cola está Llena")

    def pop_C(self):
        if self.empty_C():
            return "Lista Vacia"
        else:
            top = self.lista
            self.tope -= 1
            self.lista = self.lista[1:]
            return top

    def show_C(self):
        if self.empty_C():
            print("Lista vacia")
        else:                    
            for tope in range(0,self.tope):
                print("[{}]".format(self.lista[tope])) 

    def buscar_C(self,buscado):
        try:
            c=self.lista.index(buscado)
            print(c+1)
        except ValueError as e:
            print("Error: ",e)

    def longitud_C(self):
        return self.tope

    def empty_C(self):
        return self.tope == 0
   
pila = Cola(3)
pila.push_C("4")       
pila.push_C("3")       
pila.push_C("2")       
pila.push_C("5")       
pila.push_C("20")       
pila.push_C("10")   
pila.show_C()
pila.buscar_C("10")    
print(pila.pop_C())
print(pila.pop_C())
print(pila.pop_C())
print(pila.pop_C())
print(pila.pop_C())
print(pila.pop_C())
