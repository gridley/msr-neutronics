#/usr/bin/env python3
# writes the first version of the MSRE parametric writer
# i.e. treating stuff as perturbations about steady-state

from msreInputWriter import main
import os
import numpy as np

CRpositions = np.linspace(208.0, 23.622, 10)
fuelTemps = np.linspace(459.0+273.0, 2000.0, 10)
modTemps  = np.linspace(459.0+273.0, 2000.0, 10)
