from DesignPatterns.abstractFactoryDP.Factory.os_factory import OSFactory


def Deploy(val):

    abs = OSFactory().create_type(val)

    button = abs.create_button().create()
    button.click()
    checkbox = abs.create_checkbox().create()
    checkbox.click()

if __name__ == "__main__":
    Deploy("android")
    Deploy("ios")