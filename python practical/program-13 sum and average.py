#sum and average
numbers =[25,68,69,8,78]
total = sum(numbers)
average = total/len(numbers)
print("sum = ",total)
print("average = ",average)
for i in numbers:
    if i%2==0:
        print(i)
