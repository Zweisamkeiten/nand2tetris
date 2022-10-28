import os
import sys
from parser import Parser

from encode import Code

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 assembler xxx.asm")
    try:
        fp = open(sys.argv[1], mode="r")
        file_to_write = str(sys.argv[1]).split(".")[0] + ".tmp"
        fw = open(file_to_write, mode="w")
        times = 1
        p = Parser()
        while True:
            line = fp.readline()
            if not line:
                break
            p.parser(line, times)
            if p.ainstrution == "":
                c = Code()
                encode_str = "111" + str(c.comp(p)) + str(c.dest(p)) + str(c.jump(p))
                fw.write(encode_str + "\n")
            else:
                if p.ainstrution[0] == "@":
                    fw.write(f"{p.ainstrution}\n")

        fw.close()
        fp.close()

        fp = open(str(sys.argv[1]).split(".")[0] + ".tmp", mode="r")
        file_to_write = str(sys.argv[1]).split(".")[0] + ".hack"
        fw = open(file_to_write, mode="w")
        times = 2
        while True:
            line = fp.readline()
            if not line:
                break
            p.parser(line, times)
            if p.ainstrution == "":
                fw.write(line)
            else:
                string = "{0:b}".format(int(p.ainstrution[1:])).zfill(16) + "\n"
                fw.write(string)
        fw.close()
        fp.close()

        os.remove(sys.argv[1].split(".")[0] + ".tmp")

    except OSError as e:
        raise e
