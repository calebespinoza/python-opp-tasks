# I would like to change my first option that was 20 for 2000

options = [5, 10, 15, 20, 25, 30, 4, 20]
flag = False

for i in range(len(options)):
    if options[i] == 20 and flag == False:
        options[i] = 2000
        flag = True

print(options)