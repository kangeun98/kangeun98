Python 3.5.1 |Anaconda 2.4.1 (64-bit)| (default, Dec  7 2015, 15:00:12) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
>>> cars=100
>>> space_in_a_car=4.0
>>> drivers=30
>>> passengers=90
>>> cars_not_driven=cars-drivers
>>> cars_driven=drivers
>>> carpool_capacity=cars_driven*space_in_a_car
>>> average_passengers_per_car=passengers/cars_driven
>>> 
>>> print"there are",cars,"cars available"
SyntaxError: invalid syntax
>>> print"there are",cars,"cars available"
SyntaxError: invalid syntax
>>> print("there are",cars,"cars available")
there are 100 cars available
>>> print("there are only",drivers,"drivers available.")
there are only 30 drivers available.
>>> print("there will be",cars_not_driven,"empty cars today.")
there will be 70 empty cars today.
>>> print("we can transport",carpool_capacity,"people today.")
we can transport 120.0 people today.
>>> print"we can transport",carpool_capacity,"people today.")
SyntaxError: invalid syntax
>>> print("we can transport",carpool_capacity,"people today.")
we can transport 120.0 people today.
>>> print("we have",passengers,"to carpool today.")
we have 90 to carpool today.
>>> print("we need to put about",average_passengers_per_car,"in each car.")
we need to put about 3.0 in each car.
>>> 
