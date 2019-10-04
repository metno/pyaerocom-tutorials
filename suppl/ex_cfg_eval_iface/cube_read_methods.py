#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Additional methods that may be used to compute additional variables when reading
gridded data
"""
from pyaerocom.io.aux_read_cubes import (add_cubes, subtract_cubes, 
                                         compute_angstrom_coeff_cubes)

FUNS = {'add_cubes'         : add_cubes,
        'subtract_cubes'    : subtract_cubes,
        'calc_ae'           : compute_angstrom_coeff_cubes}
