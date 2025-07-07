import datetime
import json
import os
import datetime

FILENAME = "tareas.json"
EXPORT_FILENAME = "tareas_exportadas.json"

# Estructura para almacenar las tareas
todo_list = []
task_id_counter = 1

# Función para agregar una nueva tarea
def add_task():
    global task_id_counter
    title = input("Título de la tarea: ")
    description = input("Descripción: ")
    created_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    task = {
        "id": task_id_counter,
        "title": title,
        "description": description,
        "completed": False,
        "created_at": created_at
    }
    todo_list.append(task)
    print("Tarea agregada con éxito.\n")
    task_id_counter += 1

# Función para listar todas las tareas
def list_tasks():
    if len(todo_list)==0:
        print("No hay tareas en la lista.\n")
    else:
        for task in todo_list:
            status = "✅" if task["completed"] else "❌"
            print(f"ID: {task['id']} | {status} {task['title']}")
            print(f"   Descripción: {task['description']}")
            print(f"   Fecha de creación: {task['created_at']}\n")
    

# Función para marcar una tarea como completada
def complete_task():
    task_id = int(input("Ingrese el ID de la tarea completada: "))
    for task in todo_list:
        if task["id"] == task_id:
            task["completed"] = True
            print("Tarea marcada como completada.\n")
        else:
            print("Tarea no encontrada.\n")

# Función para limpiar toda la lista de tareas
def clear_tasks():
    global todo_list
    confirm = input("¿Estás seguro que deseas eliminar todas las tareas? (s/n): ")
    if confirm.lower() == 's':
        todo_list = []
        print("Lista de tareas eliminada.\n")
    else:
        print("Acción cancelada.\n")
        
#Contar tareas completadas y pendientes
def count_tasks():
    completed = sum(task["completed"] for task in todo_list)
    pending = len(todo_list) - completed
    print("\n Resumen de tareas:")
    print("✅ Completadas:\n",completed)
    print("❌ Pendientes: \n",pending)

#Exportar la lista de tareas a un archivo .json
def export_tasks():
    if not todo_list:
        print("📭 No hay tareas para exportar.\n")
        return
    with open(EXPORT_FILENAME, "w", encoding="utf-8") as f:
        json.dump(todo_list, f, indent=4, ensure_ascii=False)
    print(f"Tareas exportadas correctamente a '{EXPORT_FILENAME}'.\n")
    
    
# Menú principal
def main():
    while True:
        print("\n^^^ GESTOR DE TAREAS ^^^")
        print("1. Agregar tarea")
        print("2. Listar tareas")
        print("3. Marcar tarea como completada")
        print("4. Limpiar lista de tareas")
        print("5. Contar tareas completadas y pendientes")
        print("6. Exportar lista de tareas a JSON")
        print("7. Salir")

        choice = input("Seleccione una opción (1-7): ")

        
        if choice == "1":
            add_task()
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            clear_tasks()
        elif choice == "5":
            count_tasks()
        elif choice == "6":
            export_tasks()
        elif choice == "7":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente de nuevo.\n")

if __name__ == "__main__":
    main()
