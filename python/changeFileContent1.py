import os,string
import imghdr
from optparse import OptionParser

#def listAllFiles():
def listFiles(dirPath):
	fileList=[]
	for root,dirs,files in os.walk(dirPath):
		for fileObj in files:
			fileList.append(os.path.join(root,fileObj))
			return fileList
def main():
	fileDir = "D:/linzhangfeng/python/wenjian/kao_stbw.json"
	#regex = ur'FUNC_SYS_ADD_ACCDETAIL'
	f = open(fileDir,'r+')
	output  = open("kao_stbw.json",'w+')  
	all_the_lines=f.readlines()
	for line in all_the_lines:
		if ('Version' in line):
			temp = line.split(': ');
			lengs = len(temp)
			str = temp[0] + ': ' + '"2.3.2.4",'
			print str
			#output.write(str);


# -------------- main --------------
if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)