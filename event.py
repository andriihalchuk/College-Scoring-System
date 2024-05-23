# Define the Event class to represent an event in the tournament
class Event:

    # Constructor to initialize the Event object with provided attributes
    def __init__(self, eventName, participants, eventType, points):
        self.eventName = eventName  # Name of the event
        self.participants = participants  # Number of participants
        self.eventType = eventType  # Type of event (Team/Individual)
        self.points = points  # Points awarded for the eventpoints):

