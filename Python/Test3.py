value = int(input("enter the purchase amount: "))
received = int(input("enter the value received: "))

print("---------------")
if received > value:
        print("your change is equal to: ",received-value)
         
else:
    print("insufficient amount to pay")