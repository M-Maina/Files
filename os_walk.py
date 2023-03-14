import os

def top_down_walk():
    for dirpath, dirnames, files in os.walk('folder/'):
        print("Directory: ", dirpath)
        print("Includes these directories")
        for dirname in dirnames:
            print(dirname)
        print("Include these files")
        for filename in files:
            print(filename)
        print()
        
        
def bottom_up_walk():
    for dirpath, dirnames, files in os.walk('folder/', topdown=False):
        print("Directory: ", dirpath)
        print("Includes these directories")
        for dirname in dirnames:
            print(dirname)
        print("Include these files")
        for filename in files:
            print(filename)
        print()
    
        
        
if __name__ == '__main__':
   # top_down_walk()
    bottom_up_walk()