import sys
import Server


def main():
    if len(sys.argv) != 3:
        return print("You have not entered necessary arguments.")

    input_name = sys.argv[1]
    output_name = sys.argv[2]

    c = Server.init()
    if Server.input(c, input_name) != 0:
        if Server.out(c, output_name) != 0:
            Server.clear(c, output_name)


if __name__ == '__main__':
    print("START")
    main()
    print("STOP")