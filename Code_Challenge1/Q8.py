# Question 8 We have a string that contains the names of different fruits. I want you to convert this string into multiple substrings where each substring includes one fruit's name.
# fruits_string = " Apple, Banana, Mango, Kiwi, Guava, Grapes, Pomegranate, Orange, Watermelon"
fruits_string = " Apple, Banana, Mango, Kiwi, Guava, Grapes, Pomegranate, Orange, Watermelon"
fruits = fruits_string.split(',')
for fruit in fruits:
    print(fruit)