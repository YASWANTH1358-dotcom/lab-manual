#print 1 to 100
a = 1;
while a<=100:
    print(a);
    a=a+1;


#print odd numbers 1to 50
for i in range(1,50):
     if(i%2!=0):
         print(i);


#print sum of first 20 natural numbers
sum=0;
for i in range(1,21):
     sum=sum+i;
print("sum of first 20 natural numbers is :",sum);


#print even 0 to 50 
for i in range(1,51):
     if(i%2==0):
         print(i);


#reverse a given number using loop
#sum = 100
#for i in sum():
 #    sum = sum-i;
  #   print(sum);


#factorial of a number
num = int(input("enter a number :" ));
factorial = 1;
if(num<0):
     print("factorial does not exist for negitive numbers");
elif(num == 0):
     print("the factorial of 0 is 1");
else:
     for i in range(1,num + 1):
         factorial = factorial * i;
print("the factorial of a ",num,"is",factorial);

