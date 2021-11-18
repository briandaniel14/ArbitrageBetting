d = [["Mark", 12, 95],
     ["Jay", 11, 88],
     ["Jack", 14, 90]]

print("{:<8} {:<15} {:<10}".format('Name', 'Age', 'Percent'))

for v in d:
    name, age, perc = v
    print("{:<8} {:<15} {:<10}".format(name, age, perc))
