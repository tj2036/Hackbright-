class Contact(object):
    def __init__(self, first_name, last_name):
        self.first_name = first_name  
        self.last_name = last_name
        self.mobile_number = ""
        self.work_number = ""
        self.email  = ""

    def send_message(self, message):
        print "To: %s - %s" % (self.mobile_number, message)

contact_tania = Contact("Tania", "Jimene")
contact_tania.mobile_number = "301-385-4841"
print contact_tania.mobile_number

contact_tania.send_message("Hello! How are you?")

# main()

if __name__ == "__main__":
    contact_amy = Contact("Amy", "Smith")
    contact_diana = Contact("Diana", "Banana")

    contact_list = []
    contact_list.append(contact_amy)
    contact_list.append(contact_diana)
    contact_list.append(contact_tania)

    for item_contact in contact_list:
        print item_contact.first_name

