from classes.task import Task

StopApp = False
tasks = []



def add_task():
    print('Veuillez entrer le nom de votre tache :')
    name = input()
    print('Veuillez entrer la description de votre tache :')
    description = input()
    task = Task(name, description)
    tasks.append(task)
    print('Tache ajoutée avec succès !')

def list_tasks():
    for task in tasks:
        print(f'Nom : {task.name}')
        print(f'Description : {task.description}')
        print(f'Terminée : {task.completed}')

def mark_task_completed():
    print('Veuillez entrer le nom de la tache à marquer comme complétée :')
    for task in tasks:
        print(f'- {task.name}')
    name = input()
    for task in tasks:
        if task.name == name:
            task.mark_completed()
            print('Tache marquée comme complétée !')
            return
    print('Tache non trouvée !')

def home():
    print('Veuillez choisir une des options disponible ci-dessous :')
    print('\n\n1/ Ajouter une tache')
    print('2/ Lister mes taches')
    print('3/ Marquer une tache comme complétée')
    print('4/ Sortir de l application')
    choice = input()
    return choice



while StopApp == False:
    print('Bienvenue sur mon gestionnaire de taches')
    choice = home()
    if choice == '1':
        add_task()
    elif choice == '2':
        list_tasks()
    elif choice == '3':
        mark_task_completed()
    elif choice == '4':
        print('Merci d avoir utilisé mon application')
        StopApp = True
    else:
        print('Veuillez entrer une option valide')








    
