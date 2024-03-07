class Employee:
    all_employees = {}
    global_task_counter = 0

    def __init__(self, name):
        self.name = name
        self.finished_tasks = {}
        self.unfinished_tasks = {}
        Employee.all_employees[name] = self

class TaskManager:
    def add_order(self):
        description = input("description: ")
        programmer, workload = input("programmer and workload estimate: ").split()

        if programmer in Employee.all_employees:
            employee = Employee.all_employees[programmer]
        else:
            employee = Employee(programmer)

        # Increment the global task counter
        Employee.global_task_counter += 1
        task_id = Employee.global_task_counter

        if employee.name in employee.unfinished_tasks:
            employee.unfinished_tasks[employee.name].append([task_id, description, workload])
        else:
            employee.unfinished_tasks[employee.name] = [[task_id, description, workload]]

        print("added!")

    def status_of_programmer(self):
        programmer_name = input("programmer: ")
        if programmer_name in Employee.all_employees:
            employee = Employee.all_employees[programmer_name]
            finished_tasks_count = len(employee.finished_tasks.get(programmer_name, []))
            unfinished_tasks_count = len(employee.unfinished_tasks.get(programmer_name, []))
            finished_hours = sum(int(task[2]) for task in employee.finished_tasks.get(programmer_name, []))
            unfinished_hours = sum(int(task[2]) for task in employee.unfinished_tasks.get(programmer_name, []))
            print(f"programmer: {employee.name}")
            print(f"tasks: finished {finished_tasks_count} not finished {unfinished_tasks_count}, hours: done {finished_hours} scheduled {unfinished_hours}")
        else:
            print("programmer not found")


    def list_finished_tasks(self):
        if any(employee.finished_tasks for employee in Employee.all_employees.values()):
            for employee in Employee.all_employees.values():
                for task in employee.finished_tasks.get(employee.name, []):
                    task_id, description, workload = task
                    print(f"{task_id}: {description} ({workload} hours), programmer {employee.name} FINISHED")
        else:
            print("no finished tasks")

    def list_unfinished_tasks(self):
        for employee in Employee.all_employees.values():
            for task in employee.unfinished_tasks.get(employee.name, []):
                task_id, description, workload = task
                print(f"{task_id}: {description} ({workload} hours), programmer {employee.name} NOT FINISHED")

    def mark_task_as_finished(self):
        task_id = int(input("id: "))

        for employee in Employee.all_employees.values():
            for task in employee.unfinished_tasks.get(employee.name, []):
                if task_id == task[0]:
                    employee.finished_tasks.setdefault(employee.name, []).append(task)
                    employee.unfinished_tasks[employee.name].remove(task)
                    print("marked as finished")
                    return
        print("task not found")

    def list_programmers(self):
        for name in Employee.all_employees:
            print(name)



class Display:
    def __init__(self):
        self.task_manager = TaskManager()

    def menu(self):
        print("commands:")
        print("0 exit")
        print("1 add order")
        print("2 list finished tasks")
        print("3 list unfinished tasks")
        print("4 mark task as finished")
        print("5 programmers")
        print("6 status of programmer")

    def execute(self):
        self.menu()

        while True:
            print()
            command = input("command: ")

            if command == "0":
                break
            elif command == "1":
                self.task_manager.add_order()
            elif command == "2":
                self.task_manager.list_finished_tasks()
            elif command == "3":
                self.task_manager.list_unfinished_tasks()
            elif command == "4":
                self.task_manager.mark_task_as_finished()
            elif command == "5":
                self.task_manager.list_programmers()
            elif command == "6":
                self.task_manager.status_of_programmer()  # causing problem

d = Display()
d.execute()
