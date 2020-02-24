"""
Author: Peter Elliott       Created:    19/02/2020

            Task
Taking the following EDIFACT message text,
write some code to parse out the all the LOC segments
and populate an array with the 2nd and 3rd element of each segment.

Note:  the ‘+’ is an element delimiter
each + symbol seperates different words

        Notes to self
1. Read in EDIFACT file, question as edifact or text as above say EDIFACT message text
2. find all LOC segments and seperate them
3. Fill an array with each LOC entry 2nd and 3rd elements
4. Display
"""

file = open("Exercise1.txt", "r")  # task stated EDIFACT message text didn't mention file format so I defaulted it to text file
entered_data = file.readlines()  # open file and read each line

LOC_data = []  # array for LOC segments 2nd and 3rd element

for line in entered_data: # this cycles through each line of the file
    if "LOC" in line:  # if line contains the word LOC
        LOC = line.split("+")  # split the
        LOC_data.append({"Element 2": LOC[1], "Element 3": LOC[2].rstrip()})  # rstrip() removes \n at the end each string
        # above the 2nd and 3rd elements are placed in a dictionary and then added to a list

print(len(LOC_data), " items where found")  # number of tags found
if len(LOC_data) > 0:  # if tags were found display them
    for entry in LOC_data:  # print each element of  array
        print("2nd Element : ", entry["Element 2"], "    and    3rd Element :", entry["Element 3"])

input('Press enter to continue')