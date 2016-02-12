table = {}
def code():
    '''
    Implements an initial table for LZW algorithm 
    '''
    table = {}
    table[1] = 't'
    table[2] = 'o'
    table[3] = 'b'
    table[4] = 'e'
    table[5] = 'r'
    table[6] = 'n'
    table[7] = ' '
    return table
table = code()
def rev_table():
    """
    Bytter om keys og values i table og legger resultatet inn i en ny dictionary
    """
    rev_table = {v : k for k, v in table.items()}
    return rev_table
inv_table= rev_table()
print inv_table