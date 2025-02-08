import time

def test_anim():
    while not KeyboardInterrupt:  # Loop until 'q' is pressed
        print(".  ")
        time.sleep(0.1)
        print(" . ")
        time.sleep(0.1)
        print("  .")
        time.sleep(0.1)
        print(" . ")
        time.sleep(0.1)

if __name__ == "__main__":
    test_anim()