################
#global variables
file_path = "/home/ubuntu/madan/important.txt"
word_to_search = "age"
actual_sentence = "age : xx\n"

###########
def modify_file(file_path,word_to_search,modified_sentence):
    with open(file_path,"r") as file:
        lines = file.readlines()
    with open(file_path,"w") as file:
        for line in lines:
          if word_to_search in line:
            file.write(modified_sentence)
          else:
            file.write(line)

def check_input():
 y = input("enter the age to be updated:")
 if not y:
   print("you have not entered anything")
 elif not y.isdigit():
   print(f"{y} is not a integer value")
 else:
  modified_sentence = actual_sentence.replace("xx", y)
  modify_file(file_path,word_to_search,modified_sentence)

check_input()



