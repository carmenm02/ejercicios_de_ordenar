lista = [] 
fin=len(lista)

class ordenacion_dicotomica:

  def __init__(self,tabla,inicio,fin):
    self.lista=lista
    self.inicio=inicio
    self.fin=fin
    
  def ordenar(self):
    while self.inicio < self.fin:
      for i in range (self.inicio+1,self.fin):