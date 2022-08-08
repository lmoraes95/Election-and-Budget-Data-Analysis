


import os
import csv


t_months = 0
net_amount = 0
month_change = []
month_count = []
g_increase = 0
g_month_increase = 0
g_decrease = 0
g_month_decrease = 0

csvpath = os.path.join('.','Resources', 'budget_data.csv')

# open and read
with open(csvpath, newline='') as csvfile:
    
    reader = csv.reader(csvfile)
    
    csv_header = next(reader)
    row = next(reader)
    
    # Totals 
    previous_row = int(row[1])
    t_months += 1
    net_amount += int(row[1])
    g_increase = int(row[1])
    g_month_increase = row[0]

    
    for row in reader:
        
        t_months += 1
        
       #profits
        net_amount += int(row[1])

        # calc changes
        profit_change = int(row[1]) - previous_row
        month_change.append(profit_change)
        previous_row = int(row[1])
        month_count.append(row[0])
        
        
        
    # average and high/low
    change = sum(month_change)/ len(month_change)
    
    high = max(month_change)
    low = min(month_change)

print(f"Financial Analysis")
print(f"---------------------------")
print(f"Total Months: {t_months}")
print(f"Total: ${net_amount}")
print(f"Average Change: ${change:.2f}")
print(f"Greatest Increase in Profits:, (${high})")
print(f"Greatest Decrease in Profits:, (${low})")

# txt file output
output_file = os.path.join('.', 'analysis', 'Budget_Analysis.txt')

with open(output_file, 'w',) as txtfile:

# print into txt
    txtfile.write(f"Financial Analysis\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Total Months: {t_months}\n")
    txtfile.write(f"Total: ${net_amount}\n")
    txtfile.write(f"Average Change: ${change}\n")
    txtfile.write(f"Greatest Increase in Profits:, (${high})\n")
    txtfile.write(f"Greatest Decrease in Profits:, (${low})\n") 