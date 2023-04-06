def get_deliv_summary(day_number):
    print("Day " + day_number)
    print("\n")
    the_file = open("um-deliveries-day-" + day_number + ".txt")
    for line in the_file:
        line = line.rstrip()
        words = line.split('|')

        #melon = words[0]
        #count = words[1]
        #amount = words[2]
        melon, count, amount = words

        print(f"Delivered {count} {melon}s for total of ${amount}")
    the_file.close()

get_deliv_summary("1")
print("\n")
get_deliv_summary("2")
print("\n")
get_deliv_summary("3")


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
