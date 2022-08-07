from console_gfx import ConsoleGfx #import files


def to_hex_string(*data):
    hex_dict = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'a', 11: 'b',
                12: 'c', 13: 'd', 14: 'e', 15: 'f'}
    data=data[0]
    hex_string=""
    for i in data:
        x = hex_dict[i]
        hex_string=hex_string+x
    return hex_string


def count_runs(*flat_data):
    flat_data = flat_data[0]  # list comes through in a tuple. This solves that issue
    counter = 0
    same_num = False # boolean for when the last int is the same as the previous run
    count = 1 #len(flat_set)
    for index,value in enumerate(flat_data):
        a=len(flat_data)-1
        b=flat_data[index-1]
        if index <= len(flat_data)-1: #if not done iterating
            if index != 0:
                if value != flat_data[index-1]: #if a new run
                    count+=1
                    same_num=False
            if index != a:
                if value == flat_data[index + 1]: #if value is the same as next value
                    counter += 1
                    if counter >= 15:
                        count += 1 #adds a new run
                        counter = 0 #resets counter
                        #if value == flat_data[index + 1]:
                            #counter += 1
                            #continue
                        same_num=True
                        continue
                    else:
                        continue
                else:
                    counter=0 #resets counter when new number
        else:
            break
        continue
    return count


def encode_rle(flat_data):
    count = 1
    current_number = flat_data[0]
    final = []
    index = len(flat_data)  # sets total digits

    for val in flat_data[1:]:
        if val == current_number:  # for matching number
            count += 1  # raises count
            index -= 1  # iterates index
            if count >= 15:
                final.append(count)
                final.append(current_number)
                count = 0
                current_number = val

        else:  # if new number
            final.append(count)
            final.append(current_number)
            count = 1  # resets count
            current_number = val  # selects next number
            index -= 1  # iterates index

    if index == 1:  # for final digit
        final.append(count)
        final.append(current_number)

    if count >= 15:
        final.append(count)
        final.append(current_number)
        count = 0
        current_number = val

    return final

def get_decoded_length(rle_data):
    total=0
    for i in rle_data[::2]:
        total+=i
    return total

def decode_rle(rle_data):
    rle_list=[]
    count=0
    multiplier = rle_data[::2] #count
    values = rle_data[1::2] #value
    while count < (len(multiplier)):
        for i in range(multiplier[count]):
            rle_list.append(values[count])
        count+=1
    return rle_list

def string_to_data(data_string):
    hex_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'a': 10 , 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15}
    hex_list=[]
    hex_list2=[]
    for letter in data_string:
        hex_list.append(letter)
    for letter in hex_list:
        x = hex_dict[letter]
        hex_list2.append(x)
    return hex_list2




def to_rle_string(rle_data):
    hex_dict = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'a', 11: 'b',
                12: 'c', 13: 'd', 14: 'e', 15: 'f'}  # dictionary for hexadecimal values
    rle_data = rle_data
    final_string = ""
    for index,value in enumerate(rle_data):
        if index % 2 ==0:
            value=str(value)
            final_string+=(value)
        elif index % 2 != 0:
            digit_to_add = hex_dict.get(value)
            final_string+=(digit_to_add)
            final_string=final_string+(":")
    if final_string[-1]==":":
        final_string=final_string[0:-1]
    return final_string


def string_to_rle(rle_string):
    hex_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'a': 10, 'b': 11,
                'c': 12, 'd': 13, 'e': 14, 'f': 15}  # dict for conversions
    final_list = []  # final product
    rle_string = rle_string
    rle_split = rle_string.split(":")  # splits our string

    for numbers in rle_split:

        if len(numbers) == 3: #when 3 digits
            first_digit = numbers[0:2]
            first_digit = int(first_digit)
            final_list.append(first_digit)
            second_digit = numbers[-1]
            second_digit = hex_dict.get(second_digit)
            final_list.append(second_digit)

        elif len(numbers) == 2: #when 2 digits
            first_digit = numbers[0:1]
            first_digit = hex_dict.get(first_digit)
            final_list.append(first_digit)
            second_digit = numbers[-1]
            second_digit = hex_dict.get(second_digit)
            final_list.append(second_digit)
    return final_list


# RUN CODE
def main():
    play = True
    image = 0
    picture = 0
    print("Welcome to the RLE image encoder!")
    print("")
    print("Displaying Spectrum Image:")
    ConsoleGfx.display_image(ConsoleGfx.test_rainbow)

    while play == True:
        print("")
        print("RLE Menu")
        print("--------")
        print("0. Exit")
        print("1. Load File")
        print("2. Load Test Image")
        print("3. Read RLE String")
        print("4. Read RLE Hex String")
        print("5. Read Data Hex String")
        print("6. Display Image")
        print("7. Display RLE String")
        print("8. Display Hex RLE Data")
        print("9. Display Hex Flat Data")
        print("")
        choice = int(input("Select a Menu Option: "))
        if choice == 0:
            quit()
        elif choice == 1:
            picture = input("Enter name of file to load: ")
            image = ConsoleGfx.load_file(picture)
            continue
        elif choice == 2:
            image = ConsoleGfx.test_image
            print("Test image data loaded.")
            continue
        elif choice == 3:
            picture = input("Enter an RLE string to be decoded: ")
            picture = string_to_rle(picture)
            image=decode_rle(picture)
            continue
        elif choice == 4:
            picture = input("Enter the hex string holding RLE data: ")
            picture = string_to_data(picture)
            image = decode_rle(picture)
            continue
        elif choice == 5:
            picture = input("Enter the hex string holding flat data: ")
            image = string_to_data(picture)
            continue
        elif choice == 6:
            print("Displaying image...")
            ConsoleGfx.display_image(image)
            continue
        elif choice == 7:
            image = encode_rle(image)
            image = to_rle_string(image)
            print(f"RLE representation: {image}")
            continue
        elif choice == 8:
            image = encode_rle(image)
            image = to_hex_string(image)
            print(f"RLE hex values: {image}")
            continue
        elif choice == 9:
            image=to_hex_string(image)
            print(f"Flat hex values: {image}")
            continue
        else:
            print("Error! Invalid input.")
            continue

if __name__ == "__main__":
    main()










