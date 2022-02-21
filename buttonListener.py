from mapElements.button import Button


class ButtonListener:
    listeners = []

    def __init__(self, func, buttonNumber):
        self.buttonNumber = buttonNumber
        self.func = func

        ButtonListener.listeners.append(self)

    def action(self):
        self.func()

    def getButtonNumber(self):
        return self.buttonNumber

    @staticmethod
    def buttonAction(mousePosition):
        for listener in ButtonListener.listeners:
            if listener.getButtonNumber() == Button.isAnyButtonClicked(mousePosition):
                listener.action()
                break
