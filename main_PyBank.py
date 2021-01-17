# Import Dependencies
import os, csv
import statistics

# create variable to store path location 
budget_data = os.path.join("PyBank",'Resources', "budget_data.csv")

# Open csv 
with open(budget_data,newline="", encoding="utf-8") as budget:

     # create variable csvreader to store budget.csv info
    csvreader = csv.reader(budget) 

    # Skip the header 
    next(csvreader)  

# Create lists
    Tm = []
    Tp = []
    mth_profit_change = []

    # loop through the rows in the file 
    for row in csvreader: 

        # Append the total months and total profit to the lists
        Tm.append(row[1])
        Tp.append(int(row[1]))

    # loop through the profits in order to get the monthly change in profits
    for row in range(1, len(Tp)):
        
        # Take the difference between months and append to monthly profit change
        mth_profit_change.append(Tp[row]-Tp[row-1])
        
# Obtain the max and min of the the montly profit change list
greatest_increase = max(mth_profit_change)
greatest_decrease = min(mth_profit_change)

# Create variable to store Max and Min increase in month info
max_increase_month = mth_profit_change.index(greatest_increase) + 1
max_decrease_month = mth_profit_change.index(greatest_decrease ) + 1 

# Print Statements

print()
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(Tm)}")
print(f"Total: ${sum(Tp)}")
print(f"Average Change: ${round(sum(mth_profit_change)/len(mth_profit_change),2)}")
print(f"Greatest Increase in Profits: {Tm[max_increase_month]} (${(str(greatest_increase))})")
print(f"Greatest Decrease in Profits: {Tm[max_decrease_month]} (${(str(greatest_decrease))})")
print()

# output to a text file

output_file = os.path.join("PyBank",'Resources', "budget_data_analysis.txt")
with open(output_file,"w") as file:

    file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Months: {len(Tm)}")
    file.write("\n")
    file.write(f"Total: ${sum(Tp)}")
    file.write("\n")
    file.write(f"Average Change: ${round(sum(mth_profit_change)/len(mth_profit_change),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {Tm[max_increase_month]} (${(str(greatest_increase))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {Tm[max_decrease_month]} (${(str(greatest_decrease))})")
