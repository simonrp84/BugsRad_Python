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
"""Compute blackbody emission using Planck function."""

from BugsRad.Utils.BugsRadConsts import n_ir_bands
import numpy as np


planck_coefs = np.array([[-25.889132, 0.75038381, -0.87074567e-02,
                          0.50701144e-04, -0.14856755e-06, 0.17579587e-09],
                         [25.397471, -0.59596460, 0.53117737e-02,
                          -0.21681758e-04, 0.36630792e-07, -0.11541419e-10],
                         [57.891546, -1.4745788, 0.14577775e-01,
                          -0.68637478e-04, 0.14707480e-06, -0.98862337e-10],
                         [21.837317, -0.63194381, 0.71338812e-02,
                          -0.38569394e-04, 0.95685257e-07, -0.76188561e-10],
                         [0.83155466, -0.15281669, 0.31020500e-02,
                          -0.23768837e-04, 0.74605666e-07, -0.67494167e-10],
                         [-19.432674, 0.37744942, -0.22166529e-02,
                          0.11663914e-05, 0.22128830e-07, -0.28943829e-10],
                         [-51.844021, 1.2280373, -0.10600353e-01,
                          0.38135251e-04, -0.45111018e-07, 0.16679671e-10],
                         [-31.210771, 0.85737498, -0.87947387e-02,
                          0.39416747e-04, -0.67469797e-07, 0.43711306e-10],
                         [-5.4417604, 0.28970317, -0.44571665e-02,
                          0.26395273e-04, -0.52111967e-07, 0.37627129e-10],
                         [14.646543, -0.25202253, 0.67234738e-03,
                          0.67552180e-05, -0.19815201e-07, 0.17221281e-10],
                         [12.218584, -0.31591213, 0.26032011e-02,
                          -0.58878366e-05, 0.73276694e-08, -0.38798834e-11],
                         [1.0183416, -0.79710154e-01, 0.13753393e-02,
                          -0.40247214e-05, 0.63186167e-08, -0.41250652e-11]])


def compute_onelayer_emis(temperature, cur_ir_band):
    """Compute the emissivity for a given layer"""
    if type(cur_ir_band) != int:
        raise TypeError("Input band must be an integer")
    if cur_ir_band < 0 or cur_ir_band >= n_ir_bands:
        raise ValueError("IR band number should be between 0 and " + str(n_ir_bands) + '.')
    return planck_coefs[cur_ir_band, 0] + temperature * (
            planck_coefs[cur_ir_band, 1] + temperature * (
                planck_coefs[cur_ir_band, 2] + temperature * (
                    planck_coefs[cur_ir_band, 3] + temperature * (
                        planck_coefs[cur_ir_band, 4] + temperature *
                        planck_coefs[cur_ir_band, 5]))))


def planck_function(n_columns, n_layers, cur_ir_band, surf_tmp, atm_layer_tmp):
    """Calculate blackbody emission in W/m^2."""

    # Temporary array for the interface temperature
    tmp_arr = np.zeros(n_columns)

    bb_emis = np.zeros((n_columns, n_layers))

    # Blackbody emission at top level in the model
    bb_emis[:, 0] = compute_onelayer_emis(atm_layer_tmp[:, 0], cur_ir_band)

    # Blackbody emission at interface levels
    for i_lay in range(2, n_layers):
        tmp_arr[:] = 0.5 * (atm_layer_tmp[:, i_lay - 1] + atm_layer_tmp[:, i_lay])
        bb_emis[:, i_lay] = compute_onelayer_emis(tmp_arr, cur_ir_band)

        # Blackbody emission at the surface
        bb_emis[:, 0] = compute_onelayer_emis(surf_tmp, cur_ir_band)

    return bb_emis
