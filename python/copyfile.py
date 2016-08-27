#-*- coding:utf-8 -*-
import os
import shutil
 
def cp_tree_ext(exts,src,dest):
    """
    Rebuild the director tree like src below dest and copy all files like XXX.exts to dest 
    exts:exetens seperate by blank like "jpg png gif"
    """
    fp={}
    extss=exts.lower().split()
    f = open("a"+'.txt',"r")
    lines = f.readlines()
    length = len(lines)
    for dn,dns,fns  in os.walk(src):
        for fl in fns:
           # print "==>"+fl
            for line in lines:
                temp = line.split("\n");
                if	temp[0] == fl:
                    print "<=###=>" + temp[0]				
                    if os.path.splitext(fl.lower())[1][1:] in extss:
                        if dn not in fp.keys():
                            fp[dn]=[]
                        fp[dn].append(fl)
                    print "yes"
    for k,v in fp.items():
        relativepath=k[len(src)+1:]
        newpath=os.path.join(dest,relativepath)
        for f in v:
            oldfile=os.path.join(k,f)
            print("Copying ["+oldfile+"] To ["+newpath+"]")
            if not os.path.exists(newpath):
                os.makedirs(newpath)
            shutil.copy(oldfile,newpath)
 
def find_path(src):
    currentDir = "E:\linzhangfeng\linzhangfengSvn\jiaotongbiaozhi\res\allCat\mainSceneCat\catRen\Animation"
    for dirName, subdirList, fileList in os.walk(currentDir):
        print('%s' % dirName)
        for fname in fileList:
            abspath=dirName+'\\'+fname
            print(abspath)  	
			
if __name__ == "__main__":
    cp_tree_ext("png","E:/linzhangfeng/linzhangfengSvn/jiaotongbiaozhi/res/allCat/mainSceneCat/catRen/Animation","C:/Users/Administrator/Desktop/cat/test")