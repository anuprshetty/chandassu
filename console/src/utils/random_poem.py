import os
import random
import re


def get_random_poem():
    random_poem = ""

    poems_folder_name = "chandassu_poems"
    poems_folder_path = os.path.join(
        os.path.dirname(__file__), "../../", poems_folder_name
    )

    poem_file_paths = []
    for (
        sub_folder_path,
        dir_names,
        file_names,
    ) in os.walk(poems_folder_path):
        for file_name in file_names:
            if not file_name.endswith(".txt"):
                continue

            poem_file_path = os.path.join(sub_folder_path, file_name)
            poem_file_paths.append(poem_file_path)

    if not poem_file_paths:
        return random_poem

    random_poem_file_path = random.choice(poem_file_paths)

    with open(random_poem_file_path, "r", encoding="utf-8") as poem_fd:
        poem_file_content = poem_fd.read().strip()
        poems = re.split(r"\n\s*\n", poem_file_content)

    if not poems:
        return random_poem

    random_poem = random.choice(poems)

    return random_poem
