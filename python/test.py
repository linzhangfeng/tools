import os  
  
def direc():  
    for d,fd,fl in os.walk('/home/shichao/gun-ucos'):  
            for f in fl:  
                    sufix = os.path.splitext(f)[1][1:]  
            if ( (sufix == 'h') or (sufix == 'c') ):  
                #print sufix  
                func(d + '/' + f)  
  
  
def func(filename):  
    input   = open(filename)  
    lines   = input.readlines()  
    input.close()  
  
    output  = open(filename,'w')  
    for line in lines:  
        if not line:  
            break  
        if (('Type' in line) and ('Normal' in line) ):  
            temp    = line.split("Normal")  
            temp1   = temp[0] + 'MarkedSubImage' + temp[1]  
            output.write(temp1)
        elif 'Plist' in line:  
            temp    = line.split(": ")  
            temp1   = temp[0] + ": " + '"' + 'picture.plist' + '"' + '\n' 
            output.write(temp1)
        else:  
            output.write(line)    
    output.close()  
  
if __name__ == "__main__":  
    func("kao_stbw.json") 