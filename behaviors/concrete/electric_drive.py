from behaviors.drive_behavior import DriveBehavior

class ElectricDrive(DriveBehavior):
    def drive(self):
        print("Driving silently with electric power")