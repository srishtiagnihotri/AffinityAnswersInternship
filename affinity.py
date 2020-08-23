racial_slurs = []
print('Please provide File Name where instagram comments are present')
file_name = input()
print('Enter total number of slurs word which you want to add')
for i in range(int(input())):
    print('Enter word ',i+1,' ',end=' ')
    racial_slurs.append(input())
file_comments = open(file_name, 'r')
lines = file_comments.readlines()
line_count=1
for line in lines:
    count=0
    for racial in racial_slurs:
        if racial.upper() in line.upper():
            count+=1
    print('degree of racial_words at line ',line_count,' is ',count)
    line_count+=1
