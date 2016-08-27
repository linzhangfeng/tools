#!/usr/bin/python  
import sys 
import traceback 
from PIL import Image
import os
from optparse import OptionParser
import os,string

 
def change_image_size_ios(image_path,num):
    image = image_path + '/image.png'

    if os.path.exists(image)==False:
        print "image does not exist!!!"
    	return

    img = Image.open(image)
    imageName = 'Icon-'+str(num)
    imageName = imageName+'.png'
    num1 = int(num) 
    size = (num1,num1)
    img = img.resize(size,Image.ANTIALIAS)


    temdir = image_path +'/'+'ios'
    print temdir
    if os.path.exists(temdir):
        print 'aaaa'
    else :
    	os.mkdir("ios")
        print 'bbbb'
        dir = temdir 
 #       print temdir

    os.chdir(temdir)
    print imageName
    img.save(imageName)
    if num == 57:
    	img.save('Icon.png')
    elif num == 114:
    	img.save('Icon@2x.png')

def change_image_size_android(image_path,num):
    image = image_path + '/image.png'
    img = Image.open(image)
    if os.path.exists(image)==False:
        print "image does not exist!!!"
    	return

    temdir = image_path +'/'+'android'
    print temdir
    if os.path.exists(temdir):
        print 'aaaa'
    else :
    	os.mkdir("android")
        print 'bbbb'
        dir = temdir 
    
    os.chdir(temdir)
    print num 
    if num ==1 :
    	name = "drawble"
    	size = (192,192)
    	img = img.resize(size,Image.ANTIALIAS)
    	if os.path.exists(name) == False:
            os.mkdir(name)
        os.chdir(name)
        img.save('icon.png')

        os.chdir('..')
        name = "drawble-xxxhdpi" 
        if os.path.exists(name) == False:
            os.mkdir(name)
        os.chdir(name)
        img.save('icon.png')
        os.chdir('..')

    elif num == 2:
    	name = "drawble-hdpi" 
    	size = (72,72)
    	img = img.resize(size,Image.ANTIALIAS)
        if os.path.exists(name) == False:
            os.mkdir(name) 
        os.chdir(name)
        img.save('icon.png')
        os.chdir('..')

    elif num == 3:
    	name = "drawble-xhdpi" 
    	size = (96,96)
    	img = img.resize(size,Image.ANTIALIAS)
        if os.path.exists(name) == False:
            os.mkdir(name) 
        os.chdir(name)
        img.save('icon.png')
        os.chdir('..')
    elif num == 4:
    	name = "drawble-xxhdpi"
    	size = (144,144)
    	img = img.resize(size,Image.ANTIALIAS)
        if os.path.exists(name) == False:
            os.mkdir(name) 
        os.chdir(name)
        img.save('icon.png')
        os.chdir('..')
    elif num == 5:
        size = (512,512)
        img = img.resize(size,Image.ANTIALIAS)
        img.save('icon.png')

 
 
#change_image_size('image.png')

def makeIosIcons(image_path):
    arr = [29,40,50,57,58,72,76,80,100,114,120,144,152]

    for num in arr:
        change_image_size_ios(image_path,num)

def makeAndroidIcons(image_path):
	print 'android'
	arr = [72,96,144,192]
	for num in range(1,6):
		change_image_size_android(image_path,num)

def main():
    parser = OptionParser()
	
    parser.add_option("-f", "--p", dest="platform",
    help='Parameter for file platform')
    
    (opts, args) = parser.parse_args()
    platform = opts.platform
    if not platform:
        platform = 'android'
        
    dir =  os.getcwd()

    image_path = dir

    if platform == 'ios':
        print 'ios'
        makeIosIcons(image_path)	
    elif platform == 'android':
        print 'android'
        makeAndroidIcons(image_path)
    

    

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)