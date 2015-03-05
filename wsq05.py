print ("Ernesto Gutierrez Valdes")
print ("A00817392")
fa = int(input("Insert temperature in Farenheit"))
ce = int(5*((fa - 32)/ 9))

print ("Your temperature in Celsius is: " , (ce))

if (ce > 100):
    print ("The state of the water is: gas")

if ( 100 > ce > 0):
    print ("The state of the water is: liquid")

if (ce < 0  ):
    print ("The state of water is: solid")
