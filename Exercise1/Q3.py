name = ('Shaun', 'Ron', 'Michael')
seat_numbers = (101, 102, 103)
d = {}
for i in range(len(name)):
    if name[i] not in d:
        d[name[i]] = seat_numbers[i]
print(d)
