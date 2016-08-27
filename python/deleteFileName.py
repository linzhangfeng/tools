import os,string
import imghdr
from optparse import OptionParser

#def listAllFiles():
	
def main():
	parser = OptionParser()
	
	parser.add_option("-d", "--dir", dest="dir",
	help='Parameter for file dir')

	parser.add_option("-f", "--fileName",dest="fileName",
	help='Parameter for file dir')

	parser.add_option("-c", "--count",dest="count",
	help='Parameter for file dir')
	
	parser.add_option("-t", "--type", dest="Type",
    help='Parameter for file dir')
	(opts, args) = parser.parse_args()
	dir = opts.dir
	count = opts.count
	fileName = opts.fileName
	if not count:
		count = 6;
	else:
		count = string.atoi(count)
	if not dir:
		dir =  os.getcwd()
	print "rename starting..."
	
	for i in os.listdir(dir):
		oldname=os.path.basename(i)
		imgType = imghdr.what(oldname)
		if imgType == 'png':
			print 'oldname '+oldname
			print count
			fileName1 = oldname[count:]
			print 'fileName1 '+fileName1
			os.rename(oldname,fileName1)
#			print i
			

# -------------- main --------------
if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)