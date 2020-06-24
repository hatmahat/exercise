import print_name as pn
from print_name import function as fc

hatma = pn.Name('Hatma', 19, 167, 56)
hatma.print_name()
hatma.print_age()
# help(pn.Name)
print(fc.adds(20,20))
new = fc.random(20)
print(new.get_seed())