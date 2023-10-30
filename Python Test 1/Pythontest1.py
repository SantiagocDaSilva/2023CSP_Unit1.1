# Follow the instructions in the lab document to calculate the mortgage information.
# Everytime you have a new value to output to the screen, make sure to use the proper variable from below.


# Starting data and variable setup - DO NOT EDIT
principal = 250000
annualRate = 4.85
numYears = 30
monthlyPayment = 0
totalPayments = 0
totalInterest = 0


# All student work should be between this and the output section.
#DO NOT EDIT ABOVE HERE
numMonths = 12 * 30
annualRate = 4.85 / 100
monthlyPaymentn= annualRate * (1 + annualRate ** numMonths)
monthlyPaymentd = (1 + annualRate ** numMonths)-1
monthlyPayment = (monthlyPaymentn/monthlyPaymentd)*principal




#DO NOT EDIT BELOW HERE
#Output the data after your calculations here:
print("Principle: " + str(principal))
print("Annual rate: " + str(annualRate))
print("Number of Years: " + str(numYears))
print("Monthly Payments: " + str(monthlyPayment))
print("Total Payments: " + str(totalPayments))
print("Total Interest: " + str(totalInterest))


