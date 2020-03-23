# from package_1.package_2.package_3.shopping_cart import buy_item
# importing the only function, we are interested in ^
# from ... import * - means import everything
from package_1.package_2.package_3 import shopping_cart  # importing the only package we're interested in

print(shopping_cart.buy_item('apples'))
