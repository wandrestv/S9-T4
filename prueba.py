class Lista:
    def __init__(self,datos=[]) -> None:
        self.lista=datos
    
    def insertar(self,dato):
        self.lista.append(dato)
        
    def obtener(self):
        ultimo = self.lista.pop()
        return ultimo
    
    def eliminarElemento(self,pos):
       if pos in range(0,len(self.lista)):
            ele = self.lista[pos]     
            self.lista = self.lista[0:pos] + self.lista[pos+1:]
            # listaAux = []
            # for ind in range(0,len(self.lista)):
            #     if ind != pos:
            #         listaAux += [self.lista[ind]]
               
            # for indice in range(0,pos):
            #     listaAux = listaAux + [self.lista[indice]] 
            # for indice in range(pos+1,len(self.lista)):
            #     listaAux = listaAux + [self.lista[indice]] 
            # self.lista=listaAux  
            return ele
       else:
            return None
            #return "Posicion:{} no existe en la lista".format(pos) 
                          #    2   7
    def insertarElemento(self,pos,dato):
        pass
        #[2,4,6,8,10] = [2,4,7,6,8,10] 
        # 0 1 2 3 4
        
    def mostrar(self):
        pass
    
numeros = Lista()
numeros.insertar("Ana")
numeros.insertar("Daniel")
numeros.insertar("Jose")
numeros.insertar("Miguel")
numeros.insertar("Moises")
#print(numeros.obtener())
print(numeros.lista)
resp = numeros.eliminarElemento(4)
print(resp if resp else "posicion:{} no valida".format(40))
#print(resp)
print(numeros.lista)