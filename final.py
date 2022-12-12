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