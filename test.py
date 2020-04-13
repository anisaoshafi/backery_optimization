from solution import process_order, get_orders

# packs is a dictionary with existing types of articles.
# add a new article in this way:
# packs[code] = {pack_size_1: cost_1, pack_size_2: cost_2, ... pack_size_n: cost_n}
packs = {'VS5': {3: 6.99, 5: 8.99},
         'MB11': {2: 9.95, 5: 16.95, 8: 24.95},
         'CF': {3: 5.95, 5: 9.95, 9: 16.99}
         }

# get orders from console input
orders = get_orders()

# process each order and show the optimal packages
for code, num in orders.items():
    print(process_order(num, code, packs))
