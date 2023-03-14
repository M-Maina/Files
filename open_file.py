

def print_content():
    f = open('folder/hello.txt', 'r')
    contents = f.read()
    print(contents)
    f.close()
    
def write_new_content():
    f = open('folder/hello.txt', 'w')
    f.write("Once you have created the branch, you can try pushing your changes again using the following command:")
    f.close()
    
    #USING WITH PATTERN
    
def print_file_content():
    with open('folder/hello.txt', 'r') as f:
        print(f.read(20)) #Reads the first 10 bytes
    
    
def write_new_content():
    with open('folder/hello.txt', 'w') as f:
         f.write("Once you have created the branch, you can try pushing your changes again using the following command:")
    
    
    
def print_file_content_readlines():
    with open('folder/hello.txt', 'r') as f:
        content = f.readlines()
        print(content[1])
    
    
def print_file_content_readline():
    with open('folder/hello.txt', 'r') as f:
        line = f.readline()
        while line != '':
            print(line, end='')
            line = f.readline()
        
        
           
if __name__ == '__main__':
   # write_new_content() 
   # print_content()
    #print_file_content()
    print_file_content_readline()