import os
def findpswrd():

    for root, dirs, files in os.walk("C:\Users\Desktop\pop_assignment_1\documents"): #for name in files

        for current_file in files:              #runs a loop for each file in files
            joined_file = os.path.join(root,current_file)
            file_data=open(joined_file, "r")   #opens all the file in the list call files
            file_contents = file_data.read()    #reads all the data in the text file currently selected

            if (file_contents == ""):           #tests to see if the file was empty
                print("ping")                   #everything is empty?
            #print(file_contents)