
class Vehicle():
    def __init__(self, reg_num, owner):
        self.registration = reg_num
        self._owner = owner

    def change_owner(self, new_owner):

        self._owner = new_owner

        print(f"the new owner of this vehicle in {self._owner}")


my_car = Vehicle("123-321-4444444", "Travis Peck")

print(f"Current Owner: {my_car._owner}")

my_car.change_owner("Brad Kerwin")