from problem.problems import des_to_hex, des_to_oct

num_list = [0, 1, 2, 6, 8, 11, 15, 20, 22]
def test_des_to_hex():
    print("Test des_to_hex")
    for num in num_list:
        print(f"{num} -> {des_to_hex(num)}")

def test_des_to_oct():
    print("Test des_to_oct")
    for num in num_list:
        print(f"{num} -> {des_to_oct(num)}")

if __name__ == "__main__":
    test_des_to_hex()
    test_des_to_oct()