import os, time
from models.stats import Stats
from utils.storage import load_tasks, save_tasks, save_journal, load_journal, save_goals, load_goals
from utils.display import display_tasks, print_menu, print_stats_sub_menu, print_journal_sub_menu, print_goal_sub_menu, print_welcome, print_todo_sub_menu
from utils.charts import show_completion_chart, show_priority_chars, show_tag_chart

task_list = load_tasks()
journal_list = load_journal()
goal_list = load_goals()
stats = Stats(task_list)

print_welcome()

os.system('cls')

while True:
    print_menu()

    option = input("What do you want to do?: ")

    match option:
        case "1":
            os.system('cls')

            while True:
                print_todo_sub_menu()
                todo_sub_option = input("What do you want to do?: ")

                match todo_sub_option:
                    case "1":
                        name = input("Add task name: ")
                        try:
                            priority = int(input("Enter priority (1-3): "))
                            
                            if priority > 3 or priority < 1:
                                print("Please enter a valid number!")
                                continue
                        except ValueError:
                            print("Please enter a valid number!")
                            continue
                        due_date = input("Enter due date: ")
                        tags = input("Enter tags (comma separated): ").split(",")

                        tags = [tag.strip() for tag in tags]
                        task_list.add(name, priority, due_date, tags)
                    case "2":
                        name = input("Enter a task to delete: ")
                        task_list.delete(name)
                        time.sleep(1)
                        print(f"Successfully deleted {name}!")
                    case "3":
                        name = input("Enter a task to mark complete: ")
                        task_list.complete(name)
                        time.sleep(1)
                        print(f"Successfully completed {name}!")
                    case "4":
                        task_list.undo_complete()
                        time.sleep(1)
                        print(f"Successfully undid last completed task!")
                    case "5":
                        tags = input("Enter what tags to filter through: ")
                        
                        print()
                        task_list.filter_by_tag(tags)
                        print()
                    case "6":
                        try:
                            priority = int(input("Enter what priority to filter through: "))
                        
                            if priority > 3 or priority < 1:
                                print("Please enter a valid number!")
                                continue
                        except ValueError:
                            print("Please enter a valid number!")
                            continue

                        task_list.filter_by_priority(priority)
                    case "7":
                        print()
                        display_tasks(task_list)
                        print()
                    case "8":
                        os.system('cls')

                        break
                    case _:
                        print("Please enter a valid option!")
                        continue
        case "2":
            os.system('cls')

            while True:
                print_stats_sub_menu()
                stats_sub_option = input("What do you want to do?: ")

                match stats_sub_option:
                    case "1":
                        show_priority_chars(stats)
                    case "2":
                        show_tag_chart(stats)
                    case "3":
                        show_completion_chart(stats)
                    case "4":
                        os.system('cls')

                        break
                    case _:
                        print("Please enter a valid option!")
                        continue
        case "3":
            os.system('cls')

            while True:
                print_journal_sub_menu()
                journal_sub_option = input("What do you want to do?: ")

                match journal_sub_option:
                    case "1":
                        content = input("Add content: ")
                        tags = input("Enter tags (comma separated): ").split(",")
                        tags = [tag.strip() for tag in tags]

                        journal_list.add_entry(content, tags) 
                    case "2":
                        journal_list.list_entries()
                    case "3":
                        date = input("Enter date: ")

                        print(journal_list.search_by_date(date))
                    case "4":
                        tag = input("Enter what tag to filter by: ")

                        journal_list.filter_by_tag(tag)
                    case "5":
                        os.system('cls')

                        break
                    case _:
                        print("Please enter a valid option")
                        continue
        case "4":
            os.system('cls')

            while True:
                print_goal_sub_menu()
                goal_sub_option = input("What do you want to do?: ")

                match goal_sub_option:
                    case "1":
                        title = input("Enter your title: ")
                        desc = input("Enter your description: ")

                        goal_list.add(title, desc)
                    case "2":
                        title = input("Enter goal title: ")
                        if title in goal_list.title_lookup:
                            milestone_title = input("Enter milestone title: ")
                            goal_list.title_lookup[title].add_milestone(milestone_title)
                        else:
                            print("Goal not found!")
                    case "3":
                        title = input("Enter the goal title: ")
                        if title in goal_list.title_lookup:
                            milestone_title = input("Enter milestone to complete: ")
                            goal_list.title_lookup[title].complete_milestone(milestone_title)
                        else:
                            print("Goal not found!")
                    case "4":
                        goal_list.list_goals()
                    case "5":
                        keyword = input("Enter a goal to search for: ")
                        result = goal_list.search(keyword)
                        if result:
                            print(result)
                    case "6":
                        os.system('cls')

                        break
                    case _:
                        print("Please enter a valid option")
                        continue
        case "5":
            save_tasks(task_list)
            save_journal(journal_list)
            save_goals(goal_list)

            os.system('cls')

            exit()
        case _:
            print("Please enter a valid option!")
            continue