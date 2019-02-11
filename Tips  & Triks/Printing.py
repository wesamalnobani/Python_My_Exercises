
#Printing

name = 'wesam'
age  = 36

print('My name is :{} and my age is {}'.format(name, age))

#print(f" My name is :{name} and my age is {age}")

multiStr = "select * from multi_row \
where row_id < 5"
print(multiStr)

multiStr2 = """select * from multi_row 
where row_id < 5"""
print(multiStr2)

multiStr3 = ("select * from multi_row "
"where row_id < 5 "
"order by age")
print(multiStr3)

#Shell

