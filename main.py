import numpy as np

data_type = [('name' , 'S15'), ('class' , int), ('height' , float)]

student_details = [('Darshil' , 5 , 48.5) , ('Paul' , 5 , 42.10) , ('James' , 5 , 40.11)]

students = np.array(student_details , dtype = data_type)
print("ORIGINAL ARRAY :")
print(students)
print("SORT BY HEIGHT :")
print(np.sort(students , order = 'height'))