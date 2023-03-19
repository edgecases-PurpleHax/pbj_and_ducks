class Bird:
    def __init__(self, vocal):
        self.beaks = 1
        self.wings = 2
        self.feathertype = "Boring placeholder text here"
        self.feet = 2
        self.vocalization = vocal

    def describe_bird(self):
        return f"" \
               f"A bird has {self.beaks} beak, " \
               f"{self.wings} wings, {self.feathertype}, " \
               f"{self.feet} feet, and can speak {self.vocalization}"


class Duck(Bird):
    def __init__(self, vocal):
        super().__init__(vocal=vocal)
        self.swim = True


class BlueJay(Bird):
    def __init__(self, vocal):
        super().__init__(vocal=vocal)
        self.wings = 1


our_bird = Bird(vocal="quack quack")
our_bird_2 = Bird(vocal="Chirp Chirp")
print(our_bird.describe_bird())
print(our_bird_2.describe_bird())
our_duck = Duck(vocal="Quack Quack")
print(our_duck.describe_bird())
our_bluejay = BlueJay(vocal="chirp chirp")
print(our_bluejay.describe_bird())
