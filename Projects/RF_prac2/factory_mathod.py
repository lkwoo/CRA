from abc import ABC, abstractmethod


class SaveAction:
    def run(self):
        print("파일 저장...")


class ExitAction:
    def run(self):
        print("프로그램 종료...")


class Button(ABC):
    def click(self):
        action = self.create_action()
        action.run()

    @abstractmethod
    def create_action(self):
        ...


class SaveButton(Button):

    def create_action(self):
        return SaveAction()


class ExitButton(Button):

    def create_action(self):
        return ExitAction()


btn1 = SaveButton()
btn2 = ExitButton()

btn1.click()
btn2.click()
