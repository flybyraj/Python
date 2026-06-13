# Conditional Statements

light = "Green"

if (light == "Red"): # if always check
    print("Stop")
elif (light == "Green"): # elif only check if all above conditions are False
    print("Go")
elif (light == "Yellow"):
    print("Look")
else:                    # Else run when all above conditions are false
    print("Light is Broken") 

print("End of code")