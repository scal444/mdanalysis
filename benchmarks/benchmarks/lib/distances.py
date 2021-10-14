import MDAnalysis
import numpy as np

from MDAnalysisTests.datafiles import GRO
from MDAnalysis.lib import distances


class BondedDistancesBench(object):
    """Benchmarks for MDAnalysis.lib.distances functions.
    """

    params = ([10, 100, 1000, 10000, 100000, 1000000, 10000000],  ['serial', 'openmp'])
    param_names = ['num_atoms', 'backend']

    def setup(self, num_atoms, backend):
        np.random.seed(17809)
        self.coords_1 = np.random.random_sample((num_atoms, 3)).astype(np.float32)
        np.random.seed(9008716)
        self.coords_2 = np.random.random_sample((num_atoms, 3)).astype(np.float32)

    def time_calc_bonded_distance(self, num_atoms, backend):
        """Benchmark calculation of all distances
        between two numpy arrays of coordinates,
        using default arguments to distance_array.
        """
        distances.calc_bonds(self.coords_1,
                             self.coords_2,
                             box=None,
                             result=None,
                             backend=backend)
