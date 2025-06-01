class NodoArbol:
    def __init__(self, clave, valor):
        self.clave = clave
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None

    def insertar(self, clave, valor):
        if not self.raiz:
            self.raiz = NodoArbol(clave, valor)
        else:
            self._insertar_recursivo(self.raiz, clave, valor)

    def _insertar_recursivo(self, nodo, clave, valor):
        if clave < nodo.clave:
            if nodo.izquierdo:
                self._insertar_recursivo(nodo.izquierdo, clave, valor)
            else:
                nodo.izquierdo = NodoArbol(clave, valor)
        elif clave > nodo.clave:
            if nodo.derecho:
                self._insertar_recursivo(nodo.derecho, clave, valor)
            else:
                nodo.derecho = NodoArbol(clave, valor)
        else:
            nodo.valor = valor

    def buscar(self, clave):
        return self._buscar_recursivo(self.raiz, clave)

    def _buscar_recursivo(self, nodo, clave):
        if not nodo:
            return None
        if clave == nodo.clave:
            return nodo.valor
        elif clave < nodo.clave:
            return self._buscar_recursivo(nodo.izquierdo, clave)
        else:
            return self._buscar_recursivo(nodo.derecho, clave)

    def en_orden(self):
        resultado = []
        self._en_orden_recursivo(self.raiz, resultado)
        return resultado

    def _en_orden_recursivo(self, nodo, resultado):
        if nodo:
            self._en_orden_recursivo(nodo.izquierdo, resultado)
            resultado.append((nodo.clave, nodo.valor))
            self._en_orden_recursivo(nodo.derecho, resultado)

    def eliminar(self, clave):
        self.raiz = self._eliminar_recursivo(self.raiz, clave)

    def _eliminar_recursivo(self, nodo, clave):
        if not nodo:
            return None

        if clave < nodo.clave:
            nodo.izquierdo = self._eliminar_recursivo(nodo.izquierdo, clave)
        elif clave > nodo.clave:
            nodo.derecho = self._eliminar_recursivo(nodo.derecho, clave)
        else:
            if not nodo.izquierdo:
                return nodo.derecho
            if not nodo.derecho:
                return nodo.izquierdo

            sucesor = self._encontrar_minimo(nodo.derecho)
            nodo.clave = sucesor.clave
            nodo.valor = sucesor.valor
            nodo.derecho = self._eliminar_recursivo(nodo.derecho, sucesor.clave)

        return nodo

    def _encontrar_minimo(self, nodo):
        while nodo.izquierdo:
            nodo = nodo.izquierdo
        return nodo
