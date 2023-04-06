def get_deliv_summary(day_number, file_name): # defines function to generate delivery report
    print("Day " + day_number) #prints what day report is for
    print("\n") 
    input_file = open(file_name) #opens file passed as parameter into function
    deliv_summary = open("Delivery Report.txt", "a") #creates new text file if it doesn't exist
                                                    # to write report to
    deliv_summary.write("Day " + day_number + "\n\n") #writes day of report + new line in the text file
    for line in input_file:    # loops through each line in parameter file
        line = line.rstrip()   # strips that line of leading and trailing white space
        words = line.split('|')  # breaks up that line by every "|" into a list called words

        #melon = words[0]
        #count = words[1]
        #amount = words[2]
        melon, count, amount = words  #create variable for each index of the list words
                                      # by list unpacking instead explicit indexing

        print(f"Delivered {count} {melon}s for total of ${amount}")  # outputs report line
        deliv_summary.write(f"Delivered {count} {melon}s for total of ${amount}\n") # writes line to txt file
    deliv_summary.write("\n") # new line in txt file
    input_file.close()  # closes parameter file
    deliv_summary.close() # closes new txt file


get_deliv_summary("1", "um-deliveries-day-1.txt") #calling function for day 1 deliveries from existing txt file
print("\n")
get_deliv_summary("2", "um-deliveries-day-2.txt") #calling function for day 1 deliveries from existing txt file
print("\n")
get_deliv_summary("3", "um-deliveries-day-3.txt") #calling function for day 1 deliveries from existing txt file




# print("Day 1")
# the_file = open("um-deliveries-day-1.txt")
# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[2]
#     amount = words[1]

#     print(f"Delivered {count} {melon}s for total of ${amount}")
# the_file.close()


# print("Day 2")
# the_file = open("um-deliveries-day-2.txt")
# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[0]
#     amount = words[0]

#     print(f"Delivered {count} {melon}s for total of ${amount}")
# the_file.close()


# print("Day 3")
# the_file = open("um-deliveries-day-3.txt")
# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[0]
#     amount = words[0]

#     print(f"Delivered {count} {melon}s for total of ${amount}")
# the_file.close()
