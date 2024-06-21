# Lecture Notes: OOP Principles

## 1. OOP Principles

- **Abstraction**: Focus the what its doing and not how its doing it
- **Encapsulation**: Bundling data and methods within a class and controlling access to them
- **Inheritance**: Extending a parent class, and giving it additional functionality and characteristic
- **Polymorphism**: Objects from differnt classes responding similarly to the same method in their unique way.


## 2. Encapsulation: 
Bundling data and methods within a class and controlling access to them

- **Public Attributes**: that are accessible from anywhere both inside and outside the class they are defined

- **Private Attributes**: indicated by a double underscore (dunder) `__name`. Accessible only within the class they are defined in. Useful for hiding and securing data

- **Proctected Attributes**: indicated by a single underscore `_name`. Accessible in both the class its defined and any subclass

```python
class Smartphone():

    def __init__(self, model, credit_card, operating_system):
        self.model = model
        self.__wallet = credit_card # Private Attribute
        self._operating_system = operating_system # Protected Attribute

    def show_info(self):
        print(f'Model: {self.model}')
        print(f'Wallet: *****')
        print(f"OS: {self._operating_system}")

    def get_wallet(self):
        return self.__wallet
    
    def set_wallet(self, new_card):
        print(f'Setting new credit card endinging {new_card[4:]}')
        self.__wallet = new_card




iphone = Smartphone('15 Pro Max', '1234567', 'IOS 27')
iphone.show_info()
#iphone.__wallet will throw an error because it is private
```

### Getters and Setters

**Getter**: method used to access any attribute (including private), since they are not accessible otherwise
```python
print(iphone.get_wallet())
```

**Setter**: method used to set any attribute (including private atts)
```python
iphone.set_wallet('09876543')
print(iphone.get_wallet())
```

## 3. Inheritance & Polymorphism

### Inheritance: 

- Extending a parent class, and giving it additional functionality and characteristic

- Inheritance allows a class (child class) to inherit the attributes and methods of another class (parent class), enabling code reuse and creating a hierarchical relationship.

General -> Specific


### Polymorphism: 
- Objects from differnt classes responding similarly to the same method in their unique way.

- Polymorphism allows objects of different classes to be treated as objects of a common super class. *It is achieved through method overriding*, where a subclass provides a specific implementation of a method already defined in its superclass.

```python
#Parent Class
class User():

    def __init__(self, email, password, username):
        self.email = email
        self.password = password
        self.username = username

    #All methods are inherited by the child
    def user_info(self):
        print(f"User: {self.username} can be contacted at {self.email}")

    def set_password(self, new_pass):
        self.password = new_pass


#Child Class that inherits from User
class AdminUser(User): #pass parent class in as a parameter
    isadmin = True
    def __init__(self, email, password, username, admin_id):
        super().__init__(email, password, username)
        self.admin_id = admin_id
        
    #polymorphism - Overwriting Parent method, but using it in a similar way.
    def user_info(self):
        print(f'Admin #{self.admin_id}: {self.username} can recieve support tickets at {self.email}.')


#instantiating User Class
billy_bob = User('bb@email.com', 'password', 'billy-b')
billy_bob.user_info()
#instantiating Admin Class
travis = AdminUser('travispeck@email.com', '12345', 'travisp', 1)
travis.user_info()
travis.set_password('1029383874')
print(travis.isadmin)
print(travis.password)
```
