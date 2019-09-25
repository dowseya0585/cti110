# A company has determined that its annual profit is typically 23 percent of total sales. This program calculates the profit that will be made from the amount.
# 9/17/2019
# CTI-110 - Sales Prediction
# Antonio Dowsey

#Get the projected total sales
total_sales = float(input('Enter the projected sales :'))

# Calculate the profit as 23 percent of total sales.
profit = total_sales *0.23

#Display the profit.
print('The profit is $', format(profit, ',.2f'))

