# Write a program that reads a CSV file and finds the total sales revenue for a specific product.

import csv

csvfile = r"C:\WORKS\Learning\Python Learn\python-pdf\day_8\6revenue_specific_product\salesfile.csv"

product_name = input("Enter the product name: ")

total = 0 
with open(csvfile, 'r') as file:
    reader = csv.DictReader(file)    # read csv file
    for i in reader:
        if i["product_name"].lower() == product_name.lower():    #conver lower and check the name
            quantiy_sold = int(i["quantity_sold"])      # get the quantity data
            price_per_unit = int(i["price_per_unit"])   # get the price data
            total += quantiy_sold * price_per_unit      # add the total value with the q*p

print("The total sales is:", total)