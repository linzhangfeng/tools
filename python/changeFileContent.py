import os,string
import imghdr
from optparse import OptionParser
import re

#def listAllFiles():
	
def listFiles(dirPath):
	fileList=[]
	for root,dirs,files in os.walk(dirPath):
		lengdd = len(files)
		print lengdd
		return files

 

def main():
	fileDir =  os.getcwd()
	regex = ur'FUNC_SYS_ADD_ACCDETAIL'
	fileList = listFiles(fileDir)
	lengdd = len(fileList)
	print lengdd
	for fileObj in fileList:
		print "file "+fileObj
		if fileObj != "changeFileContent.py":
			print "22"
			f = open(fileObj)
			print "33"
			all_the_lines=f.readlines()
			f.close()
			fwrite = open(fileObj,'w+')
			leng = len(all_the_lines)
			#print leng
			for line in all_the_lines:
				#print line
				if not line: 
					print "not" + line			
					break 		
				if ('Version' in line):
					temp = line.split(': ');
					lengs = len(temp)
					str = temp[0] + ': ' + '"2.3.2.6",' + '\n'
					#print str
					fwrite.write(str)
				else:  
					#print "else" + line
					fwrite.write(line)
			fwrite.close()
		
# -------------- main --------------
if __name__ == '__main__':
	try:
		main()
	except Exception as e:
		#traceback.print_exc()
		#sys.exit(1)
		print 'aaaaaa'