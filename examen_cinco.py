import csv
from datetime import datetime
import os

# Verificar el directorio de trabajo actual
print("Directorio de trabajo actual:", os.getcwd())

# Cambiar el directorio de trabajo si es necesario
os.chdir('C:/Users/Irisbel/Desktop/algoritmos_V/Proyecto_usando_Arboles')
print("Directorio de trabajo después de cambiar:", os.getcwd())

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

class Proyectos:
    def __init__(self, id, nombre, descripcion, fecha_inicio, fecha_vencimiento, estado_actual, empresa, gerente, equipo):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha_inicio = fecha_inicio
        self.fecha_vencimiento = fecha_vencimiento
        self.estado_actual = estado_actual
        self.empresa = empresa
        self.gerente = gerente
        self.equipo = equipo
        self.tareas = []
        
class Tareas:
    def __init__(self, id, nombre, empresa,  cliente, descripcion, fecha_inicio, fecha_vencimiento, estado_actual, porcentaje):
        self.id = id
        self.nombre = nombre
        self.empresa = empresa
        self.cliente = cliente
        self.descripcion = descripcion
        self.fecha_inicio = fecha_inicio
        self.fecha_vencimiento = fecha_vencimiento
        self.estado_actual = estado_actual
        self.porcentaje = porcentaje
        self.subtareas = []
        
class subTareas:
    def __init__(self, id, nombre, empresa,  cliente, descripcion, fecha_inicio, fecha_vencimiento, estado_actual, porcentaje):
        self.id = id
        self.nombre = nombre
        self.empresa = empresa
        self.cliente = cliente
        self.descripcion = descripcion
        self.fecha_inicio = fecha_inicio
        self.fecha_vencimiento = fecha_vencimiento
        self.estado_actual = estado_actual
        self.porcentaje = porcentaje

#nodo para lista enlazada
class NodoEmpresa:
    def __init__(self, empresa):
        self.empresa = empresa
        self.siguiente = None


#clase de gestion de acciones de la empresa
class Gestion:
    def __init__(self):
        self.cabeza = None
    
    #cargo datos en el archivo csv
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
    
    
    #guardo datos en el archivo csv         
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
                
    #agrego la empresa a la lista
    def agregar_empresa(self, empresa):
        nuevo_nodo = NodoEmpresa(empresa)
        
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            
        else:
            nodo_actual = self.cabeza
            while nodo_actual.siguiente is not None:
                nodo_actual = nodo_actual.siguiente
            nodo_actual.siguiente = nuevo_nodo
            
        with open('algo.csv', 'a', newline='') as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=['id', 'nombre', 'descripcion', 'fecha_creacion', 'direccion', 'telefono', 'correo', 'gerente', 'equipo_contacto'])
            escritor.writerow({
                'id': empresa.id,
                'nombre': empresa.nombre,
                'descripcion': empresa.descripcion,
                'fecha_creacion': empresa.fecha_creacion,
                'direccion': empresa.direccion,
                'telefono': empresa.telefono,
                'correo': empresa.correo,
                'gerente': empresa.gerente,
                'equipo_contacto': ','.join(empresa.equipo_contacto)})
         
    #busco la empresa por su id en la lista   
    def buscar_empresa_por_id(self, id_empresa):
        nodo_actual = self.cabeza
        while nodo_actual is not None:
            if nodo_actual.empresa.id == id_empresa:
                return nodo_actual.empresa
            nodo_actual = nodo_actual.siguiente
        return None
    
    #modifico segun el id
    def modificar_empresa(self, id_empresa, nuevo_nombre, nueva_descripcion, nueva_fecha_creacion, nueva_direccion, nuevo_telefono, nuevo_correo, nuevo_gerente, nuevos_miembros_equipo):
        empresa_a_modificar = self.buscar_empresa_por_id(id_empresa)
        if not empresa_a_modificar:
            print(f"Error: No se encontró la empresa con ID {id_empresa}.")
            return
        
        empresa_a_modificar.nombre = nuevo_nombre
        empresa_a_modificar.descripcion = nueva_descripcion
        empresa_a_modificar.fecha_creacion = nueva_fecha_creacion
        empresa_a_modificar.direccion = nueva_direccion
        empresa_a_modificar.telefono = nuevo_telefono
        empresa_a_modificar.correo = nuevo_correo
        empresa_a_modificar.gerente = nuevo_gerente
        empresa_a_modificar.equipo_contacto = nuevos_miembros_equipo
        
        # Actualizar el registro correspondiente en el archivo "algo.csv"
        with open('algo.csv', 'r') as archivo_lectura:
            lector = csv.DictReader(archivo_lectura)
            lineas = list(lector)
            
        with open('algo.csv', 'w', newline='') as archivo_escritura:
            escritor = csv.DictWriter(archivo_escritura, fieldnames=['id', 'nombre', 'descripcion', 'fecha_creacion', 'direccion', 'telefono', 'correo', 'gerente', 'equipo_contacto'])
            escritor.writeheader()
            
            for linea in lineas:
                if int(linea['id']) == id_empresa:
                    linea['nombre'] = nuevo_nombre
                    linea['descripcion'] = nueva_descripcion
                    linea['fecha_creacion'] = nueva_fecha_creacion
                    linea['direccion'] = nueva_direccion
                    linea['telefono'] = nuevo_telefono
                    linea['correo'] = nuevo_correo
                    linea['gerente'] = nuevo_gerente
                    linea['equipo_contacto'] = ','.join(nuevos_miembros_equipo)
                escritor.writerow(linea)
        
    #consulto segun el id
    def consultar(self, id_empresa):
        nodo_actual = self.cabeza
        while nodo_actual is not None:
            if nodo_actual.empresa.id == id_empresa:
                print(f"Información de la empresa con ID {id_empresa}:")
                print(f"Nombre: {nodo_actual.empresa.nombre}")
                print(f"Descripción: {nodo_actual.empresa.descripcion}")
                print(f"Fecha de creación: {nodo_actual.empresa.fecha_creacion}")
                print(f"Dirección: {nodo_actual.empresa.direccion}")
                print(f"Teléfono: {nodo_actual.empresa.telefono}")
                print(f"Correo electrónico: {nodo_actual.empresa.correo}")
                print(f"Gerente: {nodo_actual.empresa.gerente}")
                print(f"Miembros del equipo: {', '.join(nodo_actual.empresa.equipo_contacto)}")
                return nodo_actual.empresa
            nodo_actual = nodo_actual.siguiente
        return None
        
    #lista de todas las empresas con id y nombre   
    def listar_empresas(self):
        if self.cabeza is None:
            print("No hay empresas registradas.")
            return

        nodo_actual = self.cabeza
        while nodo_actual is not None:
            print(f"- ID: {nodo_actual.empresa.id} - Nombre: {nodo_actual.empresa.nombre}")
            nodo_actual = nodo_actual.siguiente

   

    #elimino la empresa de la lista
    def eliminar_empresa(self, id_empresa):
        nodo_anterior = None
        nodo_actual = self.cabeza
        
        while nodo_actual is not None:
            if nodo_actual.empresa.id == id_empresa:
                if nodo_anterior is None:
                    self.cabeza = nodo_actual.siguiente
                    
                else:
                    nodo_anterior.siguiente = nodo_actual.siguiente
                
                with open('algo.csv', 'r') as archivo_lectura:
                    lector = csv.DictReader(archivo_lectura)
                    lineas = list(lector)
                    
                with open('algo.csv', 'w', newline='') as archivo_escritura:
                    escritor = csv.DictWriter(archivo_escritura, fieldnames=['id', 'nombre', 'descripcion', 'fecha_creacion', 'direccion', 'telefono', 'correo', 'gerente', 'equipo_contacto'])
                    escritor.writeheader()
                    
                    for linea in lineas:
                        if int(linea['id']) != id_empresa:
                            escritor.writerow(linea)
                
                print(f"Empresa con ID {id_empresa} eliminada exitosamente.")
                return
            
            nodo_anterior = nodo_actual
            nodo_actual = nodo_actual.siguiente
        

           
def menu():
    print("-----MODULO DE GESTION DE EMPRESAS----")
    print("1. Crear empresa")
    print("2. Modificar empresa")
    print("3. Consultar empresa")
    print("4. Listar empresas")
    print("5. Eliminar empresa")
    print("6. Salir del modulo de gestion de empresas")
    
    print("-----MODULO DE GESTION DE PROYECTOS----")
    print("7. Crear proyecto")
    print("8. Modificar proyeco")
    print("9. Consultar proyecto")
    print("10. Listar proyecto")
    print("11. Eliminar proyecto")
    print("12. Salir del modulo de gestion de proyectos")
    
    print("-----MODULO DE GESTION DE TAREAS Y PRIORIDADES----")
    print("13. Crear tarea")
    print("14. Agregar subtarea")
    print("15. Modificar tarea")
    print("16. Consultar tarea")
    print("17. Listar tarea")
    print("18. Eliminar tarea y subtareas de la tarea")
    print("19. Salir del modulo de gestion de tareas y prioridades")
    
def main():
    empresa_principal = Empresa(
        0,
        "nombre",
        "descripcion",
        datetime.now(),
        "direccion",
        "telefono",
        "correo",
        "gerente",
        "miembros_equipo",
        )
    
    gestion_empresas = Gestion()
    gestion_empresas.cargar_datos("algo.csv")
    gestion_empresas.guardar_datos("algo.csv")
    
    #manejo el menu de opciones
    while True:
        menu()
        opcion = input("Seleccione una opcion: ")
        
        if opcion=='1':
            id_empresa = int(input("Ingrese el ID de la empresa: "))
            nombre = input("Ingrese el nombre de la empresa: ")
            descripcion = input("Ingrese la descripción de la empresa: ")
            fecha_creacion = input("Ingrese la fecha de creación (YYYY-MM-DD): ")
            direccion = input("Ingrese la dirección de la empresa: ")
            telefono = input("Ingrese el teléfono de la empresa: ")
            correo = input("Ingrese el correo electrónico de la empresa: ")
            gerente = input("Ingrese el nombre del gerente de la empresa: ")
            miembros_equipo = input("Ingrese los nombres de los miembros del equipo (separados por comas): ").split(',')
            
            nueva_empresa = Empresa(id_empresa, nombre, descripcion, fecha_creacion, direccion, telefono, correo, gerente, miembros_equipo)
            gestion_empresas.agregar_empresa(nueva_empresa)
            print("Empresa agregada exitosamente.")
            
        elif opcion=='2':
            id_empresa = int(input("Ingrese id de empresa a modificar: "))
            nuevo_nombre = input("Ingrese el nuevo nombre de la empresa : ") 
            nueva_descripcion = input("Ingrese la nueva descripción de la empresa : ") 
            nueva_fecha_creacion = input("Ingrese la nueva fecha de creación (YYYY-MM-DD) : ")
            nueva_direccion = input("Ingrese la nueva dirección de la empresa: ")
            nuevo_telefono = input("Ingrese el nuevo teléfono de la empresa: ")
            nuevo_correo = input("Ingrese el nuevo correo electrónico de la empresa: ")
            nuevo_gerente = input("Ingrese el nuevo nombre del gerente de la empresa: ")
            nuevos_miembros_equipo = input("Ingrese los nuevos nombres de los miembros del equipo (separados por comas): ").split(',')
             
            gestion_empresas.modificar_empresa(
                id_empresa,
                nuevo_nombre,
                nueva_descripcion,
                nueva_fecha_creacion,
                nueva_direccion,
                nuevo_telefono,
                nuevo_correo,
                nuevo_gerente,
                nuevos_miembros_equipo,
            )
            print("Empresa modificada exitosamente.")
        
        elif opcion =='3':
            id_empresa = int(input("Ingrese id de empresa a consultar: "))
            gestion_empresas.consultar(id_empresa)
            
        elif opcion =='4':
            gestion_empresas.listar_empresas()
            
        elif opcion =='5':
            id_empresa = int(input("Ingrese el ID de la empresa que desea eliminar: "))
            gestion_empresas.eliminar_empresa(id_empresa)
            
        if opcion =='6':
            break

if __name__ == "__main__":
    main()

