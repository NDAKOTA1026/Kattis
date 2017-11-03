def get_file_line_number(file_name: str) -> int:
    """
    get_file_line_number
    """
    input_file = open(file_name, 'r')
    data = input_file.read().splitlines()
    print(len(data))
    return len(data)


if __name__ == "__main__":
    file_name = input("Enter the name of the file: ")
    get_file_line_number(file_name)
