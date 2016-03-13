"""
Source: https://gist.github.com/sfcgeorge/0e4d2977ebcdd050927c

Mer spennende, mer lærerutbytte, selvlagd kode finnes i RiverCrossing mappen. 

"""

class FCG:
    M, F, C, G = 0, 1, 2, 3 #Man, fox, chicken, GRAIN

    start, goal = [[M, F, C, G], [], []]  ,  [[], [], [M, F, C, G]]

    def __init__(self, state = None):
        self.state = state or self.start[:]

    def won(self): return self.state == self.goal

    def successors(self):
        for move in [[0, 1], [1, 0], [1, 2], [2, 1]]:
            for possibility in self.move_source_dest(*move):
                if not self.invalid(possibility): yield FCG(possibility)

    def move_source_dest(self, s, d):
        source_orig = self.state[s][:]
        if FCG.M in source_orig: # move one
            state = self.state[:]
            state[s], state[d] = self.state[s][:], self.state[d][:]
            state[s].remove(FCG.M)
            state[d].insert(0, FCG.M)
            yield state
        if FCG.M in source_orig and len(source_orig) >= 2: # move two
            source_orig.remove(FCG.M)
            for i in range(len(source_orig)):
                state = self.state[:]
                state[s], state[d] = source_orig[:], self.state[d][:]
                state[d] += [FCG.M, state[s].pop(i)]
                state[d].sort()
                yield state

    def invalid(self, s):
        # boat has two max
        if len(s[1]) > 2: return True
        for i in range(3):
            # goat must not be left alone with cabbage
            if FCG.C in s[i] and FCG.G in s[i] and not FCG.M in s[i]:
                return True
            # wolf must not be left alone with goat
            if FCG.F in s[i] and FCG.C in s[i] and not FCG.M in s[i]:
                return True


class Run:
    history, won = [], False

    def go(self, problem):
        self.next(problem, 0)
        return self.history

    def next(self, problem, depth):
        self.history.append(problem.state)
        if problem.won():
            self.won = True
        else:
            for s in problem.successors():
                if not self.won:
                    self.history = self.history[:depth+1]
                    if not s.state in self.history: self.next(s, depth+1)


#for s in Run().go(FCG()): print s


class FCGPrinter:
    def __init__(self, n):
        with open(n) as f: self.symbols = f.read().split('\n\n')
        for i in range(len(self.symbols)):
            self.symbols[i] = self.symbols[i].split('\n')
            self.symbols[i].reverse()

    def width(self, symbol):
        return max(len(s) for s in symbol)

    def total_width(self):
        return sum(self.width(s) +2 for s in self.symbols)

    def max_height(self):
        return max(len(s) for s in self.symbols)

    def print_state(self, state):
        lines = []
        for i in range(-1, self.max_height()+1): # each row of ascii prints out
            row = ""
            for p in range(len(state)): # position of the state (bank, boat...)
                pos = ""
                g = '-' if (i == -1 or i == self.max_height()) and (p != 0 and p != len(state)-1) else ' '
                for sym in state[p]: # symbol in the position (wolf, goat...)
                    s = self.symbols[sym]
                    pos += g+(s[i] if s[i:i+1] else '').ljust(self.width(s),g)+g
                row += g * (self.total_width() - len(pos)) + pos
                br = '/' if i == 0 else ('\\' if i == self.max_height()-1 else ('~' if i == -1 or i == self.max_height() else '|'))
                bl = '\\' if i == 0 else ('/' if i == self.max_height()-1 else ('~' if i == -1 or i == self.max_height() else '|'))
                if p == len(state)-2: row += br + "~("
                if p == 0: row += ")~" + bl
            lines.insert(0, row)
        for line in lines: print line


printer = FCGPrinter('fcg_ascii.txt')
for s in Run().go(FCG()): printer.print_state(s)