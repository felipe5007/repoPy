class Cliente:
    def __init__(self, nombre, edad, rut, celular):
        self.nombre = nombre
        self.edad = edad
        self.rut = rut        
        self.celular = celular
        self.items_comprados = []

    def __str__(self):
        return f'Cliente: {self.nombre}'

    def comprar(self, item):
        self.items_comprados.append(item)
        print(f'El item {item} ha sido comprado')

    def mostrar_items_comprados(self):
        if not self.items_comprados:
            print("No has comprado ningún item aún.")
        else:
            items = ', '.join(str(item) for item in self.items_comprados)
            print(f"Los items comprados son: {items}")


Felipe = Cliente('Felipe', '27', 123456789, 56995435462)