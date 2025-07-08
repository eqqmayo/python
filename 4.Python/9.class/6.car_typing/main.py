from driver import Driver
from car import Car

driver = Driver('abby', 25, '1종보통')

driver.drive(30)

car = Car('Mazda', 'model 3')

driver.assign_car(car)

driver.drive(50)
driver.drive(100)

car.update_odometer(100)
car.update_odometer(200)
car.read_odometer()

car2 = Car('Hyundai', 'Sonata')
driver = Driver('park', 26, '2종보통', car2)