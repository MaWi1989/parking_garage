class Garage():
    def __init__(self):
        self.spots = {'sedan' : 100,
                     'truck' : 50,
                     'bike' : 20,
                     'EV' : 20,}
        self.rate = {'sedan' : '$10',
                     'truck' : '$15',
                     'bike' : '$8',
                     'EV' : '$20',}
        self.tickets = {'sedan' : 0,
                     'truck' : 0,
                     'bike' : 0,
                     'EV' : 0,}
        self.count = {'sedan' : 0,
                     'truck' : 0,
                     'bike' : 0,
                     'EV' : 0,}
        self.find_car = {
                    {'sedan' : {}},
                    {'truck' : {}},
                    {'bike' : {}},
                    {'EV' : {}}
                    }
        self.type_ = ''

        self.lost_ticket_fee = '$5'
    
        self.tickets = self.count


    def enter(self):
        vehicle = input ("What type of vehicle will you be parking today? ['sedan']['truck'/'SUV']['bike']['EV']")
        self.type_ = vehicle
        if vehicle == 'sedan':
            print(f"Available spots: {self.spots['sedan']}")
            if self.spots['sedan'] > 0:
                    print(f"The hourly rate for sedans is {self.rate['sedan']}")
                    self.spots['sedan'] -= 1
                    self.count['sedan'] += 1
                    print(f"Your ticket number is {self.tickets['sedan']} ")
                    print("Please take your ticket!")
            else:
                print("Sorry, we can't fit any more sedans right now!")

        elif vehicle == 'truck' or vehicle == 'SUV':
            print(f"Available spots: {self.spots['truck']}")
            if self.spots['truck'] > 0:
                    print(f"The hourly rate for trucks / SUVs is {self.rate['truck']}")
                    self.spots['truck'] -= 1
                    self.count['truck'] += 1
                    print(f"Your ticket number is {self.tickets['truck']} ")
                    print("Please take your ticket!")
                                     
            else:
                print("Sorry, we can't fit any more trucks / SUVs right now!")

        elif vehicle == 'bike': 
            print(f"Available spots: {self.spots['bike']}")
            if self.spots['bike'] > 0:
                    print(f"The hourly rate for bikes is {self.rate['bike']}")
                    self.spots['bike'] -= 1
                    self.count['bike'] += 1
                    print(f"Your ticket number is {self.tickets['bike']} ")
                    print("Please take your ticket!")
                                            
            else:
                print("Sorry, we can't fit any more bikes right now!")

        elif vehicle == 'EV': 
            print(f"Available spots: {self.spots['EV']}")
            if self.spots['EV'] > 0:
                    print(f"The hourly rate for electric vehicles is {self.rate['EV']}")
                    self.spots['EV'] -= 1
                    self.count['EV'] += 1
                    print(f"Your ticket number is {self.tickets['EV']} ")
                    print("Please take your ticket!")
            else:
                print("Sorry, we can't fit any more electric vehicles right now!")


    def reg_license_plate(self): 
        # self.type_ = input("What type of vehicle are you parking today? ")
        self.plate = input("Please provide your license plate number!" )
        self.find_car[self.type_][1] = self.plate
        



    def find_my_car(self):
        # self.type_ = input("What type of vehicle are you trying to locate? ")
        self.response = input("Would you like to search by ticket number ['t'], or by license plate number ['l']?")
        if self.response.lower().strip() == 't':
            self.number = input("Please tell me your ticket number! ")
            self.find_car[self.type_][0] = self.number
            print(f"Your vehicle is in the {self.type_}-section of the parking garage. \nParking spot: {self.number}")
        elif self.response.lower().strip() == 'l': 
            self.plate = input("Please provide your license plate number!" )
            print(f"Your vehicle is in the {self.type_}-section of the parking garage. \nParking spot: {self.find_car[self.plate]}")
       

    def pay(self):
         self.hours = float(input("How many hours did you park for? "))  
         self.parking_cost = float(lambda x: x * self.rate['self.type_'])  
         print(f"Your parking cost is {self.parking_cost}. Please pay before you leave!")

    def exit(self):
         print("Thank you for parking with us! Have a great day!")
        
    def lost_ticket(self):
         print("SOL... Have fun walking home!!\nJust kidding! Please pay lost ticket fee of $5")
         self.plate = input("Please provide your license plate number! ")



    def run():
         print("Welcome to our parking garage!")
         action = input("How can I help you? \nOptions:\nEnter\nFind Vehicle\nPay\nLost Ticket\nExit")



        #  self.response = input("Did you pay your bill? y/n ")
        #  if self.response == 'n':
        #       print("Please pay now!") 

        #  elif self.esponse = 'y'
     
    
my_car = Garage()
my_car.enter()

# print(my_car.tickets) 
# print(my_car.count)
