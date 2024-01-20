
class Subject:
    
    def __init__(self):
        self.observers = set()

    def Attach(self, observer):
        """Attaches observer to subject"""
        self.observers.add(observer)

    def Detach(self, observer):
        """Detaches observer from subject"""
        self.observers.remove(observer)

    def Notify(self, statement):   
        for observer in self.observers:
            observer.update(statement)

