from datetime import datetime as dt

class Entry:
    def __init__(self, content, tags, next=None):
        self.content = content
        self.tags = tags
        self.next = next
        self.date = dt.now().strftime("%Y-%m-%d")

    def __str__(self):
        tags_str = " ".join("#" + tag for tag in self.tags)
        return f"[{self.date}] {self.content} {tags_str}"

class Journal:
    def __init__(self):
        self.head = None
        self.date_lookup = {}
        self.tag_index = {}
        self.sorted_dates = []

    def add_entry(self, content, tags):
        new_node = Entry(content, tags)

        if self.head != None:
            curr = self.head

            while curr.next != None:
                curr = curr.next 

            curr.next = new_node
        else:
            self.head = new_node

        self.date_lookup[new_node.date] = new_node

        for tag in tags:    
            if tag not in self.tag_index:
                self.tag_index[tag] = []
            self.tag_index[tag].append(new_node)
        
        self.sorted_dates.append(new_node.date)
        self.sorted_dates.sort()

    def search_by_date(self, date):
        l = 0
        r = len(self.sorted_dates) - 1

        found = False

        while l <= r:
            m = l + (r - l) // 2

            if date == self.sorted_dates[m]:
                found = True

                return self.date_lookup[self.sorted_dates[m]]
            elif self.sorted_dates[m] < date:
                l = m + 1
            else:
                r = m - 1
            
        if not found:
            print("Task was not found!")

    def filter_by_tag(self, tag):
        if tag not in self.tag_index:
            print("No tags found!")
        else:
            for entry in self.tag_index[tag]:
                print(entry)

    def list_entries(self):
        curr = self.head

        while curr is not None:
            print(curr)

            curr = curr.next