#-*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

def slow():
    line1 = plt.plot([0.033776, 0.033359, 0.033358], label = 'Thomas')
    line2 = plt.plot([0.021271, 0.211480, 2.145288], label = 'Sindre')
    line3 = plt.plot([0.002965, 0.027365, 0.276646], label = 'Lene')
    line4 = plt.plot([0.060384, 0.060384, 0.606931], label = 'Robert')
    line5 = plt.plot([0.034457, 0.250204, 1.802864], label = 'Guro')
    line6 = plt.plot([0.030948, 0.030948, 3.076967], label = 'Martin')
    plt.ylabel('Tid i sekunder(Timeit med number=100')
    plt.xlabel('Antall elementer i listen')
    plt.title('ICA05: Sammenligning av search_slow')
    plt.legend(bbox_to_anchor = (0.05, 0.95), loc = 2, borderaxespad = 0.)
    plt.grid(True)
    plt.show()
    
def fast():
    line1 = plt.plot([0.003508, 0.015614, 0.001385], label = 'Thomas')
    line2 = plt.plot([0.006075, 0.012783, 0.1154730], label = 'Sindre')
    line3 = plt.plot([0.000644, 0.003976, 0.029681], label = 'Lene')
    line4 = plt.plot([0.000139, 0.002894, 0.007416], label = 'Robert')
    line5 = plt.plot([0.004798, 0.087521, 0.306595], label = 'Guro')
    line6 = plt.plot([0.005479, 0.005479, 0.128483], label = 'Martin')
    plt.ylabel('Tid i sekunder(Timeit med number=100')
    plt.xlabel('Antall elementer i listen')
    plt.title('ICA05: Sammenligning av search_fast')
    plt.legend(bbox_to_anchor = (0.05, 0.95), loc = 2, borderaxespad = 0.)
    plt.grid(True)
    plt.show()

def sammenligne():
    line1 = plt.plot([0.02186, 0.192866, 1.323675666], label = 'slow')
    line2 = plt.plot([0.0034405, 0.02137783333, 0.09817216666], label = 'fast')
    plt.ylabel('Tid i sekunder(Timeit med number=100')
    plt.xlabel('Antall elementer i listen')
    plt.title('ICA05: Gjennomsnitt av fast og slow')
    plt.legend(bbox_to_anchor = (0.05, 0.95), loc = 2, borderaxespad = 0.)
    plt.grid(True)
    plt.show()