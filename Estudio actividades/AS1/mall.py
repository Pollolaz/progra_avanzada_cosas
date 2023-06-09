from locales import Entretenimiento, Comida, Tienda, Casino, Supermercado
from personas import Cliente


class Mall:

    def __init__(self, clientes, locales):
        self.clientes = clientes
        self.locales = locales

        # Definir self.abierto
        self.abierto = True

    # Modifica este método como property (agregar más métodos si es necesario)
    @property
    def utilidades(self):
        util = 0
        for local in self.locales.values( ):
            util += local.utilidades()
        return util

    def pedir_resumen(self):
        # Completar
        for local in self.locales.values():
            local.entregar_resumen() 

    def vender(self, local, cliente):
        # Completar
        producto = local.obtener_producto_a_vender()
        dinero = cliente.dinero
        precio = local.productos[producto]

        if precio <= dinero:
            cliente.dinero -= precio
            local.utilidades += precio
            print(f"{cliente.nombre} ha comprado {producto}")
        else:
            print(f"{cliente.nombre} no puede comprar {producto}")
        

    def iniciar_simulacion(self):
        # No modificar
        clientes_fuera = []
        for cliente in self.clientes:
            # Verificamos que el local existe
            if cliente.nombre_local_favorito not in self.locales:
                continue

            local = self.locales[cliente.nombre_local_favorito]
            if local.abierto:
                # Si el local está abierto se intenta ingresar al cliente
                if local.cliente_ingresa(cliente):
                    self.vender(local, cliente)
                else:
                    clientes_fuera.append(cliente)
            else:
                # Si el local está cerrado solo imprimimos
                print("-" * 75)
                print(f"{local.nombre} cerrado, {cliente.nombre} no puede entrar")

        # Motrar resumen de la simulación
        self.pedir_resumen()
        print("")
        print(f"Quedaron {len(clientes_fuera)} clientes fuera de sus locales favoritos")
