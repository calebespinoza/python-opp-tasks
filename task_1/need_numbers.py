# A crazy trainer returns my grade into single string and I need to know the total and the average

simple_string = "English=68 Logic=75 Uml=87 Code=80"
grades = []

for i in simple_string.split():
    tmp_list = i.split("=")
    grades.append(tmp_list[1])

for i in range(len(grades)):
    grades[i] = int(grades[i])

total = sum(grades)
average = total / len(grades)

print("Sum Total is: {}".format(total))
print("Average is: {}".format(average))
