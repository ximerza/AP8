class TiendaLibros:
    def __init__(self):
         self.catalogo = {}
         self.carrito = CarroCompras()

    def adicionar_libro_a_catalogo(self, isbn:str, titulo:str, precio:float, existencias:int)-> Libro():
        if isbn in self.catalogo:
            raise LibroExistenteError(isbn)

        libro = Libro(isbn, titulo, precio, existencias)
        self.catalogo[isbn] = Libro
        return libro

    def agregar_libro_a_carrito(self, isbn, cantidad):
        libro = self.obtener_libro_por_isbn(isbn)

        if libro is None:
            raise LibroAgotadoError(isbn)

        if libro.existencias < cantidad:
            raise ExistenciasInsuficientesError(libro, cantidad)

    
        self.carrito.agregar_libro(libro, cantidad)  


    def retirar_item_de_carrito(self, isbn):
        libro = self.obtener_libro_por_isbn(isbn)

        if libro is None:
            raise LibroNoEnCarritoError(isbn)

        self.carrito.quitar_item(isbn)


