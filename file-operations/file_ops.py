def read_file(file_name):
    with open(file_name, "r") as f:
        contents = f.read()
    print(contents)
    return contents


def read_file_into_list(file_name):
    with open(file_name, "r") as f:
        return [line for line in f]


def write_first_line_to_file(file_contents, output_filename):
    first_line = file_contents.split('\n')[0]
    with open(output_filename, "w") as f:
        f.write(first_line)


def read_even_numbered_lines(file_name):
    with open(file_name, "r") as f:
        return [line for i, line in enumerate(f) if i % 2 == 1]


def read_file_in_reverse(file_name):
    with open(file_name, "r") as f:
        return f.readlines()[::-1]


def main():
    file_contents = read_file("sampletext.txt")
    print("File Contents:\n", file_contents)

    print(read_file_into_list("sampletext.txt"))
    write_first_line_to_file(file_contents, "output.txt")
    print(read_even_numbered_lines("sampletext.txt"))
    print(read_file_in_reverse("sampletext.txt"))


if __name__ == "__main__":
    main()