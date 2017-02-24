#!/usr/bin/python
import argparse
import random
import sys


class State:
    A = 'A'
    B = 'B'


class StateManager:
    def __init__(self, state, value):
        self._states = [state]
        self._values = [value]

    def add(self, state, value):
        self._states.append(state)
        self._values.append(value)

    def current(self):
        return self._states[len(self._states) - 1]

    def is_in(self, state):
        return self.current() == state

    def get_values(self):
        return self._values

    def get_states(self):
        return self._states

    def get_pairs(self):
        res = []
        for i in range(0, len(self._states)):
            res.append("{s}:{v}".format(s=self._states[i], v=self._values[i]))
        return res

    def __repr__(self):
        return ', '.join(self.get_pairs())


def check_probability(value, name):
    if value < 0 or value > 1:
        print "'{name}' must be a value from <0, 1>".format(name=name)
        sys.exit(1)


def check_count(value, name):
    if value <= 0:
        print "'{name}' must be a value greater than 0".format(name=name)
        sys.exit(1)


def rand():
    return random.uniform(0, 1)


def main(alpha, beta, count, p=None, dest=None):
    state = StateManager(State.A, 1)

    if p is None:
        mmrp(alpha, beta, count, state)
    else:
        mmbp(alpha, beta, p, count, state)

    values = ' '.join([str(v) for v in state.get_values()])
    if dest is None:
        # print it out
        print values
    else:
        # write to file
        f = open(dest, 'w')
        f.write(values)
        f.close()



def mmrp(alpha, beta, count, state):
    # print 'MMRP'
    for i in range(0, count):
        if state.is_in(State.A):
            if rand() < alpha:
                state.add(State.B, 0)
            else:
                state.add(State.A, 1)
        elif state.is_in(State.B):
            if rand() < beta:
                state.add(State.A, 1)
            else:
                state.add(State.B, 0)


def mmbp(alpha, beta, p, count, state):
    # print 'MMBP'
    for i in range(0, count):
        if state.is_in(State.A):
            if rand() < alpha:
                state.add(State.B, 0)
            else:
                if rand() < p:
                    state.add(State.A, 1)
                else:
                    state.add(State.A, 0)

        elif state.is_in(State.B):
            if rand() < beta:
                if rand() < p:
                    state.add(State.A, 1)
                else:
                    state.add(State.A, 0)
            else:
                state.add(State.B, 0)


###########################################################
# Main
###########################################################
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--alpha', required=True,
                        help="Alpha")
    parser.add_argument('-b', '--beta', required=True,
                        help="Beta")
    parser.add_argument('-p', '--p', required=False,
                        help="Bernoulli p")
    parser.add_argument('-c', '--count', required=True,
                        help="Count of generated values")
    parser.add_argument('-d', '--dest', required=False,
                        help="Destination file")
    args = parser.parse_args()

    # check params
    alpha = float(args.alpha)
    check_probability(alpha, 'alpha')
    beta = float(args.beta)
    check_probability(beta, 'beta')
    p = None
    if args.p is not None:
        p = float(args.p)
        check_probability(p, 'p')
    count = int(args.count)
    check_count(count, 'count')

    # run
    main(alpha=alpha, beta=beta, count=count, p=p, dest=args.dest)
