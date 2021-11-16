#!/usr/bin/env python3

# Copyright © 2021 Helmholtz Centre Potsdam GFZ German Research Centre for Geosciences, Potsdam, Germany
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.

"""
Tests for the command line execution.
"""

import os
import subprocess
import unittest

import geopandas as gpd


class TestCmdExecution(unittest.TestCase):
    """
    Test case for the command line execution.
    """

    def test_in_germany(self):
        """
        Runs the test with a bounding box for chile.
        Must not contain results.
        """

        current_dir = os.path.dirname(os.path.abspath(__file__))

        path_to_assetmaster = os.path.join(current_dir, "assetmaster.py")

        lonmin = 50.0
        lonmax = 55.0
        latmin = 11.0
        latmax = 15.0
        schema = "SARA_v1.0"
        assettype = "res"
        querymode = "intersects"
        model = "ValpCVSaraDownscaled"

        subprocess.run(
            [
                "python3",
                path_to_assetmaster,
                str(lonmin),
                str(lonmax),
                str(latmin),
                str(latmax),
                schema,
                assettype,
                querymode,
                model,
            ],
            check=True,
        )

        path_to_output_file = os.path.join(
            current_dir,
            "output",
            "query_output.geojson",
        )

        output = gpd.read_file(path_to_output_file)

        self.assertEqual(0, len(output))

    def test_in_peru(self):
        """
        Runs the test with a bounding box for peru.
        Must contain results.
        """

        current_dir = os.path.dirname(os.path.abspath(__file__))

        path_to_assetmaster = os.path.join(current_dir, "assetmaster.py")

        lonmin = -84.99
        lonmax = -67.63
        latmin = -18.81
        latmax = -3.33
        schema = "SARA_v1.0"
        assettype = "res"
        querymode = "intersects"
        model = "LimaCVT1_PD70_TI30_5000"

        subprocess.run(
            [
                "python3",
                path_to_assetmaster,
                str(lonmin),
                str(lonmax),
                str(latmin),
                str(latmax),
                schema,
                assettype,
                querymode,
                model,
            ],
            check=True,
        )

        path_to_output_file = os.path.join(
            current_dir,
            "output",
            "query_output.geojson",
        )

        output = gpd.read_file(path_to_output_file)

        self.assertLess(0, len(output))

    def test_in_chile(self):
        """
        Runs the test with a bounding box for chile.
        Must contain results.
        """

        current_dir = os.path.dirname(os.path.abspath(__file__))

        path_to_assetmaster = os.path.join(current_dir, "assetmaster.py")

        lonmin = -71.8
        lonmax = -71.4
        latmin = -33.2
        latmax = -33.0
        schema = "SARA_v1.0"
        assettype = "res"
        querymode = "intersects"
        model = "ValpCVTBayesian"

        subprocess.run(
            [
                "python3",
                path_to_assetmaster,
                str(lonmin),
                str(lonmax),
                str(latmin),
                str(latmax),
                schema,
                assettype,
                querymode,
                model,
            ],
            check=True,
        )

        path_to_output_file = os.path.join(
            current_dir,
            "output",
            "query_output.geojson",
        )

        output = gpd.read_file(path_to_output_file)

        self.assertLess(0, len(output))

    def test_in_ecuador_torres(self):
        """
        Runs the test with a bounding box for ecuador (torres).
        Must contain results.
        """

        current_dir = os.path.dirname(os.path.abspath(__file__))

        path_to_assetmaster = os.path.join(current_dir, "assetmaster.py")

        lonmin = -78.85
        lonmax = -78.43
        latmin = -1.05
        latmax = -0.62
        schema = "Torres_Corredor_et_al_2017"
        assettype = "res"
        querymode = "intersects"
        model = "LatacungaRuralAreas"

        subprocess.run(
            [
                "python3",
                path_to_assetmaster,
                str(lonmin),
                str(lonmax),
                str(latmin),
                str(latmax),
                schema,
                assettype,
                querymode,
                model,
            ],
            check=True,
        )

        path_to_output_file = os.path.join(
            current_dir,
            "output",
            "query_output.geojson",
        )

        output = gpd.read_file(path_to_output_file)

        self.assertLess(0, len(output))

    def test_in_ecuador_mavrouli(self):
        """
        Runs the test with a bounding box for ecuador (mavrouli).
        Must contain results.
        """

        current_dir = os.path.dirname(os.path.abspath(__file__))

        path_to_assetmaster = os.path.join(current_dir, "assetmaster.py")

        lonmin = -78.85
        lonmax = -78.43
        latmin = -1.05
        latmax = -0.62
        schema = "Mavrouli_et_al_2014"
        assettype = "res"
        querymode = "intersects"
        model = "LatacungaRuralAreas"

        subprocess.run(
            [
                "python3",
                path_to_assetmaster,
                str(lonmin),
                str(lonmax),
                str(latmin),
                str(latmax),
                schema,
                assettype,
                querymode,
                model,
            ],
            check=True,
        )

        path_to_output_file = os.path.join(
            current_dir,
            "output",
            "query_output.geojson",
        )

        output = gpd.read_file(path_to_output_file)

        self.assertLess(0, len(output))


if __name__ == "__main__":
    unittest.main()
