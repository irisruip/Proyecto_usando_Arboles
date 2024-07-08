import csv
from datetime import datetime
import os

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
         
    #busco la empresa por su id en la lista   
    def buscar_empresa_por_id(self, id_empresa):
        nodo_actual = self.cabeza
        while nodo_actual is not None:
            if nodo_actual.empresa.id == id_empresa:
                return nodo_actual.empresa
            nodo_actual = nodo_actual.siguiente
        return None
    
    #modifico segun el id
    def modificar_empresa(self, id_empresa):
        empresa_a_modificar = self.buscar_empresa_por_id(id_empresa)
        if not empresa_a_modificar:
            print(f"Error: No se encontró la empresa con ID {id_empresa}.")
            return
        
    #consulto segun el id
    def consultar(self, id_empresa):
        empresa_a_consultar = self.buscar_empresa_por_id(id_empresa)
        if not empresa_a_consultar:
            print(f"Error: No se encontró la empresa con ID {id_empresa}.")
            return
        
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
                    print(f"Empresa con ID {id_empresa} eliminada exitosamente.")
                    return
            nodo_anterior = nodo_actual
            nodo_actual = nodo_actual.siguiente
            
        print(f"Error: No se encontró la empresa con ID {id_empresa}.")
        
        
def menu():
    print("1. Crear empresa")
    print("2. Modificar empresa")
    print("3. Consultar empresa")
    print("4. Listar empresas")
    print("5. Eliminar empresa")
    print("6. Salir empresa")
    
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
    gestion_empresas.cargar_datos("empresa.csv")
    gestion_empresas.guardar_datos("empresa.csv")
    
    
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
            
            nueva_empresa = Empresa(id_empresa, nuevo_nombre, nueva_descripcion, nueva_fecha_creacion, nueva_direccion, nuevo_telefono, nuevo_correo, nuevo_gerente, nuevos_miembros_equipo)
            gestion_empresas.modificar_empresa(nueva_empresa)
        
        
        elif opcion =='3':
            id_empresa = int(input("Ingrese id de empresa a consultar: "))
            empresa_principal.consultar(id_empresa)
            
        elif opcion =='4':
            gestion_empresas.listar_empresas()
            
            
        elif opcion =='5':
            id_empresa = int(input("Ingrese el ID de la empresa que desea eliminar: "))
            empresa_principal.gestion_empresas.eliminar_empresa(id_empresa)
            
        elif opcion =='6':
            break

