#!/usr/bin/python

from mm import main as mm


def main():
    count = 1000
    s = 8
    ps = [.1, .3, .5, .7, .9]

    for p in ps:
        dest = 'mmrp_a{a}_b{b}.txt'.format(a=p, b=p)
        mm(alpha=p, beta=p, count=count, sample_size=s, dest=dest)

    # for a in ps:
    #     for b in ps:
    #         dest = 'mmrp_a{a}_b{b}.txt'.format(a=a, b=b)
    #         mm(alpha=a, beta=b, count=count, sample_size=s, dest=dest)
    #
    #         for p in ps:
    #             dest = 'mmbp_a{a}_b{b}_p{p}.txt'.format(a=a, b=b, p=p)
    #             mm(alpha=a, beta=b, sample_size=s, p=p, count=count, dest=dest)


if __name__ == '__main__':
    main()
