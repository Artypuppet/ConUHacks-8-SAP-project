class Subject:

    def __init__(self):
        self.observers = set()

    def attach(self, observer):
        """Attaches observer to subject"""
        self.observers.add(observer)

    def detach(self, observer):
        """Detaches observer from subject"""
        self.observers.remove(observer)

    def notify(self, appointment):
        for observer in self.observers:
            observer.update(appointment)
