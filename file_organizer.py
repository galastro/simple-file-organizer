import os
import shutil

def organize_files():
   
    files = [f for f in os.listdir('.') if os.path.isfile(f)]

  
    specific_folders = {
        'images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
        'text': ['.txt', '.doc', '.docx', '.pdf'],
        'spreadsheets': ['.xslx', '.csv'],
        'executables': ['.exe', '.msi'],
        'zips': ['.zip', '.rar', '.7z'],
        'videos': ['.mp4', '.mov', '.mkv']
    }

   
    for file in files:
        file_name, file_extension = os.path.splitext(file)
        file_extension = file_extension.lower()

        for folder, extensions in specific_folders.items():
            if file_extension in extensions:
                if file != 'file_organizer.exe':
                    folder_path = os.path.join('.', folder)
                    if not os.path.exists(folder_path):
                        os.makedirs(folder_path)
                    shutil.move(file, os.path.join(folder, file))
                break
        else:
            
            if file != 'file_organizer.exe':
                folder = file_extension[1:]  
                folder_path = os.path.join('.', folder)
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)
                shutil.move(file, os.path.join(folder, file))

if __name__ == "__main__":
    organize_files()
    print("File organization complete.")
