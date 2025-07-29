import numpy as np
from ase.eos import EquationOfState
from ase.io.trajectory import Trajectory
from ase.io import read, write
from mace.calculators import mace_mp
import matplotlib.pyplot as plt

surfaces = ['CuCu', 'CuIr', 'CuNi', 'CuPd', 'CuPt', 'CuRh']
models = ['small', 'medium', 'large', 'medium-mpa-0', 'small-0b', 'medium-0b', 'small-0b2', 'medium-0b2', 'medium-0b3', 'large-0b2', 'medium-omat-0']

for surface in surfaces:
    for model in models:
        alloy = surface[-2:]
        a = 4.0
        b = a / 2
        atom = read(f'../initialstructures/{alloy}-bulk.traj')
        cell = atom.get_cell()
        traj = Trajectory(f'../RMSD_Zhongwei/Geometries/{surface}/{alloy}{model}-bulk.traj', 'w')
        for x in np.linspace(0.95, 1.05, 10): # Use 10 sampling points
            atom.calc = mace_mp(model= model, default_dtype= 'float64', dispersion= False, device= 'cpu') #Assign the MACE calculator
            atom.set_cell(cell * x, scale_atoms=True)
            atom.get_potential_energy()
            traj.write(atom)
        configs = read(f'../RMSD_Zhongwei/Geometries/{surface}/{alloy}{model}-bulk.traj@0:10')
        volumes = [ag.get_volume() for ag in configs]
        energies = [ag.get_potential_energy() for ag in configs]
        eos = EquationOfState(volumes, energies)
        v0, e0, B = eos.fit()
        a0 = (v0 ** (1/3))
        print(a0)
        plt.figure()
        eos.plot(f'EOS/{alloy}{model}-eos.png')
        plt.close()
        optimized_atom = atom.copy()
        optimized_atom.set_cell(np.identity(3) * a0, scale_atoms=True)
        optimized_atom.calc = mace_mp(model=model, default_dtype='float64', dispersion=False, device='cpu')
        optimized_atom.get_potential_energy()
        write(f'../initialstructures/{alloy}{model}-bulk.traj', optimized_atom)
