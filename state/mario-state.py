import signal

class SmallMario:
    pass

class BigMario:
    pass

class MediumMario:
    pass

class MarioState(object):
    """
    Interface mario state
    """

    def __init__(self, context):
        self.context = context
        # initial instance
        self.smallMario = SmallMario()
        self.mediumMario = MediumMario()
        self.bigMario = BigMario(None)
        # initial state
        self.context.state = self.smallMario
    
    def hit(self):
        """ When mario hit enemy """

    def trigger(self):
        """ When trigger mario to be unveiable """

    def eat(self):
        """ When mario eat mushroom """

class SmallMario(MarioState):

    def __init__(self):
        "Do nothing"
    
    def eat(self):
        """ Bigger """
        self.context.state = mediumMario

    def hit(self):
        """ Die """
        self.context.state = None
    
    def trigger(self):
        """ Biggest """
        self.bigMario.lastState = smallMario
        self.context.state = bigMario
        self.bigMario.setAlarm()

class MediumMario(MarioState):

    def __init__(self):
        "Do nothing"

    def eat(self):
        """ Nothing happed """

    def hit(self):
        """ Shrink """
        self.context.state = smallMario
    
    def trigger(self):
        """ Stretch out """
        self.bigMario.lastState = self.mediumMario
        self.context.state = self.bigMario
        self.bigMario.setAlarm()

class BigMario(MarioState):
    
    def __init__(self, lastState):
        self.lastState = lastState

    def setAlarm(self):
        """ Set alarm to shrink """
        signal.signal(signal.SIGALRM, timeOut)
    
    def timeOut(self):
        """ Turn into last state """
        self.context.state = lastState

    def hit(self):
        """ Nothing happend """

    def eat(self):
        """ Nothing happend """

    def trigger(self):
        """ Nothing happend """

class Context(object):
    """ Mario context such as hit, eat... managerment """

    def __init__(self):
        self.state = None
        MarioState(self)

    def hit(self):
        self.state.hit()

    def eat(self):
        self.state.eat()

    def trigger(self):
        self.state.trigger()

    def die(self):
        print("Mario died")

if __name__ == "__main__":
    context = Context()
    print(context.state)
    context.state.hit()
    print(context.state)
    """
    print(dir())
    print(__name__)
    print(__file__)
    print(__builtins__)
    """
