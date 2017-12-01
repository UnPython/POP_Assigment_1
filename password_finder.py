"""
Author: Matthew Ross
Version: 1.0
Python Version: 2.7.8
"""
import os
def findpswrd():
    """
    This function is used to find the file with the signiture Millenium2000 in it.
    This function then returns the whole contents of the file found.
    EXCEPTIONS:
    - If there is no file with Millenium2000 in it then you may get a runtime error.
    - If your files are not encoded in hex then you will not get a return value.
    RETURN:
    - The entier contents of the text file where Millenium2000 was found.
    Veriable Description:
    - root, dirs, files are used to walk though each file in the selected location and all sub direcotrys.
      root is the full path, dirs is a list of all the directorys in that path and files is a list of all
      the files one of those directorys
    - joined_file is the path for the current file selected.
    - file_data if the current file in use.
    - file_contents is the contents of that file NOTE: this will still be in hex.
    - decode is the decoded version of that file that should now be in plain text.
    - file_found is the content of the file where Millenium2000 was found
    """
    for root, dirs, files in os.walk("documents\documents"):
    #NOTE: if you set this a c:/ then this will look through EVERYTHING on your c drive and probably crash in the process
    #for entities in this directory do this...
        
        for file_current in files:
        #runs a loop for each file in files
            joined_file = os.path.join(root,file_current)
            file_data=open(joined_file, "r")
            #opens all the file in the list called files
            file_contents = file_data.read()
            #reads all the data in the textfile currently selected
            decode = file_contents.decode("hex")
            
            if ("Millenium2000" in decode ):#this should
                print("Found Millenium2000 in {} {}".format(root, file_current))
                file_found = decode
    return(file_found)
    print(file_found)
    #the whole file is returned by this function here
findpswrd()
#fundtion is called here to start searching for Millenium2000

"""
Problems Incountred
everything is empty? RESOLVED: didnt join the file name and the path to that file
couldn't find the password in hex? RESOLVED: you must first convert the text file to plain text using a hex converter
before reading it. this has now been added to this function
"""
