# Perla Robles
# 3/10/25
# P3HW2
# Determine employee's regular pay, OT pay, and gross pay

'''
Pseudocode:

Get employee name from user (use input function)
Get hours worked from user (use input function and float function)
Get employee pay rate from user (use input function and float function)

# Overtime worked
Calcuate values:
if hours_worked > 40:
    Calculate OT_hours (hours_worked - 40)
    Calculate_OT_pay_rate (pay_rate*1.5)
    Calculate OT_pay (OT_hours * OT_pay_rate)
    reg_hours is equal to 40 (Create a variable)
    Calculate reg_pay (reg_hours * pay_rate)
    Calculate gross_pay (OT_pay + reg_pay)

# No Overtime is worked
else:
    OT_hours is zero (Create a variable)
    OT_pay_rate is zero (Create a varibale)
    Calculate OT_pay (OT_hours * OT_pay_rate)
    reg_hours is equal to hours_worked (Create a variable)
    Calculate reg_pay (reg_hours * pay_rate)
    Calculate gross_pay (OT_pay + reg_pay)

Display all values with width formatting

print(f"{'Hours work':<20}{'Pay Rate':<20}")
print("----"*10)
print(f"{hours_worked:<20}${pay_rate;<20.2f}")
'''

emp_name = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))

print("----"*10)
print("Employee Name: ", emp_name)
print()

if hours_worked > 40:
    ot_hours = hours_worked - 40
    ot_pay_rate = pay_rate * 1.5
    ot_pay = ot_hours * ot_pay_rate
    reg_hours = 40
    reg_pay = reg_hours * pay_rate
    gross_pay = ot_pay + reg_pay
else:
    ot_hours = 0
    ot_pay_rate = 0
    ot_pay = ot_hours * ot_pay_rate
    reg_hours = hours_worked
    reg_pay = reg_hours * pay_rate
    gross_pay = ot_pay + reg_pay

print(f"{'Hours Worked':<20}{'Pay Rate':<20}{'OverTime':<20}{'OverTime Pay':<20}{'RegHour Pay':<20}{'Gross Pay'}")
print("----"*35)
print(f"{hours_worked:<20}${pay_rate:<20.2f}{ot_hours:<19}${ot_pay:<19.2f}${reg_pay:<19.2f}${gross_pay:<.2f}")

