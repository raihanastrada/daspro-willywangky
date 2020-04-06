class admin:
    #class atribute
    role = "administrator"

    #instance attribute
    def __init__(self,name,username,password):
        self.name = admin
        self.username


with open('user.csv','r') as read:
    csv_reader = csv.DictRead(read)
    for row in csv_reader:
        if (row['Username']=="admin" and row['Password']=="admin"):
            adminOption()
