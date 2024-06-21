# Inheritance and Polymorphism

#-- Inheritance: Extending a parent class and giving it additional finctionality and characteristics
    #-- Inheritance allows a child class to inherit attributes and methods from another class (parent class)

# General functionality --> more specific functionality

#-- Polymorphism: Objects from different classes (sub classes) responding similarly to the same method in their own unique way
    #-- is achieved through method overrriding, where a subclass provides a specific implementation of a method already defined in its parent class (superclass)

# Parent class (superclass)
class User():

    def __init__(self, email, password, username):
        self.email = email
        self._password = password
        self.username = username

    # All methods are inherited be the sub class (child class)
    def user_info(self):
        print(f"User: {self.username} can be contacted at {self.email}")

    def set_password(self, new_pass):
        self._password = new_pass

    def get_username(self):
        print(self.username)

# class that inherits from User
class Admin(User):

    def __init__(self, email, _password, username, admin_id, isadmin = True):
        super().__init__(email, _password, username)
        self.admin_id = admin_id
        self.isadmin = isadmin

    def user_info(self):
        print(f"Admin: #{self.admin_id} {self.username} can recieve support tickets at {self.email}")

    def get_password(self):
        print(self._password)
    
# Instantiating a User class object
billy_bob = User('billy@email.com', '1234', 'billy-b')
billy_bob.user_info()
    
# Instantiate an Admin class object
travis = Admin('travisp@codingtemple.com', '1234', 'traviicii', 1)
travis.user_info()


billy_bob.get_username()
billy_bob.set_password("this is the password now")

# print(billy_bob.__password) # Produces an error because that attribute is private

travis.set_password("123456677")
travis.get_password()

print(travis.isadmin)