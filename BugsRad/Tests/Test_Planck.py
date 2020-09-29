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

from BugsRad.Utils import Planck
import numpy as np
import unittest


class PlanckTests(unittest.TestCase):
    """Test functions for calculating blackbody emissivity."""
    def test_onelayer_errors(self):
        """Check that the emissivity calc raises correct errors."""

        # Out of range (0-11) bands
        with self.assertRaises(ValueError):
            Planck.compute_onelayer_emis(1., -1)
        with self.assertRaises(ValueError):
            Planck.compute_onelayer_emis(1., 14)

        # Band as a float
        with self.assertRaises(TypeError):
            Planck.compute_onelayer_emis(1., 5.)
        # Band as a list
        with self.assertRaises(TypeError):
            Planck.compute_onelayer_emis(1., [5, 10])

    def test_onelayer_calc(self):
        """Emissivity calculation on one layer."""

        # Set up some variables for the computation
        single_band = 5
        single_temp = 273.1
        multi_temp = np.array([273.1, 280.1, 250.5, 235.6, 221.2, 203.1, 240.6])

        # Check calculation works with single band + single temperature
        self.assertAlmostEqual(Planck.compute_onelayer_emis(single_temp, single_band),
                               21.20632162645144)

        # Check calculation works with single band + multiple temperature
        out_emis = np.array([21.20632163, 24.32141717, 12.94241574,
                             8.87748245, 5.87418111, 3.213468, 10.12735758])
        np.testing.assert_allclose(Planck.compute_onelayer_emis(multi_temp, single_band),
                                   out_emis)


if __name__ == '__main__':
    unittest.main()
