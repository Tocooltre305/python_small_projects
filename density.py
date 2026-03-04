def density():
    volume = float(input("Enter volume in cm^3:"))
    mass = float(input("Enter mass in g:"))
    density = mass / volume
    print(f"The density is {density} g/cm^3")
    
density()