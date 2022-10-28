class Parser:
    """
    Parser
    >>> string = "D= M + 1 ; JGT // this is comment"
    >>> p = Parser()
    >>> p.parser(string)
    >>> p.comp()
    'M+1'
    >>> p.dest()
    'D'
    >>> p.jump()
    'JGT'
    >>> string = "D=M; JEQ // this is comment"
    >>> p.parser(string)
    >>> p.comp()
    'M'
    >>> p.dest()
    'D'
    >>> p.jump()
    'JEQ'
    >>> string = "0; JEQ // this is comment"
    >>> p.parser(string)
    >>> p.comp()
    '0'
    >>> p.dest()
    ''
    >>> p.jump()
    'JEQ'
    >>> del(p)
    """

    def __init__(self):
        self.__destt = ""
        self.__compp = ""
        self.__jumpp = ""
        self.__line_counts = 0
        self.symbol_table = {
            "R0": 0,
            "R1": 1,
            "R2": 2,
            "R3": 3,
            "R4": 4,
            "R5": 5,
            "R6": 6,
            "R7": 7,
            "R8": 8,
            "R9": 9,
            "R10": 10,
            "R11": 11,
            "R12": 12,
            "R13": 13,
            "R14": 14,
            "R15": 15,
            "SCREEN": 16384,
            "KBD": 24576,
            "SP": 0,
            "LCL": 1,
            "ARG": 2,
            "THIS": 3,
            "THAT": 4,
        }
        self.__n = 16

    def parser(self, str, times):
        self.__destt = ""
        self.__compp = ""
        self.__jumpp = ""
        self.ainstrution = ""
        str = self.__rm_whitespace_comments(str)
        if str == "":
            self.ainstrution = "blankline"
            return
        if times == 1:
            if str[0] == "(":
                self.symbol_table[str[1:-1]] = self.__line_counts
                self.ainstrution = "label"
            elif str[0] == "@":
                self.ainstrution = str
                self.__line_counts += 1
            else:
                if str.find("=") != -1:
                    self.__destt = str[: str.find("=")]
                    str = str[str.find("=") + 1 :]
                if str.find(";") != -1:
                    self.__compp = str[: str.find(";")]
                    str = str[str.find(";") + 1 :]
                    self.__jumpp = str[:]
                else:
                    self.__compp = str[:]
                self.__line_counts += 1
        elif times == 2:
            if str[0] == "@":
                if str[1:].isdigit():
                    self.ainstrution = f"{str}"
                else:
                    value = self.symbol_table.get(str[1:])
                    if value == None:
                        self.symbol_table[str[1:]] = self.__n
                        self.__n += 1
                    value = self.symbol_table.get(str[1:])
                    self.ainstrution = f"@{value}"

    def __rm_whitespace_comments(self, str):
        has_comment = str.find("/")
        if has_comment != -1:
            str = str[: 0 if has_comment == 0 else has_comment - 1]

        # remove all whitespace
        str = "".join(str.split())
        return str

    def comp(self):
        return self.__compp

    def dest(self):
        return self.__destt

    def jump(self):
        return self.__jumpp
