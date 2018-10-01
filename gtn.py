import gtn_header_files
option = chr
guess = int
result = int
diff = int
guess_result = ""
option = input("Do you want to guess ? (y/n): ")
while option == 'y':
    guess = input("Guess the no.: ")
    result = gtn_header_files.validate_input(int(guess))
    if result == 0:
        print("Please enter an integer...")
        continue
    diff = gtn_header_files.difference(guess)
    guess_result = gtn_header_files.comparison(diff)
    print(guess_result)
    option = input("Do you want to guess ? (y/n): ")
