#Advanced python

# 1. find expected output of the follwing python program:

#solution:
data = [10, 501, 22, 37, 100, 999, 351] 
result = filter(lambda x: x > 4, data)
#to check given list, if any number is greater 4 and print that number in a list format
print(list(result))
#expected_output = [10, 501, 22, 37, 100, 999, 351]

#2. write a python code using lambda function to check every element of a list is an integer or string:
#given:
Given_list = [23, 45, 'you', "are", 78, 'greater']
#solution:
string_list = list(filter(lambda str_list:type(str_list) == str, Given_list))
#to find string in list we useing lambdafunction with filter(), we can get string elements
integer_list = list(filter(lambda int_list:type(int_list) == int, Given_list))
#to integer elements we using same concept
print("Actual given list :" +str(Given_list))
print(" strings are present in given list :" +str(string_list))
print("integers are present in a given list :" +str(integer_list))

#3.using python lambda function create afibonacci series from 1 to 50 elements:
#solution:
from functools import reduce
fibonaic_list = lambda tot_element:reduce(lambda given_list,_: given_list + [given_list[-1] + given_list[-2]], range(tot_element-2), [0,1])
print("fibonaicc series from 1 to 50 :" +str(fibonaic_list))

# 4. write python function to validate Regular Expression for the following:

#we use re module from library
import re
# we create class and add multiple methods
class Regex:
    def __init__(self, details):
        self.details = details
        #a.validate Email_Address
    def email_address(self):
        email_regex = "^[\w.]+[\@][a-z]{5}+[\.][a-z]{3}$"
        if re.match(email_regex, self.details):
            return "it is a valid email_Address"
        else:
            return "it is not valid email_address"
        #b.to validate bangladesh mobile number using regex
    def validate_bangladesh_number(self):
        mobile_number = "^[01]{2}[0-5]{4}[0-9]{5}$"
        if re.match(mobile_number, self.details):
            return "it is a valid mobile number"
        else:
            return "it is not valid mobile number"
        #c.verifying its  usa telephone number or not:
    def validate_usa_telephone_number(self):
        telephone_number = "^([+1]){2}[1-2]{3}[4-6]{3}[0-9]{4}$"
        if re.match(telephone_number, self.details):
            return "it is valid telephone number"
        else:
            return "it is not valid telephone number"
        #d.validate apassword
    def password_validation(self):
        password = '^(?=.*[\w])(?=.*[A-Z])(?=.*[\d])(?=.*[!@#$%^&*])[A-Za-z\d!@#$%^&*]{16}$'
        if len(self.details) < 16:
            return "password must be 16 character"
        elif not re.search('[0-9]', self.details):
            return "password must contain single digit"
        elif not re.search('[A-Z]', self.details):
            return ("password must contain 1 upper case")
        elif not re.search('[a-z]', self.details):
            return ("password should have one lower case")
        elif not re.search('[!@#$%^&*]', self.details):
            return ("password must contain one special character")
        elif re.match(password, self.details):
            return ("it is valid password")
        else:
            return "it is not valid password"
print(Regex("dk78091@gmail.com").email_address())
print(Regex("01234589421").validate_bangladesh_number())
print(Regex("+11226455431").validate_usa_telephone_number())
print(Regex("Quite@2023inyouT").password_validation())