from abc import ABC, abstractmethod

class DriveBehavior(ABC):
    @abstractmethod
    def drive(self):
        "How the car drives"
        pass