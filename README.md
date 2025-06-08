[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/jw4FdbL-)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=19731068)
# COMP 170 SU25 WEEK 02

For this week's assignment focus on last week's reading assignment and work on the following items. Write your code in `week02.py`.

## Function to greet a person

Write a function named `greet` that takes one argument, say `name`, and **returns** a greeting string. For example, `greet("Thomas")` should **return** the string:
```
Hello Thomas. How are you?
```

## Greet a few friends

Create a simple list (not a dictionary) with the names of some friends. For example:
```python
my_friends = ["Frodo", "Sam", "Gandalf"]
```
Then write a function that takes the list of friends and **prints** a greeting for every one of them using function `greet(name)` from earlier.

## Solve an equation

The quadratic equation is defined as $ax^2+bx+c=0$. When $b^2-4ac< 0$ the equation has no solutions among real numbers (and we don't want to deal with *complex numbers,* at least not yet. 

When however,  $b^2-4ac\geq 0$ the solutions to the equation are

$$
x_1 = \frac{-b-\sqrt{b^2-4ac}}{2a}
$$

and

$$
x_2 = \frac{-b+\sqrt{b^2-4ac}}{2a}
$$

Write a function called `solve_quadratic` that takes three arguments, `a`, `b`, and `c`, and **prints** the solutions to the quadratic equation or prints the message "no real solutions".
