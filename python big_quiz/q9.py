def num_line(filename):
    with open(filename,"r") as file:
        lines = file.readlines()
        return len(lines)
print(num_line("file name"))
