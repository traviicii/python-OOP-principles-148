
# Ecapsulation: Bundling data and methods within a class and cotrolling access to them

#-- Public Attributes: Are accessible from anywhere both inside and outside the class they are defined in

#-- Private Attributes: Are indicated by a double underscore preceding the attribute name -> (dunder) __name. 
    #-- Accessible only within the class they are defined in. Usefule for securing and hiding data

#-- Protected Attributes: Indicated by a single underscore _name.
    #-- Accessible in both the class it's defined in, as well as any subclasses


class Smartphone():

    def __init__(self, model, credit_card, operating_system):
        self.model = model # Public attribute
        self.__wallet = credit_card # Private attribute, only accessible within this class
        self._operating_system = operating_system # Protected attribute, accessible within this class and subclasses

    def show_info(self):
        print(f"Model: {self.model}")
        print(f"Walet: *************")
        print(f"OS: {self._operating_system}")
        
    def get_wallet(self):
        return self.__wallet
    
    def set_wallet(self, new_card):
        flag = False
        for i in new_card:
            if i.isdigit():
                flag = True
                continue
            else:
                print("Please enter a valid credit card number.")
                flag = False
                break
        if flag: # After checking all characters, if it's a valid card number, then change the wallet to the new card
            self.__wallet = new_card
            print(f"New card set to: ************{new_card[-4:]}")

iphone = Smartphone("15 Pro Max", "1111222233334444", "IOS 27")
iphone.show_info()

# Getters and Setters

# Getter: method used to access any attribute (including private and protected), since they are not accessible otherwise

print(iphone.get_wallet())

# Setter: Method used to set any attribute (including private and protected attributes)

iphone.set_wallet("9999888877775555")