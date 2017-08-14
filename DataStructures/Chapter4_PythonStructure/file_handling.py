blah = open(filename, 'w', encoding= 'utf8') # writing
blah = open(filename, 'r', encoding= 'utf8') # reading
blah = open(filename, 'a', encoding= 'utf8') # appending - to the end
blah = open(filename, 'r+', encoding= 'utf8') # both reading and writing

blah.read(optional size argument) # can read the whole file or a certain amount of it

blah.readline() # reads one line from the file
blah.readlines() # returns a list of all the lines of data in the file
blah.write()

# tell and seek
tell() # returns an integer giving the file object's current position in the file, measured in bytes from the beginning of the file
seek() # changes the tell() position to a chosen new one

close() # closes the file and frees any system resources taken up by the open file

input()

peek(n) # returns n bytes without moving the file pointer position

fileno() # returns the underlying file's 'file descriptor' (if it has one)

# The Shutil package for manipulating files in the system
	# changing file extensions
'''
import os 
import sys
import shutil

def change_file_ext():
	if len(sys.argv) >2:
		print("Usage: change_ext.py filename.old_ext 'new_ext'")
		sys.exit()
	name = os.path.splitext(sys.argv[1])[0] + "." + sys.argv[2]
	print(name)
	try:
		shutil.copyfile(sys.argv[1], name)
	except OSError as err:
		print(err)
'''

'''
----- Pickle -----
Essentially, pickle can take almost any python object and turn it into a string
To pickle:
	pickle.dump(x, output_name)
To unpickle:
	pickle.load(output_name)

Export serialized pickle data:
import pickle

def export_pickle(data, filename='test.dat', compress=False):
	fh = None
	try:
		if compress:
			fh = gzip.open(filename, 'wb') # write binary
		else:
			fh = open(filename, 'wb') # compact binary pickle format
			pickle.dump(data, fh, pickle.HIGHEST_PROTOCOL)
	except(EnvironmentError, pickle.PicklingError) as err:
		print("{0}: export error: {1}".format(os.path.basename(sys.argv[0], err)))
		return False
	finally: # always executed before leaving the error handling
		if fh is not None:
			fh.close()

Reading data with Pickle:
import pickle

def import_pickle(filename):
	fh = None
	try:
		fh = open(filename, 'rb') # read binary
		mydict2 = pickle.load(fh)
		return mydict2
	except (EnvironmentError) as err:
		print ("{0}: import error:{0}".format(os.path.basename(sys.arg[0]), err))
		return false
	finally:
		if fh is not None:
		fh.close()
'''

# The Struct module
# We can convert Python objects to and from suitable binary representation using struct
	# this object can handle only strings with a specific length

struct.pack() # takes a struct format string and returns a byte object
struct.unpack() # takes a format and a byte or bytearray object and returns a tuple of values

data = struct.pack("<2h", 11, -9)
items = struct.unpack("<2h", data)