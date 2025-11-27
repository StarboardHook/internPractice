from abc import ABC, abstractmethod

class HonkBehavior(ABC):
    @abstractmethod 
    def honk(self):
        "How the car honks"
        pass