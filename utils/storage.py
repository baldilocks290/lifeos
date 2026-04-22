import json
import os
from models.goal import GoalList, Goal
from models.journal import Journal
from models.task import TaskList

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TASKS_FILE = os.path.join(BASE_DIR, "data", "tasks.json")
JOURNAL_FILE = os.path.join(BASE_DIR, "data", "journal.json")
GOAL_FILE = os.path.join(BASE_DIR, "data", "goals.json")

def save_tasks(task_list):
    os.makedirs(os.path.dirname(TASKS_FILE), exist_ok=True)
    
    curr = task_list.head
    node_list = []

    while curr is not None:
        node_list.append({
            "Name": curr.name,
            "Priority": curr.priority,
            "Due Date": curr.due_date,
            "Tags": curr.tags,
            "Created At": curr.created_at,
            "Completed": curr.completed,
        })

        curr = curr.next

    with open(TASKS_FILE, "w") as f:
        json.dump(node_list, f)


def load_tasks():
    task_list = TaskList()

    try:
        with open(TASKS_FILE, "r") as f:
            data = json.load(f)

        for task in data:
            task_list.add(task["Name"], task["Priority"], task["Due Date"], task["Tags"])

        return task_list
    except (FileNotFoundError, json.JSONDecodeError):
        return TaskList()
    

def save_journal(journal: Journal):
    os.makedirs(os.path.dirname(JOURNAL_FILE), exist_ok=True)

    curr = journal.head
    node_list = []

    while curr is not None:
        node_list.append({
            "Content": curr.content,
            "Tags": curr.tags,
            "Date": curr.date
        })

        curr = curr.next

    with open(JOURNAL_FILE, "w") as f:
        json.dump(node_list, f)


def load_journal():
    journal = Journal()

    try:
        with open(JOURNAL_FILE, "r") as f:
            data = json.load(f)

        for journals in data:
            journal.add_entry(journals["Content"], journals["Tags"])

        return journal
    except (FileNotFoundError, json.JSONDecodeError):
        return Journal()


def save_goals(goals: Goal):
    os.makedirs(os.path.dirname(GOAL_FILE), exist_ok=True)

    curr = goals.head
    node_list = []

    while curr is not None:
        milestones = []
        milestones_curr = curr.head

        while milestones_curr is not None:
            milestones.append({
                "Title": milestones_curr.title,
                "Completed": milestones_curr.completed
            })

            milestones_curr = milestones_curr.next

        node_list.append({
            "Title": curr.title,
            "Description": curr.description,
            "Created At": curr.created_at,
            "Milestones": milestones
        })

        curr = curr.next

    with open(GOAL_FILE, "w") as f:
        json.dump(node_list, f)


def load_goals():
    goals = GoalList()

    try:
        with open(GOAL_FILE, "r") as f:
            data = json.load(f)

        for goal in data:
            goals.add(goal["Title"], goal["Description"])
            goal_obj = goals.title_lookup[goal["Title"]]

            for milestones in goal["Milestones"]:
                goal_obj.add_milestone(milestones["Title"])
                if milestones["Completed"]:
                    goal_obj.complete_milestone(milestones["Title"])

        return goals
    except (FileNotFoundError, json.JSONDecodeError):
        return GoalList()