# Third-party
class UserInterface(object):

    def __init__(self):
        print('SLDKFJ')
        self.name = ''

    def getName(self):
        pass

    def setName(self):
        pass

class User(UserInterface):
    
    def __init__(self, name):
        super().__init__()
        self.name = name

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

# Adapter, working with legacy code
class CustomerInteface(object):
    def __init__(self):
        print('dslkf')
        self.user = None
        self.firstName = ''
        self.lastName = ''

    def getFirstName(self):
        pass

    def getLastName(self):
        pass
    
    def setFirstName(self):
        pass

    def setLastName(self):
        pass
    
def Customer(CustomerInteface):

    def __init__(self, user):
        super().__init__()
        print('sdss')
        self.user = user
        self.firstName = user.getName.split(' ')[0]
        self.lastName = user.getName.split(' ')[len(user.getName) - 1]

    def getFirstName(self):
        return self.firstName 
    
    def getLastName(self):
        return self.lastName
    
    def setFirstName(self, firstName):
        self.firstName = firstName

    def setLastName(self, lastName):
        self.lastName = lastName
    
if __name__ == "__main__":
    user = User('le cong')
    customer = Customer(user)
    print(customer)
    print(customer.getFirstName())
    print(customer.getLastName())