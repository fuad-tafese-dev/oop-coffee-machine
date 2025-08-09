from menu import Menu, MenuItem
from money_machine import MoneyMachine
from coffee_maker import CoffeeMaker
coffe_chef = CoffeeMaker()
casher = MoneyMachine()
menu = Menu()
machin_on = True

while machin_on:
    user_order = input(f"What would you like? {menu.get_items()} ").lower()
    if user_order == "off":
        machin_on = False
    elif user_order == "report":
        coffe_chef.report()
        casher.report()
    else:
        ordered_drink = menu.find_drink(user_order)
        if coffe_chef.is_resource_sufficient(ordered_drink):
            casher.make_payment(ordered_drink.cost)
            coffe_chef.make_coffee(ordered_drink)




