# password validation

import re

pattern = re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,}$")

password = 'BlablaB123$$$'

result = pattern.fullmatch(password)

if result:
    print('valid password')
else:
    print('invalid password')