import prettytable

table = prettytable.PrettyTable()

table.add_column("Pokemon Name",["Pikachu","Charmander","Squirtle"])
table.add_column("Type",["Electric","Fire","Water"])
table.align = "l"
print(table)