from __future__ import annotations
from abc import abstractmethod, ABC


class ObserverAbstract(ABC):
    @abstractmethod
    def update(self, consumer: ConsumerAbstract):
        pass
    
    
class ConsumerAbstract(ABC):
    @abstractmethod
    def attach(self, observer: ObserverAbstract):
        pass
    
    @abstractmethod
    def detach(self, observer: ObserverAbstract):
        pass
    
    @abstractmethod
    def notify(self):
        pass


class Consumer(ConsumerAbstract):
    _state = False
    _observers: list[ObserverAbstract] = []
    
    def attach(self, observer: ObserverAbstract):
        print(f"Attach to observer {observer}")
        self._observers.append(observer)
        
    def detach(self, observer: ObserverAbstract):
        print(f"Detach observer {observer}")
        self._observers.remove(observer)
        
    def notify(self):
        for observer in self._observers:
            observer.update(self)
    
    def some_changes(self):
        self._state = True
            

class Observer1(ObserverAbstract):
    def update(self, consumer: Consumer):
        if consumer._state:
            print(f"notify {consumer}")


class Observer2(ObserverAbstract):
    def update(self, consumer: Consumer):
        print(f"notify {consumer}")
        

if __name__ == "__main__":
    consumer = Consumer()
    
    observer_1 = Observer1()
    observer_2 = Observer2()
    
    consumer.attach(observer_1)
    consumer.attach(observer_2)
    consumer.attach(100_100_100)
    
    consumer.notify()
    
    consumer.some_changes()
    
    consumer.notify()