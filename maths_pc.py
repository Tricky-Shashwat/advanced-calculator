#I am sorry for being inspired by OnePlus                                                                                                                                                                                                                                                                                       Deliberately slowing down processes                                                                                    
print("                                            ")
print("                                            ")
print("                                            ")
print("                                              Maths Calculator & Converter")
print("                                            ")
print("                                            ")
print("                                                   Made By Shashwat")
print(' ')
print(' ')

print(" Note: Use only given options, using others will return error")
#There are so many spaces so as to look nice ;D
print("     Select Operation")
print("  A. Convert")
print("  B. Arithmetic Operaions")
print("  C. Arithmetic Progressions")
print("  D. Geometric Progressions")
print("  E. Table of numbers")
print("  F, Area and perimeter and volume Calculator")
print("  G. Exit")
print("    ")
while True:
        
    choice = input("     Enter choice(A/B/C/D/E/F/G): ")
#*There was one infinite repeating loop error and the only proof is in my phone*
#Cleaned the interface to look neat
    if choice == 'A':
            print("                                            ")
            print("                                            ")
            print("     Select Operation")
            print(" 1.  Celsius into Fahrenheit.")
            print(" 2.  Fahrenheit into Celsius")
            print(" 3.  Celsius into Kelvin")
            print(" 4.  Centimeters into Meter")
            print(" 5.  Meter into Centimeters")
            print(" 6.  Kilometers into Meters")
            print(" 7.  Grams into Kilograms")
            print(" 8.  Kilograms into Grams")
            print(" 9.  Tonne into Kilograms")
            print(" 10. Kilograms to Pounds")
            print("  ")
           
            choice = input("     Enter choice(1/2/3/4/5/6/7/8/9/10): ")
            if choice == '1':
                
                    x = float(input("    Enter value for x "))
                    print("    The temperature in Fahrenheit is", (x*9/5)+32,"⁰F")

            elif choice == '2':
                    x = float(input("    Enter value for x "))
                    print("    The temperature in Celsius is", (x-32)*5/9,"⁰C")
        
            elif choice == '3':
                    x = float(input("    Enter value for x "))
                    print("    The temperature in Kelvin is ", x+273.15,"K")

            elif choice == '4':
                    x = float(input("    Enter value for x "))
                    print("    The distance in Meter is", x/100,"m")
            
            elif choice == '5':
                    x = float(input("    Enter value for x "))
                    print("    The distance in Centimeters is", x*100,"cms")
           
            elif choice == '6':
                    x = float(input("    Enter value for x "))
                    print("    The distance in meters is", x*1000,"m")
          
            elif choice == '7':
                    x = float(input("    Enter value for x "))
                    print("    The mass in kilograms is", x/1000,"Kgs")
          
            elif choice == '8':
                    x = float(input("    Enter value for x "))
                    print("    The mass in Grams is", x*1000,"g")
         
            elif choice == '9':
                    x = float(input("    Enter value for x "))
                    print("    The mass in Kilograms is", x*1000,"Kgs")
                    
            elif choice == '10':
                    x = float(input("    Enter value for x "))
                    print("    The mass in pounds is", x*2.2046,"lbs")
                    
            else:
                                    print("                                            ")
                                    print("    INVALID INPUT")        
                   
            break

#Update 09/08/2021 Added exit and arithmetic progressions                               
    elif choice == 'B':
            print("                                            ")
            print("                                            ")    
            print("     Select Operation")
            print(" 1.  Addition.")
            print(" 2.  Subtraction of b from a")
            print(" 3.  Multiplication")
            print(" 4.  Dividing a by b")
            print(" 5.  The remainder when dividing a by b")
            print(" 6.  Quotient of a/b")
            print(" 7.  Is the numbere divisible?")
            print(" 8.  a raised to power b")
            print(" 9.  Is x greater than y?")
            print(" 10. Is x is equal to y?")
            print(" 11. Is x not equal to y?")
            print("  ")
            choice = input("     Enter choice(1/2/3/4/5/6/7/8/9/10/11): ")
            if choice == '1':
                    x = float(input("    Enter value for x "))
                    y = float(input("    Enter value for y "))
                    print("    ",x, "+", y, "=", x+y)

            elif choice == '2':
                    x = float(input("    Enter value for x "))
                    y = float(input("    Enter value for y "))
                    print("    ",x, "-", y, "=", x-y)

            elif choice == '3':
                    x = float(input("    Enter value for x "))
                    y = float(input("    Enter value for y "))
                    print("    ",x, "multiplied by", y, "=", x*y)

            elif choice == '4':
                    x = float(input("    Enter value for x "))
                    y = float(input("    Enter value for y "))
                    print("    ",x, "divided by", y, "=", x/y)
            
            elif choice == '5':
                    x = float(input("    Enter value for x "))
                    y = float(input("    Enter value for y "))
                    print("    ",x, "remainder of x/y", y, "=", x%y)
           
            elif choice == '6':
                    x = float(input("    Enter value for x "))
                    y = float(input("    Enter value for y "))
                    print("    When",x, "/", y, "The quotient=", x//y)
            
            elif choice == '7':
                    x = float(input("    Enter value for dividend "))
                    y = float(input("    Enter value for divisor "))
                    if x%y==0:
                        print("The no. is divisible")
                    else:
                        print("The no. is not divisible")
            elif choice == '8':
                    x = float(input("    Enter value for x "))
                    y = float(input("    Enter value for y "))
                    print("    ",x, "raised to the power", y, "=", x**y)
          
            elif choice == '9':
                    x = float(input("    Enter value for x "))
                    y = float(input("    Enter value for y "))
                    print("    ",x, "is greater than", y, "    ", x>y)
          
            elif choice == '10':
                    x = float(input("    Enter value for x "))
                    y = float(input("    Enter value for y "))
                    print("    ",x, "is equal to", y, "    ", x==y)
            
            elif choice == '11':
                    x = float(input("    Enter value for x "))
                    y = float(input("    Enter value for y "))
                    print("    ",x, "not equal to", y, "    ", x!=y)
            else:
                    print("                                            ")
                    print("    INVALID INPUT")
#Ah those nasty errors are finally resolved
                    break
                    
    elif choice == 'C':
            print("                                            ")
            print("                                            ")    
            print("    Select Operation")
            print(" 1. Find the nth term")
            print(" 2. Find sum using main formula")
            print(" 3. Find sum using first and final term")   
            choice = input("    Enter choice(1/2/3): ")
            if choice == '1':
                    a = float(input("    Enter value for first term "))
                    b = float(input("    Enter value for n "))
                    c = float(input("    Enter value for common difference "))
                    an=a+(b-1)*c
                    print("   ",an)
                    
            elif choice == '2':
                    a = float(input("    Enter value for first term "))
                    b = float(input("    Enter value for n"))
                    c = float(input("    Enter value for common difference "))
                    sn=(b/2)*((2*a)+(b-1)*c)
                    print("    The sum of terms is",sn)
           
            elif choice == '3':
                    a = float(input("    Enter value for first term "))
                    b = float(input("    Enter value for n "))
                    d = float(input("    Enter value of last term "))
                    Sn=(b/2)*(a+d)
                    print("    The sum of terms is",Sn)
                    
            else:
                    print("                                            ")
                    print("    INVALID INPUT")
    
                    break
#Update: 2 September added GP
    elif choice == 'D':
            print("                                            ")
            print("                                            ")    
            print("    Select Operation")
            print(" 1. Find Common ratio")
            print(" 2. Find G.P. sum")
            print(" 3. Find nth term")
            choice = input("    Enter choice(1/2/3): ")
            if choice == '1':
                    a = float(input("    Enter first term "))
                    at = float(input("    Enter the another term "))
                    n = int(input("    which th term is the another term "))
                    w = 1/(n-1)
                    R=at/a
                    f = R**w
                    print("    The common ratio is",f)
            elif choice == '2':
                    a = float(input("    Enter first no. "))
                    r = float(input("    Enter common ratio "))
                    n = float(input("    Enter till which term "))
                    Sni=r**n
                    Snf=Sni-1
                    Sn= a*Snf
                    Snk=r-1 
                    Snff=Sn/Snk
                    print("    The sum is",Snff)
            elif choice == '3':
                    a = float(input("    Enter first no. "))
                    r = float(input("    Enter common ratio "))
                    n = float(input("    Enter which term "))
                    anf=n-1
                    ani=r**anf
                    an=a*ani
                    print("    The term is",an)
            else:
                                    print("                                            ")
                                    print("    INVALID INPUT")        
    elif choice == 'E':
            num=int(input("    Enter number     "))
            x=int(input("    Till what times  "))
            for i in range(1,x+1):
                print("   ",num,'x',i,'=',num*i)
    
    elif choice == 'F':
            print("                                            ")
            print("                                            ")    
            print("    Select Operation")
            print(" 1. Square and Cube")
            print(" 2. Rectangle and Cuboid")
            print(" 3. Circle and Sphere")
            print(" 4. Cylinder")
            print(" 5. Cone")
            print(" 6. Semi-circle and Hemisphere")
            choice = input("    Enter choice(1/2/3/4/5/6): ")
            if choice == '1':
                    a = float(input("    Enter the side "))
                    print("     Perimeter = ",4*a,"units","\n","    Area      = ",a**2,"sq. units","\n" ,"    Volume    = ",a**3,"cubic units")
            elif choice == '2':
                    l = float(input("    Enter the length "))
                    b = float(input("    Enter the breadth "))
                    h = float(input("    Enter the Height "))
                    print("     Perimeter =   ",2*(l+b),"units","\n","    Area      = ",l*b,"sq. units","\n" ,"    Volume    = ",l*b*h,"cubic units")
            elif choice == '3':
                    r = float(input("    Enter the radius "))
                    print("     Circumference= ",2*22/7*r,"units","\n","    Area         = ",22/7*r*r,"sq. units","\n","    Volume       = ",(1.34)*22/7*r*r*r,"cubic units")
            elif choice == '4':
                    r = float(input("    Enter the radius "))
                    h = float(input("    Enter the height "))
                    print("     Volume= ",22/7*r*r*h,"cubic units")
            elif choice == '5':
                    r = float(input("    Enter the radius "))
                    h = float(input("    Enter the height "))
                    print("     Volume= ",1/3*22/7*r*r*h,"cubic units")
            elif choice == '6':
                    r = float(input("    Enter the radius "))
                    print("     Circumference= ",22/7*r,"units","\n","    Area         = ",11/7*r*r,"sq. units","\n","    Volume       = ",(1.34)*11/7*r*r*r,"cubic units")

            else:
                                    print("                                            ")
                                    print("    INVALID INPUT")   
    elif choice == 'G':
                    exit()
                    
    else:
                    print("                                            ")
                    print("    INVALID INPUT")
    
    break           
else:
    
    print("                                            ")
    print("    Invalid Input")