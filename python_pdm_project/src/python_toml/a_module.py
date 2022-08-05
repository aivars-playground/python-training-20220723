from .b_module import main_function as b_module_main_function


def main_function():
    print("1: toml_base package / a_module / call main_function")


def call_b_module():
    print("2: toml_base package / a_module / call b_module")
    b_module_main_function()
