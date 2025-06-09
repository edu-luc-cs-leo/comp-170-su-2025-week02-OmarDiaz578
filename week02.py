#   Function to greet people

def greet(name):
    return f"Hello {name}. How are you?"
print(greet("Omar"))

#   Greet a few friends

friends_list = ["Sam", "Porter", "Ramzi"]

def greet_friends(friends_list):
    for friend in friends_list:
        message = greet(friend)
        print(message)

greet_friends(friends_list)

#   Solve an equation

def solve_equation(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return "No real solutions"
    elif discriminant == 0:
        x = -b / (2*a)
        return f"One real solution: x = {x}"
    else:
        x1 = (-b + discriminant**0.5) / (2*a)
        x2 = (-b - discriminant**0.5) / (2*a)
        return f"Two real solutions: x1 = {x1}, x2 = {x2}"
print(solve_equation(1, -3, 2))  
print(solve_equation(1, 2, 1))
print(solve_equation(1, 0, 1))
