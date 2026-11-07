from tasks import show_tasks, save_tasks, load_tasks
from dotenv import load_dotenv 
import os 

load_dotenv()


name = input("enter your name: ")
print("welcome", name)
admin_mod = input("do you want admin mod? yes/no: ")
if admin_mod == "yes":
    password = input("enter admin password : ")
    if password == os.getenv("admin_pass"):
        print("admin mod in on ")
    else:
        print("wrong password")
task = load_tasks()
how_many = int(input("how many task do you want to do ? : "))

for i in range(how_many):
    task_name = input("enter a task: ")
    priority = input("emter a priority (low,mediom high) : ").lower()
    tasks ={
        "name"  : task_name,
        "priority": priority
    }
    task.append(task)

show_tasks(task)
save_tasks(task)
load_tasks()
