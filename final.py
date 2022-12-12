from argparse import ArgumentParser
import string
import random
import re
import sys
import pandas as pd
import matplotlib.pyplot as plt


class User:
    """Defines a user object for the person planning the event
    
        Attributes:
            fname(str): The first name of the person
            lname(str): The last name of the person
            email(str): The UMD email of the person
            org(str): The organization the event is for
    """

    def __init__(self, fname, lname, email, org):
        """ 
            Creates a User class. - Palrika                                     
                
            Args:  
                fname (str): The first name of the user.
                lname (str): The last name of the user.
                email (str): The email address of the user.
                org (str): The name of the organziation that he user is planning the event for.
                
            Side effects:
                A user object is created with the aforementioned attributes.
            """
        self.fname = fname
        self.lname = lname
        self.email = email
        self.org = org
        
        

class Event:
    
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
            return(f"You are overspending your budget. Your group will need to fundraise ${abs(event.budget_obj.amount)}.")
        else:
            return self.budget_obj
    

class Budget:

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
            budget = float(input("\nPlease provide the budget for your event: "))
            
            hours = float(input("\nHow long is your event going to be? (in Hrs): "))
            loc_budget = float(input("How much do you want to spend on the location? "))
            
            print("\nFollowing are the available locations within your location budget:")
            
            affordable_loc = loc_checker(loc_budget, hours)
                
            locOptions = {}
            x = 1
            for loc_name, price in affordable_loc:
                locOptions[x] = f"{loc_name}: ${price*hours}"
                x += 1              
            for option in locOptions:
                print(f"{option}: {locOptions[option]}")
                
            choice = int(input("\nSelect a number to pick a location: "))
            if choice in locOptions:                
                selection = locOptions[choice].split(": $")
                location_name = selection[0]
                loc_cost = float(selection[1])
               
            else:
                raise IndexError("Selection out of range")
            
            food = True if input("\nDo you want food in your event?(yes/no) ").lower() == "yes" else False
            food_budget = float(input("How much do you want to spend on food? ")) if food == True else 0
            
            equip = True if input("\nDo you need equipments for your event?(yes/no) ").lower() == "yes" else False
            equip_budget = float(input("How much do you want to spend on equipment? ")) if equip == True else 0
            
            supplies = True if input("\nDo you need supplies for your event?(yes/no) ").lower() == "yes" else False
            supplies_budget = float(input("How much do you want to spend on supplies? ")) if supplies == True else 0
            
           
            
            budget_obj = Budget("total", budget)        
            food_obj = Budget("food", food_budget)
            equip_obj = Budget("equip", equip_budget)
            supplies_obj = Budget("supplies", supplies_budget)
            location_obj = Budget(location_name, loc_cost)
            
            event = Event(name, budget_obj, food_obj, equip_obj, supplies_obj, location_obj, hours)
            
            event.confirmation()
            
            if event.budget_obj.amount < 0:
                print(f"You are overspending your budget. Your group will need to fundraise ${abs(event.budget_obj.amount)}.")
            else:
                event.bud_vis()
            
            begin = input("\nDo you want to plan another event? ")
            
            id_set.add(event.event)    
      



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