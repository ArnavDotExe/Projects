def passwd_to_dict():
    
    inputFile = r"D:\College\python\codes\HigherLower\instaFollowers.txt"
    
    mydict = {}
    
    with open(inputFile, 'r') as filedata:
        
        lines = filedata.readlines()
        
        for line in lines:
            if line.startswith("#") or line.startswith(" "):
                continue
            else:
                line = line.split(":")
                if line[0] not in mydict:
                    mydict[line[0]] = int(line[2])
                    
    return mydict
            
passwd_to_dict()