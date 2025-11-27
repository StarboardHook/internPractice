from behaviors.honk_behavior import HonkBehavior

class AggressiveHonk(HonkBehavior):
    def honk(self):
        print("Honking aggressively: HONK HONK!")