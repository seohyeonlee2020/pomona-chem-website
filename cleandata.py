import pandas as pd

#data cleaning functions
#names I can't process with functions



#combine title, firstname, lastname to generate page title
#.apply to df, axis = 1 (apply to each row)
def generateName(row):
    if row['given_first']: 
        row['fullname'] = row['title'] + " " + row['givenname'] + " " + row['surname']
    else: 
        row['fullname'] = row['title'] + " " + row['surname'] + " " + row['givenname']

#combine firstname, lastname in first_last or last_first format to match scientist name with image filename
def findImage(row):
    template = "{}_{}.png"
    #make everything lowercase
    given = row['givenname'].lower()
    given = given.split(" ")
    if len(given[0]) <=2:
        #cases like F. MiddleName LastName
        givenName = given[1]
    else:
        # FirstName M. LastName
        givenName = given[0]
    sur = row['surname'].lower()
    sur = sur.split([" -"]) #split by space or dash
    surName = "".join(sur)
    if row['given_first']: 
        row['imagefile'] = template.format(given, sur)
    else: 
        row['imagefile'] = template.format(sur, given)

