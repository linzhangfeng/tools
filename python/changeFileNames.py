import os,string
import imghdr
from optparse import OptionParser

#def listAllFiles():
	
def main():
	parser = OptionParser()
	
	parser.add_option("-d", "--dir", dest="dir",
    help='Parameter for file dir')
	
	parser.add_option("-f", "--fileName", dest="fileName",
    help='Parameter for file dir')
	
	parser.add_option("-t", "--type", dest="Type",
    help='Parameter for file dir')
	(opts, args) = parser.parse_args()
	dir = opts.dir
	fileName = opts.fileName
	if not fileName:
		print "no file name "
		return

	
	if not dir:
		dir =  os.getcwd()
	print "rename starting..."
	print "direction: "+dir 
	count = 1
	for i in os.listdir(dir):
		print i
		oldname=os.path.basename(i)
#		print "oldname "+imghdr.what(oldname)
		imgType = imghdr.what(oldname)
#		print imgType
		if imgType == 'png':
#			print oldname
			print 'fileName '+fileName
			strCount = str(count).zfill(2)
			fileName1 = fileName+'_'+strCount+'.png'
			print 'fileName '+fileName1
			print 'oldname ' +oldname
			os.rename(oldname,fileName1)
			print i
			count += 1

# -------------- main --------------
if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)