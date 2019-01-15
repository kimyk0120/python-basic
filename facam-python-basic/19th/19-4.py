'''
    file write mode

'''

user_input = input("Input : ")
datafile = open('textfile.txt', 'a')
datafile.write(user_input + '\n')
datafile.close()


'''
'r'       open for reading (default)
'w'       open for writing, truncating the file first
'x'       create a new file and open it for writing
'a'       open for writing, appending to the end of the file if it exists
'b'       binary mode
't'       text mode (default)
'+'       open a disk file for updating (reading and writing)
'U'       universal newline mode (deprecated)
'''