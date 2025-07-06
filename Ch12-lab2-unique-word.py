# Tim Lucas
# Lab 12-1
# 2025-07-06

def main():
    print("Unique Word Counter")
    print()

    file_name = input("Enter the name of the file you wish to process: ")

    while True:        
        try:
            with open(file_name) as file:
                text = file.read()   
            
                text = text.replace(".", "")
                text = text.replace(",", "")
                text = text.replace("\n", " ")

                word_list = text.split(" ")

                word_set = set(word_list)

                print(f"there are {len(word_set)} unique words in {file_name}.")
                print()
                print("Thanks for using the program")
                break
                
        except FileNotFoundError:
            print(f"The file \"{file_name}\" could not be found!")
            user_input = input("Enter the name of the file you wish to process or type exit to quit: ")
            if user_input == "exit":
                print()
                print("Thanks for using the program!")
                break
            else:
                file_name = user_input                    

# I didn't use the "os" library because it seemed the instructions only gave the option 
# to use it, but did not require it's use. If not using the "os" library would cause me 
# to lose any points, I will redo the assignmet and include the library.  

if __name__ == "__main__":
    main()