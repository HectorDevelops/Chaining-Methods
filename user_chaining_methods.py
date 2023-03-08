class User:
    def __init__(self, first_name, last_name, email, age, is_rewards_member = False, gold_card_points = 0):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = is_rewards_member
        self.gold_card_points = gold_card_points

# display_info(self) - Have this method print all of the users' details on separate lines.
    def display_info(self):
        print("First Name: ", self.first_name)
        print("Last Name: ", self.last_name )
        print("Current Email: ", self.email)
        print("Current Age:", self.age)
        print("Is this user a reward's member?", self.is_rewards_member)
        print("Points balance: ", self.gold_card_points)
        return self

# enroll(self) - Have this method change the user's member status to True and set 
# their gold card points to 200.
    def enroll(self):
        self.is_rewards_member = True
        self.gold_card_points = 200
        return self

# spend_points(self, amount) - have this method decrease the user's points by the amount specified.
    def spend_points(self, amount):
        self.gold_card_points -= amount
        print(f"{self.first_name}'s new balance is {self.gold_card_points} after spending {amount} points.")
        return self


# Creating an instance of the class and passing information 
Hector = User("Hector", "Rosario", "Hector@mail.com", 29, False, 0)

# Calling this method to make updates to the User's current information
Hector.enroll().spend_points(50).display_info()

# Creating this print statement to add a line break between User's output. 
print("\n")

# Creating a second instance of the class and passing information 
Elvis = User("Elvis", "Martinez", "Elvis@mail.com", 43)

# Chaining methods
Elvis.enroll().spend_points(80).display_info()




        