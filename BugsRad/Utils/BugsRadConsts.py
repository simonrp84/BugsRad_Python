#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2020 Simon R Proud
#
# This file is part of python_bugsrad.
#
# python_bugsrad is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# python_bugsrad is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE.  See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# python_bugsrad.  If not, see <http://www.gnu.org/licenses/>.
"""Some useful constants."""
import numpy as np

# Number of InfraRed and ShortWave bands.
n_ir_bands = 12
n_sw_bands = 6

# Physical and mathematical constants
gravity = 9.80665  # m s^-2
cp_dry_air = 1.004e+03  # J kg^-1 K^-1
R_d = 287.0  # J K^-1 kg^-1
R_star = 8.3143e+03  # J K^-1 kmol^-1
sol_const = 1.360e+03  # W m^-2
P_std = 1.01325e+05  # Pa
T_std = 273.15  # K
molar_volume = 2.2421e+4  # cm3-atm
N_av = 6.0221367e23

# Molecular weights in g/mol
MW_dry_air = 28.964
MW_h2o = 18.016
MW_co2 = 44.010
MW_o3 = 48.000
MW_ch4 = 16.042
MW_n2o = 44.016

# Other useful values
epsilon = MW_h2o / MW_dry_air
f_virt = (1. - epsilon)/epsilon
ri = np.array([1.19234e-26, 7.6491e-28, 9.0856e-29,
               1.97266e-29, 6.13005e-30, 2.06966e-30])
