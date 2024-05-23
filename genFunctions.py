from event import Event
from individual import Individual
from team import Team

# Function to clear the console by printing 50 empty lines
def clear_console():
    print('\n' * 50)
  
# Function to create teams with player names
def createTeam():
    teams = []
    for i in range(4):
        teamName = input("Enter the name of TEAM number " + str(i+1) + ": ")
        p1 = input("Enter the name of the first player: ")
        p2 = input("Enter the name of the second player: ")
        p3 = input("Enter the name of the third player: ")
        p4 = input("Enter the name of the fourth player: ")
        p5 = input("Enter the name of the fifth player: ")
        team = Team(teamName, p1, p2, p3, p4, p5)
        teams.append(team)
        teams[i].printTeam()
        clear_console()
    return teams

# Function to create individual players
def createPlayer():
    individuals = []
    for _i in range(20):
        name = input("Enter the name of INDIVIDUAL player number " + str(_i+1) + ": ")
        individual = Individual(name)
        individuals.append(individual)
    clear_console()
    return individuals

# Function to create events with their attributes
def createEvent():
    events = []
    event = Event("Football", "Team", "Sporting", 60)
    events.append(event)
    event = Event("Basketball", "Team", "Sporting", 60)
    events.append(event)
    event = Event("Volleyball", "Team", "Sporting", 60)
    events.append(event)
    event = Event("Group Discussions", "Team", "Academic", 90)
    events.append(event)
    event = Event("Improvisation", "Team", "Academic", 90)
    events.append(event)
    event = Event("Table Tennis", "Individual", "Sporting", 60)
    events.append(event)
    event = Event("Swimming", "Individual", "Sporting", 90)
    events.append(event)
    event = Event("Running", "Individual", "Sporting", 90)
    events.append(event)
    event = Event("Debating", "Individual", "Academic", 60)
    events.append(event)
    event = Event("Speed Quizzes", "Individual", "Academic", 60)
    events.append(event)
    return events

# Function to print the points and ranking of teams
def printTeamPoints(teams):
    print("This is the teams table: \n")
    # Sort teams based on score
    sorted_teams = sorted(teams, key=lambda x: x.score, reverse=True)
    # Print the sorted list of teams
    for team in sorted_teams:
        print(team.teamname, team.score)

# Function to print the points and ranking of individuals
def printIndPoints(individuals):
    print('This is the individuals table: \n')
    # Sort individuals based on score
    sorted_individuals = sorted(individuals, key=lambda x: x.score, reverse=True)
    # Print the sorted list of individuals
    for individual in sorted_individuals:
        print(individual.name, individual.score)