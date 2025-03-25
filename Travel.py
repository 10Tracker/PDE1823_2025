year = int(input("Greetings! What is your year of origin? ")) # missing = , ", bracket after int

if year <= 1900: # missing :, 
    print ("Woah, that's the past!") # ' instead "
elif 1900 < year <= 2020: # present range of time
    print ("That's totally the present!")
else:      # elif instead of else
    print ("Far out, that's the future!!")
