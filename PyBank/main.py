# Import modules
import os
import csv

# Set up the path for the csv file
csvpath = os.path.join("Resources", "budget_data.csv")

# Set up empty lists to store data
months = []
profits = []
profitChanges = []

# Open the csv, ensuring it recognizes that the columns are separated by commas. Use the next function to skip the header row
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)

# Loop through each row, add the month to the list titled months, add the profit or loss to the list titled profits
    for row in csvreader:
        months.append(row[0])
        profits.append(int(row[1]))

# Look through the profits list, which is already ordered chronologically, and find the current and previous month's values. Set them as variables so they can be manipulated 
    for i in range(1, len(profits)):
        currentMonth = profits[i]
        previousMonth = profits[i - 1]

# Append the profitChanges list with the difference between the current and previous months, use these values to calculate the average change and put it in a variable
        profitChanges.append(currentMonth - previousMonth)
    averageChange = sum(profitChanges) / len(profitChanges)

# Using the max and min functions, find the greatest increase and decrease from the profitChanges list
    greatestIncrease = max(profitChanges)
    greatestDecrease = min(profitChanges)

# Use the index function to find the index of the greatest increase or decrease from the profitChanges list. Add one to it so it aligns with the proper month
# in the months list, and set this value to the index for the months list for greatestIncreaseMonth and greatestDecreaseMonth
    greatestIncreaseMonth = months[profitChanges.index(greatestIncrease) + 1]
    greatestDecreaseMonth = months[profitChanges.index(greatestDecrease) + 1]

# Print the results to the terminal
    print("Financial Analysis")
    print("----------------------------")
    print("Total Months: " + str(len(months)))
    print("Total: $" + str(sum(profits)))
    print("Average change: $" + str(round(averageChange, 2))) # The round function rounds it to cents
    print("Greatest Increase in Profits: " + greatestIncreaseMonth + " ($" + str(greatestIncrease) + ")")
    print("Greatest Decrease in Profits: " + greatestDecreaseMonth + " ($" + str(greatestDecrease) + ")")

# Set up the output file
output_file = os.path.join("Analysis", "Financial_Analysis.txt")
with open(output_file, "w") as textfile:

# Using the textfile.write function, print the same things as are printed in the terminal. The \n command ensures each line is printed on a new line.
    textfile.write("Financial Analysis\n")
    textfile.write("----------------------------\n")
    textfile.write("Total Months: " + str(len(months)) + "\n")
    textfile.write("Total: $" + str(sum(profits)) + "\n")
    textfile.write("Average change: $" + str(round(averageChange, 2)) + "\n") # The round function rounds it to cents
    textfile.write("Greatest Increase in Profits: " + greatestIncreaseMonth + " ($" + str(greatestIncrease) + ")\n")
    textfile.write("Greatest Decrease in Profits: " + greatestDecreaseMonth + " ($" + str(greatestDecrease) + ")\n")