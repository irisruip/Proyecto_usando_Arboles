import csv
class Empresa:
    def __init__(self, id, nombre, descripcion, fecha_creacion, direccion, telefono, correo, gerente, equipo_contacto):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha_creacion = fecha_creacion
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo
        self.gerente = gerente
        self.equipo_contacto = equipo_contacto
        self.proyectos = []

class NodoEmpresa:
    def __init__(self, empresa):
        self.empresa = empresa
        self.siguiente = None
        
class Gestion:
    def __init__(self):
        self.cabeza = None
    
    def cargar_datos(self, archivo_csv):
        with open(archivo_csv, 'r') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                empresa = Empresa(
                    int(fila['id']),
                    fila['nombre'],
                    fila['descripcion'],
                    fila['fecha_creacion'],
                    fila['direccion'],
                    fila['telefono'],
                    fila['correo'],
                    fila['gerente'],
                    fila['equipo_contacto'].split(',')
                )
                self.agregar_empresa(empresa)
                
    def guardar_datos(self, archivo_csv):
        with open(archivo_csv, 'w', newline='') as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=['id', 'nombre', 'descripcion', 'fecha_creacion', 'direccion', 'telefono', 'correo', 'gerente', 'equipo_contacto'])
            escritor.writeheader()
            nodo_actual = self.cabeza
            while nodo_actual is not None:
                escritor.writerow({
                    'id': nodo_actual.empresa.id,
                    'nombre': nodo_actual.empresa.nombre,
                    'descripcion': nodo_actual.empresa.descripcion,
                    'fecha_creacion': nodo_actual.empresa.fecha_creacion,
                    'direccion': nodo_actual.empresa.direccion,
                    'telefono': nodo_actual.empresa.telefono,
                    'correo': nodo_actual.empresa.correo,
                    'gerente': nodo_actual.empresa.gerente,
                    'equipo_contacto': ','.join(nodo_actual.empresa.equipo_contacto)
                    })
                nodo_actual = nodo_actual.siguiente
    
    
            
    def agregar_empresa(self, empresa):
        nuevo_nodo = NodoEmpresa(empresa)
        
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            
        else:
            nodo_actual = self.cabeza
            while nodo_actual.siguiente is not None:
                nodo_actual = nodo_actual.siguiente
            nodo_actual.siguiente = nuevo_nodo
            
    def listar_empresas(self):
        if self.cabeza is None:
            print("No hay empresas registradas.")
            return

        nodo_actual = self.cabeza
        while nodo_actual is not None:
            print(f"- ID: {nodo_actual.empresa.id} - Nombre: {nodo_actual.empresa.nombre}")
            nodo_actual = nodo_actual.siguiente
    
    def buscar_empresa_por_id(self, id_empresa):
        nodo_actual = self.cabeza
        while nodo_actual is not None:
            if nodo_actual.empresa.id == id_empresa:
                return nodo_actual.empresa
            nodo_actual = nodo_actual.siguiente
        return None
    
    def modificar_empresa(self, id_empresa):
        empresa_a_modificar = self.buscar_empresa_por_id(id_empresa)
        if not empresa_a_modificar:
            print(f"Error: No se encontró la empresa con ID {id_empresa}.")
            return

        # Modificar datos de la empresa
        nuevo_nombre = input(f"Ingrese el nuevo nombre de la empresa ({empresa_a_modificar.nombre}): ") or empresa_a_modificar.nombre
        nueva_descripcion = input(f"Ingrese la nueva descripción de la empresa ({empresa_a_modificar.descripcion}): ") or empresa_a_modificar.descripcion
        nueva_fecha_creacion = input(f"Ingrese la nueva fecha de creación (YYYY-MM-DD) ({empresa_a_modificar.fecha_creacion}): ") or empresa_a_modificar.fecha_creacion

        empresa_a_modificar.nombre = nuevo_nombre
        empresa_a_modificar.descripcion = nueva_descripcion
        empresa_a_modificar.fecha_creacion = nueva_fecha_creacion

        print("Empresa modificada exitosamente.")
        
    def eliminar_empresa(self, id_empresa):
        nodo_anterior = None
        nodo_actual = self.cabeza
        
        while nodo_actual is not None:
            if nodo_actual.empresa.id == id_empresa:
                if nodo_anterior is None:
                    self.cabeza = nodo_actual.siguiente
                    
                else:
                    nodo_anterior.siguiente = nodo_actual.siguiente
                    print(f"Empresa con ID {id_empresa} eliminada exitosamente.")
                    return
            nodo_anterior = nodo_actual
            nodo_actual = nodo_actual.siguiente
            
        print(f"Error: No se encontró la empresa con ID {id_empresa}.")
        
    def crear_empresa(self):
        # Solicitar datos al usuario
        id_empresa = int(input("Ingrese el ID de la empresa: "))
        nombre = input("Ingrese el nombre de la empresa: ")
        descripcion = input("Ingrese la descripción de la empresa: ")
        fecha_creacion = input("Ingrese la fecha de creación (YYYY-MM-DD): ")
        direccion = input("Ingrese la dirección de la empresa: ")
        telefono = input("Ingrese el teléfono de la empresa: ")
        correo = input("Ingrese el correo electrónico de la empresa: ")
        gerente = input("Ingrese el nombre del gerente de la empresa: ")
        miembros_equipo = input("Ingrese los nombres de los miembros del equipo (separados por comas): ").split(',')

        # Crear objeto Empresa
        nueva_empresa = Empresa(
            id_empresa,
            nombre,
            descripcion,
            fecha_creacion,
            direccion,
            telefono,
            correo,
            gerente,
            miembros_equipo,
        )

        # Agregar la empresa a la lista enlazada
        self.agregar_empresa(nueva_empresa)

        print("Empresa creada exitosamente.")


gestion_empresas = Gestion()


gestion_empresas.cargar_datos("empresas.csv")


gestion_empresas.crear_empresa()


gestion_empresas.listar_empresas()


gestion_empresas.guardar_datos("empresas.csv")
