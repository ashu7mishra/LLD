from DesignPatterns.abstractFactoryDP.UIElements.checkbox import CheckBox


class AndroidCheckBox(CheckBox):

    def click(self):
        print("Android check box got clicked")