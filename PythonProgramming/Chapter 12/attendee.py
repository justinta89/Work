# program keeps track of conference attendees

# attendee class
#       - Name
#       - Company
#       - State
#       - Email address

# should be able to add new attendee, delete attendee, get info of attendee
# get name and email addresses of all attendees

# attendee list should be a file that is loaded when the program starts

class Attendee:
    """Attendee class to keep create a new attendee and call attendee info.
    """

    def __init__(self, name, email, company, state):

        self.name = name
        self.email = email
        self.company = company
        self.state = state
        self.info = "Name:{0} \nEmail:{1} \nCompany:{2} \nState:{3}".format(
            self.name, self.email, self.company, self.state)


    def getName(self):
        return self.name

    def getEmail(self):
        return self.email

    def getCompany(self):
        return self.company

    def getState(self):
        return self.state

    def getInfo(self):
        """
        Returns the attendee information in nice ordered format.
        """
        return self.info