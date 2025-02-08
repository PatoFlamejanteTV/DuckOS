import time

def test_anim():
    while not KeyboardInterrupt:
        print(".  ")
        time.sleep(0.1)
        print(" . ")
        time.sleep(0.1)
        print("  .")
        time.sleep(0.1)
        print(" . ")
        time.sleep(0.1)

def test_anim2():
    while not KeyboardInterrupt:
        print("|")
        time.sleep(0.1)
        print("/")
        time.sleep(0.1)
        print("-")
        time.sleep(0.1)
        print("\\")
        time.sleep(0.1)

if __name__ == "__main__":
    test_anim()