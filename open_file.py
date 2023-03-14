

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
def write_new_content():
    with open('folder/hello.txt', 'w') as f:
         f.write("Once you have created the branch, you can try pushing your changes again using the following command:")
    
    
if __name__ == '__main__':
    write_new_content() 
    print_content()