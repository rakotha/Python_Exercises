# Question 3 Find out the number of letters and digits from the given alpha-numeric text.
# sample_text = "Learning Journal 2020"
sample_text = "Learning Journal 2020"
total_digits = 0
total_letters = 0

for s in sample_text:
    if s.isnumeric():
        total_digits += 1
    if s.isalpha():
        total_letters += 1

print("Number of Letters :", total_letters)
print("Number of Digits  :", total_digits)
