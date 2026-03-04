task = int(input("Enter task: "))
number_of_workers = int(input("Enter number of workers: "))
task_per_worker = task / number_of_workers
remainder = task % number_of_workers
print(f"Each worker will do {task_per_worker} tasks and the remainder will be {remainder}")