import os

dir_path_list=[]
file_path_list=[]

# a = os.walk("/home/adminuser/madan")
for dirname,subdirname,filename in os.walk("/home/adminuser/madan"):
    for files in filename:
        file_path = os.path.join(dirname,files)
        file_path_list.append(file_path)
    for sub_dir in subdirname:
        dir_path = os.path.join(dirname,sub_dir)
        dir_path_list.append(dir_path)     


with open("/home/adminuser/logs/dirpath.txt","w") as f:
    for items in dir_path_list:
       f.write("cd" " " + items + "\n")
    print("updated dirpath.txt")


with open("/home/adminuser/logs/filepath.txt","w") as h:
    for items in file_path_list:
       h.write("cat" " " + items + "\n")
    print("updated filepath.txt")