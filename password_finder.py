import os
def findpswrd():
    for root, dirs, files in os.walk("H:\Year 1 CSM\Principles of Programming\Assignment 1 - Due 4-12-17\POP_Assigment_1-master\documents"): #for name in files
        
        for file_current in files:              #runs a loop for each file in files
            joined_file = os.path.join(root,file_current)
            file_data=open(joined_file, "r")   #opens all the file in the list call files
            file_contents = file_data.read()    #reads all the data in the text file currently selected

            if ("4D696C6C656E69756D32303030" in file_contents ):           #tests to see if the file was empty
                print("Found Millenium2000 in {}".format(file_current))
            #print(file_contents)

#everything is empty? RESOLVED: didnt join the file name and the path to that file
