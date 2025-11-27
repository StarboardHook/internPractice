from behaviors.honk_behavior import HonkBehavior

class QuietHonk(HonkBehavior):
    def honk(self):
        print("Honking quietly: beep beep")