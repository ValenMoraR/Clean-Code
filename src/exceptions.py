# Custom exceptions for specific validation error cases
class NegativeValue(Exception): 
    pass

class InvalidValue(Exception): 
    pass

class NotAnIntegerValue(Exception):
    pass

class CommaSeparator(Exception):
    pass

class MoreThan8HoursWorkedOnHoliday(Exception):
    pass

class ZeroWeeksWorked(Exception):
    pass