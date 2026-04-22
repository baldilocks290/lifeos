from models.stats import Stats
import matplotlib.pyplot as plt

def show_priority_chars(stats: Stats):
    df = stats.get_tasks_by_priority()
    plt.bar(df.index, df.values)
    plt.title("TASKS BY PRIORITY")
    plt.xlabel("PRIORITY")
    plt.ylabel("TASKS")
    plt.show()

def show_tag_chart(stats: Stats):
    df = stats.get_tasks_by_tags()
    plt.bar(df.index, df.values)
    plt.title("TASKS BY TAGS")
    plt.xlabel("TAGS")
    plt.ylabel("TASKS")
    plt.show()

def show_completion_chart(stats: Stats):
    df = stats.get_completion_rate()

    if df["completed"] == 0 and df["pending"] == 0:
        print("No tasks to display!")
        return

    plt.pie(df.values(), labels=df.keys(), autopct="%1.1f%%")
    plt.title("COMPLETED TASKS")
    plt.show()