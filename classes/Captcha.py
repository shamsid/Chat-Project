'''
Created on Oct 16, 2015

@author: vikas.yadav09
'''
import random;
import string;
class Captcha:
    def __init__(self):
        self.__captcha='';
    def generate_captcha(self):
        self.__captcha=''.join([random.choice(string.ascii_letters + string.digits) 
                     for i in range(5)]);   
    def get_captcha(self):
        self.generate_captcha();
        return self.__captcha; 
               