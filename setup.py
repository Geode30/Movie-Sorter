from cx_Freeze import setup, Executable

setup(
    name = "Sort Movies",
    version = "0.1",
    description = "Create folders based on movies' name then move them to their own folders",
    executables = [Executable("main.py")]
)
