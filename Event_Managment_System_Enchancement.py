class Event:
    def __init__(self, name, date):
# name: The name of the event (str)
# date: The date of the event (str or date)
        self.name = name
        self.date = date
        self.participant_count = 0  # Initialize participant count to 0

    def add_participant(self):
        #Increases the participant count by 1 each time a new participant joins the event.
        self.participant_count += 1
        print(f"New participant added. Total participants: {self.participant_count}")

    def get_participant_count(self):
        # Returns the current number of participants in the event
        return self.participant_count
    
    def event_name(self):
        # Returns the name of the event and it's date
        return f"The event titled {self.name} will be on {self.date}."

# Create an Event object
event1 = Event("Championship Match", "2001-08-11")

# State the event
print(event1.event_name())

# Display initial participant count
print(f"Initial participant count: {event1.get_participant_count()}")

# Add participants to the event
event1.add_participant()
event1.add_participant()
event1.add_participant()

# Display updated participant count
print(f"Updated participant count: {event1.get_participant_count()}")