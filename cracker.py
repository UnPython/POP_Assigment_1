"""
Module Name: cracker
Author: Matthew Ross
Version: 1.0
Python Version: 2.7.8
"""
import decoder as de
    """
    This functoin is used to decode a message hidden in decode_me.txt and return
    the output
    EXCEPTIONS:
    - if decode_me.txt is not in the same file as this module then you will get
    and error as this function will be unable to locate it
    RETURNS:
    - the decoded string hidden within decode_me.txt
    Veriable Description:
    - coded is used to store the coded message from decode_me.txt
    - decoded_dec is used to store the decimal decoded messgae that is given after
    using de.decodeID
    -decoded_plain this is the message once it has been fully decoded and will display
    in plain text
    """
def decode():
    coded = open("decode_me.txt", "r").read()
    #opens the file and reads it
    decoded_dec = de.decodeID(coded, "s5063380")
    #decodes the file to decimal
    decoded_plain = de.bin2utf(decoded_dec)
    #decodes the file to plain text
    print(decoded_plain)
    return (decoded_plain)
    #returnt the decoded message in plain text
decode()

    
