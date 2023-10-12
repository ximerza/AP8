from tiendalibros.modelo.libro_error import LibroError


class ExistenciasInsuficientesError(LibroError):
    def __init__(self, isbn, cantidad_a_comprar):
        super().__init__(f"La cantidad a comprar del libro con ISNB {isbn} es mayor que la cantidad de existencias.")
        self.cantidad_a_comprar = cantidad_a_comprar

    def __repr__(self):
        return f"E libro con titulo {self.titulo} y ISBN {self.isbn} no tiene suficientes existencias para realizar la compra: cantidad a comprar: {self.cantidad_a_comprar}, existencias: {self.libro.existencias}."


    
