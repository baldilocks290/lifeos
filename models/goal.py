from datetime import datetime as dt

class Milestone:
    def __init__(self, title, next=None):
        self.title = title
        self.next = next
        self.completed = False

    def __str__(self):
        status = "✓" if self.completed else " "
        return f"[{status}] {self.title}"
    

class Goal:
    def __init__(self, title, description, next=None):
        self.title = title
        self.description = description
        self.created_at = dt.now().strftime("%Y-%m-%d %H:%M")
        self.next = next
        self.completed = False 
        self.head = None

    def add_milestone(self, title):
        new_node = Milestone(title)

        if self.head != None:
            curr = self.head

            while curr.next != None:
                curr = curr.next

            curr.next = new_node
        else:
            self.head = new_node

    def complete_milestone(self, title):
        curr = self.head
        found = False

        while curr is not None:
            if curr.title == title:
                curr.completed = True
                found = True
                break
            curr = curr.next

        if not found:
            print("Milestone not found!")

    def _check_milestone(self, node):
        if node is None:
            return True
        if not node.completed:
            return False
        return self._check_milestone(node.next)

    def is_complete(self):
        return self._check_milestone(self.head)

    def __str__(self):
        total = 0
        complete = 0
        curr = self.head
        milestone_str = ""

        while curr is not None:
            milestone_str += str(curr) + "\n"
            total += 1
            if curr.completed == True:
                complete += 1

            curr = curr.next


        return f"🎯 {self.title}\n{self.description}\nProgress: {complete}/{total} milestones done\n{milestone_str}"
    

class GoalList:
    def __init__(self):
        self.head = None
        self.title_lookup = {}
        self.sorted_titles = []

    def add(self, title, description):
        new_node = Goal(title, description)

        if self.head != None:
            curr = self.head

            while curr.next != None:
                curr = curr.next

            curr.next = new_node
        else:
            self.head = new_node

        self.title_lookup[title] = new_node
        self.sorted_titles.append(title)
        self.sorted_titles.sort()

    def delete(self, title):
        prev = None
        curr = self.head

        if title not in self.title_lookup:
            print("No goal found!")
        else:
            while curr is not None:
                if prev is None and curr.title == title:
                    self.head = curr.next
                    break
                elif curr.title == title:
                    prev.next = curr.next
                    break
                else:
                    curr = curr.next

            self.sorted_titles.remove(title)
            self.title_lookup.pop(title)

    def list_goals(self):
        curr = self.head

        while curr is not None:
            print(curr)

            curr = curr.next

    def search(self, keyword):
        l = 0
        r = len(self.sorted_titles) - 1
        found = False

        while l <= r:
            m = l + (r - l) // 2

            if keyword == self.sorted_titles[m]:
                found = True

                return self.title_lookup[self.sorted_titles[m]]
            elif keyword < self.sorted_titles[m]:
                r = m - 1
            else:
                l = m + 1

        if not found:
            print("Goal not found!")