import os
import shutil

def list_directories_files(path):
    return [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))], \
           [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))], \
           os.listdir(path)

def check_access(path):
    return os.path.exists(path), os.access(path, os.R_OK), os.access(path, os.W_OK), os.access(path, os.X_OK)

def path_info(path):
    return os.path.exists(path), os.path.dirname(path), os.path.basename(path)

def count_lines(file_path):
    with open(file_path, 'r') as f:
        return sum(1 for _ in f)

def write_list_to_file(lst, file_path):
    with open(file_path, 'w') as f:
        f.writelines(f"{item}\n" for item in lst)

def generate_text_files():
    for c in range(65, 91):
        with open(f"{chr(c)}.txt", 'w') as f:
            pass

def copy_file(src, dest):
    shutil.copyfile(src, dest)

def delete_file(path):
    if os.path.exists(path) and os.access(path, os.W_OK):
        os.remove(path)
        return True
    return False

print(list_directories_files("."))  
print(check_access("test.txt"))     
print(path_info("test.txt"))        
print(count_lines("test.txt"))      
write_list_to_file(["Hello", "World"], "output.txt")  
generate_text_files()               
copy_file("output.txt", "copy.txt")
print(delete_file("copy.txt"))      
