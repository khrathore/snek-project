from argparse import ArgumentParser
import random
import re
import sys
import pandas as pd

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
    
    def __init__(self, name, budget, food_budget, equip_budget, supplies_budget, location, loc_cost):
        self.name = name
        self.budget = budget
        self.name = name
        self.food_budget = food_budget
        self.equi_budget = equip_budget
        self.supplies_budget = supplies_budget
        self.loc_cost = loc_cost
        self.location = location
        
        
        
def loc_checker(loc_budget, hours, filepath = "Locations.txt"):
        best_location = {}
        with open(filepath, "r",encoding= "utf-8") as f:
            for line in f:
                values= line.split(",")
                if (float(values[1].strip())* hours) <= loc_budget:
                    best_location[values[0]] = float(values[1].strip())
            return best_location
        
        
            
def main(fname, lname, email, orgname):
    print(f"Welcome to Terp Planner {fname} {lname}!")
    
    user = User(fname, lname, email, orgname)
    
    if user.email_check() == True & user.org_check() == True:
        begin = input("\nDo you want to plan an event? (yes/no): ")
        
        if begin.lower() == "yes":
            name = input("\nPlease provide the name of the event: ")
            budget = float(input("Please provide the budget for your event: "))
            
            food = True if input("Do you want food in your event? ").lower() == "yes" else False
            food_budget = float(input("How much do you want to spend on food? ")) if food == True else 0
            
            equip = True if input("Do you need equipments for your event? ").lower() == "yes" else False
            equip_budget = float(input("How much do you want to spend on equipment? ")) if equip == True else 0
            
            supplies = True if input("Do you need supplies for your event? ").lower() == "yes" else False
            supplies_budget = float(input("How much do you want to spend on supplies? ")) if supplies == True else 0
            
            hours = float(input("How long is your event going to be? (in Hrs): "))
            loc_budget = float(input("How much do you want to spend on the location? "))
            
            print("\nFollowing are the available locations within your location budget:")
            affordable_loc = loc_checker(loc_budget, hours)
                
            locChoices = {}
            x = 1
            for location in affordable_loc:
                locChoices[x] = f"{location}: ${affordable_loc[location]}"
                x += 1              
            for choice in locChoices:
                print(f"{choice}: {locChoices[choice]}")
                
            choice = int(input("\nSelect a number to pick a location: "))
            selection = locChoices[choice].split(":")
            location = selection[0]
            loc_cost = affordable_loc[location] * hours
            
            
                
            
                
    
    
        
        
    event1 = Event(name, budget, food_budget, equip_budget, supplies_budget, location, loc_cost)
            
            
            
            
        
        
    
    #         name=input("Please provide the name of the event: ")
    #         event=Event()
    #         budget=float(input("Please provide the budget for your event: "))
    #         if event.evbudget(budget) == True:
    #             event.budget_tracker()
    #         p1=float(input("Provide your budget for location: "))
    #         if event.location(p1)==True:
    #             s0=event.loc_checker()
    #         p2=input("Does your event have a food budget? (yes/no): ")
    #         if p2== p2.lower("yes"):
    #             if event.food(p2)==True:
    #                 food_bud=float(input("Please provide the budget for food: "))
    #                 s1=event.budget_tracker()-event.food(food_bud)
    #         p3=input("Do you want to have an equipment budget?(yes/no)")
    #         if p3==p3.lower("yes"):
    #             if event.equip(p3) == True:
    #                 equip_bud=float(input("Please provide the budget for equipment: "))
    #                 s2=event.budget_tracker()-event.equip(equip_bud)
    #         p4= input("Do you want to have a music budget? (yes/no)")
    #         if p4==p4.lower("yes"):
    #             if event.music == True:
    #                 music_bud=float(input("Please provide the budget for music: "))
    #                 s3=event.budget_tracker()-event.music(music_bud)
    #         p5= input("Do you want to have a supplies budget? (yes/no)")
    #         if p5==p5.lower("yes"):
    #             if event.supplies== True:
    #                 supp_bud=float(input("Please provide the budget for supplies: "))
    #                 s4=event.budget_tracker()-event.supplies(supp_bud)   

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
