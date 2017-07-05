#!/usr/bin/env python3
# MSRE State Point sss2 input generator
# generates serpent input that determines MSRE group constants as functions
# of temperature.
#
# Current approach is treating all GC interpolation as a perturbation from steady-state

import numpy as np
import os

def main(fuelTemp, modTemp, CR1pos, CR2pos, CR3pos, groupStruct):

    # check input
    if groupStruct not in [1,2,3]:
        print(" Use option 1, 2, or 3. 1,2 are G=4. 3 is G=13.")
        raise Exception("This isn't one the group structures from Cole's PhD")

    # make group structure strings
    opt1 = "set nfg 4 7.3000e-7 2.9023e-5 9.1188e-3"
    opt2 = "set nfg 4 1.8554e-6 2.9023e-5 9.1188e-3"
    opt3 = [2.0000e+1,
            1.4739e-4,
            4.5000e-7,
            2.9074e-7,
            2.5103e-7,
            2.2769e-7,
            1.8443e-7,
            1.4572e-7,
            1.1157e-7,
            1.2396e-8,
            3.5500e-8,
            1.0000e-12,
            5.6922e-8,
            8.1968e-8, ]
    opt3.sort()
    opt3 = "".join(["{} ".format(ener) for ener in opt3])
    opt3 = "set nfg 13 " + opt3
    optdict = {1: opt1, 2:opt2, 3:opt3}

    # read in the templates:
    with open('templateMSRE.txt') as fh:
        msreTemplate = "".join(fh.readlines())
    with open('templateMaterials.txt') as fh:
        materialTemplate = "".join(fh.readlines())

    # format the templates
    msreTemplate.format(**locals())
    materialTemplate.format(**locals())

    # append group structure
    msreTemplate += '\n' + optdict[groupStruct] + "\n"

    print(materialTemplate)

if __name__ == '__main__':
    # test case
    import sys
    args = [int(arg) for arg in sys.argv[1:]]
    main(*args)




        
