class Individual:
  # Define the Individual class representing an individual player in the tournament

  def __init__(self, name):
      # Constructor to initialize the Individual object with player's name

      self.name = name
      self.score = 0

  def increaseScore(self, amount):
      # Method to increase the individual player's score by the specified amount

      self.score = self.score + amount

  def printPlayer(self):
      # Method to print the player's name and score

      print(self.score,'-',self.name)