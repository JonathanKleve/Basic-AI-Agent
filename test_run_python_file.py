from functions.run_python_file import run_python_file

def test_run_python_file():
    result = run_python_file("calculator", "main.py")
    print(f"main.py result: {result}")
    result = run_python_file("calculator", "main.py", ["3 + 5"])
    print(f"main.py 3 + 5 result: {result}")
    result = run_python_file("calculator", "tests.py")
    print(f"tests.py result: {result}")
    result = run_python_file("calculator", "../main.py")
    print(f"../main.py result: {result}")
    result = run_python_file("calculator", "nonexistent.py")
    print(f"nonexistent.py result: {result}")
    result = run_python_file("calculator", "lorem.txt")
    print(f"lorem.txt result: {result}")

if __name__ == "__main__":
    test_run_python_file()