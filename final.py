from argparse import ArgumentParser
import string
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