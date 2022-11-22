#This program is to input feet and inches from the user and converting that to meters
while True:

    feet_inches = input("Enter feet and inches : ")
    try:
        def parse(feet_inches):
            parts = feet_inches.split(" ")
            feet = float(parts[0])
            inches = float(parts[1])
            return {"feet":feet,"inches":inches}
        def convert(feet_inches):

            #The split method split the string and returns a list of strings split at that character.

            #Remember the (Input) function always accepts variables as string only
            parts = feet_inches.split(" ")
            feet = float(parts[0])
            inches = float(parts[1])

            meters = feet*0.3048+inches*0.0254 # now lets convert it to meters
            return meters
             #return f"{feet} feet and {inches} inches is equal to {meters} meters.  "
        #print(convert(feet_inches))
        #what if we want to include this in a bigger program say whether or not if a kid is eligible to get in a ride
        #lets do that
        #for that we have to store the result of the function in a variable
        #but the function returns a string
        #so here comes the concept of decoupling
        #so just return one single values
        result = convert(feet_inches)
        print(f"{parse(feet_inches)['feet']} feet and {parse(feet_inches)['inches']} inches is equal to {result} meters ")
        if result < 1:
            print("Sorry the Child is too short for the ride ")
        else:
            print("Welcome to the Ride")
    except IndexError:
        print("Please Enter a Valid height , if the height is only 4 feet enter 4 0")
        continue
