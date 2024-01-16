#!/usr/bin/env python3
import math

class triangle:

	def __init__(self, base: float, height: float):
		self.base = base
		self.height = height
	
	def set_base(self, base: float):
		self.base = base
		if(self.base < 0):
			print("Invalid, length must be greater than 0")
			self.base = 0
			
	
	def set_height(self, height: float):
		self.height = height
		if(self.height < 0):
			print("Invalid, length must be greater than 0")
			self.height = 0
	
	def calc_side(self):
		self.size = 0.5 * math.sqrt(pow(self.base, 2) + 4 * pow(self.height, 2))
		print(self.size)
	
	def calc_perimeter(self):
		self.perimeter = (2) * (0.5 * math.sqrt(pow(self.base, 2) + 4 * pow(self.height, 2))) + self.base
		print(self.perimeter)
	
	def calc_area(self):
		self.area = ((self.base) * (self.height)) / 2
		print(self.area)
	
	def calc_alpha(self):
		self.alphaTheta = math.degrees(math.atan(((2) * (self.height)) / (self.base)))
		print(self.alphaTheta)
	
	def calc_beta(self):
		self.betaTheta = ((math.degrees(math.atan(((2) * (self.height)) / (self.base))) * (2)) - 180) * (-1)
		print(self.betaTheta)
		

def print_all(self) -> None:
	print(f"---------------------")
	print(f"base        : {self.base}")
	print(f"height        : {self.height}")
	print(f"side        : {self.side}")
	print(f"perimeter        : {self.perimeter}")
	print(f"area        : {self.area}")
	print(f"alpha        : {self.alphaTheta}")
	print(f"beta        : {self.betaTheta}")
	print(f"---------------------")
		
