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
"""Compute optical depth and single scattering albedo due to Rayleigh scattering.

Based on: Kurucz, 1995
Updated using: Anderson et al., 2000
"""

from BugsRad.Utils.BugsRadConsts import N_av, gravity, MW_dry_air, ri
import numpy as np


def compute_rayleigh(n_columns, n_layers, spectral_interval_idx, pressure_levels):
    """Compute the single scattering albedo and optical depth."""

    # Set up output arrays
    rayleigh_ssa = np.ones((n_columns, n_layers))
    rayleigh_opd = np.zeros((n_columns, n_layers))

    # The factor of ten here changes units from g/cm to kg/m and accounts for
    # the pressure being given in hPa
    fact = ri[spectral_interval_idx] * N_av / (MW_dry_air * gravity) * 10.

    # Top level
    rayleigh_opd[:, 0] = pressure_levels[:, 1] * fact

    # Now loop over remaining levels
    for i_lev in range(1, n_layers-1):
        rayleigh_opd[:, i_lev] = (pressure_levels[:, i_lev+1] -
                                  pressure_levels[:, i_lev]) * fact

    return rayleigh_ssa, rayleigh_opd
