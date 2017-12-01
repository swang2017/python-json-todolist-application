
import json

class Task:
    def __init__(self, taskNumber, description, priority):
        self.taskNumber = taskNumber
        self.description = description
        self.priority = priority

    def toDictionary(self):
        return{"TaskID":self.taskNumber, "Task":self.description,"Priority":self.priority}


filename = 'todolist.json'

while True:

    with open(filename) as file_object:

        dictionaryArray= json.load(file_object)
        if len(dictionaryArray)== 0:
            count = 0
        else:
            count = dictionaryArray[len(dictionaryArray)-1]["TaskID"]


    input_options = raw_input("\nplease choose what you want to do: \n '1' to add task\n '2' to remove task\n '3' to view current tasks\n 'q' to quit the program\n")
    if input_options == "1":
        add_task = raw_input("please enter the task you want to add\n")
        add_priority=raw_input("please enter the priority\n")
        count += 1
        task1 = Task(count, add_task,add_priority)

        dictionaryArray.append(task1.toDictionary())
        with open(filename,"w") as file_object:
             json.dump(dictionaryArray,file_object)

        with open(filename) as file_object:

             dictionaryArray= json.load(file_object)
             for element in dictionaryArray:
                 t = Task(element["TaskID"], element["Task"], element["Priority"])
                 print(str(t.taskNumber) + ". - " +t.description + "(" +t.priority+")")

    elif input_options == "2":
        remove_task = int(raw_input("please enter the task number you want to remove\n"))
        for element in dictionaryArray:
            if remove_task == element["TaskID"]:
                dictionaryArray.remove(element)

        with open(filename,"w") as file_object:
            json.dump(dictionaryArray,file_object)

        with open(filename) as file_object:
            dictionaryArray= json.load(file_object)
            for element in dictionaryArray:
                t = Task(element["TaskID"], element["Task"], element["Priority"])
                print(str(t.taskNumber) + ". - " +t.description + "(" +t.priority+")")

    elif input_options == "3":
        with open(filename) as file_object:

             dictionaryArray= json.load(file_object)
             for element in dictionaryArray:
                 t = Task(element["TaskID"], element["Task"], element["Priority"])
                 print(str(t.taskNumber) + ". - " +t.description + "(" +t.priority+")")

    elif input_options == "q":
        break
