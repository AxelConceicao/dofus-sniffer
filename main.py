from Sniffer import Sniffer

def action(id, msg):
    print(msg)
    print('-')

"""
Call main() from your program with your callback function as argument
"""
def main(callback = action):
    Sniffer().run(callback)

if __name__ == "__main__":
    main()