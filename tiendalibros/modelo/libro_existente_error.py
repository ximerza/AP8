from tiendalibros.modelo.libro_error import LibroError


class LibroExistenteError(LibroError):
    def __init__(self, isbn):
        super().__init__(f"El libro con ISBN {isbn} ya existe en el catalogo.")

    def __repr__(self):
        return f"El libro con titulo {self.titulo} y isbn: {self.isbn} ya existe en el catalogo."


  

