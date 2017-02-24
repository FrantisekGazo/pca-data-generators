#!/usr/bin/python

from mm import main as mm


def main():
    count = 1000
    ps = [.1, .3, .5, .7, .9]

    for a in ps:
        for b in ps:
            dest = 'mmrp_a{a}_b{b}'.format(a=a, b=b)
            mm(alpha=a, beta=b, count=count, dest=dest)

            for p in ps:
                dest = 'mmbp_a{a}_b{b}_p{p}'.format(a=a, b=b, p=p)
                mm(alpha=a, beta=b, p=p, count=count, dest=dest)


if __name__ == '__main__':
    main()
