from DesignPatterns.abstractFactoryDP.UIElements.checkbox import CheckBox


class IOSCheckBox(CheckBox):

    def click(self):
        print("ISO checkbox got clicked")