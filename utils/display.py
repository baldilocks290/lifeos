from rich.console import Console
from rich.table import Table
from rich.text import Text
from rich.panel import Panel
from datetime import datetime as dt
from rich import box

console = Console()

def print_welcome():
    content = Text(justify="center")
    content.append("L I F E O S\n", style="bold")
    content.append("─────────────\n")
    content.append("\nYour personal life manager\n")
    content.append(dt.now().strftime("\n📅 %B %d, %Y\n"))
    content.append("\nPress enter to continue...")

    console.print(Panel(content, box=box.ROUNDED, padding=(1, 4), width=45))
    input("")

def print_menu():
    table = Table(box=box.ROUNDED)
    table.add_column("Key", width=6)
    table.add_column("Action")

    table.add_row("1", "ToDo")
    table.add_row("2", "Stats")
    table.add_row("3", "Journal")
    table.add_row("4", "Goals")
    table.add_row("5", "Exit")

    console.print(table)


def print_todo_sub_menu():
    table = Table(title="ToDo", box=box.ROUNDED, title_style="None")
    table.add_column("Key", width=6)
    table.add_column("Action")

    table.add_row("1", "Add Task")
    table.add_row("2", "Delete Task")
    table.add_row("3", "Complete Task")
    table.add_row("4", "Undo Complete")
    table.add_row("5", "Filter By Tag")
    table.add_row("6", "Filter By Priority")
    table.add_row("7", "View Tasks")
    table.add_row("8", "Back")
    
    console.print(table)


def print_stats_sub_menu():
    table = Table(title="Stats", box=box.ROUNDED, title_style="None")
    table.add_column("Key", width=6)
    table.add_column("Action")

    table.add_row("1", "View Priority Tasks")
    table.add_row("2", "View Tagged Tasks")
    table.add_row("3", "View Completed Tasks")
    table.add_row("4", "Back")

    console.print(table)


def print_journal_sub_menu():
    table = Table(title="Journal", box=box.ROUNDED, title_style="None")
    table.add_column("Key", width=6)
    table.add_column("Action")

    table.add_row("1", "Add Entry")
    table.add_row("2", "List Entries")
    table.add_row("3", "Search By Date")
    table.add_row("4", "Filter By Tag")
    table.add_row("5", "Back")

    console.print(table)


def print_goal_sub_menu():
    table = Table(title="Goals", box=box.ROUNDED, title_style="None")
    table.add_column("Key", width=6)
    table.add_column("Action")

    table.add_row("1", "Add Goal")
    table.add_row("2", "Add milestone to goal")
    table.add_row("3", "Complete milestone")
    table.add_row("4", "List Goals")
    table.add_row("5", "Search Goal")
    table.add_row("6", "Back")

    console.print(table)


def display_tasks(task_list):
    curr = task_list.head
    counter = 1

    table = Table(box=box.ROUNDED)
    table.add_column("ID", width=6)
    table.add_column("Task")
    
    while curr is not None:
        table.add_row(str(counter), curr.name)
        curr = curr.next
        counter += 1

    console.print(table)