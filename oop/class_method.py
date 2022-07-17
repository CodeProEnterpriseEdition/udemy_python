
class User:

    active_users=0

# classmethod:lla on @classmethod decorator
    @classmethod
    # cls = class, classmethodeissa on tapana käyttää self:n sijasta
    # cls muuttujaa
    def display_active_users(cls):
        return f"There are currently {cls.active_users} active users"

    @classmethod
    def from_string(cls, data_str):
        first, last, age = data_str.split(",")
        return cls(first,last,int(age))


    def __init__(self, first,last,age):
        print(f"new {first} has been made!")
        self.first=first
        self.last=last
        self.age=age
        User.active_users += 1

    def __repr__(self):
        return f"{self.first} is {self.age}"

    def logout(self):
        User.active_users -= 1

    def full_name(self):
        return f"{self.first} {self.last}"

first_user = User("paavo", "paavola", 12)
first_user2 = User("maija","majala",22)
first_user3 = User("keijo","vanhatalo", 55)
tom = User.from_string("Tom,Jones,89")
print(tom.full_name())
print(tom)

print(first_user.first)
print(first_user.last)
print(User.display_active_users())
