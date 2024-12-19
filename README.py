help = """
help - напечатать справку по прогррамме
add - добавить задачу в список
show - напечатать все добавленные задачи.
exit - выход """
tasks = []

run = True
while run == True:
    command = input("Введите команду ")

    if command == "help":
        print(help)
    elif command == "show":
        print(task)
    elif command == "add":
        task = input("Введите название задачи: ")
        tasks.append(task)
        print("Задача добавлена ")
    elif command == "exit":
        run = False
    else:
        print("Неизвестная команда ")

