import def_import_pizza  # Если писать так-то нужно писать module.function
from def_import_pizza import make_pizza
from def_import_pizza import test, make_pizza  # Если писать так-то можно сразу писать function
from def_import_pizza import *  # Импортит все фунции с файла, лучше не злоупотреблять
# Лучше всего импортировать функции которые только будешь использовать

def_import_pizza.make_pizza(16, 'papperoni')
def_import_pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

make_pizza(16, 'pepperoni')
