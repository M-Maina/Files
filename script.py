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
            
    
    
    
    
    
if __name__ == "__main__":
    # display_cwd()
    # up_one_directory_level()
    # display_cwd()
    format_datetime()