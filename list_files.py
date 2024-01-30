# written by Madan Kumar A
# practising the scripting and this program made me happy
# clone this code or copy paste and execute it follow the intructions in command line arguments
# Works on Linux OS ,it outputs the requested number of files in the requested directory , the goal is to make it user friendly

import sys
import os

def list_thefiles_in_dir(cmd1,cmd2):
 try: 
  file_name = cmd1
  files_count = cmd2
  files = os.listdir(file_name)
  total_req_files = files[0:files_count]
  for i in total_req_files:
   print(i)
 except PermissionError:
  print(f"permission denied to the {sys.argv[1]} directory,please enter another folder name")
 except FileNotFoundError:
  print(f'the requested folder {sys.argv[1]} is not found')

def check_crct_input():
 try:
  a= sys.argv[1]
  b= int(sys.argv[2])
  return list_thefiles_in_dir(a,b)
 except IndexError:
  print("please enter exactly two cmd argument with spaces in between them , \n first argument should be folder name \n second argument should be number of files to be displayed")
 except TypeError:
  print(f"please enter an second argument as integer like 2,3,4 ,not: {sys.argv[2]}")
 except ValueError:
  print(f"please enter an second argument as integer like 2,3,4 ,not: {sys.argv[2]}")
 

check_crct_input()

