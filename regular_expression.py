
# Q1 A
import re
string1 = "abb29ABCLK%lCnrDBCabbbb" 
pat = "abbbb"
output = re.search(pat,string1)
print(output.group())

# Q1 B
string1= "abb29ABCLK%lCnrDBCabbbb"
s_dot= re.search("[A-Z][a-z]+", string1)
print("The outpout is: ", s_dot)

# Find the string with lowercase characters immediately after the uppercase characters until there are no more lowercase characters.