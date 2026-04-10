from dateutil import parser

class DateParser:
    def __init__(self, date_string):
        self.date_string = date_string   # correct assignment
        self.parsed_date = None

    def parse_date(self):   # method outside __init__
        self.parsed_date = parser.parse(self.date_string)

    def display(self):      # method outside __init__
        print(self.parsed_date)
        print(type(self.parsed_date))


# creating object
obj = DateParser("Oct 14 2006 7:15 AM")

# calling methods
obj.parse_date()
obj.display()