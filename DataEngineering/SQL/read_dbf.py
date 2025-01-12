import pandas as pd

orders = pd.read_csv('_CSV/orders.csv')
products = pd.read_csv('_CSV/products.csv')
customers = pd.read_csv('_CSV/customers.csv')

print(orders)
print(products)
print(customers)

class Orders:

  def __init__(self, order_id, customer_id, product_id, quantity,	timestamp):
    self.order_id = order_id
    self.customer_id = customer_id
    self.product_id = product_id
    self.quantity = quantity
    self.timestamp = timestamp

  def orders(self, order_id, customer_id, product_id, quantity, timestamp):
    # Add method body here
    pass

## order_3_description = Orders(3, 3, 3, 3, '2021-01-03 00:00:00')
