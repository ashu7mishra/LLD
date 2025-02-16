from DesignPatterns.abstractFactoryDP.UIElements.button import Button


class AndroidButton(Button):

    def click(self):
        print("Android button got clicked")
