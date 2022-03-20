# Question 10 Given below is the height (in cm) of the top 10 students in a class. Print the heights of the top 3 students from the given list.
# heights = [177, 160, 171, 163, 168, 175, 176, 183, 162, 170]
heights = [177, 160, 171, 163, 168, 175, 176, 183, 162, 170]
heights = sorted(heights, reverse=True)
print(heights[:3])