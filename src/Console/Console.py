import sys
sys.path.append("src")
sys.path.append("src/LiquidacionNomina")
from LiquidacionNomina import Liquida_nomina1, validations 

def validate_empty(value):
    return value if value else "0"

print("<<< PROGRAM RUNNING >>>")
print("::::::::::::::::::::::::::::::::")
print("**NOTE: For data that does not apply to your profile, please leave it blank, just press ENTER and continue with the next data point")
print("----------------------------------------------------------------------")
monthly_salary = validate_empty(input("Enter your monthly income ($COP):"))
weeks_worked = validate_empty(input("Enter the number of weeks worked to settle:"))
holiday_hours_worked = validate_empty(input("Enter the hours worked on holidays (ONLY IF APPLICABLE):"))
overtime_day_hours = validate_empty(input("Enter the number of daytime overtime hours worked (ONLY IF APPLICABLE):"))
overtime_night_hours = validate_empty(input("Enter the number of nighttime overtime hours worked (ONLY IF APPLICABLE):"))
holiday_overtime_hours = validate_empty(input("Enter the overtime hours worked on holidays (ONLY IF APPLICABLE):"))
leave_days = validate_empty(input("Enter the number of days you had on leave during the working period (ONLY IF APPLICABLE):"))
sick_days = validate_empty(input("If you had any sick leave during the working period, enter the number of days (ONLY IF APPLICABLE):"))

# try:
liquidacion = Liquida_nomina1.Liquidacion(
    monthly_salary, weeks_worked, holiday_hours_worked,
    overtime_day_hours, overtime_night_hours, holiday_overtime_hours, leave_days, sick_days
)
result= liquidacion.CalcularLiquidacion()
print(f"The total amount of your settlement is: {result}")
# except Exception as up_error:
    # print("*** ERROR ***")
    # print(str(up_error))