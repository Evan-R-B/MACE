import numpy as np
from ase.io import read
import csv

surfaces = ['CuCu','CuGa', 'CuIr', 'CuNi', 'CuOs', 'CuPd', 'CuPt', 'CuRh', 'CuRu', 'CuZn']
models = ['small', 'medium', 'large', 'medium-mpa-0', 'small-0b', 'medium-0b', 'small-0b2', 'medium-0b2', 'medium-0b3', 'large-0b2', 'medium-omat-0']

for surface in surfaces:
    print(surface)
    atom = str(surface[-2:])
    atoms_dft = read(f'../dft-optimized/slab_{atom}.traj@-1')
    pos_dft = atoms_dft.get_positions()
    for model in models:
        print(model)
        atoms_model = read(f'Geometries/{surface}/{model}/{model}.traj@-1')
        pos_model = atoms_model.get_positions()
        x = pos_model - pos_dft
        rms_squared = (x ** 2).sum(axis=1).mean()
        rmsd = np.sqrt(rms_squared)
        with open(f'RMSDs/{surface}.csv', 'a', newline='') as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=",")
            csvwriter.writerow([model, f'{rmsd}'])