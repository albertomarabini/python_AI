 # Put this at the top of your kata04.py file 
kata = (0, 4, 132.42222, 10000, 12345.67)
print("module_{kata[0]:02d} ex_{kata[1]:02d} : {kata[2]:.2f} {kata[3]:.2E}, {kata[4]:.2E}".format(kata = kata))