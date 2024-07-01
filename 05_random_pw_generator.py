import random

alphabet = 'a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z'
alphabet_upper = alphabet.upper()
#print(alphabet_upper) 

number = '0,1,2,3,4,5,6,7,8,9'

symbol = "@,#,&,*,$"

password_combine = alphabet + alphabet_upper + number +symbol
#print(password_combine)

list = password_combine.split(",")
#print(list)

random0 = random.choice(list)
random1 = random.choice(list)
random2 = random.choice(list)
random3 = random.choice(list)
random4 = random.choice(list)
random5 = random.choice(list)
random6 = random.choice(list)
random7 = random.choice(list)
random8 = random.choice(list)
random9 = random.choice(list)

password = random0 + random1 + random2 + random3 + random4 + random5 +random6 + random7 + random8 + random9
print(f"The generated password is: {password}" )