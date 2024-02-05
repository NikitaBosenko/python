#------------------------------------------------------------#
# Request number input of a city to fly
# Request hotel price
# Request nights to stay
# Request days to rent a car
# Request car price
# Calculate all parameters 
# Print result in a readeble way
#------------------------------------------------------------#

# Declare plane cost counter function
def plane_cost(flight):
    # Count full fligt - flight/return
    plane = flight * 2
    print(f'Flight:\t{plane} GBP')
    return plane

# Declare hotel cost counter function
def hotel_cost(hotel_day_price, num_nights):
    # Count full hotel price
    hotel = hotel_day_price * num_nights
    print(f'Hotel:\t{hotel} GBP')
    return hotel

# Declare car rental counter function
def car_rental(rental_days):
    # Count full car price
    car = car_price * rental_days
    print(f'Car:\t{car} GBP')
    return car

# Declare total cost counter function
def holiday_cost():
    # Count total cost
    holiday = hotel + plane + car
    print(f'\nTotal:\t{holiday} GBP\n{'-'*30}')

# Declare function to check valid number input
# 'data' - received input, 'min' - minimum value, 'max' - maximum value, 'btw' - (1)show message, (0)hide message
def num_check(data, min, max, btw): 
    # Use empty string if btw = 0
    if btw == 0:
        btw_info = ''
    # Use string with range data if btw = 1
    elif btw == 1:
        btw_info = f'\n> You can choose between {min}-{max}' 
    # Loop check if the input is a number
    while True:
        # Request input using text from first aggument 
        number_str = input(data)
        try:
            # Try to cast input to integer
            number = int(number_str)
            # Checking if the number in the expected range
            if number in range(min, max+1):
                return number
            else:
                print(f"> Wrong input!{btw_info}\n> Please enter a proper number!\n")
        except ValueError:
            print("> Wrong input!\n> Please enter a number!\n")

# UI START
print("Holiday Calculator Program")
# Declare text for request
city_flight_inp = "Enter city number to fly (1.London, 2.Amsterdam, 3.Paris): "
# Using function to check the input is a number in range 1-3, using 1 to show the "between" message
city_flight = num_check(city_flight_inp, 1, 3, 1)
if city_flight == 1:
    city = "London"
    # Declare one way price for London
    flight = 50
elif city_flight == 2:
    city = "Amsterdam"
    # Declare one way price
    flight = 240
elif city_flight == 3:
    city = "Paris"
    # Declare one way price
    flight = 130

# Declare text for request
hotel_day_price_inp = "Enter the hotel price: "
# Checking input is a number in range 1-99999999 and 0 - do not show "between" mesdsage
hotel_day_price = num_check(hotel_day_price_inp, 1, 99999999, 0)

num_nights_inp = "How much nights to stay?: "
# Checking input is a number in range 1-999 and 0 - do not show "between" mesdsage
num_nights = num_check(num_nights_inp, 1, 999, 0)

rental_days_inp = "Enter days to rent a car?: "
rental_days = num_check(rental_days_inp, 0, num_nights, 1)
# Check if rental days zero then car price zero too
if rental_days == 0:
    car_price = 0
# Check if rental days not zero then request car price input
elif rental_days > 0:
    car_price_inp = 'Enter price of the car: '
    car_price = num_check(car_price_inp, 1, 999999, 0)

# Print final result: city choice, journey cost text 
print(f"{'-'*30}\nYour choice: {city}")
print('\nJourney cost:\n')

# Calculate flight cost using function, print result
plane = plane_cost(flight)

# Calculate hotel cost using function, print result
hotel = hotel_cost(hotel_day_price, num_nights)

# Calculate car rental cost using function, print result
car = car_rental(rental_days)

# Calculate total cost using function, print result
holiday = holiday_cost()
    






