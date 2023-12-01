def prompt_menu():
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))

    print("""
Choose an operation
      1. Sum
      2. Difference
      3. Product
      4. Division
      5. Power
      6. Division with remainder """)

    op=int(input("enter the choice number:"))

    return a, b, op

def calculate():
  a,b,op = prompt_menu()

  if op == 1:
   print("Sum: {}+ {}= {}".format(a,b,a+b))
  elif op==2:
    print ("Difference: {} - {}= {}".format(a,b,a-b))
  elif op==3:
    print ("Product: {}*{}= {}".format(a,b,a*b))
  elif op==4:
    try:
      print ("Quotient: {} / {}= {}".format(a,b,a/b))
    except:
      print("Division by 0 not possible")
  elif op == 5:
    print ("Power: {}^{}= {}".format(a,b,a**b))
  elif op == 6:
    try:
      print ("Division with remainder: {}/{}= {} Remainder: {}".format(a,b,a//b,a%b))
    except:
      print("Division by 0 not possible")

  else: 
    print("there is no such choice")
  loop()

def loop():
  choice= input("Do you continue? (Y,N): ")
  if choice.upper() == "Y":
      calculate()
  elif choice.upper() == "N":
    print("See you later!")
  else :
    print("invalid input")
    loop()
calculate()  

