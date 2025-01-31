def potential_divider(voltage,series_resistances):
    total_resistance = 0
    for resistance in series_resistances:
        total_resistance+=resistance

    current = voltage/total_resistance

    for resistance in series_resistances:
        voltage_drop = resistance*current
        print("{:.2f}".format(voltage_drop)+"v")

list_resistor = [3000,1000]

potential_divider(9,list_resistor)
