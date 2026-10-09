# Program to find LCM
numberLargest = int(input("Enter Largest number : "))
numberSmallest = int(input("Enter Smallest number : "))

number = numberLargest
numberLCM = int((numberLargest*numberSmallest)/number)

while(numberSmallest):
    numberStore = numberSmallest
    numberSmallest = numberLargest % numberSmallest
    numberLargest = numberStore

print("LCM is : ", numberLCM)