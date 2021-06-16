#!/usr/bin/env python
# coding: utf-8
import os

main_wd="/home/EXAMPLE" #<=== INPUT PATH

folder_search="Summary_Details_GEO"

dir_save="EN_US_GEO_US" #<===  OUTPUT PATH
os.chdir(main_wd+"/"+folder_search)


import reverse_geocoder as rg
import csv

#Function to filter tweets on english, by the country column, and by the coordinates when country information is not available.
def is_english_and_usa_tweet(tweet): 
    if tweet[1] == 'en':
        if tweet[6] == "US":
            return True
        else:
            try:
                coordinates = tweet[2][1:-1].split(',')
                coordinates =[float(i) for i in coordinates]
                result_coordinates = rg.search(coordinates)[0]
                if result_coordinates['cc'] == "US":
                    return True
                else:
                    return False
            except:
                return False
        # Please use this else statement if you remove the reverse latitude functionality
        # else:
        #     return False
    else:
        return False

def save_tweet_to_filtered_file(filename, tweet):
    with open(filename,'a',newline='') as csvfilteredfile:
        writer = csv.writer(csvfilteredfile)
        writer.writerow(tweet[0:1])

# Get lisft of folderper month
from os import listdir
folders=listdir(main_wd+"/"+folder_search)

for f in folders:
#f='2020_07'
    print(f)
    if not os.path.exists(main_wd+"/"+dir_save+"/"+f):
        os.makedirs(main_wd+"/"+dir_save+"/"+f)
    
    # Get file in fodler
    os.chdir(main_wd+"/"+folder_search+"/"+f)
    files=listdir(main_wd+"/"+folder_search+"/"+f)
    for c in files:
        print(c)
        original_filename= c #filename for original source file
        filtered_filename = c.replace('Summary_Details.csv','Summary_Details_USA.csv') #filename for filtered destination file
        row_counter=0 #counter for skipping the header
        
        
        
        with open(original_filename, 'r') as csvfile:
          reader = csv.reader(csvfile)
          for row in reader:
                if row_counter == 0:
                    save_tweet_to_filtered_file(main_wd+"/"+dir_save+"/"+f+"/"+filtered_filename, row) #saving header
                elif row_counter > 0:
                    if is_english_and_usa_tweet(row) == True:
                        #print ("Saving tweet",row) uncomment for debug purposes
                        save_tweet_to_filtered_file(main_wd+"/"+dir_save+"/"+f+"/"+filtered_filename, row) #saving the tweet to the filtered file
                row_counter+=1
