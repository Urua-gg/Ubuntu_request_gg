# Base class
class FootballPlayer:
    def __init__(self, name, position, goals):
        self.name = name
        self.position = position
        self.__goals = goals  # (encapsulation)

    # Method to display player info
    def display_info(self):
        print(f"Player: {self.name}, Position: {self.position}, Goals: {self.__goals}")

    # Getter for goals
    def get_goals(self):
        return self.__goals

    # Setter for goals (encapsulation)
    def set_goals(self, goals):
        if goals >= 0:
            self.__goals = goals
        else:
            print("Invalid goal count! Goals cannot be negative.")

# Derived class (Inheritance)
class Goalkeeper(FootballPlayer):
    def __init__(self, name, position, goals, saves):
        super().__init__(name, position, goals)
        self.saves = saves

    # Polymorphism – overriding display_info()
    def display_info(self):
        print(f"Goalkeeper: {self.name}, Position: {self.position}, Saves: {self.saves}")

# Create objects
player1 = FootballPlayer("Messi", "Forward", 28)
keeper1 = Goalkeeper("Neuer", "Goalkeeper", 0, 150)

# Display info
player1.display_info()
keeper1.display_info()

# Encapsulation in action
player1.set_goals(30)
print(f"{player1.name} now has {player1.get_goals()} goals.")
