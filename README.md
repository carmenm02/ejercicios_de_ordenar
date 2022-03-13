<h1 align="center">	Ejercicios  de ordenar</h1>

<h2>Repositorio:</h2>

Este es el link del [repositorio](https://github.com/carmenm02/ejercicios_de_ordenar.git)

## Ejercicio 1:

**SOLUCION**
```
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
```
## Ejercicio 2:

**SOLUCION**
```
class Lista:
    def __init__(self, lista):
        self.lista = lista
    def ordenacion_burbuja(self):
        for i in range(len(self.lista)-1):
            for j in range(len(self.lista)-1):
                if self.lista[j] > self.lista[j+1]:
                    print ("Intercambiando {} con {}...".format(self.lista[j], self.lista[j+1]))
                    self.lista[j], self.lista[j+1] = self.lista[j+1], self.lista[j]
        return self.lista
```

## Ejercicio 3:

**SOLUCION**
```
     class segmento_de_tablas:

         def __init__(self,tabla):
             self.tabla = tabla

         def segmentos(self):
             r=[]
             for i in range(len(self.tabla)-1):

                 if self.tabla[i] >= self.tabla[i+1]:
                     r.append(self.tabla[i+1])

                     if self.tabla[i+1] < self.tabla[i+2]:
                         r.append(self.tabla[i+1])
                         n=[]
                         for j in range(i+2, len(self.tabla)-1):
                             if self.tabla[j] >= self.tabla[j+1]:
                                 n.append(self.tabla[j])
                                 if self.tabla[j+1] < self.tabla[j+2]:
                                     n.append(self.tabla[j+1])
                                     return r, n
                 else:
                     pass


         def explorar(self, segmento_de_tablas):
             mi = segmento_de_tablas[0]
             segmento_de_tablas = segmento_de_tablas[1:] + segmento_de_tablas[:1]
             return segmento_de_tablas
