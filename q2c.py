def largest_file(directory):
    if "(" not in directory:
        return ""  
    i = directory.find("(")
    h = directory.find(")")
    size = int(directory[i+1:h])
    name_start = directory[:i].find("file")
    name = directory[name_start:i]
    remaining_result = largest_file(directory[h+1:])
    if remaining_result == "":
        return name
    rstart = directory.find(remaining_result) + len(remaining_result) + 1
    rend = directory.find(")", rstart)
    rsize = int(directory[rstart:rend])
    if size > rsize:
        return name
    else:
        return remaining_result


print(largest_file("rootText[file1(10),file2o(20),subdirT[filetrash(35),subdir2[file4(25),file5(40)]]]"))
