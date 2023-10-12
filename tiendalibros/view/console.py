import sys

from tiendalibros.modelo.tienda_libros import TiendaLibros


class UIConsola:

    def __init__(self):
        self.tienda_libros: TiendaLibros = TiendaLibros()
        self.opciones = {
            "1": self.adicionar_un_libro_a_catalogo,
            "2": self.agregar_libro_a_carrito_de_compras,
            "3": self.retirar_libro_de_carrito_de_compras,
            "4": self.salir
        }

    @staticmethod
    def salir():
        print("\nGRACIAS POR VISITAR NUESTRA TIENDA DE LIBROS. VUELVA PRONTO")
        sys.exit(0)

    @staticmethod
    def mostrar_menu():
        titulo = "¡Tienda Libros!"
        print(f"\n{titulo:_^30}")
        print("1. Adicionar un libro al catálogo")
        print("2. Agregar libro a carrito de compras")
        print("3. Retirar libro de carrito de compras")
        print(f"{'_':_^30}")

    def ejecutar_app(self):
        while True:
            self.mostrar_menu()
            opcion = input("Seleccione una opción: ")
            accion = self.opciones.get(opcion)
            if accion:
                accion()
            else:
                print(f"{opcion} no es una opción válida")

    def retirar_libro_de_carrito_de_compras(self):
        isbn = input("Ingrese el ISBN del libro que desea retirar del carrito: ")

        try:
            tienda_libros.retiras_item_de_carrito(isbn)
        except LibroNoEnCarritoError as i:
            print(e)
            return

        print("Libro retirado del carrito de compras con éxito.")


    def agregar_libro_a_carrito_de_compras(self, tienda_libros):
        isbn = input("Ingrese el ISBN del libro que deseas agregar al carrito:")
        cantidad = int(input("Ingrese la cantidad de unidades del libro que desea agregar:"))

        try:
            libro = tienda_libros.obtener_libro_por_isbn(isbn)
            tienda_libros.agregar_libro_a_carrito(isbn, cantidad)
        except LibroExistenteError as e:
            print (e)
            return
        except ExistenciasInsuficientesError as e:
            print(e)
            return 

        print("Libro agregado al carrito de compras en éxito.") 


    def adicionar_un_libro_a_catalogo(self, tienda_libros):
        isbn = input("Ingrese el ISBN del libro:")
        titulo = input("Ingrese el titulo del libro:")
        precio = float(input("Ingrese el precio del libro:"))
        existencias = int(input("Ingrese las existencias del libro:"))

        try:
            tienda_libros.adicionar_libro_a_catalogo(isbn)
        except LibroExistenteError as i:
            print(i)
            return
        except ExistenciasInsuficientesError as i:
            print(i)
            return

        print("Libro añadido al catálogo con éxito.")
        