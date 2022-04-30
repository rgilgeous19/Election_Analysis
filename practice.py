#The data we need to retrieve
#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote


#Import the datetime class from the datetime module

import datetime as dt

#Use the now() attribute on the datetime class to get the present time

now = dt.datetime.now()

#Print the present time

print("The time right now is ", now)

#assign a variable for the file to load and the path

# Assign a variable for the file to load and the path.
file_to_load = 'Resources/election_results.csv'

# Open the election results and read the file.
election_data = open(file_to_load, 'r')

# To do: perform analysis.

# Close the file.
election_data.close()

# Open the election results and read the file
with open(file_to_load) as election_data:

     # To do: perform analysis.
     print(election_data)

import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Print the file object.
     print(election_data)



# Create a filename variable to a direct or indirect path to the file.

file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the open() function with the "w" mode we will write data to the file.

open(file_to_save, "w")

#create a filename variable to a direct or indirect path to the file

file_to_save = os.path.join("analysis", "election_analysis.txt")

#use the open statment to open the file as a text file

outfile = open(file_to_save, "w")

#write some data to the file

outfile.write("Hello World")

outfile.close()




#create a filename variable to a direct or indirect path to the file

file_to_save = os.path.join("analysis", "election_analysis.txt")

#using the with statmnt open the file as text file

with open(file_to_save, "w") as txt_file:

    txt_file.write("Counties in the Election\n\nArapahoe\nDenver\nJefferson")
    




