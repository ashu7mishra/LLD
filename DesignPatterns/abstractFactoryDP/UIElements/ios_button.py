from DesignPatterns.abstractFactoryDP.UIElements.button import Button


class IOSButton(Button):

    def click(self):
        print("IOS button got clicked")