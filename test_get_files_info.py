from functions.get_files_info import get_files_info

def test_get_files_info():
    print("Result for current directory:")
    print(get_files_info("calculator","."))
    print("Result for 'pkg' director:")
    print(get_files_info("calculator","pkg"))
    print("Result for '/bin' directory:")
    print(get_files_info("calculator", "/bin"))
    print("Result for '../' directory:")
    print(get_files_info("calculator", "../"))

if __name__ == "__main__":
    test_get_files_info()