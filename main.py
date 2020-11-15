from Sniffer import Sniffer

def action(msg):
    print(msg)
    print('-')

"""
Call main() from your program with your callback function as argument
"""
def main(callback = action):
    Sniffer(callback)

if __name__ == "__main__":
    main()