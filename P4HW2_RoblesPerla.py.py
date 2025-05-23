# -*- coding: utf-8 -*-
"""P4HW2_RoblesPerla.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1zyx_BISPjTuohzcXC2lOEW_K8GnJC017
"""

# Perla Robles

# 03/26/2025

# P4HW2

# Working to display multiple employees and terminating a while loop to display the total amount of accumulated employees

# Initialize variables to accumulate totals
total_employees = 0
total_overtime = 0
total_regular_hour = 0
total_gross = 0

emp_name = input("Enter employee's name or 'Done' to terminate: ")

# User is able to use lowercase or uppercase whew terminating the loop
while emp_name.lower() != "done":
  # Get the hours worked and pay rate
  hours_worked = float(input(f"How many hours did {emp_name} work? "))
  pay_rate = float(input(f"What is {emp_name}'s pay rate? "))

  # Check if overtime is applicable
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

  # Accumulate totals
  total_employees += 1
  total_overtime += ot_pay
  total_regular_hour += reg_pay
  total_gross += gross_pay

  # Display the employee's pay information
  print()
  print(F"{'Employee Name:':<15} {emp_name}")
  print()

  print(f"{'Hours Worked':<20}{'Pay Rate':<20}{'OverTime':<20}{'OverTime Pay':<20}{'RegHour Pay':<20}{'Gross Pay'}")
  print("----"*35)
  print(f"{hours_worked:<20}${pay_rate:<20.2f}{ot_hours:<19}${ot_pay:<19.2f}${reg_pay:<19.2f}${gross_pay:<.2f}")

  # Ask for the next employee's information
  emp_name = input("Enter employee's name or 'Done' to terminate: ")

# After the loop ends, display the totals
print()
print(f"Total number of employees entered: {total_employees}")
print(f"Total amount paid for overtime: ${total_overtime:.2f}")
print(f"Total amount paid for regular hours: ${total_regular_hour:.2f}")
print(f"Total amount paid in gross: ${total_gross:.2f}")

