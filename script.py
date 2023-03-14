from datetime import datetime
import os

def format_datetime(timestamp):
    utc_timestamp = datetime.utcfromtimestamp(timestamp)
    formated_date = utc_timestamp.strftime('%d %b %Y %H %M %S')
    return formatted_date

# #show current directory
# def display_cwd():
#     cwd = os.getcwd()
#     print(cwd)

# def up_one_directory_level():
#     chdir = os.chdir("../")
#     print(chdir)
    
    
    
def display_entries_in_directory(directory):
    with os.scandir(directory) as entries:
        for entry in entries:
            print("NAME: ", entry.name)
            info = entry.stat()
            print("Creation Time:", formt_datetime(info.st_ctime))
            print("Last Access Time:", format_datetime(info.st_ctime))
            print("Size: ", info.st_size)
            
            
def display_directories(directory):
    with os.scandir(directory) as entries:
        for entry in entries:
            if entry.is_dir():
                print("Directory Name: ", entry.name)
                
                
def display_files(directory):
    with os.scandir(directory) as entries:
        for entry in entries:
            if entry.is_file():
                print("File Name: ", entry.name)
    
    



    
    
if __name__ == "__main__":
    # display_cwd()
    # up_one_directory_level()
    # display_cwd()
   di