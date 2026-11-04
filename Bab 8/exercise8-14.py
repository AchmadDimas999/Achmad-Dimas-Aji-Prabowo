def make_car(manufacturer, model_name, **car_info):
	"""Buat dictionary yang berisi informasi mobil."""
	car = {"manufacturer": manufacturer, "model": model_name}
	car.update(car_info)
	return car


car = make_car("subaru", "outback", color="blue", tow_package=True)
print(car)
