# Question 9 Write a program to reverse words in a string.
# sample_text = "Python is a high-level and general-purpose programming language"
sample_text = "Python is a high-level and general-purpose programming language"
sample_text = sample_text.split(" ")
sample_text = sample_text[::-1]

for word in sample_text:
    print(word,end=' ')

print()