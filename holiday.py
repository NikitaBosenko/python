#------------------------------------------------------------#
# Request user a number input of a city to fly
# Request hotel price
# Request nights to stay
# Request days to rent a car
# Request car price
# Calculate all parameters 
# Print result in a readeble way
#------------------------------------------------------------#

destination = {1: { "city": 'London', "flight": 110 },
               2: { "city": 'Amsterdam', "flight": 210 },
               3: { "city": 'Paris', "flight": 150 },
               4: { "city": 'Helsinki', "flight": 250 },
               5: { "city": 'Prague', "flight": 320 },
               }
               
hotels = {1: { 140, 200, 280 },
          2: { 180, 240, 320 },
          3: { 160, 220, 300 },
          4: { 210, 340, 420 },
          5: { 80, 140, 190 },
            }

cars = {1: { 30, 80, 200 },
        2: { 40, 90, 30 },
        3: { 20, 60, 150 },
        4: { 35, 70, 250 },
        5: { 15, 50, 110 }
            }
           
# Declare plane cost counter function
def plane_cost(city_flight):
    flight = destination[city_flight]["flight"]
    # Count full flight (flight and return)
    plane = flight * 2
    return plane

# Declare hotel cost counter function
def hotel_cost(hotel_day_price, num_nights):
    # Count full hotel price
    hotel = hotel_day_price * num_nights
    return hotel

# Declare car rental counter function
def car_rental(rental_days):
    # Count full car price
    car = car_price * rental_days
    return car

# Declare total cost counter function
def holiday_cost():
    # Count total cost
    holiday = hotel + plane + car
    return holiday
    
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
        number_str = input(data).replace("GBP", "")
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
print("[please, select your city]")
for city in destination:
    print(f"{city}. {destination[city]["city"]} (one-way ticket: {destination[city]["flight"]} GBP)")
print()

city_flight_inp = "Enter the city number for the flight: "
# Using function to check the input is a number in range 1-3, using 1 to show the "between" message
city_flight = num_check(city_flight_inp, 1, len(destination), 1)

num_nights_inp = "How many nights to stay in the hotel?: "
# Checking input is a number in range 1-999 and 0 - do not show "between" mesdsage
num_nights = num_check(num_nights_inp, 1, 999, 0)

print("Select your hotel price.")
# Print hotels price list
for price in sorted(hotels[city_flight]):
    print(f"{price} GBP")
# Declare text for request
while True:
    hotel_day_price_inp = "Enter the hotel price: "
    # Checking input is a number in range 1-99999999 and 0 - do not show "between" mesdsage
    hotel_day_price = num_check(hotel_day_price_inp, 1, 99999999, 0)
    # Check if input in the selected list
    if hotel_day_price in hotels[city_flight]:
        break
    else:
        print("> Enter the given prices only!\n")

rental_days_inp = "Enter days number to rent a car?: "
rental_days = num_check(rental_days_inp, 0, num_nights, 1)
# Check if rental days zero then car price zero too
if rental_days == 0:
    car_price = 0
# Check if rental days not zero then request car price input
elif rental_days > 0:
    print("[select your car price]")
    # Print cars price list
    for price in sorted(cars[city_flight]):
        print(f"{price} GBP")
    while True:
        car_price_inp = 'Enter the cost of renting a car: '
        car_price = num_check(car_price_inp, 1, 999999, 0)
        # Check if input in the selected list
        if car_price in cars[city_flight]:
            break
        else:
            print("> Enter the given prices only!\n")

# Calculate flight cost using function, print result
plane = plane_cost(city_flight)

# Calculate hotel cost using function, print result
hotel = hotel_cost(hotel_day_price, num_nights)

# Calculate car rental cost using function, print result
car = car_rental(rental_days)

# Calculate total cost using function, print result
holiday = holiday_cost()

# Print final result: city choice, journey cost, details
print(f"{'-'*30}\nYour choice: {destination[city_flight]["city"]}")
print(f"Nights to stay: {num_nights}")
print(f"Car rental: {rental_days} days")
print('\nJOURNEY COST:')
print(f'Flight:\t{plane} GBP')
print(f'Hotel:\t{hotel} GBP')
print(f'Car:\t{car} GBP')
print(f'\nTotal:\t{holiday} GBP\n{'-'*30}')