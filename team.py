# Define the Team class representing a team in the tournament
class Team:

    def __init__(self, teamname, p1, p2, p3, p4, p5):
        # Constructor to initialize the Team object with team name and players

        self.teamname = teamname
        self.players = [p1, p2, p3, p4, p5]
        self.score = 0

    def increaseScore(self, amount):
        # Method to increase the team's score by the specified amount

        self.score = self.score + amount

    def printTeam(self):
        # Method to print the team's name and score

        print("Team Name:", self.teamname, "| Score:", self.score)