def get_valid_input():
    while True:
        user_input = input("Enter single digits separated by one space: ")
        digits = user_input.split()
        valid = True

        try:
            num_list = [int(digit) for digit in digits]
            if len(num_list) < 2 or num_list[0] == 0 or num_list[-1] == 0:
                raise ValueError
        except ValueError:
            print("Invalid list, try again.")
            continue

        return num_list

def reverse_list(lst):
    return list(reversed(lst))
def add_reverse(lst):
    num = int(''.join(map(str, lst)))
    reversed_num = int(''.join(map(str, reverse_list(lst))))
    result = num + reversed_num
    return list(map(int, str(result)))


if __name__ == "__main__":
    print("*" * 50)
    valid_list = get_valid_input()
    print("The initial list is:", valid_list)
