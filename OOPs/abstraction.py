from abc import ABC,abstractmethod

class Car(ABC):

	def __init__(self,brand,model,year):

		self.brand=brand

		self.model=model

		self.year=year

	@abstractmethod

	def printdetails(self):

		pass

	def accelerate(self):

		print("Speed Up...")

	def break_up(self):

		print("Slowing Down")

class Hathback(Car):

	def printdetails(self):

		print("Brand of the car:", self.brand)

		print("Model of the car:", self.model)

		print("Year of release:", self.year)

	def roofup(self):

		print("Not available")

class Suv(Car):

	def printdetails(self):

		print("Brand of the car:", self.brand)

		print("Model of the car:", self.model)

		print("Year of release:", self.year)

	def roofup(self):

		print("Available Opening up.")

car1=Suv("TATA","Safari","2024")

car1.printdetails()

car1.accelerate()

car1.roofup()

car1.break_up()
