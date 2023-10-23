import os

project_root_path = os.path.join(os.path.dirname(__file__), "..\\")
folder_data_file_path = os.path.join(os.path.dirname(__file__), "..\\TestData\\")
debug = False
globalWaitTime = 10
enableScreeshot = "true"
browser = "chrome"
headless_execution = False
driver_scope = "function"  # "class" / "function"
url = "https://www.saucedemo.com/"