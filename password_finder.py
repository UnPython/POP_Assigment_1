import os

def findpswrd():
    x = 0
    for root, dirs, files in os.walk("documents\documents"): #for name in files
        
        for file_current in files:              #runs a loop for each file in files
            joined_file = os.path.join(root,file_current)
            file_data=open(joined_file, "r")   #opens all the file in the list call files
            file_contents = file_data.read()    #reads all the data in the textfile currently selected
            decode = file_contents.decode("hex")
            x +=1
            
            if ("Millenium2000" in decode ):#this should
                print("Found Millenium2000 in {} {}".format(root, file_current))
                
    print(x)
#problems in countred
#everything is empty? RESOLVED: didnt join the file name and the path to that file
#couldn't find the password in hex? RESOLVED: you must first convert the text file to plain text using a hex converter before reading it.
#password is 7e5df39cdf57ffcf97fad07c6e7c9d61
