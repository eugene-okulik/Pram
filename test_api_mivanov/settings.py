from os import path
BASE_URL = "http://167.172.172.115:52353/"
FOLDER_TEST_DATA = "test_data"

current_file = path.realpath(__file__)
current_directory = path.dirname(current_file)

TEST_DATA_DIRECTORY = path.join(current_directory, FOLDER_TEST_DATA)
