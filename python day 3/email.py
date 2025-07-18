email = input('enter your email')
at_index = email.index('@')
username = email[:at_index]
domain = email[at_index+1:]
print('username',username)
print('domain',domain)