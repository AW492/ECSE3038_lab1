def parallel(list_of_resistances):
    total = (1/(list_of_resistances[0]))+((1/(list_of_resistances[1]))+((1/list_of_resistances[2])))
    parallel_resistance = 1/total
    print("{:.3f}".format(parallel_resistance)+" ohms")
        
        
list =[330, 1000, 2200]

parallel(list)

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

def temperature_check(body_temperature, unit_temperature):
    if body_temperature < 35 and unit_temperature =="C" :
        print("the patient is hypothermic")
    elif body_temperature < 95 and unit_temperature == "F":
        print("the patient is hypothermic")
    elif 35 <= body_temperature <= 37 and unit_temperature == "C":
        print("the patient's temperature is normral")
    elif body_temperature >37 and unit_temperature == "C":
        print("patient has a fever!") 

temperature_check(14, "C")

