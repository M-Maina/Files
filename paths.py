from pathlib import Path

def print_directory_contents():
    entries = Path.cwd()
    
    for entry in entries.iterdir():
        print(entry.name)
        print(entry.parent) 
        print(entry.parent.parent)
        print(entry.stem) #filename without extension
        print(entry.suffix) #the extension
        print(entry.stat())
        print()
        
        
if __name__ == "__main__":
    print_directory_contents()