## Vienkāršs uzdevumu saraksts

import unittest
from dataclasses import dataclass


@dataclass
class Task:
    title: str
    done: bool = False


class TodoList:
    def __init__(self):
        self.tasks = []

    def add(self, title):
        title = title.strip()
        if not title:
            raise ValueError("Uzdevuma nosaukums nedrīkst būt tukšs")
        task = Task(title)
        self.tasks.append(task)
        return task

    def _get(self, number):
        # lietotājs skaita no 1 un saraksts no 0
        if number < 1 or number > len(self.tasks):
            raise IndexError(f"Nav uzdevuma ar numuru {number}")
        return self.tasks[number - 1]

    def complete(self, number):
        task = self._get(number)
        task.done = True
        return task

    def remove(self, number):
        task = self._get(number)
        self.tasks.remove(task)
        return task

    def pending(self):
        return [t for t in self.tasks if not t.done]

    def stats(self):
        total = len(self.tasks)
        done = total - len(self.pending())
        percent = round(done / total * 100) if total else 0
        return {"total": total, "done": done, "percent": percent}

    def format(self):
        if not self.tasks:
            return "Saraksts ir tukšs."
        lines = []
        for i, task in enumerate(self.tasks, start=1):
            mark = "x" if task.done else " "
            lines.append(f"{i}. [{mark}] {task.title}")
        return "\n".join(lines)


MENU = """
1 - Pievienot uzdevumu
2 - Atzīmēt kā izpildītu
3 - Dzēst uzdevumu
4 - Parādīt sarakstu
5 - Statistika
0 - Iziet"""


def ask_number(prompt):
    try:
        return int(input(prompt))
    except ValueError:
        print("Jāievada skaitlis.")
        return None


def main():
    todo = TodoList()
    while True:
        print(MENU)
        choice = input("Izvēle: ").strip()
        try:
            if choice == "1":
                task = todo.add(input("Nosaukums: "))
                print(f"Pievienots: {task.title}")
            elif choice == "2":
                number = ask_number("Uzdevuma numurs: ")
                if number is not None:
                    print(f"Izpildīts: {todo.complete(number).title}")
            elif choice == "3":
                number = ask_number("Uzdevuma numurs: ")
                if number is not None:
                    print(f"Dzēsts: {todo.remove(number).title}")
            elif choice == "4":
                print(todo.format())
            elif choice == "5":
                s = todo.stats()
                print(f"Kopā: {s['total']}, izpildīti: {s['done']} ({s['percent']}%)")
            elif choice == "0":
                print("Uz redzēšanos!")
                break
            else:
                print("Nepareiza izvēle.")
        except (ValueError, IndexError) as error:
            print(f"Kļūda: {error}")


class TestTodoList(unittest.TestCase):
    """Tests ir šajā pašā failā. Palaiž: python -m unittest src.main -v"""

    def test_add_and_complete_task(self):
        todo = TodoList()
        todo.add("Mācīties Git")
        todo.add("Uzrakstīt testu")
        todo.complete(1)
        self.assertEqual(todo.stats(), {"total": 2, "done": 1, "percent": 50})


if __name__ == "__main__":
    main()
print("Hello from MAIN"
print ("Hello from FEATURE")


