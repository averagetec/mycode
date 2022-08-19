#!usr/bin/env python3
"""
Amazon Apprentice | Jauric Flowers | Jauric.Flowers@tlgcohort.com
This program shows the use of pandas to manipulate a static file to
show data. Also, we will a new file to excel.
"""
import sys
import time
import pandas as pd


def main():
    # variables
    delete_column = ""
    user_data = ""

    # create data frame from static file
    data_frame = pd.read_csv("anime-list.csv")

    # Introduction to program
    print("Welcome to the new anime club, where you can find out the top anime to date. "
          "Also, you may exit anytime by typing 'exit.'")
    print("=============================================================================")
    time.sleep(.5)
    print("Let's look at the top 20 anime in the world!")
    # Print top 20 anime titles only
    print(data_frame.head(20)['AnimeName'].to_csv(index=False).strip())  # print entire data frame
    print("=============================================================================")

    # Show user choice with details
    while True:
        user_pick_from_home = input("Type a numeral 1-20 from the list above and we can "
                                    "give you details. ")

        # Try except for error handling and menu formatting
        try:
            pick_data = data_frame.head(int(user_pick_from_home))
            user_pick_int = int(user_pick_from_home) - 1
            data_dict = pick_data.to_dict()
            main_dict = (str(data_dict.keys()).strip('dict_keys([').strip('])'))
            c = main_dict.split(",")
            menu = "==============="
            time.sleep(.25)
            print(f"%s %12s %12s %12s %12s" % (menu, menu, menu, menu, menu))
            text_line = (str(data_dict['AnimeName'][user_pick_int]) + str(data_dict['genre'][user_pick_int]) + str(
                data_dict['type'][user_pick_int]) + str(data_dict['episodes'][user_pick_int]) + str(
                data_dict['rating'][user_pick_int]) + str(data_dict['members'][user_pick_int]))
            print(f"%s %5s %s %s %s %5s\n" % (c[0], c[1], c[2], c[3], c[4], c[5]))
            print(text_line)
            print(f"%s %12s %12s %12s %12s\n" % (menu, menu, menu, menu, menu))
            break

        # if try fails
        except:
            print("Enter valid number 1-20. ")
            continue

    # while loop to gain user inputs
    while True:
        response = input("Type the corresponding number of anime shows you would like to see printed to the screen. "
                         "You can also exit. ").strip().lower()
        # Try except for error handling
        try:
            # user will exit out the while loop
            if response == "exit":
                sys.exit()

            # if logic for user responses
            if response != "":
                user_data = data_frame.head(int(response))
                data_len = len(user_data)
                print(user_data)
                print(f'The length of the data is: {data_len}')
                break

        # if try fails
        except:
            print("Please enter valid numeral. ")
            continue

    # data manipulation by dropping columns
    # while loop for user input
    while True:
        message = input("Would you like to drop a column i.e 'name,genre,type,episodes,rating,members. Type "
                        "1-6 to drop a corresponding column, or you may say no. ")
        if message in ('no', 'n'):
            break
        # if logic to gain user input and delete column and print updated data
        if message == "1":
            delete_column = user_data.drop(columns=['AnimeName'])
            print(delete_column)
            break
        if message == "2":
            delete_column = user_data.drop(columns=['genre'])
            print(delete_column)
            break
        if message == "3":
            delete_column = user_data.drop(columns=['type'])
            print(delete_column)
            break
        if message == "4":
            delete_column = user_data.drop(columns=['episodes'])
            print(delete_column)
            break
        if message == "5":
            delete_column = user_data.drop(columns=['rating'])
            print(delete_column)
            break
        if message == "6":
            delete_column = user_data.drop(columns=['member'])
            print(delete_column)
            break
        # error handling
        else:
            print("Please enter valid numeral 1-6. ")

    # Check responses and export new data_frame to excel
    while True:
        response = input("Would you like to export the new data frame to excel for viewing?"
                         " Enter 'y' or 'n'. ")
        # try except error handling
        try:
            if response.lower() == 'y':
                # when response is y, export to excel
                delete_column.to_excel("dropped_columns.xls")
                break
            if response.lower() == 'n':
                break
        # If try fails
        except:
            print("Please enter only 'y' or 'n'. ")
            continue


if __name__ == "__main__":
    main()
