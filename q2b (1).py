def extract_size(s):   
    if "(" in s:
        i = s.find("(")
        h = s.find(")")
        return int(s[i+1:h]), s[h+1:]
    else:
        return 0, ""
def sum_file_sizes(directory):
    if directory == "":
        return 0
    size, remain = extract_size(directory)
    return size + sum_file_sizes(remain)
