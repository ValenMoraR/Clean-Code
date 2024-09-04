import re

# Custom exceptions for specific error cases
class NegativeValue(Exception): 
    pass
class InvalidValue(Exception): 
    pass
class ZeroWeeksWorked(Exception): 
    pass
class MoreThan8HoursWorkedOnHoliday(Exception): 
    pass
class NotAnIntegerValue(Exception):
    pass
class CommaSeparator(Exception):
    pass

def CalcularLiquidacion(monthly_salary, weeks_worked,
                               time_worked_on_holidays=0, overtime_day_hours=0,
                               overtime_night_hours=0, overtime_holiday_hours=0,
                               leave_days=0, sick_days=0):
    """    
    Calculates the payroll settlement for employees in Colombia.
    ----------------------------------------------------
    monthly_salary: Base monthly salary of the employee.
    weeks_worked: Number of weeks worked during the period.
    transport_allowance: Monthly transport allowance (if applicable). Only if salary <= 2 SMLMV (2,600,000).
    time_worked_on_holidays: Time worked on holidays (not overtime).
    overtime_day_hours: Daytime overtime hours.
    overtime_night_hours: Nighttime overtime hours.
    overtime_holiday_hours: Overtime hours on holidays.
    health_contribution: Employee contribution to health (4% of the salary).
    pension_contribution: Employee contribution to pension (4% of the salary).
    solidarity_fund_contribution: Contribution to the solidarity fund (only if salary > 4 SMLMV).
    disability_deductions: Value for disabilities deducted from salary.
    sick_days: Number of days on sick leave.
    disability_percentage: Percentage of salary paid during disability leave.
    leave_days: Number of paid leave days, which may vary among:
        - 5 business days for mourning and marriage leave.
        - 14 calendar days for paternity leave.
        - 126 days for maternity or adoption leave.
    """
    # List of variables and descriptive names
    variables = [
        (monthly_salary, 'Monthly salary', True),
        (weeks_worked, 'Weeks worked', False),
        (time_worked_on_holidays, 'Time worked on holidays', False),
        (overtime_day_hours, 'Overtime day hours', False),
        (overtime_night_hours, 'Overtime night hours', False),
        (overtime_holiday_hours, 'Overtime holiday hours', False),
        (sick_days, 'Sick days', True),
        (leave_days, 'Leave days', True)
    ]

    converted_variables = []

    # Validate each variable
    for entry, variable_name, should_be_integer in variables:
        try:
            # Convert the entry to string to check if it contains a comma as a decimal separator
            entry_str = str(entry)
            # Check if the entry contains a comma as a decimal separator
            if ',' in entry_str:
                raise CommaSeparator(f"ERROR: Invalid data in {variable_name}: Use a period (.) as a decimal separator, not a comma (,).")

            # Convert to float to ensure it is numeric
            value = float(entry)

            # If it should be an integer, check that it has no decimals
            if should_be_integer and float(entry) != int(float(entry)):
                raise NotAnIntegerValue(f"ERROR: Invalid data in {variable_name}: An integer value was expected.")

            # Check if it is negative
            if value < 0:
                raise NegativeValue(f"ERROR: Invalid data in {variable_name}: Numbers cannot be negative.")
            
            # Convert to integer if it should be
            value = int(value) if should_be_integer else value
            
            # Add the converted variable to the list
            converted_variables.append((value, variable_name, should_be_integer))

        except ValueError:
            # If conversion to float also fails, it means there are non-numeric characters
            raise InvalidValue(f"ERROR: Invalid data in {variable_name}: Ensure it is a numeric value, not negative and without letters or special characters.")

    # Unpack the converted variables
    monthly_salary = converted_variables[0][0]
    weeks_worked = converted_variables[1][0]
    time_worked_on_holidays = converted_variables[2][0]
    overtime_day_hours = converted_variables[3][0]
    overtime_night_hours = converted_variables[4][0]
    overtime_holiday_hours = converted_variables[5][0]
    sick_days = converted_variables[6][0]
    leave_days = converted_variables[7][0]

    TOTAL_DAYS_IN_MONTH = 30
    DAILY_WORKING_HOURS = 8
    MAXIMUM_SALARY_WITH_TRANSPORT_ALLOWANCE = 2600000
    TOTAL_WORK_DAYS_PER_WEEK = 6
    VALUE_PER_HOUR_WORKED_ON_HOLIDAY = 1.75
    VALUE_PER_OVERTIME_DAY_HOUR = 1.25
    VALUE_PER_OVERTIME_NIGHT_HOUR = 1.75
    VALUE_PER_OVERTIME_HOLIDAY_HOUR = 2
    PERCENTAGE_TO_DEDUCT_FOR_HEALTH = 0.04
    PERCENTAGE_TO_DEDUCT_FOR_PENSION = 0.04
    PERCENTAGE_TO_DEDUCT_FOR_SOLIDARITY_FUND = 0.01
    SALARY_TO_DEDUCT_FOR_FUND = 4000000
    PERCENTAGE_TO_DEDUCT_FOR_WITHHOLDING = 0.05
    SALARY_TO_DEDUCT_FOR_WITHHOLDING = 4300000
    PERCENTAGE_TO_DEDUCT_FOR_DISABILITY = 0.333

    if weeks_worked == 0:
        raise ZeroWeeksWorked("INVALID VALUE: Weeks worked must be a number greater than or equal to 1.")
    
    if time_worked_on_holidays > DAILY_WORKING_HOURS:
        raise MoreThan8HoursWorkedOnHoliday("INVALID VALUE: Time worked on holidays cannot be more than 8 hours.")
    
    days_worked = weeks_worked * TOTAL_WORK_DAYS_PER_WEEK  # Convert weeks to days worked

    # Initial calculations
    transport_allowance = 162000 if monthly_salary <= MAXIMUM_SALARY_WITH_TRANSPORT_ALLOWANCE else 0
    daily_salary = monthly_salary / TOTAL_DAYS_IN_MONTH

    hourly_salary = daily_salary / DAILY_WORKING_HOURS
    # Calculation of additional payments
    earnings_for_holidays = time_worked_on_holidays * hourly_salary * VALUE_PER_HOUR_WORKED_ON_HOLIDAY 
    earnings_for_overtime_day = overtime_day_hours * hourly_salary * VALUE_PER_OVERTIME_DAY_HOUR
    earnings_for_overtime_night = overtime_night_hours * hourly_salary * VALUE_PER_OVERTIME_NIGHT_HOUR
    earnings_for_overtime_holidays = overtime_holiday_hours * hourly_salary * VALUE_PER_OVERTIME_HOLIDAY_HOUR

    # Total income
    total_income = (daily_salary * days_worked) + transport_allowance + earnings_for_holidays + \
                   earnings_for_overtime_day + earnings_for_overtime_night + earnings_for_overtime_holidays
          
    # Deductions
    health_deduction = total_income * PERCENTAGE_TO_DEDUCT_FOR_HEALTH
    pension_deduction = total_income * PERCENTAGE_TO_DEDUCT_FOR_PENSION
    solidarity_fund_deduction = total_income * PERCENTAGE_TO_DEDUCT_FOR_SOLIDARITY_FUND if monthly_salary > SALARY_TO_DEDUCT_FOR_FUND else 0
    leave_payment = leave_days * daily_salary
    withholding_tax = total_income * PERCENTAGE_TO_DEDUCT_FOR_WITHHOLDING if monthly_salary > SALARY_TO_DEDUCT_FOR_WITHHOLDING else 0
    disability_deduction = sick_days * daily_salary * PERCENTAGE_TO_DEDUCT_FOR_DISABILITY

    # Total amount to receive
    total_settlement = total_income - (health_deduction + pension_deduction + solidarity_fund_deduction + disability_deduction + 
                                       leave_payment + withholding_tax)
    
    return round(total_settlement, 2)
