import csv
from datetime import datetime
import os
import json


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
            
        with open('companie.csv', 'a', newline='') as archivo:
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
        
        # Actualizar el registro correspondiente en el archivo "companie.csv"
        with open('companie.csv', 'r') as archivo_lectura:
            lector = csv.DictReader(archivo_lectura)
            lineas = list(lector)
            
        with open('companie.csv', 'w', newline='') as archivo_escritura:
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
                
                with open('companie.csv', 'r') as archivo_lectura:
                    lector = csv.DictReader(archivo_lectura)
                    lineas = list(lector)
                    
                with open('companie.csv', 'w', newline='') as archivo_escritura:
                    escritor = csv.DictWriter(archivo_escritura, fieldnames=['id', 'nombre', 'descripcion', 'fecha_creacion', 'direccion', 'telefono', 'correo', 'gerente', 'equipo_contacto'])
                    escritor.writeheader()
                    
                    for linea in lineas:
                        if int(linea['id']) != id_empresa:
                            escritor.writerow(linea)
                
                print(f"Empresa con ID {id_empresa} eliminada exitosamente.")
                return
            
            nodo_anterior = nodo_actual
            nodo_actual = nodo_actual.siguiente
            
#tareas para arbol n-ario
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
        
    def serialize(self):
        def serialize_task(task):
            return {
                "id": task.id,
                "nombre": task.nombre,
                "descripcion": task.descripcion,
                "fecha_inicio": str(task.fecha_inicio), 
                "fecha_vencimiento": str(task.fecha_vencimiento),  
                "estado_actual": task.estado_actual,
                "subtareas": [serialize_task(subtask) for subtask in task.subtareas]
            }
        
        return {
            "id": self.id,
            "nombre": self.nombre,
            "descripcion": self.descripcion,
            "fecha_inicio": str(self.fecha_inicio),
            "fecha_vencimiento": str(self.fecha_vencimiento),
            "estado_actual": self.estado_actual,
            "empresa": self.empresa,
            "gerente": self.gerente,
            "equipo": self.equipo,
            "tareas": [serialize_task(tarea) for tarea in self.tareas]
        }
        
    #mostrar en el json  
    def save_to_json(self, filename="tareas.json"):
        with open(filename, "w") as file:
            json.dump(self.serialize(), file, indent=4)
     
     #agregar tarea     
    def add_task(self, tarea, parent_id=None, save=True):
        if parent_id is None:
            self.tareas.append(tarea)
        else:
            parent_task = self.find_task(parent_id)
            if parent_task:
                if not hasattr(parent_task, 'subtareas'):
                    parent_task.subtareas = []
                parent_task.subtareas.append(tarea)
            else:
                raise ValueError(f"Parent task with ID {parent_id} not found.")
        if save:
            self.save_to_json()
     
     #actualizar tarea en el json     
    def update_task(self, updated_task):
        for index, tarea in enumerate(self.tareas):
            if tarea.id == updated_task.id:
                self.tareas[index] = updated_task
                self.save_to_json()
                return True
        return False
        
     #encontrar tarea por id 
    def find_task(self, id, tareas=None):
        if tareas is None:
            tareas = self.tareas
        for tarea in tareas:
            if tarea.id == id:
                return tarea
            if hasattr(tarea, 'subtareas'):
                subtask = self.find_task(id, tarea.subtareas)
                if subtask:
                    return subtask
            
    #eliminar tarea
    def delete_task(self, id_tarea):
        for index, tarea in enumerate(self.tareas):
            if tarea.id == id_tarea:
                del self.tareas[index]
                self.save_to_json()  
                return True
        return False
    
    #listar tareas
    def list_tasks(self, level=0, tareas=None, prefix=""):
        if tareas is None:
            tareas = self.tareas
        for tarea in tareas:
            print(f"{prefix}Task ID: {tarea.id}, Name: {tarea.name}, Level: {level}")
            self.list_tasks(level + 1, tarea.subtasks, prefix + "--")


    #leer el json
    def load_from_json(self, filename):
        try:
            with open(filename, 'r') as file:
                file_content = file.read()
                if not file_content:
                    raise ValueError("File is empty")
                tasks_data = json.loads(file_content)
                if not isinstance(tasks_data, list) or not all(isinstance(task, dict) for task in tasks_data):
                    raise ValueError("JSON file must contain an array of dictionaries")
                self.tareas = [self._dict_to_task(task_data) for task_data in tasks_data]
        except FileNotFoundError:
            print("File not found. Initializing with an empty task list.")
            self.tareas = []
        except ValueError as e:
            print(f"Error loading JSON: {e}")
            self.tareas = []
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            self.tareas = []
    
    def _task_to_dict(self, tarea):
        return {
            "id": tarea.id,
            "name": tarea.name,
            "customer_company": tarea.customer_company,
            "description": tarea.description,
            "start_date": tarea.start_date.isoformat(),
            "due_date": tarea.due_date.isoformat(),
            "current_status": tarea.current_status,
            "percentage": tarea.percentage,
            "subtasks": [self._task_to_dict(subtask) for subtask in tarea.subtareas]
        }

    def _dict_to_task(self, data):
        print("Data received:", data)
        if not isinstance(data, dict):
            raise TypeError("Expected data to be a dictionary, got {}".format(type(data)))
        tarea = Tareas(
            data['id'], data['name'], data['customer_company'], data['description'],
            datetime.fromisoformat(data['start_date']), datetime.fromisoformat(data['due_date']),
            data['current_status'], data['percentage']
            )
        tarea.subtareas = [self._dict_to_task(subtask_data) for subtask_data in data.get('subtareas', [])]
        return tarea     

#inicializo altura, izquierda y derecha              
class AVLNode:
    def __init__(self, proyecto):
        self.proyecto = proyecto
        self.altura = 1
        self.izquierda = None
        self.derecha = None

#comienzo a trabajar con el arbol avl
class AVLTree:
    def insert(self, root, proyecto):
        if not root:
            return AVLNode(proyecto)
        elif proyecto.fecha_vencimiento < root.proyecto.fecha_vencimiento:
            root.izquierda = self.insert(root.izquierda, proyecto)
        else:
            root.derecha = self.insert(root.derecha, proyecto)

        root.altura = 1 + max(self.getHeight(root.izquierda), self.getHeight(root.derecha))
        balance = self.getBalance(root)

        if balance > 1 and proyecto.fecha_vencimiento < root.izquierda.proyecto.fecha_vencimiento:
            return self.rightRotate(root)
        if balance < -1 and proyecto.fecha_vencimiento >= root.derecha.proyecto.fecha_vencimiento:
            return self.leftRotate(root)
        if balance > 1 and proyecto.fecha_vencimiento >= root.izquierda.proyecto.fecha_vencimiento:
            root.izquierda = self.leftRotate(root.izquierda)
            return self.rightRotate(root)
        if balance < -1 and proyecto.fecha_vencimiento < root.derecha.proyecto.fecha_vencimiento:
            root.derecha = self.rightRotate(root.derecha)
            return self.leftRotate(root)

        return root

    #izquierda
    def leftRotate(self, z):
        y = z.derecha
        T2 = y.izquierda
        y.izquierda = z
        z.dercha = T2
        z.altura = 1 + max(self.getHeight(z.izquierda), self.getHeight(z.derecha))
        y.altura = 1 + max(self.getHeight(y.izquierda), self.getHeight(y.derecha))
        return y
    
    #derecha
    def rightRotate(self, y):
        x = y.izquierda
        T2 = x.derecha
        x.derecha = y
        y.izquierda = T2
        y.altura = 1 + max(self.getHeight(y.izquierda), self.getHeight(y.derecha))
        x.altura = 1 + max(self.getHeight(x.izquierda), self.getHeight(x.derecha))
        return x
    
    #obtengo altura
    def getHeight(self, root):
        if not root:
            return 0
        return root.altura
    
    #obtengo balance
    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.izquierda) - self.getHeight(root.derecha)
    
    #trabajo en preorden
    def preOrder(self, root):
        if not root:
            return
        print("{0} ".format(root.proyecto.nombre), end="")
        self.preOrder(root.izquierda)
        self.preOrder(root.derecha)
        
    #metodo para buscar   
    def search(self, root, key):
        if root is None or root.proyecto.id == key:
            return root
        if root.proyecto.id < key:
            return self.search(root.derecha, key)
        return self.search(root.izquierda, key)
    
    #obtengo los proyectos
    def collectProjects(self, root, projects_list):
        if root:
            self.collectProjects(root.izquierda, projects_list)
            projects_list.append(root.proyecto)
            self.collectProjects(root.derecha, projects_list)
            
    def preOrderCloseToDueDate(self, root):
        projects_list = []
        self.collectProjects(root, projects_list)
        # Sort projects by their due date, closest first
        projects_list.sort(key=lambda project: project.fecha_vencimiento)
        
        for project in projects_list:
            print(f"{project.nombre} - Vencimiento: {project.fecha_vencimiento.strftime('%Y-%m-%d')}")
    
    #elimino
    def delete(self, root, project_id):
        if not root:
            return root


        if project_id < root.proyecto.id:
            root.izquierda = self.delete(root.izquierda, project_id)
        elif project_id > root.proyecto.id:
            root.derecha = self.delete(root.derecha, project_id)
        else:
            if root.izquierda is None:
                temp = root.derecha
                root = None
                return temp
            elif root.derecha is None:
                temp = root.izquierda
                root = None
                return temp
            temp = self.getMinValueNode(root.derecha)
            root.proyecto = temp.proyecto
            root.derecha = self.delete(root.derecha, temp.proyecto.id)


        if root is None:
            return root
        

        root.altura = 1 + max(self.getHeight(root.izquierda), self.getHeight(root.derecha))

   
        balance = self.getBalance(root)


        if balance > 1 and self.getBalance(root.izquierda) >= 0:
            return self.rightRotate(root)


        if balance < -1 and self.getBalance(root.derecha) <= 0:
            return self.leftRotate(root)

     
        if balance > 1 and self.getBalance(root.izquierda) < 0:
            root.izquierda = self.leftRotate(root.izquierda)
            return self.rightRotate(root)

    
        if balance < -1 and self.getBalance(root.derecha) > 0:
            root.derecha = self.rightRotate(root.derecha)
            return self.leftRotate(root)

        return root

    def getMinValueNode(self, node):
        if node is None or node.izquierda is None:
            return node
        return self.getMinValueNode(node.izquierda) 

"""        
class Sprint:
    def __init__(self, id, nombre, fecha_inicio, fecha_fin, estado, objetivos, equipo, tareas=None):
        self.id = id
        self.nombre = nombre
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.estado = estado
        self.objetivos = objetivos
        self.equipo = equipo
        self.tareas = tareas if tareas is not None else []

    def __str__(self):
        return (f"ID: {self.id}, Nombre: {self.nombre}, Fecha de Inicio: {self.fecha_inicio}, "
                f"Fecha de Fin: {self.fecha_fin}, Estado: {self.estado}, Objetivos: {self.objetivos}, "
                f"Equipo: {self.equipo}, Tareas: {self.tareas}")     
         
def cargar_sprints(archivo_json):
    with open(archivo_json, 'r') as file:
        sprints = json.load(file)
    return sprints

def guardar_sprints(sprints, archivo_json):
    with open(archivo_json, 'w') as file:
        json.dump(sprints, file, indent=4)

def agregar_sprint(sprints):
    sprint_id = input("ID del Sprint: ")
    nombre = input("Nombre: ")
    fecha_inicio = input("Fecha de Inicio: ")
    fecha_fin = input("Fecha de Fin: ")
    estado = input("Estado: ")
    objetivos = input("Objetivos: ")
    equipo = input("Equipo: ")
    nuevo_sprint = {
        "id": sprint_id,
        "nombre": nombre,
        "fecha_inicio": fecha_inicio,
        "fecha_fin": fecha_fin,
        "estado": estado,
        "objetivos": objetivos,
        "equipo": equipo,
        "tareas": []
    }
    sprints[sprint_id] = nuevo_sprint
    guardar_sprints(sprints, 'sprints.json')

def listar_sprints(sprints):
    for sprint_id, sprint in sprints.items():
        print(sprint)

def tareas_criticas(tareas, proyecto_id):
    if proyecto_id in tareas:
        print("Tareas críticas en postorden:")
        for tarea in postorden_tareas(tareas[proyecto_id]):
            if tarea["estado_actual"] != "Completado":
                print(tarea)
    else:
        print("No hay tareas para este proyecto.")

def postorden_tareas(tareas):
    res = []
    for tarea in tareas:
        res.extend(postorden_tareas(tarea["subtareas"]))
        res.append(tarea)
    return res

def listar_sprints_nivel(avl_tree, nivel):
    sprints = listar_sprints_nivel_aux(avl_tree, nivel, 0)
    for sprint in sprints:
        print(sprint)

def listar_sprints_nivel_aux(root, nivel, actual):
    if root is None:
        return []
    if actual == nivel:
        return [root.sprint]
    return (listar_sprints_nivel_aux(root.left, nivel, actual + 1) +
            listar_sprints_nivel_aux(root.right, nivel, actual + 1))

def mostrar_tareas_preorden(tareas):
    if isinstance(tareas, dict):
        for tarea in preorden_tareas(tareas):
            print(tarea)

def preorden_tareas(tareas):
    res = []
    for tarea in tareas:
        res.append(tarea)
        res.extend(preorden_tareas(tarea["subtareas"]))
    return res
"""                                                        
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


           
def menu():
    
    print("\n")
    print("-----MODULO DE GESTION DE EMPRESAS----")
    print("1. Crear empresa")
    print("2. Modificar empresa")
    print("3. Consultar empresa")
    print("4. Listar empresas")
    print("5. Eliminar empresa")
    print("\n")
    
    print("-----MODULO DE GESTION DE PROYECTOS----")
    print("6. Crear proyecto")
    print("7. Modificar proyeco")
    print("8. Consultar proyecto")
    print("9. Listar proyecto")
    print("10. Eliminar proyecto")
    print("\n")
    
    print("-----MODULO DE GESTION DE TAREAS Y PRIORIDADES----")
    print("11. Crear tarea")
    print("12. Modificar tarea")
    print("13. Consultar tarea")
    print("14. Listar tarea")
    print("15. Eliminar tarea y subtareas de la tarea")
    print("\n")
    
    print("-----MODULO DE GESTION DE SPRINTS----")
    print("16. Crear sprint")
    print("17. Editar sprint")
    print("18. Listar sprints")
    print("19. Eliminar sprint")

    
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
    gestion_empresas.cargar_datos("companie.csv")
    gestion_empresas.guardar_datos("companie.csv")
    
    proyecto_principal = Proyectos(
        0,
        "nombre",
        "descripcion",
        datetime.now(),
        datetime.now(),
        "estado_actual",
        "empresa",
        "gerente",
        "equipo",
    )
    projects_avl_tree = AVLTree()
    root = None
    
    proyecto_principal.load_from_json('tareas.json')
    
    
    #manejo el menu de opciones
    while True:
        menu()
        print("\n")
        opcion = input("Seleccione una opcion: ")
        
        if opcion=='1':
            id_empresa = int(input("Ingrese el ID de la empresa: "))
            nombre = input("Ingrese el nombre de la empresa: ")
            descripcion = input("Ingrese la descripción de la empresa: ")
            while True:
                try:
                    fecha_creacion = input("Ingrese la nueva fecha de creación (YYYY-MM-DD): ")
                    fecha_creacion = datetime.strptime(fecha_creacion, "%Y-%m-%d")
                    break  
                except ValueError:
                    print("Formato de fecha no válido. Intente de nuevo.")
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
            while True:
                try:
                    nueva_fecha_creacion = input("Ingrese la nueva fecha de creación (YYYY-MM-DD): ")
                    nueva_fecha_creacion = datetime.strptime(nueva_fecha_creacion, "%Y-%m-%d")
                    break  
                except ValueError:
                    print("Formato de fecha no válido. Intente de nuevo.")
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

        
        elif opcion == '6':
            # Add project
            id = input("Ingrese el ID del proyecto: ")
            nombre = input("Ingrese el nombre del proyecto: ")
            descripcion = input("Ingrese la descripcion: ")
            while True:
                try:
                    fecha_inicio = input("Ingrese la fecha de inicio (YYYY-MM-DD): ")
                    fecha_inicio = datetime.strptime(fecha_inicio, "%Y-%m-%d")
                    break  
                except ValueError:
                    print("Formato de fecha no válido. Intente de nuevo.")
            while True:
                try:
                    fecha_vencimiento = input("Ingrese la fecha de vencimiento (YYYY-MM-DD): ")
                    fecha_vencimiento = datetime.strptime(fecha_vencimiento, "%Y-%m-%d")
                    break  
                except ValueError:
                    print("Formato de fecha no válido. Intente de nuevo.")
            estado_actual = input("Ingrese el estado actual: ")
            empresa = input("Ingrese nombre de la empresa: ")
            gerente = input("Ingrese el gerente: ")
            equipo = input("Ingrese el equipo: ")
            proyecto = Proyectos(id, nombre, descripcion, fecha_inicio, fecha_vencimiento, estado_actual, empresa, gerente, equipo)
            root = projects_avl_tree.insert(root, proyecto)
            print("Proyecto agregado satisfactoriamente.")
        
        
        elif opcion == '7':
            project_id = input("Ingrese el ID del proyecto: ")
            project_node = projects_avl_tree.search(root, project_id)  
            if project_node:
                print("Deje en blanco los campos que no quiera cambiar")
                new_name = input("Ingrese el nuevo nombre: ")
                if new_name:
                    proyecto.nombre = new_name            
 
                new_descripcion = input("Ingrese la nueva descripcion: ")
                if new_descripcion:
                    proyecto.descripcion = new_descripcion
                    
                new_fecha_inicio= input("Ingrese la nueva fecha (YYYY-MM-DD): ")
                if new_fecha_inicio:
                    proyecto.fecha_inicio = new_fecha_inicio
                    
                new_fecha_vencimiento= input("Ingrese la nueva fecha (YYYY-MM-DD): ")
                if new_fecha_vencimiento:
                    proyecto.fecha_inicio = new_fecha_vencimiento
                    
                new_estado_actual= input("Ingrese el nuevo estado: ")
                if new_estado_actual:
                    proyecto.estado_actual = new_estado_actual
                    
                new_empresa= input("Ingrese la nueva empresa: ")
                if new_empresa:
                    proyecto.empresa = new_empresa
                    
                new_gerente= input("Ingrese el nuevo gerente: ")
                if new_empresa:
                    proyecto.gerente = new_gerente
                    
                new_equipo= input("Ingrese el nuevo equipo: ")
                if new_equipo:
                    proyecto.equipo = new_equipo
                print("Proyecto actualizado satisfactoriamente")       
            else:
                print("Proyecto no encontrado.")
        
        elif opcion == '8':
            project_id = input("Ingrese el ID del proyecto: ")
            project_node = projects_avl_tree.search(root, project_id)
            if project_node:
                proyecto = project_node.proyecto
                print(f"ID: {proyecto.id}")
                print(f"Nombre: {proyecto.nombre}")
                print(f"Descripción: {proyecto.descripcion}")
                print(f"Fecha de inicio: {proyecto.fecha_inicio.strftime('%Y-%m-%d')}")
                print(f"Fecha de vencimiento: {proyecto.fecha_vencimiento.strftime('%Y-%m-%d')}")
                print(f"Estado actual: {proyecto.estado_actual}")
                print(f"Empresa: {proyecto.empresa}")
                print(f"Gerente: {proyecto.gerente}")
                print(f"Equipo: {proyecto.equipo}")
            
            else:
                print("Proyecto no encontrado")
            
                
        elif opcion == '9':
            print("Proyectos en el árbol AVL (preorder): ")
            projects_avl_tree.preOrderCloseToDueDate(root)
        
        elif opcion == '10':
            project_id_to_delete = input("Ingrese el ID del proyecto a eliminar: ")
            root = projects_avl_tree.delete(root, project_id_to_delete)
            print("Proyecto eliminado satisfactoriamente")
            
        elif opcion == '11':
            id = input("Tarea ID: ")
            name = input("Tarea nombre: ")
            company = input("Nombre de la empresa: ")
            customer_company = input("Cliente: ")
            description = input("Descripcion: ")
            while True:
                try: 
                    start_date = input("Fecha de inicio (YYYY-MM-DD): ")
                    start_date = datetime.strptime(start_date, "%Y-%m-%d")
                    break
                except ValueError:
                    print("Formato de fecha no válido. Intente de nuevo.")
            while True:
                try:
                    due_date = input("Fecha de vencimiento(YYYY-MM-DD): ")
                    due_date = datetime.strptime(due_date, "%Y-%m-%d")
                    break
                except ValueError:
                    print("Formato de fecha no válido. Intente de nuevo")
            current_status = input("Estado actual: ")
            percentage = float(input("Porcentaje completado: "))
            parent_id = input("Parent Task ID (dejar en blanco si no hay parent task): ")
            parent_id = None if parent_id == '' else parent_id

            tarea = Tareas(id, nombre=name, empresa=company,cliente =customer_company, descripcion = description, fecha_inicio=start_date, fecha_vencimiento=due_date, estado_actual=current_status, porcentaje = percentage)
            proyecto_principal.add_task(tarea)
            print("Task added successfully.")
              
        
        elif opcion == '12':
            id = input("ID de la tarea a modificar: ")
            tarea = proyecto_principal.find_task(id)
            if tarea:
                print("Deje en blanco si no desea cambiar nada")
                name = input(f"Nuevo nombre [{tarea.nombre}]: ") or tarea.nombre
                company = input(f"Nueva empresa[{tarea.empresa}]: ") or tarea.empresa
                customer_company = input(f"Nuevo cliente[{tarea.cliente}]: ") or tarea.cliente
                description = input(f"Nueva descripcion [{tarea.descripcion}]: ") or tarea.descripcion
                start_date = input(f"Nueva fecha de inicio (YYYY-MM-DD) [{tarea.fecha_inicio.strftime('%Y-%m-%d')}]: ") or tarea.fecha_inicio.strftime('%Y-%m-%d')
                due_date = input(f"Nueva fecha de vencimiento (YYYY-MM-DD) [{tarea.fecha_vencimiento.strftime('%Y-%m-%d')}]: ") or tarea.fecha_vencimiento.strftime('%Y-%m-%d')
                current_status = input(f"Nuevo estado actual [{tarea.estado_actual}]: ") or tarea.estado_actual
                percentage_str = input(f"Nuevo porcentaje completado [{tarea.porcentaje}]: ")
                percentage = float(percentage_str) if percentage_str else tarea.porcentaje
                
                tarea.nombre = name
                tarea.empresa = company
                tarea.cliente = customer_company
                tarea.descripcion = description
                tarea.fecha_inicio = datetime.strptime(start_date, "%Y-%m-%d")
                tarea.fecha_vencimiento = datetime.strptime(due_date, "%Y-%m-%d")
                tarea.estado_actual = current_status
                tarea.porcentaje = percentage
                
                if proyecto_principal.update_task(tarea):
                    print("Task updated successfully.")
                else:
                    print("Failed to update the task.")
            else:
                print("Task not found.")
        
        elif opcion == '13':
            id = input("Task ID to view: ")
            tarea = proyecto_principal.find_task(id)
            if tarea:
                print(f"Tarea ID: {tarea.id}")
                print(f"Tarea Name: {tarea.nombre}")
                print(f"Empresa Name: {tarea.empresa}")
                print(f"Cliente: {tarea.cliente}")
                print(f"Descripcion: {tarea.descripcion}")
                print(f"Fecha de inicio: {tarea.fecha_inicio.strftime('%Y-%m-%d')}")
                print(f"Fecha de vencimiento: {tarea.fecha_vencimiento.strftime('%Y-%m-%d')}")
                print(f"Estado actual: {tarea.estado_actual}")
                print(f"Porcentaje completado: {tarea.porcentaje}%")
            else:
                print("Task not found.")
                
        elif opcion == '14':
            if proyecto_principal.tareas:  # Asegurarse de que hay tareas para mostraar
                for tarea in proyecto_principal.tareas:
                    print(f"Tarea ID: {tarea.id}")
                    print(f"Tarea Name: {tarea.nombre}")
                    print(f"Empresa Name: {tarea.empresa}")
                    print(f"Cliente: {tarea.cliente}")
                    print(f"Descripcion: {tarea.descripcion}")
                    print(f"Fecha de inicio: {tarea.fecha_inicio.strftime('%Y-%m-%d')}")
                    print(f"Fecha de vencimiento: {tarea.fecha_vencimiento.strftime('%Y-%m-%d')}")
                    print(f"Estado actual: {tarea.estado_actual}")
                    print(f"Porcentaje completado: {tarea.porcentaje}%")
                    print("-" * 40)  # Separador entre tareas
            else:
                print("No tasks found.")
                
        elif opcion == '15':
            id_tarea = input("Ingrese el ID de la tarea a eliminar: ")
            tarea_eliminada = proyecto_principal.delete_task(id_tarea)
            if tarea_eliminada:
                print("Tarea eliminada con éxito.")
            else:
                print("Tarea no encontrada.")
                   
                

if __name__ == "__main__":
    main()

