class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, Exhale.")


class Fish(Animal):

    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print("inside the water.")

    def swim(self):
        print("Moving in the water.")


neon = Fish()
neon.swim()
neon.breathe()
