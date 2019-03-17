import sys
import Server


def main():
    if len(sys.argv) != 3:
        return print("Вы не ввели нужные аргументы.")

    input_name = sys.argv[1]
    output_name = sys.argv[2]

    c = Server.init()
    Server.input(c, input_name)
    Server.out(c, output_name)
    Server.clear(c, output_name)


if __name__ == '__main__':
    print("START")
    main()
    print("STOP")