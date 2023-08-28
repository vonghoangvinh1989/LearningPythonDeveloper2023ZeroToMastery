# List slicing
amazon_cart = ['notebooks', 'sunglasses', 'toys', 'grapes']
amazon_cart[0] = 'laptop'  # lists are mutable

# new_cart = amazon_cart
new_cart = amazon_cart[:]
new_cart[0] = 'gum'

print(new_cart)
print(amazon_cart)

# slicing in list will create a complete new list,
# but assign one list to another will copy the address of the original list which caused changing new list will affect the original list
