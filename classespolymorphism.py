
# classespolymorphism.py
class FootballEntity:
    def move(self):
        print("Moving on the field...")

# Player Class (inherits from FootballEntity) 
class FootballPlayer(FootballEntity):
    def __init__(self, name, position, goals):
        self.name = name
        self.position = position
        self.__goals = goals   # private attribute (encapsulation)

    def display_info(self):
        print(f"Player: {self.name} | Position: {self.position} | Goals: {self.__goals}")

    # Getter
    def get_goals(self):
        return self.__goals

    # Setter with validation
    def set_goals(self, goals):
        if goals >= 0:
            self.__goals = goals
        else:
            print("Invalid number of goals! Must be non-negative.")

    # Polymorphism — overriding move()
    def move(self):
        print(f"{self.name} is running with the ball ")

# === Goalkeeper Class (inherits from FootballPlayer) ===
class Goalkeeper(FootballPlayer):
    def __init__(self, name, position, goals, saves):
        super().__init__(name, position, goals)
        self.saves = saves

    # Override display_info (polymorphism)
    def display_info(self):
        print(f"Goalkeeper: {self.name} | Position: {self.position} | Saves: {self.saves}")

    # Override move()
    def move(self):
        print(f"{self.name} dives to make an incredible save ")

# === Referee Class (inherits from FootballEntity) ===
class Referee(FootballEntity):
    def __init__(self, name):
        self.name = name

    def move(self):
        print(f"Referee {self.name} jogs to follow the play ")

if __name__ == "__main__":
    # Creating objects
    player1 = FootballPlayer("Messi", "Forward", 28)
    keeper1 = Goalkeeper("Neuer", "Goalkeeper", 0, 150)
    ref1 = Referee("Oliver")

    # Displaying information
    print("\n--- Player Info ---")
    player1.display_info()
    keeper1.display_info()

    # Demonstrate encapsulation
    print("\n--- Updating Goals ---")
    player1.set_goals(32)
    print(f"{player1.name} now has {player1.get_goals()} goals.")

    # Demonstrate polymorphism
    print("\n--- Game Movements (Polymorphism) ---")
    entities = [player1, keeper1, ref1]
    for entity in entities:
        entity.move()
