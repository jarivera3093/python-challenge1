#import the oc module and module for reading CSV files
import csv
import  sys
import locale

#budget data
csvpath = 'budget_data.csv'

with open (csvpath, encoding='UTF-8') as csvfile:  
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)  #  discard headers
    #Read the header row first
    row = next(csvreader)

    #assign variables
    total = 0
    max_profit = 0
    min_profit = sys.maxsize

    month, amount = row
    amount = int(amount)
    count = 0
    total += amount
    # no delta for first value
    previous_amount = amount
    sum_delta = 0

    #Read each row of data after the header
    for row in csvreader:
            month, amount = row 
            amount = int(amount)
            count += 1               
            total += amount
            delta = amount - previous_amount
            previous_amount = amount
            sum_delta += delta

            if delta > max_profit:
                    max_profit = delta
                    max_month = month

            if delta < min_profit:
                    min_profit = delta
                    min_month = month

    avg_delta = sum_delta / count
    avg_delta = round(avg_delta, 2)

    locale.setlocale( locale.LC_ALL, '' )
    total = locale.currency( total, grouping=True )  
    avg_delta = locale.currency( avg_delta, grouping=True )     
    max_profit = locale.currency( max_profit, grouping=True )
    min_profit = locale.currency( min_profit, grouping=True )

with open ('Budget_Data.txt', 'w') as file:

    #write to an ouput file
    print("Financial Analysis")
    file.write("Financial Analysis\n")
    print("-----------------------------")
    print("Total Months:" + str(count))
    print("Total:" + str(total))
    print("Average Change:" + avg_delta)
    print(f"Greatest Increase in Profit {max_month} ({max_profit})") 
    print(f"Greatest Decrease in Profit {min_month} ({ min_profit})")
    
    file.write("-----------------------------\n")
    file.write("Total Months:" + str(count) + '\n')
    file.write("Total:" + str(total) + '\n')
    file.write("Average Change:" + (avg_delta) + '\n')
    file.write(f"Greatest Increase in Profit {max_month} ({max_profit})\n")
    file.write(f"Greatest Decrease in Profit {min_month} ({ min_profit})\n")