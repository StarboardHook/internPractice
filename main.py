from Cars import Cars

from behaviors.concrete.diesel_drive import DieselDrive
from behaviors.concrete.electric_drive import ElectricDrive
from behaviors.concrete.gas_drive import GasDrive
from behaviors.concrete.aggressive_honk import AggressiveHonk
from behaviors.concrete.normal_honk import NormalHonk
from behaviors.concrete.quiet_honk import QuietHonk

def main():
    truck = Cars("Ford F-150", AggressiveHonk(), DieselDrive())
    ev = Cars("Tesla Model S", QuietHonk(), ElectricDrive())
    muscle = Cars("Dodge Charger", NormalHonk(), GasDrive())

    truck.display()
    truck.perform_honk()
    truck.perform_drive()
    print()

    ev.display()
    ev.perform_honk()
    ev.perform_drive()
    print()

    muscle.display()
    muscle.perform_honk()
    muscle.perform_drive()
    print()

    # Changing behaviors at runtime
    print("Changing the Dodge Charger to honk quietly and drive like an EV...")
    muscle.set_honk_behavior(QuietHonk())
    muscle.set_drive_behavior(ElectricDrive())
    muscle.perform_honk()
    muscle.perform_drive()
    print()