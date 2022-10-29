class Code:
    """
    ENCODE the components
    >>> string = "D= M + 1 ; JGT // this is comment"
    >>> p = Parser()
    >>> p.parser(string)
    >>> c = Code()
    >>> c.comp(p)
    '1110111'
    >>> c.dest(p)
    '010'
    >>> c.jump(p)
    '001'
    >>> string = "0; JEQ // this is comment"
    >>> p.parser(string)
    >>> c.comp(p)
    '0101010'
    >>> c.dest(p)
    '000'
    >>> c.jump(p)
    '010'
    """

    def __init__(self):
        self.__encode_comp = ""
        self.__encode_dest = ""
        self.__encode_jump = ""

    def comp(self, p):
        comp_table = {
            "0": "0101010",
            "1": "0111111",
            "-1": "0111010",
            "D": "0001100",
            "A": "0110000",
            "M": "1110000",
            "!D": "0001101",
            "!A": "0110001",
            "!M": "1110001",
            "-D": "0001111",
            "-A": "0110011",
            "-M": "1110011",
            "D+1": "0011111",
            "A+1": "0110111",
            "M+1": "1110111",
            "D-1": "0001110",
            "A-1": "0110010",
            "M-1": "1110010",
            "D+A": "0000010",
            "D+M": "1000010",
            "D-A": "0010011",
            "D-M": "1010011",
            "A-D": "0000111",
            "M-D": "1000111",
            "D&A": "0000000",
            "D&M": "1000000",
            "D|A": "0010101",
            "D|M": "1010101",
        }

        self.__encode_comp = comp_table.get(p.comp())
        return self.__encode_comp

    def dest(self, p):
        dest_table = {
            "": "000",
            "M": "001",
            "D": "010",
            "MD": "011",
            "DM": "011",
            "A": "100",
            "AM": "101",
            "AD": "110",
            "AMD": "111",
        }
        self.__encode_dest = dest_table.get(p.dest())
        return self.__encode_dest

    def jump(self, p):
        jump_table = {
            "": "000",
            "JGT": "001",
            "JEQ": "010",
            "JGE": "011",
            "JLT": "100",
            "JNE": "101",
            "JLE": "110",
            "JMP": "111",
        }
        self.__encode_jump = jump_table.get(p.jump())
        return self.__encode_jump
