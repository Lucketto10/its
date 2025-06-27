def calculateCharges(hours):
    import math
    base_rate = 2.00
    additional_rate = 0.50
    max_charge = 10.00
    
    if hours <= 3:
        return base_rate
    else:
        extra_hours = math.ceil(hours - 3)
        charge = base_rate + extra_hours * additional_rate
        return min(charge, max_charge)

parking_hours = [1.5, 4.0, 5.5, 24.0]

print(f"{'Car':<10}{'Hours':<15}{'Charge'}")

total_hours = 0
total_charge = 0

for i, hours in enumerate(parking_hours, start=1):
    charge = calculateCharges(hours)
    total_hours += hours
    total_charge += charge
    print(f"{i:<10}{hours:<15.2f}{charge:.2f} $")

print(f"{'TOTAL':<10}{total_hours:<15.2f}{total_charge:.2f} $")
