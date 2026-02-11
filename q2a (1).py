def count_files(directory):
     if "," in directory   :  
         i = directory.find(",")
         l = directory[:i]         
         r = directory[i+1:]
         return count_files(l) + count_files(r)     
     else:         
        return 1
