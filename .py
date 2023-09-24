from dataclasses import dataclass

@dataclass
class Elemento:
    nombre: str

    def __eq__(self, other):
        if isinstance(other, Elemento):
            return self.nombre == other.nombre
        return False

@dataclass
class Conjunto:
    _contador = 0

    def __init__(self, nombre):
        self.elementos = []
        self.nombre = nombre
        self.__id = Conjunto._contador
        Conjunto._contador += 1

    @property
    def id(self):
        return self.__id

    def contiene(self, elemento):
        return any(elemento == e for e in self.elementos)

    def agregar_elemento(self, elemento):
        if not self.contiene(elemento):
            self.elementos.append(elemento)

    def unir(self, otro_conjunto):
        for elemento in otro_conjunto.elementos:
            self.agregar_elemento(elemento)

    def __add__(self, otro_conjunto):
        resultado = Conjunto(f"{self.nombre} UNION {otro_conjunto.nombre}")
        resultado.unir(self)
        resultado.unir(otro_conjunto)
        return resultado

    @classmethod
    def intersectar(cls, conjunto1, conjunto2):
        elementos_interseccion = [elem for elem in conjunto1.elementos if conjunto2.contiene(elem)]
        nombre_resultado = f"{conjunto1.nombre} INTERSECTADO {conjunto2.nombre}"
        resultado = Conjunto(nombre_resultado)
        resultado.elementos = elementos_interseccion
        return resultado

    def __str__(self):
        elementos_str = ', '.join(str(elem.nombre) for elem in self.elementos)
        return f"Conjunto {self.nombre}: ({elementos_str})"
elemento1 = Elemento("A")
elemento2 = Elemento("B")

conjunto1 = Conjunto("Conjunto 1")
conjunto1.agregar_elemento(elemento1)
conjunto2 = Conjunto("Conjunto 2")
conjunto2.agregar_elemento(elemento2)

print(conjunto1)
print(conjunto2)  

union = conjunto1 + conjunto2
print(union) 

interseccion = Conjunto.intersectar(conjunto1, conjunto2)
print(interseccion)  