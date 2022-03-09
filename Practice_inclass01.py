num=int(input())
while(num<0):
    print("Please input an positive number") 
    num=int(input())
else:
    if(num%2 == 0 | num%3 == 0 | num%4 ==0):
        print("The number",num,"is multiple of 2,3,4")
    else:
        print("The number",num,"is not multiple of 2,3,4")

print("End of program")
