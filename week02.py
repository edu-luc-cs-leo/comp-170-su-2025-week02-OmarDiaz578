# Function to greet people

def greet(name):
    return f"Hello {name}. How are you?"
print(greet("Omar"))

#Greet a few friends

friends_list = ["Sam", "Porter", "Ramzi"]

def greet_friends(friends_list):
    for friend in friends_list:
        message = greet(friend)
        print(message)

greet_friends(friends_list)