from DesignPatterns.abstractFactoryDP.UIElements.button import Button


class IOSButton(Button):

    def click(self):
        print("Android button got clicked")