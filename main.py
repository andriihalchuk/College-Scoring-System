import genFunctions
from genFunctions import clear_console

# Print welcome message
clear_console()
print(" -------------------------------------------")
print("| Welcome to the tournament scoring system! |")
print(" -------------------------------------------")
print("\nPlease follow the instructions.\n")

def main():

    # Initialize teams, individuals, and events
    teams = genFunctions.createTeam()
    individuals = genFunctions.createPlayer()
    clear_console()
    events = genFunctions.createEvent()

    cont = True

    eventChoice = 0
  
    while cont is True:
          
          try:
            # Ask user to select an event
            eventChoice = int(input(
                "Select what you would like to play\n\nIf you are part of a team, please select one of the events 1-5. \n\n 1 - Football - 60 points \n 2 - Basketball - 60 points \n 3 - Volleyball - 60 points \n 4 - Group Discussions - 90 points \n 5 - Improvisation - 90 points \n\nIf you're an Individual, please select one of the events 6-10. \n\n 6 - Table Tennis - 60 points \n 7 - Swimming - 90 points \n 8 - Running - 90 points \n 9 - Debating - 60 points \n 10 - Speed Quizzes - 60 points \n\nEnter your choice: "
            ))
            clear_console()

            if eventChoice < 1 or eventChoice > 10:
                raise ValueError("Event number must be between 1 and 10")

          except ValueError as e:
            clear_console()
            print("Invalid input. Please enter a valid integer between 1 and 10 for events.")
            continue

          if eventChoice <= 5:
              # Get ranking for teams
              print("Who took the first place?\n\n 1 -", teams[0].teamname, "\n 2 -",
                    teams[1].teamname, "\n 3 -", teams[2].teamname, "\n 4 -",
                    teams[3].teamname, "\n\nSelect the team from 1 through 4")

              try:
                  firstPlace = int(input())
                  if firstPlace < 1 or firstPlace > 4:
                      raise ValueError("Team number must be between 1 and 4")
              except ValueError as e:
                  clear_console()
                  print("Invalid input. Please enter a valid team number between 1 and 4 for team ranking.\n")
                  continue

              clear_console()

              print("Who took second place?\n\n 1 -", teams[0].teamname, "\n 2 -",
                    teams[1].teamname, "\n 3 -", teams[2].teamname, "\n 4 -",
                    teams[3].teamname, "\n\nSelect the team from 1 through 4")

              try:
                  secondPlace = int(input())
                  if secondPlace < 1 or secondPlace > 4:
                      raise ValueError("Team number must be between 1 and 4")
              except ValueError as e:
                  clear_console()
                  print("Invalid input. Please enter a valid team number between 1 and 4 for team ranking.\n")
                  continue

              clear_console()

              print("Who took third place?\n\n 1 -", teams[0].teamname, "\n 2 -",
                    teams[1].teamname, "\n 3 -", teams[2].teamname, "\n 4 -",
                    teams[3].teamname, "\n\nSelect the team from 1 through 4")

              try:
                  thirdPlace = int(input())
                  if thirdPlace < 1 or thirdPlace > 4:
                      raise ValueError("Team number must be between 1 and 4")
              except ValueError as e:
                  clear_console()
                  print("Invalid input. Please enter a valid team number between 1 and 4 for team ranking.\n")
                  continue

              clear_console()

              # Update scores for teams based on ranking
              teams[firstPlace - 1].increaseScore(events[eventChoice - 1].points)
              teams[secondPlace - 1].increaseScore(events[eventChoice - 1].points / 2)
              teams[thirdPlace - 1].increaseScore(events[eventChoice - 1].points / 3)

              genFunctions.printTeamPoints(teams)

          elif eventChoice >= 6:
            # Get ranking for individuals
            print("Who took first place?\n")
            for individual in range(20):
                print(individual + 1, "-", individuals[individual].name)
            print("\nSelect the individual from 1 through 20")

            try:
                firstPlace = int(input())
                
            except ValueError as e:
                clear_console()
                print("Invalid input. Please enter a valid integer between 1 and 20 for individual player selection.\n")
                continue
            clear_console()
            print("Who took second place?\n")
            for individual in range(20):
                print(individual + 1, "-", individuals[individual].name)
            print("\nSelect the individual from 1 through 20")

            try:
                secondPlace = int(input())
            except ValueError as e:
                clear_console()
                print("Invalid input. Please enter a valid integer between 1 and 20 for individual player selection.\n")
                continue
            clear_console()
            print("Who took third place?\n")
            for individual in range(20):
                print(individual + 1, "-", individuals[individual].name)
            print("\nSelect the individual from 1 through 20")

            try:
                thirdPlace = int(input())
            except ValueError as e:
                clear_console()
                print("Invalid input. Please enter a valid integer between 1 and 20 for individual player selection.\n")
                continue
            clear_console()
            # Update scores for individuals based on ranking
            individuals[firstPlace - 1].increaseScore(events[eventChoice - 1].points)
            individuals[secondPlace - 1].increaseScore(events[eventChoice - 1].points/2)
            individuals[thirdPlace - 1].increaseScore(events[eventChoice - 1].points/3)
            genFunctions.printIndPoints(individuals)

          anotherEvent = int(
          input(
            "\nIf you want to continue please enter 1, if you wish to end please enter 2\n"
        ))
          clear_console()

          if anotherEvent == 2:
            cont = False
            genFunctions.printTeamPoints(teams)
            genFunctions.printIndPoints(individuals)

main()