import random 
salary = int(input("Enter your salary: "))
percent_increment = random.uniform(0.05, 0.15)
new_salary = salary * (percent_increment * 100)
rounded_new_salary = round(new_salary, 2)
print(f"Your new salary is: {rounded_new_salary}")