class Lista:
    def __init__(self):
        self.lista = []
        self.ind = 0
        pass

    def push_A(self,dato):
        self.lista.append(dato)
        self.ind = self.ind + 1

    def empty_A(self):
        if self.ind == 0:
            True
        else:
            False

    def pop_A(self):
        if self.empty_A():
            return "Lista Vacia"
        else:
            self.lista.pop()
            self.ind -= 1

    def show_A(self):                   
        for a in self.lista:
            print("[{}]".format(a)) 
    
    def eliminarElemento_A(self,pos):
        if pos in range(0,len(self.lista)):
            ele = self.lista[pos-1]     
            self.lista = self.lista[0:pos-1] + self.lista[pos:]
            self.ind -= 1
            return ele
        else:
            return None

    def insertarElemento_A(self,pos,dato):
        if pos in range(0,len(self.lista)):
            self.lista.insert(pos,dato)
            self.ind += 1
            return self.lista
        else:
            print("La posición {} no existe".format(pos))
        
    def buscar_A(self,buscado):
        try:
            c=self.lista.index(buscado)
            print(c+1)
        except ValueError as e:
            print("Error: ",e)
    
# numeros = Lista()
# numeros.push_A("Ana")
# numeros.push_A("Daniel")
# numeros.push_A("Jose")
# numeros.push_A("Miguel")
# numeros.push_A("Moises")
# #print(numeros.obtener())
# print(numeros.lista)
# print (numeros.eliminarElemento_A(3))
# print(numeros.lista)
# numeros.insertarElemento_A(0,"Andrés")
# #print(resp if resp else "posicion:{} no valida".format(5))
# print(numeros.pop_A())
# print(numeros.pop_A())
# print(numeros.pop_A())
# #print(resp)
# print(numeros.lista)