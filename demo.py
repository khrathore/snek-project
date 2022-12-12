from argparse import ArgumentParser
import random
import re
import sys
import pandas as pd
import matplotlib.pyplot as plt


class User:
   
    def __init__(self, fname, lname, email, org):
        self.fname = fname
        self.lname = lname
        self.email = email
        self.org = org
        
    def email_check(self):
        patt1 = re.compile(r"^[^@]+@terpmail.umd.edu")
        patt2 = re.compile(r"^[^@]+@umd.edu")
        match1 = patt1.search(self.email)
        match2 = patt2.search(self.email)
        if match1 or match2:
            return True 
        else:
            raise ValueError("The email you provided is not valid.")
        
    def org_check(self, org_file = "Organizations.txt"):
        org_list = []
        with open(org_file, 'r') as f:
            for line in f:
                org_list.append(line.strip())
        
        if self.org in org_list:
            return True
        else:
            raise ValueError(f"{self.org} is not an active Campus Org")
        

class Event():
    
    def __init__(self, name, budget_obj, food_obj, equip_obj, supplies_obj, location_obj, duration):
        self.name = name
        self.budget_obj = budget_obj
        self.food_obj = food_obj
        self.equip_obj = equip_obj
        self.supplies_obj = supplies_obj
        self.location_obj = location_obj
        self.duration = duration
    
    def budget_tracker(self):
        self.budget_obj.amount = self.budget_obj - self.food_obj 
        self.budget_obj.amount = self.budget_obj - self.equip_obj
        self.budget_obj.amount = self.budget_obj - self.supplies_obj
        self.budget_obj.amount = self.budget_obj - self.location_obj
        
        if self.budget_obj.amount < 0:
            return("You do not have enough budget for the expected spendings for this event.")
        else:
            return self.budget_obj
    
    def confirmation(self):
        newline = '\n'
        with open(f"{self.name}.txt", 'w', encoding= "utf-8") as f:
            f.write("Event Confirmation\n\n")
            f.write(f"Event name                     : {self.name}{newline}")
            f.write(f"Your budget for the event      : ${self.budget_obj.amount}{newline}")
            f.write(f"Location                       : {self.location_obj.type}{newline}")
            f.write(f"Duration of the event          : {self.duration} hours{newline}")
            f.write(f"Total rent for location        : ${self.location_obj.amount}{newline}")
            f.write(f"Expected food expense          : ${self.food_obj.amount}{newline}")
            f.write(f"Expected equipment expense     : ${self.equip_obj.amount}{newline}")
            f.write(f"Expected supplies expense      : ${self.supplies_obj.amount}{newline}")
            
            if isinstance(self.budget_tracker(), str):
                f.write(self.budget_tracker())
            else:
                f.write(f"Remaining Budget for your Event: ${self.budget_obj.amount}")
                
    def bud_vis(self):
        labels = ["location", self.food_obj.type, self.equip_obj.type, self.supplies_obj.type]
        data = [self.location_obj.amount, self.food_obj.amount, self.equip_obj.amount, self.supplies_obj.amount]
       
        #plt.xticks(range(len(data)), labels)
        plt.xlabel('Expenses')
        plt.ylabel('Amounts')
        plt.title('Expenses Distribution')
        plt.bar(labels, data) 
        plt.show()
        
        
        

class Budget():    
    def __init__(self, type, amount):
        self.type = type
        self.amount = amount
        
    def __sub__(self, other):
        check = self.amount - other.amount
        return check
        
        
        
def loc_checker(loc_budget, hours, filepath = "Locations.txt"):
    best_location = {}
    with open(filepath, "r",encoding= "utf-8") as f:
        for line in f:
            values= line.strip().split(":")
            if (float(values[1])* hours) <= loc_budget:
                best_location[values[0]] = float(values[1])
    
    return sorted(best_location.items(), key= lambda x : x[1])
    
        
            
def main(fname, lname, email, orgname):
    print(f"Welcome to Terp Planner {fname} {lname}!")
    user = User(fname, lname, email, orgname)
    id_set = set()
    
    if user.email_check() == True & user.org_check() == True:
        begin = input("\nDo you want to plan an event? (yes/no): ")
        
        while begin.lower() == "yes":
            name = input("\nPlease provide the name of the event: ")
            budget = float(input("\nPlease provide the budget for your event (in dollars): "))
            
            food = True if input("\nDo you want food in your event? (yes/no): ").lower() == "yes" else False
            food_budget = float(input("How much do you want to spend on food? ")) if food == True else 0
            
            equip = True if input("\nDo you need tech equipments for your event? (yes/no): ").lower() == "yes" else False
            equip_budget = float(input("How much do you want to spend on equipment? ")) if equip == True else 0
            
            supplies = True if input("\nDo you need supplies for your event? (yes/no): ").lower() == "yes" else False
            supplies_budget = float(input("How much do you want to spend on supplies? ")) if supplies == True else 0
            
            hours = float(input("\nHow long is your event going to be? (in hours): "))
            loc_budget = float(input("How much do you want to spend on the location? "))
            
            print("\nFollowing are the available locations within your location budget:")
            
            affordable_loc = loc_checker(loc_budget, hours)
                
            locOptions = {}
            x = 1
            for loc_name, price in affordable_loc:
                locOptions[x] = f"{loc_name}: ${price}"
                x += 1              
            for option in locOptions:
                print(f"{option}: {locOptions[option]}")
                
            choice = int(input("\nSelect a number to pick a location: "))
            if choice in locOptions:                
                selection = locOptions[choice].split(": $")
                location_name = selection[0]
                loc_cost = float(selection[1]) * hours
               
            else:
                raise IndexError("Selection out of range")
            
            budget_obj = Budget("total", budget)        
            food_obj = Budget("food", food_budget)
            equip_obj = Budget("equip", equip_budget)
            supplies_obj = Budget("supplies", supplies_budget)
            location_obj = Budget(location_name, loc_cost)
            
            event = Event(name, budget_obj, food_obj, equip_obj, supplies_obj, location_obj, hours)
            
            event.confirmation()
            
            if event.budget_obj.amount < 0:
                print("You do not have enough budget for the expected spendings for this event.")
            else:
                event.bud_vis()
            
            begin = input("\nDo you want to plan another event? ")
    
    
    
    
    
def parse_args(comline):    
    parser = ArgumentParser()
    parser.add_argument("fname", help="first name of the student")
    parser.add_argument("lname", help = "last name of the student")
    parser.add_argument("email", help = "email of the student")
    parser.add_argument("orgname", help = "name of the organization")

    return parser.parse_args(comline)

  
if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.fname, args.lname, args.email, args.orgname)