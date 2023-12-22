'''2.Write a Python program to check the validity of a password.
Primary conditions for password validation:
Minimum 8 characters
The alphabet must be between[a-z]
At least one alphabet should be of uppecase[A-Z]
At least one number or digit between[0-9]
At least one character from[_ or @ or $]
'''

l,u,sp,d=0,0,0,0
s='Harikakotha83@'
if (len(s)>=8):
    for i in s:
        if(i.islower()):
            l+=1
        if(i.isupper()):
            u+=1
        if(i.isdigit()):
            d+=1
        if(i=='_' or i=='@' or i=='$'):
            sp+=1
if (l>=1 and u>=1 and sp>=1 and d>=1 and l+u+sp+d==len(s)):
    print('valid password')
else:
    print('invalid password')
