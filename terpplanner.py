
# Terp Planner: helps a student org plan their event on campus
import sys

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
        Init method - Palrika
            Takes in 
                name (first) and (last)
                email
                organization name
        """
        
    def email_check(self):
        """
        Khushboo: Uses a regex expression to check whether the email provided is a umd one.
        
        Errors:
            None: If the program does not find a match, it gets angee
        """
        
    def org_check(self):
        """
        Takes the org name
        with statement to read the file
        compares to make sure it's an active campus org, otherwises errors
        
        Args:
            org_name(str): Name of organization
        
        Returns: 
            Boolean Value
        """
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
        
    """
    def __init__(self, location, evlength, evbudget,  full_budget, food=False, equip=False, music=False, supplies=False):
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
            
            Establish the location
            The length of the event calculations - hourly pay for the location 
            budget categories boolean optional parameter default false
        """
        
    def loc_checker(self, filepath):
        """Determines the best location to hold an event based on a given budget. - Sandra
        Args: 
            filepath(str):A path to a file of locations on campus.
        Return:
            str: The specific location that is within the given budget
        Confirms if the location is on campus
        Will have the with statement for a csv file with UTF-8 encoding
        Ask the user on the budget for location
        User then picks the location that suits them
        This method will showcase a List Comprehension that gives the location options available 
        based on a given budget.
        """
        
    def event_id(self, idset):
        """
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
            Placeholder for the different categories of the overall budget
            estimate()
            Only runs if the food attribute boolean is true
            Conditional expression if food= true
            Asks for an estimate of how much the food gonna cost
            if budget trackers becomes negative call fundraise  
        """
        
    def fundraise(self):
       """
        Fundraise - f-string - Kabindra
            If the budget tracker becomes negative print a statement that uses f-strings to say "this is how much you need"
        """
        
    def bud_vis(self):
        """
        Khushboo: pyplot usage, creates a diagram of the budget distribution     
        returns: a graph

        """

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
        Init() method - Khushboo
        """
    def __sub__(self, other):
        """
        Sub magic() method - Magic Method - Palrika
            Error check for sub to check that they are two budget objects
            Will call and subtract from the budget tracker method
        """

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
    In order to achieve this we will impllement a loop
    Once the user is  done the program will write to a doc the info of the event (including budget)
    Do you want to plan another event? if yes, restart loop
    """

def parse_args(comline):
    """
    # KABINDRA Parses the arguments of the command line that are giving the user information. 
    
    Args :
        comline(str) : arguments users input in the command line
    # Shows the class and sequence unpacking
    """
    return

  
if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    # I think for main, we should take the user's info and then everything else will be prompt based
    main(args.fname, args.lname, args.email, args.orgname)
