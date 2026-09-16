from rental import ElectricCar, Motorbike, Renter, Vehicle


car = Vehicle("Toyota", "Yaris", "1AB234")
electric_car = ElectricCar("Tesla", "Model 3", "EV123", 75)
motorbike = Motorbike("Honda", "PCX", "MB456", 160)
renter = Renter("May", 12345)

print(car)
car.rent()
print(car)
car.return_vehicle()
print(car)
print(f"Renter: {renter.name}, license: {renter.license_no}")

for name, license_no in [("", 123), ("Sam", 0)]:
    try:
        Renter(name, license_no)
    except ValueError as error:
        print(f"Error: {error}")

print("\nAll vehicles:")
for vehicle in [car, electric_car, motorbike]:
    print(vehicle)
