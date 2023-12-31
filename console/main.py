import os
from src.features.chandassu_type import get_chandassu_type


def form_output(chandassu_type):
    write_output_to_file(chandassu_type)

    write_output_to_console(chandassu_type)


def write_output_to_console(chandassu_type):
    print(f"\nChandassu Name: {chandassu_type.name()}\n")
    print(f"Chandassu Info: \n\n{chandassu_type.poem_chandassu()}")


def write_output_to_file(chandassu_type):
    output_folder_name = "output"

    chandassu_name_file_name = "chandassu_name.txt"
    poem_chandassu_file_name = "poem_chandassu.txt"

    output_folder_path = os.path.join(os.path.dirname(__file__), output_folder_name)

    if not os.path.exists(output_folder_path):
        os.makedirs(output_folder_path)

    chandassu_name_file_path = os.path.join(
        output_folder_path, chandassu_name_file_name
    )
    with open(chandassu_name_file_path, "w") as chandassu_name_fd:
        chandassu_name_fd.write(chandassu_type.name())

    poem_chandassu_file_path = os.path.join(
        output_folder_path, poem_chandassu_file_name
    )
    with open(poem_chandassu_file_path, "w") as poem_chandassu_fd:
        poem_chandassu_fd.write(chandassu_type.poem_chandassu())


def main():
    input_poem_file_path = os.path.join(
        os.path.dirname(__file__), "input_kannada_poem.txt"
    )
    with open(input_poem_file_path, "r") as input_poem_fd:
        input_poem = input_poem_fd.read()

    chandassu_type = get_chandassu_type(input_poem)

    form_output(chandassu_type)


if __name__ == "__main__":
    main()
