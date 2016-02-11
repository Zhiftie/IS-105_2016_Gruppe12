#  -*- coding: utf-8-*-

def code():
    """
    LZW
    """
    table = {}
    table[0] = 'NUL'
    table[1] = 'SOH'
    table[2] = 'STX'
    table[3] = 'ETX'
    table[4] = 'EOT'
    table[5] = 'ENQ'
    table[6] = 'ACK'
    table[7] = 'BEL'
    table[8] = 'BS'
    table[9] = 'TAB'
    table[10] = 'LF'
    table[11] = 'VT'
    table[12] = 'FF'
    table[13] = 'CR'
    table[14] = 'SO'
    table[15] = 'SI'
    table[16] = 'DLE'
    table[17] = 'DC1'
    table[18] = 'DC2'
    table[19] = 'DC3'
    table[20] = 'DC4'
    table[21] = 'NAK'
    table[22] = 'SYN'
    table[23] = 'ETB'
    table[24] = 'CAN'
    table[25] = 'EM'
    table[26] = 'SUB'
    table[27] = 'ESC'
    table[28] = 'FS'
    table[29] = 'GS'
    table[30] = 'RS'
    table[31] = 'US'
    table[32] = 'Space'
    table[33] = '!'
    table[34] = '"'
    table[35] = '#'
    table[36] = '$'
    table[37] = '%'
    table[38] = '&'
    table[39] = "'"
    table[40] = '('
    table[41] = ')'
    table[42] = '*'
    table[43] = '+'
    table[44] = ','
    table[45] = '-'
    table[46] = '.'
    table[47] = '/'
    table[48] = '0'
    table[49] = '1'
    table[50] = '2'
    table[51] = '3'
    table[52] = '4'
    table[51] = '5'
    table[52] = '6'
    table[53] = '7'
    table[54] = '8'
    table[55] = '9'
    table[56] = ':'
    table[57] = ';'
    table[58] = '<'
    table[59] = '='
    table[60] = '>'
    table[61] = '?'
    table[64] = '@'
    table[65] = 'A'
    table[66] = 'B'
    table[67] = 'C'
    table[68] = 'D'
    table[69] = 'E'
    table[70] = 'F'
    table[71] = 'G'
    table[72] = 'H'
    table[73] = 'I'
    table[74] = 'J'
    table[75] = 'K'
    table[76] = 'L'
    table[77] = 'M'
    table[78] = 'N'
    table[79] = 'O'
    table[80] = 'P'
    table[81] = 'Q'
    table[82] = 'R'
    table[83] = 'S'
    table[84] = 'T'
    table[85] = 'U'
    table[86] = 'V'
    table[87] = 'W'
    table[88] = 'X'
    table[89] = 'Y'
    table[90] = 'Z'
    table[91] = '['
    #table[92] = ' \ '
    table[93] = ']'
    table[94] = '^'
    table[95] = '_'
    table[96] = '`'
    table[97] = 'a'
    table[98] = 'b'
    table[99] = 'c'
    table[100] = 'd'
    table[101] = 'e'
    table[102] = 'f'
    table[103] = 'g'
    table[104] = 'h'
    table[105] = 'i'
    table[106] = 'j'
    table[107] = 'k'
    table[108] = 'l'
    table[109] = 'm'
    table[110] = 'n'
    table[111] = 'o'
    table[112] = 'p'
    table[113] = 'q'
    table[114] = 'r'
    table[115] = 's'
    table[116] = 't'
    table[117] = 'u'
    table[118] = 'v'
    table[119] = 'w'
    table[120] = 'x'
    table[121] = 'y'
    table[122] = 'z'
    table[123] = '{'
    table[124] = '|'
    table[125] = '}'
    table[126] = '~'
    table[127] = 'DEL'
    return table
table = code()

def encode(message): 
    table = code()
    string = ""
    code_for_string = []
    for byte in message:
        symbol = byte
        if (string + symbol) in table.values():
            string = string + symbol
#leser tekst som skal komprimeres i bytes. 
#Sjekker også om symbolet og stringen som leses allerede finnes i dictionary. 
        else:
            for k,v in table.iteritems(): 
                if v == string:
                    code_for_string.append(k) #Hvis det finnes en tilsvarende value i dictionary som er lik symbol vil det lages en ny liste.
            table[max(table.keys())+1] = string + symbol 
            string = symbol
    for k,v in table.iteritems():
        if v == string:
            code_for_string.append(k)
    print table
    return code_for_string


def test():
    test_message = "hahdsahdahdhadhdshdhahdahdhadhadhdhadh hasdas  hdshdash dahsdhas dhasdhahdas hdashdas dashdhas dhashdas hashd hasdhasd hasdhas djasdasjd ajasjdjas djadas dasdas dkasdlk dslfsd fdffd l"
    print encode(test_message)
test()


if __name__ == '__main__':
    unittest.main()

        
