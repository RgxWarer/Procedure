import sys
import Server


def main():
    if len(sys.argv) != 3:
        return print("You have not entered necessary arguments.")

    input_name = sys.argv[1]
    output_name = sys.argv[2]

    c = Server.Init()
    if Server.Input(c, input_name) != 0:
        open(output_name, 'w').close()
        if Server.Out(c, output_name) != 0:
            Server.Sort(c)
            Server.Out(c, output_name)
            Server.Out_Filter(c, output_name)
            Server.Clear(c, output_name)


if __name__ == '__main__':
    print("START")
    main()
    print("STOP")

