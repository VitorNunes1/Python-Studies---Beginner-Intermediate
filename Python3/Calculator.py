def calculator():
 try:
   calculator=("   Calculator", "Enter: (a) to addition", "Enter: (s) to substraction", "Enter: (m) to multiplication", "Enter: (d) to division")
   
   for c in calculator:
     print(c)

   calc=input("Enter which operation will you use: ")
   input1=int(input("Enter the firts value: "))
   input2=int(input("Enter the other value: "))
   
   if calc == "a":
     print(input1+input2)
   elif calc == "s":
     print(input1-input2)
   elif calc == "m":
     print(input1*input2)
   elif calc == "d":
     print(input1/input2)
   else:
     print("Try using one of the options.")
 except:
  print("option not viable")

calculator()