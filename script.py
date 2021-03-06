import codecademylib
import pandas as pd

# Load data from inventory.csv in a variable called inventory
inventory = pd.read_csv('inventory.csv')

# Inspect the first 10 rows of inventory
print(inventory.head(10))

# Save the first 10 rows into a variable called staten_island
staten_island = inventory.head(10)

# Select the column product_description from staten_island and save it to the variable product_request.
product_request = staten_island.product_description

# Select all rows where location is equal to Brooklyn and product_type is equal to seeds and save them to the variable seed_request
seed_request = inventory[(inventory.location == 'Brooklyn') & (inventory.product_type == 'seeds')]

# Add a column to inventory called in_stock which is True if quantity is greater than 0 and False if quantity equals 0.
inventory['in_stock'] = inventory.apply(lambda row: True if row.quantity > 0 else False, axis=1)

# Create a column called total_value that is equal to price multiplied by quantity.
inventory["total_value"] = inventory.apply(lambda row: row.price * row.quantity, axis=1)

# combine_lambda function
combine_lambda = lambda row: \
    '{} - {}'.format(row.product_type,
                     row.product_description)

# Create a new column in inventory called full_description that has the complete description of each product.
inventory['full_description'] = inventory.apply(combine_lambda, axis=1)

# Inspect inventory
print(inventory.head(10))