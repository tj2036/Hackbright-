
class Phone(object):
    """A simple Phone class to keep track of contacts"""

    def __init__(self, number, name, contacts=None):
        self.number = number
        self.name = name
        if contacts:
            self.contacts = contacts
        else:
            self.contacts = {}

    # The __repr__ method gives the class a print format that is meaningful to
    # humans, in this case we chose first and last name
    def __repr__(self):

        return self.name

    def add_contact(self, first_name, last_name, number):
        """Creates new Contact instance and adds the instance to contacts"""
        # See the types of each parameter from the function call in contact_ui.py
        # self.first_name = first_name
        # self.last_name = last_name
        # self.number = number
        # self.contacts[first_name] = Contact(self.first_name, self.last_name, self.number)
        new_contact = Contact(first_name, last_name, number)
        new_key = self._get_contact_key(first_name, last_name)
        self.contacts[new_key] = new_contact
        # print self.contacts
        # return self.contacts

    def call(self, first_name):
        """Call a contact."""

        pass

    def text(self, first_name, last_name, message):
        """Send a contact a message."""
        text_key = self._get_contact_key(first_name, last_name)
        found_contact = self.contacts[text_key]
        found_contact.mobile_phone



        print "To: %s - %s" % (first_name, message)



        pass

    def del_contact(self, first_name, last_name):
        """Remove a contact from phone"""
        key = self._get_contact_key(first_name, last_name)
        del self.contacts[key]

    def _get_contact_key(self, first_name, last_name):
        """This is a private method. It's meant to be used only from within
        this class. We notate private attributes and methods by prepending with
        an underscore.
        """
        return first_name.lower() + " " + last_name.lower()


# class definition for a Contact
class Contact(object):
    """A class to hold information about an individual"""
    # initialize an instance of the object Contact
    def __init__(self,
                 first_name,
                 last_name,
                 mobile_phone,
                 email="",
                 twitter_handle=""):
        self.first_name = first_name
        self.last_name = last_name
        self.mobile_phone = mobile_phone
        self.email = email
        self.twitter_handle = twitter_handle

    # The __repr__ method gives the class a print format that is meaningful to
    # humans, in this case we chose first and last name
    def __repr__(self):
        return "%s %s" % (self.first_name, self.last_name)


    def full_name(self):
        return self.first_name + " " + self.last_name

# some examples of how to use these two classes

# Make a Phone instace
# tommys_phone = Phone(5555678, "Tommy Tutone's Phone")

# # Use the Phone class to add new contacts!
# tommys_phone.add_contact("Jenny", "From That Song", 8675309)
# katherine_phone = Phone(444444, "Katherine's Phone")
# katherine_phone.add_contact("Tania", "J", 11111)
# katherine_phone.add_contact("Bill", "Gates", 333333)

# katherine_phone.del_contact("Tania")