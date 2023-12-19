import re
import random


def validate_telephone(phone):
    """
    中国联通的号码段： 
        130,131,132,155,156,185,186,145,176
    中国移动的号码段： 
        134,135,136,137,138,139,147,150,151,152,157,158,159,178,182,183,184,187,188
    中国电信的号码段
        133,153,189
    """
    reg = '^1(3[0-9]|4[5,7]|5[0,1,2,3,5,6,7,8,9]|6[2,5,6,7]|7[0,1,6,7,8]|8[0-9])\d{8}$'
    if re.match(reg, phone):
        return True
    return False




def generate_verify_code():
    codes = random.sample('123456789', 6)
    return ''.join(codes)


