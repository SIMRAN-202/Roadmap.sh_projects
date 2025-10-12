import json
import argparse
import os
from datetime import datetime

# Make a parser
pars = argparse.ArgumentParser (
    prog='Received Add task command',
    description='Add a command will be used for adding task in tracker',
    epilog='Example usage: python3 tracker.py filename.json -a "New Task"'
)

# Adding argument
pars.add_argument('-a', '--add', help='Fill it to add the task', required=False)
pars.add_argument('-l', '--list', help='type -l "todo" or "in progress" or "done" or "all" for showing tasks', required=False)
pars.add_argument('-p', '--pick', help='Pick which id you want to look', required=False)
pars.add_argument(
    '-u', '--update', help='Type new description or something you want', required=False)
pars.add_argument(
    '-m', '--mark', help='Type "in progress" or "done"', required=False)
pars.add_argument(
    '-d', '--delete', help='Delete', required=False)

# Processing the argument
args = pars.parse_args()

# Make a condition between pick and update

# Accessing to the arguments
print(f'Added: {args.add if args.add else "No task(s) added"}')
print(f'List: {args.list if args.list else "No list(s) choosed"}')
print(f'id: {args.pick if args.pick else "No id choosed"}')
print(f'update: {args.update if args.update else "Nothing updated lately"}')
print(f'mark: {args.mark if args.mark else "Nothing marked in here"}')
print(f'delete: {args.delete if args.delete else "There is no item"}')

file_path = "task_tracker.json"

# Date Format to dd-mm-yy HH:MM
time = datetime.now()
formatted_time = time.strftime('%H:%M %d %B %Y')

# List the Tasks
def show_tasks_list(status):
    with open('task_tracker.json', 'r') as file:
        data = json.load(file)
        
    if status == 'all':
        #This status will show all the tasks 
        print("All tasks has been shown")
        print(json.dumps(data, indent=4))
        
    elif status == 'todo':
        #This status will show the todo list
        todo_tasks = [task for task in data if task.get('status')== 'todo']
        print('Todo List Tasks has been shown')
        print(json.dumps(todo_tasks, indent=4))
        
    elif status == 'in progress':
        # This will show all task 'in progress'
        in_progress_tasks = [
            task for task in data if task.get('status') == 'in progress']
        print('In Progress Tasks has been shown')
        print(json.dumps(in_progress_tasks, indent=4))

    elif status == 'done':
        # This will show all task 'done'
        tasks_done = [task for task in data if task.get('status') == 'done']
        print('Done Tasks has been shown')
        print(json.dumps(tasks_done, indent=4))

    else:
        print('There is no data about that..')
        exit()
        
# Get to know the task based on 'id' and update description
def update_task_id():
    with open('task_tracker.json', 'r') as file:
        data = json.load(file)
        
        task_found = False
        for task in data:
            if task['id'] == int(args.pick):
                task['description'] = str(args.update)
                task['updatedAt'] = formatted_time
                task_found = True
                break

        if task_found:
            # Save the updated data to json
            with open('task_tracker.json', 'w') as file:
                json.dump(data, file, indent=4)
            print(f'Task description from id {args.pick}')
            print(f'has been updated to {args.update}')
            
        else:
            print('There is something wrong with your arguments')
            exit()
            
# Get task based on 'id' and mark status on task tracker
def mark_task_id():
    with open('task_tracker.json', 'r') as file:
        data = json.load(file)
        
        task_found = False
        for task in data:
            if task['id'] == int(args.pick):
                task['status'] = str(args.mark)
                task['updatedAt'] = formatted_time
                task_found = True
                break

        if task_found:
            # Save update to json file
            with open('task_tracker.json', 'w') as file:
                json.dump(data, file, indent=4)
            print(f'Task status from id {args.pick}')
            print(f'has been marked {args.mark}')
            
        else:
            print('There is something wrong with your arguments')
            exit()
            
# Insert an arguments into a JSON file
def add_into_json():
    # value args.add into variable named task(s)
    tasks = args.add
    # make a condition if json file didn't exist then make a new one
    if not os.path.exists(file_path):
        # turn task into a dictionary because of new json file
        tasks = [
            {
                'id': 1,
                'description': args.add,
                'status': 'todo',
                'createdAt': formatted_time,
                'updatedAt': formatted_time
            }
        ]
        with open(file_path, 'w') as file:
            json.dump(tasks, file, indent=4)

    # if the item is exist, add into existing json
    else:
        with open(file_path, 'r') as file:
            data = json.load(file)
            # Getting last id from json file
            last_id = max(item['id'] for item in data) if data else 0
            new_task = {
                'id': last_id + 1,
                'description': args.add,
                'status': 'todo',
                'createdAt': formatted_time,
                'updatedAt': formatted_time
            }
            data.append(new_task)
            # data['description'] = tasks

        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
            
# Delete the item based on id 
def delete_task_baseon_id():
    with open('test_tasks.json', 'r') as file:
        data = json.load(file)

        task_to_remove = None
        for task in data:
            if task['id'] == int(args.pick):
                task_to_remove = task
                task_found = True
                break

        if task_to_remove:
            data.remove(task_to_remove)
            # Save update to json
            with open('test_tasks.json', 'w') as file:
                json.dump(data, file, indent=4)
            print(f'Task status from id {args.pick}')
            print(f'has been deleted {args.delete}')


if args.add:
    add_into_json()

elif args.list:
    show_tasks_list(str(args.list))

elif args.pick:
    if args.update:
        update_task_id()
    elif args.mark:
        mark_task_id()
    elif args.delete:
        delete_task_baseon_id()
    else:
        pars.error('For pick, you must specify either --update or --mark')

else:
    exit()

        