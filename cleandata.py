import pandas as pd
import numpy as np

#data cleaning functions
#names I can't process with functions

file_path = 'data/robbins_speakers.csv'
data = pd.read_csv(file_path)
#combine title, firstname, lastname to generate page title
#make a list of page title and append to df as series later

#.apply to df, axis = 1 (apply to each row)
def generateName(row):
    if row['given_first']: 
        pageTitle = row['title'] + " " + row['givenname'] + " " + row['surname']
    else: 
        pageTitle = row['title'] + " " + row['surname'] + " " + row['givenname']
    pageTitles.append(pageTitle)



#combine firstname, lastname in first_last or last_first format to match scientist name with image filename
def generateLinkName(row):
    template = "{}_{}"
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
    if row['given_first']: 
        linkName = template.format(givenName, sur)
    else: 
        linkName = template.format(sur, givenName)
    linkNames.append(linkName)

def generateImageSrc(row):
    template = "/images/{}.png"
    row['link_']



#how to I pack these three lines into a function
pageTitles = []
data.apply(generateName, axis=1)
data['page_title'] = np.array(pageTitles)

linkNames = []
data.apply(generateLinkName, axis=1)
data['link_name'] = np.array(linkNames)

imageLinkTemplate = "/images/{}.png"
imageSrc = list(map(lambda x: imageLinkTemplate.format(x), linkNames))
#print(imageSrc)

hrefTemplate = "/{}"
href = list(map(lambda x: hrefTemplate.format(x), linkNames))

data['image_src'] = np.array(imageSrc)
data['href'] = np.array(href)


#print(data['page_title'])
#print(data['link_name'])
