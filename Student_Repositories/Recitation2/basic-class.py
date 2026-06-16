class MessagePrinter:
    def __init__(self, message_type):
        self.message_type = message_type

    def print_message(self, message):
        print(f"{self.message_type}: {message}")


announcements = MessagePrinter("Announcement")

announcements.print_message("Hello students")

for i in range(5):
    announcements.print_message(f"Homework {str(i + 1)}  just published!")


grades = MessagePrinter("Grade")


for i in range(5):
    grades.print_message(f"Assignment {str(i+1)} has been graded!")
