from datetime import datetime as dt

class Task:
    def __init__(self, name, priority, due_date, tags, next=None):
        self.name = name
        self.priority = priority
        self.due_date = due_date
        self.tags = tags
        self.created_at = self.created_at = dt.now().strftime("%Y-%m-%d %H:%M")
        self.next = next
        self.completed = False

    def __str__(self):
        tags_str = " ".join("#" + tag for tag in self.tags)
        return f"[{self.priority}] {self.name} (due: {self.due_date}) {tags_str}"
    

class TaskList:
    def __init__(self):
        self.head = None
        self.name_lookup = {}
        self.priority_queues = {}
        self.sorted_names = []
        self.undo_stack = []

    def add(self, name, priority, due_date, tags):
        created_at = dt.now().strftime("%Y-%m-%d %H:%M")
        new_node = Task(name, priority, due_date, tags, created_at)

        if self.head != None:
            curr = self.head

            while curr.next != None:
                curr = curr.next 

            curr.next = new_node
        else:
            self.head = new_node

        self.name_lookup[name] = new_node

        if priority not in self.priority_queues:
            self.priority_queues[priority] = []
        self.priority_queues[priority].append(new_node)
        
        self.sorted_names.append(name)
        self.sorted_names.sort()

    def delete(self, name):
        prev = None
        curr = self.head

        if name not in self.name_lookup:
            print("No task found!")
        else:
            while curr is not None:
                if prev is None and curr.name == name:
                    self.head = curr.next
                    break
                elif curr.name == name:
                    prev.next = curr.next
                    break
                else:
                    curr = curr.next

            priority = self.name_lookup[name].priority

            self.priority_queues[priority].remove(self.name_lookup[name])
            self.sorted_names.remove(name)
            self.name_lookup.pop(name)

    def complete(self, name):
        if name in self.name_lookup:
            self.name_lookup[name].completed = True 
            self.undo_stack.append(self.name_lookup[name])

            self.delete(name)
        else:
            print("Task does not exist!")

    def undo_complete(self):
        if len(self.undo_stack) != 0:
            task = self.undo_stack.pop()

            self.add(task.name, task.priority, task.due_date, task.tags)
        else:
            print("Nothing to undo!")

    def search(self, keyword):
        l = 0
        r = len(self.sorted_names) - 1

        found = False

        while l <= r:
            m = l + (r - l) // 2

            if keyword == self.sorted_names[m]:
                found = True

                return self.name_lookup[self.sorted_names[m]]
            elif keyword < self.sorted_names[m]:
                r = m - 1
            else:
                l = m + 1 

        if not found:            
            print("Task not found!")

    def list_tasks(self):
        curr = self.head

        while curr is not None:
            print(curr)
            
            curr = curr.next

    def filter_by_tag(self, tag):
        curr = self.head

        while curr is not None:
            if tag in curr.tags:
                print(curr)

            curr = curr.next
            
    def filter_by_priority(self, priority):
        curr = self.head

        while curr is not None:
            if curr.priority == priority:
                print(curr) 
            
            curr = curr.next