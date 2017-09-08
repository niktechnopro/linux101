#Fibonacci
#make the fib function which returns the value of the fib number if you put an argument in it
def fib(position):
    if(position ==0 or position ==1):
        return 1;
    else:
        return fib(position-2) + fib(position-1);

#loop through the fib function to find the sum from 1 to when sum of fib numbers exceeds 4000000
sum = 0;
#final_position = int(input("enter the number position in Fibonacci sequence: "))
counter = 1
while True:    
  if fib(counter) >= 4000000:
    print ("fibonacci number is higher than 4000000,")
    print ("Position: %s and Fib number: %d" % (counter, fib(counter)))
    break
  else:
    if fib(counter)%2 == 0:
      sum +=fib(counter);
  counter += 1  
print("Total sum of even numbers: %s" % (sum));