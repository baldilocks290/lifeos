import pandas as pd
from models.task import TaskList

class Stats:
    def __init__(self, task_list: TaskList):
        self.task_list = task_list

    def get_tasks_by_priority(self):
        curr = self.task_list.head

        priorities = []
        
        while curr is not None:
            priorities.append(curr.priority)
            curr = curr.next

        df = pd.Series(priorities).value_counts()

        return df
    
    def get_tasks_by_tags(self):
        curr = self.task_list.head

        tags = []

        while curr is not None:
            tags.extend(curr.tags)
            curr = curr.next

        df = pd.Series(tags).value_counts()

        return df

    def get_completion_rate(self):
        curr = self.task_list.head

        count = 0
        while curr is not None:
            count += 1
            curr = curr.next

        return {
            "completed": len(self.task_list.undo_stack),
            "pending": count
        }