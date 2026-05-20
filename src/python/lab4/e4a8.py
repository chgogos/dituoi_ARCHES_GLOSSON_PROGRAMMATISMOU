class TodoList:
    def __init__(self, title):
        self.title = title
        self.todos = []

    def add(self, item_description):
        todo = Todo(item_description)
        self.todos.append(todo)

    def stats(self):
        stats_dict = {"open": 0, "completed": 0}
        for todo in self.todos:
            if todo.completed:
                stats_dict["completed"] += 1
            else:
                stats_dict["open"] += 1
        print(stats_dict)


class Todo:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def toggle(self):
        self.completed = not self.completed

    def __repr__(self):
        return f"description={self.description} completed={self.completed}"


def main():
    tdl = TodoList("groceries")
    tdl.add("milk")
    tdl.add("bread")
    print(tdl.todos)
    tdl.todos[0].toggle()
    tdl.stats()


if __name__ == "__main__":
    main()
