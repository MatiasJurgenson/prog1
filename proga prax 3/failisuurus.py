import os #faili suuruse lugemise sain siit https://www.digitalocean.com/community/tutorials/how-to-get-file-size-in-python

def faili_suurus(UwU):
    file_stats = os.stat(UwU)
    
    return file_stats.st_size

#print(faili_suurus("owo.txt"))

def teisenda(suurus): #37065
    if suurus >= 1024:
        if suurus >= 1024*1024:
            return str(round((suurus / (1024*1024)), 1)) + " MB"
        else:
            return str(round((suurus / 1024), 1)) + " KB"
        
def faili_suurus2lul(txt):
    print(teisenda(faili_suurus(txt)))

faili_suurus2lul("50MB.bin")            
    