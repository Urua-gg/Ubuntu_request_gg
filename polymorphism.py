class FootballEntity:
    def move(self):
        print("Moving on the field...")

class Player(FootballEntity):
    def move(self):
        print("Running with the ball")

class Referee(FootballEntity):
    def move(self):
        print("Jogging to keep up with play")

class Goalkeeper(FootballEntity):
    def move(self):
        print("Diving to make a save ")

# Demonstrate polymorphism
entities = [Player(), Referee(), Goalkeeper()]

for entity in entities:
    entity.move()
