from abc import ABC, abstractmethod

# Receiver
class TextEditor:
    def __init__(self):
        self.text = ""

    def write(self, text):
        self.text += text

    def delete(self, count):
        self.text = self.text[:-count]

    def __str__(self):
        return self.text


class ICommand(ABC):
    @abstractmethod
    def execute(self):
        pass

class Invoker:
    def __init__(self):
        self.commands = []

    def add_command(self, cmd):
        self.commands.append(cmd)

    def run(self):
        for cmd in self.commands:
            cmd.execute()


class WriteCommand(ICommand):
    def __init__(self, te, text):
        self.te = te
        self.text = text

    def execute(self):
        self.te.write(self.text)


class DeleteCommand(ICommand):
    def __init__(self, te, count):
        self.te = te
        self.count = count

    def execute(self):
        self.te.delete(self.count)


te = TextEditor()
cmd1 = WriteCommand(te, "hello,")
cmd2 = WriteCommand(te, "world!!@#$!")
cmd3 = DeleteCommand(te, 3)

invoker = Invoker()
invoker.add_command(cmd1)
invoker.add_command(cmd2)
invoker.add_command(cmd3)
invoker.run()

print(te)