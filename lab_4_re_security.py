import re
text = input('Please Input your password. The passsword has to have 12 characters with special letter and uppercase with lowercase letters')
matches = re.findall(r'.{12,}', text)
if matches:
  has_len=True
else:
  has_len=False
  print('It does not meet the input requirement1')
matches = re.findall(r'[A-Z]', text)
if matches:
  has_letter=True
else:
  has_letter=False
  print('It does not meet the input requirement2')
matches = re.findall(r'[a-z]', text)
if matches:
  has_cap=True
else:
  has_cap=False
  print('It does not meet the input requirement3')
matches = re.findall(r'[!~#$%^&*{}+_]', text)
if matches:
  has_symboll=True
else:
  has_symboll=False
  print('It does not meet the input requiremet4')
matches = re.findall(r'[0-9]', text)
if matches:
  has_num=True
else:
  has_num=False
  print('It does not meet the input requirement5')
print()
if has_len and has_letter and has_cap and has_symboll and has_num:
  combine = True
  print('The password is strong, please click "next" to continue with the registration')
else:
  combine = False
  print('Password is weak Please create a password with numbers, capital and small letter, and special characters')
