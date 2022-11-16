'''
Terp Planner: helps a student org plan their event on campus

class User:

Init method - Palrika
    Takes in name (first) and (last)
    email
    organization name
    
Email_check: - Regex - Khushboo
    check if it's a umd.edu email using a regex
    if it isn't, throw an error
    
Org_check: - With Statement - Rabindra
    Takes the org name
    with statement to read the file
    compares to make sure it's an active campus org, otherwises errors
       

class Event:
    To create the event and get the specifics for the student group

Init method - Optional Param - Sandra
    Establish the location
    The length of the event calculations maybe? - hourly pay for the location 
    Food boolean optional parameter default false - optional parameter 

Location checker - List Comprehension - Sandra
    Confirms if the location is on campus
    Will have the with statement
    Ask the user on the budget for location
    Create a List comprehension that gives the options available based on the user’s budget.
    User then picks the location that suits them
    
Event_ID(set, self) - Sets - Rabindra
    Give an rand event ID for each event, also add it to a set of IDS
    check intersection or sth of the new random number and the set of IDs
    if the event ID already exists, do another randomization
    

Budget tracker - Conditional Expression - Palrika
    Placeholder for the different categories of the overall budget
    estimate()
    Only runs if the food attribute boolean is true
    Conditional expression if food= true
    Asks for an estimate of how much the food gonna cost
    if budget trackers becomes negative call fundraise 

Budget_chart - Khushboo - Pyplot
    Create a plot of the money allocation
    
Fundraise - f-string - Kabindra
    If the budget tracker becomes negative print a statement that uses f-strings to say "this is how much you need"

class Budget:
    To ask for and keep a track of the group’s budget, and make sure that they don’t go over budget 

Init() method - Khushboo

Sub magic() method - Magic Method - Palrika
    Error check for sub to check that they are two budget objects
    Will call and subtract from the budget tracker method

Main - Sandra
    loop
        write to a doc the info of the event (including budget)
    Do you want to plan another event? if yes, restart loop
    
Argument parser - ArgParse - Kabindra
    sequence unpacking 

if __name__ == "__main__"
'''