# help(int)

# self keyword refers to the current class instance
# viittaa jokaiseen yksittäiseen instanssiin
# self:n pitää olla aina ensimmäinen parametri __init__ ja 
# missä tahansa muussa luokan methodissa

# __init__ methodia kutsutaan aina kun luot uuden instanssin luokasta
class User:

    # class attribute
    active_users=0

    def __init__(self, first,last,age):
        print(f"new {first} has been made!")
        self.first=first
        self.last=last
        self.age=age
        # yksittäinen alaviiva kertoo vain kehittäjille että 
        # muuttujan on tarkoitus olla piilossa
        self._secret = "hi"
        # tän periaattessa saa _className__msg viitteellä ulos
        self.__msg = "i like turtles"
        # class attribuutteja voi käyttää, kunhan kutsuu luokan nimellä
        User.active_users += 1

    def logout(self):
        User.active_users -= 1

    def full_name(self):
        return f"{self.first} {self.last}"

first_user = User("paavo", "paavola", 12)
first_user2 = User("maija","majala",22)
first_user3 = User("keijo","vanhatalo", 55)

print(first_user.first)
print(first_user.last)
print(first_user._User__msg)
print(first_user.full_name())
print(first_user2.full_name())
print(first_user3.full_name())
print(first_user.active_users)
print(first_user.logout())
print(first_user.active_users)

# 