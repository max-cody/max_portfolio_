#holiday calulator, errors have been numbered for debugging.
def calculate_city_flight(city, ticket_class):
    #dictionary of cities a ticket costs
    economy_ticket_prices = {"Venice": 55, "Paris": 135, "Tokyo":861, "Miami": 818, "Cape Town": 685, "Buenos Aires": 1153, "New York": 750, "Berlin": 350, "Geneva": 250, "Jakarta": 1050, "Sydney": 1200} 
    first_class_tickets = {"Venice": 350, "Paris": 500, "Tokyo":1650, "Miami": 1200, "Cape Town":978, "Buenos Aires": 2500, "New York": 18, "Berlin":650, "Geneva": 450, "Jakarta": 2350, "Sydney": 3000}


    # check if the city is in the dictionary, otherwise raise an exception
    if city not in economy_ticket_prices:
        raise ValueError("Invalid city choice*1")

    if ticket_class not in ['economy', 'first']:
        raise ValueError("Invalid ticket class selected*2")

#calc price based on class
    if ticket_class == 'economy':
        return economy_ticket_prices[city]
    else:
        return first_class_tickets[city]
    
def calculate_hotel_cost(nights, nightly_cost):
    #check if num_nights and nightly costs are positive integers
    if nights > 0 and nightly_cost > 0:
        return nights * nightly_cost
    else:
        raise ValueError("Invalid number of nights or cost*3")

def calculate_car_rental(rental_days, daily_cost):
    #check if number of days and daily cost are positive
    if rental_days > 0 and daily_cost > 0:
        return rental_days * daily_cost
    else:
        raise ValueError("Invalid Input please enter a valid number*4")
    
while True:   
    try:
        #get user input for city, nights,and number of days renting a car
        print("Welcome to the holiday calculator, Here are the available destinations:")
        print("Venice")
        print("Paris")
        print("Tokyo")
        print("Miami")
        print("Cape Town")
        print("Bueno Aires")
        print("New York")
        print("Berlin")
        print("Geneva")
        print("Jakarta")
        print("Sydney")

        city = input("Enter city of destination:")
        nights = int(input("Enter number of nights staying:"))
        rental_days = int(input("Enter the number of days you are renting a car:"))

        #get the nightly hotel cost and rental cost 
        nightly_cost = float(input("Enter nightly hotel cost:"))
        if nightly_cost < 0:
            raise ValueError("Nightly cost should be non negative")
        
        daily_cost = float(input("Enter daily rental cost:"))
        if daily_cost < 0:
            raise ValueError("Rental cost should be non negative.")


        #ask user what class of ticket they wish to purchase
        ticket_class = input("Enter ticket class (economy or first):")
        if ticket_class not in ['economy', 'first']:
            raise ValueError("Invalid ticket class selected")

        #calc total cost by calling each function
        ticket_price = calculate_city_flight(city, ticket_class)
        hotel_cost = calculate_hotel_cost(nights, nightly_cost)
        car_rental_cost = calculate_car_rental(rental_days, daily_cost)
        total_cost = ticket_price + hotel_cost + car_rental_cost

        #print out the results
        print(f"The total cost of your holiday is {total_cost}.")

        #exit the loop since valid input was provided
        break

    except ValueError as e:
        #handle any exceptions raised by the user
        print("Error*5", e)


