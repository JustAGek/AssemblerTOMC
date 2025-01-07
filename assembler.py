class Assembler(object):
    def __init__(self, asmpath='', mripath='', rripath='', ioipath='') -> None:
        super().__init__()
        self.__address_symbol_table = {}
        self.__bin = {}
        if asmpath:
            self.read_code(asmpath)
        self.__mri_table = self.__load_table(mripath) if mripath else {}
        self.__rri_table = self.__load_table(rripath) if rripath else {}
        self.__ioi_table = self.__load_table(ioipath) if ioipath else {}

    def read_code(self, path: str):
        assert path.endswith('.asm') or path.endswith('.S')
        self.__asmfile = path.split('/')[-1]
        with open(path, 'r') as f:
            self.__asm = [s.rstrip().lower().split() for s in f.readlines()]

    def assemble(self, inp='') -> dict:
        assert self.__asm or inp
        if inp:
            assert inp.endswith('.asm') or inp.endswith('.S')
        if not self.__asm:
            self.read_code(inp)
        self.__rm_comments()
        self.__first_pass()
        self.__second_pass()
        return self.__bin

    def __load_table(self, path) -> dict:
        with open(path, 'r') as f:
            t = [s.rstrip().lower().split() for s in f.readlines()]
        return {opcode: binary for opcode, binary in t}

    def __is_label(self, string) -> bool:
        return string.endswith(',')

    def __rm_comments(self) -> None:
        for i in range(len(self.__asm)):
            for j in range(len(self.__asm[i])):
                if self.__asm[i][j].startswith('/'):
                    del self.__asm[i][j:]
                    break

    def __format2bin(self, num: str, numformat: str, format_bits: int) -> str:
        if numformat == "dec":
            val = int(num)
            if val < 0:
                return bin((1 << format_bits) + val)[-format_bits:]
            return "{:0{}b}".format(val, format_bits)
        elif numformat == "hex":
            return "{:0{}b}".format(int(num, 16), format_bits)
        else:
            raise Exception("format2bin: Unsupported format provided.")

    def __first_pass(self) -> None:
        lc = 0
        for i in self.__asm:
            if i[0] == "org":
                lc = int(i[1], 16)
                continue
            elif i[0] == "end":
                break
            elif i[0][-1] == ",":
                self.__address_symbol_table[i[0]] = self.__format2bin(str(lc), "dec", 12)
                if len(i) > 1 and (i[1] == "dec" or i[1] == "hex"):
                    lc += 1
            else:
                lc += 1

    def __second_pass(self) -> None:
        lc = 0
        for i in self.__asm:
            if i[0][-1] == ",":
                i = i[1:]
            if i[0] == "org":
                lc = int(i[1], 16)
                continue
            elif i[0] == "end":
                break
            elif i[0] in ("dec", "hex"):
                x = self.__format2bin(i[1], i[0], 16)
                self.__bin[self.__format2bin(str(lc), "dec", 12)] = x
            elif i[0] in self.__mri_table:
                opcode = self.__mri_table[i[0]]
                if i[1][-1] == ',':
                    x = self.__address_symbol_table[i[1]]
                else:
                    x = self.__address_symbol_table[i[1] + ","]
                instruction = "0" + opcode + x
                self.__bin[self.__format2bin(str(lc), "dec", 12)] = instruction
            elif i[0] in self.__rri_table:
                self.__bin[self.__format2bin(str(lc), "dec", 12)] = self.__rri_table[i[0]]
            elif i[0] in self.__ioi_table:
                self.__bin[self.__format2bin(str(lc), "dec", 12)] = self.__ioi_table[i[0]]
            else:
                print(f"Error: Invalid instruction '{i[0]}' at line {lc}")
            lc += 1
