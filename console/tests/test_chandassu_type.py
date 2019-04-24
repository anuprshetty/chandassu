import unittest
import os
import re
from src.features.chandassu_type import get_chandassu_type
from src.utils.constant import Constant


class TestChandassuType(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.poems_folder_name = "chandassu_poems"
        cls.poems_folder_path = os.path.join(
            os.path.dirname(__file__), "../", cls.poems_folder_name
        )

    @classmethod
    def tearDownClass(cls):
        pass

    # runs before each test cases
    def setUp(self):
        pass

    # runs after each test cases
    def tearDown(self):
        pass

    def test_get_chandassu_type(self):
        print(f"poems_folder_path: {self.poems_folder_name}\n")

        print(f"sub_folder_paths: ")

        for sub_folder_path_no, (
            sub_folder_path,
            dir_names,
            file_names,
        ) in enumerate(os.walk(self.poems_folder_path), 1):
            sub_folder_relative_path = os.path.relpath(
                sub_folder_path, self.poems_folder_path
            )
            print(f"\n   -> {sub_folder_relative_path}\n")

            for file_name_no, file_name in enumerate(file_names, 1):
                if not file_name.endswith(".txt"):
                    continue

                poem_file_path = os.path.join(sub_folder_path, file_name)
                print(f"       * {file_name}")

                with open(poem_file_path, "r") as poem_fd:
                    poem_file_content = poem_fd.read().strip()
                    poems = re.split(r"\n\s*\n", poem_file_content)

                    for poem_no, poem in enumerate(poems, 1):
                        chandassu_type = get_chandassu_type(poem)
                        actual_chandassu_name = chandassu_type.name()

                        expected_chandassu_name = self.get_expected_chandassu_name(
                            sub_folder_path, file_name
                        )

                        self.assertEqual(actual_chandassu_name, expected_chandassu_name)

                        print(
                            f"           {poem_no}) '{actual_chandassu_name}' ... passed"
                        )

    def get_expected_chandassu_name(self, sub_folder_path, file_name):
        sub_folder_relative_path = os.path.relpath(
            sub_folder_path, self.poems_folder_path
        )
        if sub_folder_relative_path == ".":
            chandassu_hierarchy_names = []
        else:
            chandassu_hierarchy_names = sub_folder_relative_path.split("/")

        chandassu_hierarchy_name = os.path.splitext(file_name)[0]
        chandassu_hierarchy_names.append(chandassu_hierarchy_name)

        expected_chandassu_name = Constant.chandassu_names
        for hierarchy_name in chandassu_hierarchy_names:
            expected_chandassu_name = expected_chandassu_name[hierarchy_name]

        return expected_chandassu_name
