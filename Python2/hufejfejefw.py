lower_Range = int(input("Enter lower range : "))  
upper_Range = int(input("Enter upper range : "))  
  
for n in range(lower_Range,upper_Range + 1):  
   sum = 0  
   temp = n  
   while temp > 0:  
       digit = temp % 10  
       sum = sum + digit ** 3  
       temp = temp // 10  
  
   if n == sum:  
       print(n) 