# At least 8 char long
# contain any sort letters, numbers $%#@
# has to end with a number
import re

pattern = re.compile(
    r"(^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$)")
string = 'andrei'

pattern2 = re.compile(r"[a-zA-Z0-9$%#@]{8,}\d")
password = 'sdfs'
check = pattern2.fullmatch(password)
print(check)
