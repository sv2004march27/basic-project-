import periodic_table

Atomic_no = int(input("Enter elements atomic No:"))
element = periodic_table.element[Atomic_no]
print("Atomic_number:",element.number)
print("Symbol:",element.symbol)
print("Name:",element.name)
print("Atomic_mass:",element.mass)
print("density:",element.density)

