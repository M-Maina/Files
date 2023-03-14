import glob


def display_pngs():
    png_files = glob.glob('*.png') #filtering with file type
    print(png_files)
    
def find_monster_one():
    filtered_items = glob.glob('*monster01*') #filtering with filenames
    print(filtered_items) 
    
def find_monster_one_in_subdirs():
    for file in glob.iglob('**/scripts*', recursive=True): #filtering even in subfolders
        print(file)
    
    
    
    
if __name__ == '__main__':
    # display_pngs()
    # find_monster_one()
    find_monster_one_in_subdirs()