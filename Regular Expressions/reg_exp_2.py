# e-mail validation

import re

pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
e_mail = 'bartekhenry14@gmail.com'

result = pattern.match(e_mail)
print(result)
