filename = 'file_directory/programming.txt'

with open(filename, 'a') as file_object:  # 'w' for write | 'r' for read | 'a' for post | 'r+' for read and write
    file_object.write("I love programming \n")