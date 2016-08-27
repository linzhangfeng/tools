import os,string,sys
from PIL import Image
from optparse import OptionParser

def findPictureName(fileName,scale):
	print "start ...1"
	fileName = "rsz2_nm_rjtbz_0"
	f = open(fileName+'.json',"r")
	ff = open("a.txt", "a")
	lines = f.readlines()
	length = len(lines)
	count = 0
	while count<length:
		line = lines[count].strip()
		if line.find('/')!=-1:	
			print "start ...find"
			temp    = line.split('"')	
			temp1 = temp[3].split('/')
			leng = len(temp1)
			print "start ..."+temp1[leng-1]
			ff.write(temp1[leng-1]+'\n')
		count = count +1
	ff.close()
	f.close()

def main():
	parser = OptionParser()
	print "start ..."
	parser.add_option("-f", "--fileName", dest="fileName",
    help='Parameter for file dir')
		
	parser.add_option("-s", "--scale", dest="scale",
    help='Parameter for scale')

	(opts, args) = parser.parse_args()
	fileName = opts.fileName
	scale = opts.scale
	

	if not scale:
		scale = 0.5
	
	if not fileName:
		print "no file name "
		return
	else:
		print "run changeSingleAnimSize=" +fileName
		findPictureName(fileName,scale)
	dir =  os.getcwd()


if __name__ == '__main__':
    try:
        main()
       
    except Exception as e:
        # traceback.print_exc()
        sys.exit(1)