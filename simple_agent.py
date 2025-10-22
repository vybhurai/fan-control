# SimpleAgent.py

def simple_agent(temperature):
    if temperature > 30:
        return "Turn ON the fan"
    else:
        return "Fan OFF"

# Simulate environment perception
current_temp = int(input("Enter current temp"))
action = simple_agent(current_temp)
print(f"At temperature {current_temp}°C: {action}")
