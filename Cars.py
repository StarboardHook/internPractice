from behaviors.honk_behavior import HonkBehavior
from behaviors.drive_behavior import DriveBehavior

# Cars class (Name, Honk type, Drive type)
class Cars:
    def __init__(self, name: str, honk_behavior: HonkBehavior, drive_behavior: DriveBehavior):
        self.name = name
        self.honk_behavior = honk_behavior
        self.drive_behavior = drive_behavior

    def perform_honk(self):
        print(f"[{self.name}] Honking:")
        self.honk_behavior.honk()

    def perform_drive(self):
        print(f"[{self.name}] Driving:")
        self.drive_behavior.drive()

    def display(self):
        print(f"This is a {self.name}")

    # Methods to set behaviors at runtime (e.g., make a musle car drive like a EV)
    def set_honk_behavior(self, honk_behavior: HonkBehavior):
        self.honk_behavior = honk_behavior

    def set_drive_behavior(self, drive_behavior: DriveBehavior):
        self.drive_behavior = drive_behavior