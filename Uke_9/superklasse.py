class SM:
    def start(self):
        self.state = self.startState
        
#Once it has started, we can ask it to take a step, using the step method, which, given an input,
#computes the output and updates the internal state of the machine, and returns the output value.

    def step(self, inp):
        (s, o) = self.getNextValues(self.state, inp)
        self.state = s
        return o
    
#To run a machine on a whole sequence of input values, we can use the transduce method, which
#will return the sequence of output values that results from feeding the elements of the list inputs
#into the machine in order. 

    def transduce(self, inputs):
        self.start()
        return [self.step(inp) for inp in inputs]
    
    
    

