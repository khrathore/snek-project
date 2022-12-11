
# Terp Planner: helps a student org plan their event on campus
from argparse import ArgumentParser
import re
import sys
import pandas as pd
import matplotlib.pyplot as plt
import csv

class User:
    """Defines a user object for the person planning the event
    
    Attributes:
        fname(str): The first name of the person
        lname(str): The last name of the person
        email(str): The UMD email of the person
        org(str): The organization the event is for
        
    Methods:
        email_check(): Checks that the email is a UMD email
        org_check(): Checks that the org is one registered with UMD
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
        
    def email_check(self):
        """
        Uses a regex expression to check whether the email provided is a umd one.
        
        Raises:
            ValueError If the program does not find a matching email
        """
        patt1 = re.compile(r"^[^@]+@terpmail.umd.edu")
        patt2 = re.compile(r"^[^@]+@umd.edu")
        match1 = patt1.search(self.email)
        match2 = patt2.search(self.email)
        if match1 or match2:
            return True 
        else:
            raise ValueError("The email you provided is not valid.")
        
    def org_check(self, org_file="Organizations.txt"):
        """ Rabindra
        Takes the org name
        with statement to read the file
        compares to make sure it's an active campus org, otherwises errors
        
        Args:
            org_name(str): Name of organization
        
        Returns: 
            Boolean Value
        """
        org_list = []
        with open(org_file, 'r') as f:
            for line in f:
                org_list.append(line.strip())
        if self.org in org_list:
            return True
        else:
            raise ValueError(f"{self.org} is not an active Campus Org")
        
class Event:
    """ Plans the event for a student organization based on different categories.
    Attributes:
        location(str): The location of the event.
        evlength(float): The length of the event.
        evbudget(float): The budget of the event as specified by the user.
        food(bool): Determines whether the event will include food; default
        is False.
        equip(bool): Determines whether the event will need equipment;
        default is False.
        music(bool):Determines whether the event will need music;
        default is False.
        supplies(bool):Determines whether the event will need supplies;
        default is False.
        
    Methods: 
        loc_checker(str): Determines the best location to hold an event based on a given budget
        event_id)(set of INT):  Give an random event ID for each event, also add it to a set of IDS.
        budget_tracker(float):Keeps track of the budget to help the user to not overspend.  
        fundraise():If the budget tracker becomes negative print a statement that uses f-strings to say "this is how much you need".
        bud_vis(): Creates a diagram of the budget distribution.
    """
    def __init__(self, length, name, budget, food_budget, equip_budget, supplies_budget, loc_budget, budlist):
        """ Initializes the Event Class. - Sandra
        Args:
            location(str): The location of the event.
            evlength(float): The length of the event.
            evbudget(float): The budget of the event as specified by the user.
            food(bool): Determines whether the event will include food; default
            is False.
            equip(bool): Determines whether the event will need equipment;
            default is False.
            music(bool):Determines whether the event will need music;
            default is False.
            supplies(bool):Determines whether the event will need supplies;
            default is False.
            full_budget(list): A list or dictionary that holds the money per category
        Side effects:
            Creates the location, evlength, evbudget, food, equip, music, and 
            supplies attributes.
            This method will showcase the  Optional Parameter that will be used to 
            determine the budgets for the different event budget categories. 
        """
        self.name = name
        self.length = length
        self.budget = budget
        self.name = name
        self.loc_budget = loc_budget
        self.food_budget = food_budget
        self.equi_budget = equip_budget
        self.supplies_budget = supplies_budget
        self.budlist = budlist
        
    def loc_checker(self, filepath):
        """Determines the best location to hold an event based on a given budget. - Sandra
        Args: 
            filepath(str):A path to a file of locations on campus.
        Return:
            str: The specific location that is within the given budget
        Confirms if the location is on campus
        Will have the with statement for a txt file with UTF-8 encoding
        Ask the user on the budget for location
        User then picks the location that suits them
        This method will showcase a List Comprehension that gives the location options available 
        based on a given budget.
        """
        best_location = {}
        with open(filepath, "r",encoding= "utf-8") as f:
            best_location={}
            for line in f:
                values= line.split(",")
                if float(values[1].strip()) <= self.loc_budget*self.length:
                    best_location[values[0]] = float(values[1].strip())
            return best_location
        
    def event_id(self, idset): 
        """ Rabindra
            Give an rand event ID for each event, also add it to a set of IDS
            check intersection or sth of the new random number and the set of IDs
            if the event ID already exists, do another randomization
            
        Args:
            idset(set of INT): A set of event ids of events on campus
        
        Side Effects:
            Creates a new set of event ids for new events.
        
        Returns: event_id(int)
            
        """
    
    def budget_tracker(self, budget):
        """
        Budget tracker - Conditional Expression - Palrika
        Keeps track of the budget and prints a fundraise f-string based on 
        whether the group is overspending or not.   
            
        Args: 
            budget (float): User-inputted funds they have to plan the event.
            
        Side effect:
            Creates new budget object

        """
        if self.budget < 0:
            f"You are overspending your budget. Your group will need to fundraise ${abs(self.budget)}."
        else:
            f"You have ${self.budget} left in your budget."

        
    def bud_vis(self):
        """
        Khushboo: pyplot usage, creates a diagram of the budget distribution     
        Side effects: 
            Shows a bar graph of spending
        """
        buddf = pd.DataFrame(self.budlist, columns=['Type', 'Budget'])
        plt.xticks(rotation = 90)
        plt.bar(buddf['Type'],buddf['Budget'])

class Budget:
    """Tracks budget objects
    
    Attributes:
        type(str): The category of the budget
        money(float): The budgeted amount for that category
        
    Methods:
        bud_vis(): pyplot visualizaton of the budget distribution
    """
    
    def __init__(self, type, money):
        """
        Creates a budget object
        Args:
            type(str): The category of the budget
            money(float): The budgeted amount for that category
            
        Side efffects:
            Creates a budget object
        
        """
        self.type = type
        self.money = money
        
    def __sub__(self, other):
        """
        Sub magic() method - Magic Method - Palrika
        Compares the given budget with contemporary budget and raise error if the user overspends.
        
        Args:
            other(Budget): The amount of money the user uses while planning the event.
            
        Raises:
            type: If user overspends, this method will raise a type error.
        """
        
        check = self.money - other.money
        if check > 0:
            return f"${check} of your budget is left to spend."
    

def main(fname, lname, email, orgname):
    """ Calculates the overall event budget based on user input and then writes the completed
    event to a different file. -Sandra
    Args:
        fname(str): The user's first name.
        lname(str): The user's last name.
        email(str): The user's email.
        orgname(str):The organization the user is associated with.
    Return:
        file: A txt file containg the completed event plan with budget details.
    The user will be prompted to fill in the corresponding information for their event to determine the
    budget calculations of the event.
    In order to achieve this we will implement a loop
    Once the user is  done the program will write to a doc the info of the event (including budget)
    Do you want to plan another event? if yes, restart loop
    """
    user = User(fname, lname, email, orgname)
    if user.email_check() == True & user.org_check() == True:
        efile = open(f"{user.lname}{user.fname}.csv", 'w')
        writer = csv.writer(efile)
        begin = input("\nDo you want to plan an event? (yes/no): ")
        if begin.lower() == "yes":
            name = input("\nPlease provide the name of the event: ")
            evl = input("\nHow long will your event be: ")
            budget = Budget("Event", float(input("Please provide the budget for your event: ")))
            bud_full = []
            loc_budget = Budget("Location", float(input("How much do you want to spend on the location? ")))
            if loc_budget.money > 0:
                bud_full.append([loc_budget.type, loc_budget.money])
            food_budget = Budget("Food", float(input("How much do you want to spend on food? ")))
            if food_budget.money > 0:
                bud_full.append([food_budget.type, food_budget.money])
            equip_budget = Budget("Equipment", float(input("How much do you want to spend on equipment? ")))
            if equip_budget.money > 0:
                bud_full.append([equip_budget.type, equip_budget.money])
            supplies_budget = Budget("Supplies",float(input("How much do you want to spend on supplies? ")))
            if supplies_budget.money > 0:
                bud_full.append([supplies_budget.type, supplies_budget.money])
            event1 = Event(name, evl, budget, food_budget, equip_budget, supplies_budget, loc_budget, bud_full)
            print("\nFollowing are the available locations within your location budget:")
            affordable_loc = event1.loc_checker()
            for location in affordable_loc:
                print(f"{location}: ${affordable_loc[location]}")
            event1.budget = budget-loc_budget-food_budget-equip_budget-supplies_budget
            if event1.budget < 0:
                event1.budget_tracker
        writer.writerow(f"Event Planner: {user.fname} {user.lname} - {user.email}\nOrganization:{user.org}")
        
    print(f"Thank you for creating a profile with TerpPlanner. Your events will be saved in the file {user.lname}{user.fname}.csv")
    

    

def parse_args(comline):
    """
    # KABINDRA Parses the arguments of the command line that are giving the user information. 
    
    Args :
        comline(str) : arguments users input in the command line
    # Shows the class and sequence unpacking
    """
    parser = ArgumentParser()
    parser.add_argument("fname", help="first name of the student")
    parser.add_argument("lname", help = "last name of the student")
    parser.add_argument("email", help = "email of the student")
    parser.add_argument("orgname", help = "name of the organization")

    return parser.parse_args(comline)

  
if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    # I think for main, we should take the user's info and then everything else will be prompt based
    main(args.fname, args.lname, args.email, args.orgname)
