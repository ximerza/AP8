from tiendalibros.modelo.libro_error import LibroError


class LibroAgotadoError(LibroError):
    def __init__(self, isbn):
        super().__init__(f"El libro con ISBN {isbn} esta agotado.")


    def __repr__(self):
        return f"El libro con titulo {self.titulo} y ISBN: {self.isbn} esta agotado."
