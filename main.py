import pathlib
from pathlib import Path
from plistlib import InvalidFileException
from typing import Tuple, Dict, List

from colorama import Fore

#TASK 1 START
print()
print("--------------TASK 1--------------")


def task1(file_path: str) -> Tuple[int, float]:
    with open(file_path, mode="r") as file:
        total_salary = 0
        employees_count = 0
        while True:
            line = file.readline()
            if not line:
                break

            try:
                parts = line.split(",")
                salary = int(parts[1])
                total_salary += salary
                employees_count += 1
            except ValueError as e:
                raise InvalidFileException(f"Invalid file format at line: {employees_count + 1}. "
                                           f"Expected name(str),salary(int) ") from e

        average_salary = total_salary / employees_count
        return total_salary, average_salary


file_path_task1 = "./users.csv"
total_salary_r, average_salary_r = task1(file_path_task1)
print(f"Total salary: {total_salary_r}")
print(f"Average salary: {average_salary_r}")
# TASK 1 END

# TASK 2 START
print()
print("--------------TASK 2-------------")

file_path_task2 = "./cats.csv"


def get_cats_info(path: str) -> List[Dict[str, str]]:
    cats_info = []

    with open(path, mode="r") as file:
        for line in file.readlines():
            parts = line.strip().split(",")
            cat_id = str(parts[0])
            name = str(parts[1])
            age = int(parts[2])

            entry = {"id": cat_id, "name": name, "age": age}
            cats_info.append(entry)

    return cats_info


cats_info_result = get_cats_info(file_path_task2)
for cat in cats_info_result:
    print(f"ID: {cat['id']}, Name: {cat['name']}, Age: {cat['age']}")
# TASK 2 END


# TASK 3 START
print()
print("--------------TASK 3--------------")
SUFFIX_COLOR = Fore.RED
DIR_COLOR = Fore.BLUE
STEM_COLOR = Fore.YELLOW
FILE_INDENT = "  "


def print_directory_contents(path: str, indent="") -> None:
    directory = pathlib.Path(path)
    if not directory.exists() or not directory.is_dir():
        print(Fore.RED + f"{directory} is not a valid directory.")
        return

    for file in sorted(directory.iterdir()):
        if file.is_dir():
            print(DIR_COLOR, file.name)
            new_indent = indent + FILE_INDENT
            print_directory_contents(str(file), new_indent)
        elif file.is_file():
            colorized_file = get_colorized_file(file, indent)
            print(colorized_file)


def get_colorized_file(file: Path, indent: str) -> str:
    if not file.is_file():
        raise InvalidFileException(f"{file} is not a valid file.")
    return STEM_COLOR + indent + file.stem + SUFFIX_COLOR + file.suffix


task3_input = "task3test"
print_directory_contents(task3_input)
# TASK 3 END
