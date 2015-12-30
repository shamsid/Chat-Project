'''
Created on Oct 16, 2015

@author: shamsher.ahmed
'''
class MobileNumberNotPresent(Exception):
    def __init__(self):
        super().__init__("The mobile number is not present")
      
class InvalidPassword(Exception):
    def __init__(self):
        super().__init__("The password is invalid")
        
class InvalidPasswordException(Exception):
    def __init__(self):
        super().__init__("The password is invalid")

class InvalidMobileNumberException(Exception):
    def __init__(self):
        super().__init__("Invalid Mobile Number")
        
class InvalidConfirmPasswordException(Exception):
    def __init__(self):
        super().__init__("Password and Confirm Password do not match")          
        
class InvalidSecurityQuestionException(Exception):
    def __init__(self):
        super().__init__("Security Question Not Valid")     

class InvalidSecurityAnswerException(Exception):
    def __init__(self):
        super().__init__("Security Answer Not Valid")    
         
class InvalidCaptchaException(Exception):
    def __init__(self):
        super().__init__("Invalid Captcha")  
class InvalidAnswerException(Exception):
    def __init__(self):
        super().__init__("Wrong Answer")
class InvalidDateFormatException(Exception):
    def __init__(self):
        super().__init__("Invalid Date format Entered");
class MobileNumberEmptyException(Exception):
    def __init__(self):
        super().__init__("Mobile Number Empty")
class SenderSameAsReceiver(Exception):
    def __init__(self):
        super().__init__("Sender Same as Receiver")
class InvalidReceiver(Exception):
    def __init__(self):
        super().__init__("Invalid Receiver")