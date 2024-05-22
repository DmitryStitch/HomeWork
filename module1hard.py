grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
# students1 = list(students)
table_mid = {'Johnny':sum(grades[2])/len(grades[2]),'Bilbo':sum(grades[1])/len(grades[1]), 'Steve':sum(grades[4])/len(grades[4]), 'Khendrik':sum(grades[3])/len(grades[3]), 'Aaron':sum(grades[0])/len(grades[0])}
sorted_table_mid = dict(sorted(table_mid.items()))
print(sorted_table_mid)