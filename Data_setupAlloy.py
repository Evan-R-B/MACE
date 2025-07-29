from ase.io import read
from pathlib import Path
from mace.calculators import mace_mp
import csv
import numpy as np

surfaces = ['CuIr', 'CuNi', 'CuPd', 'CuPt', 'CuRh']
models = ['small', 'medium', 'large', 'medium-mpa-0', 'small-0b', 'medium-0b', 'small-0b2', 'medium-0b2', 'medium-0b3', 'large-0b2', 'medium-omat-0']

for surface in surfaces:
    atom = str(surface[-2:])
    for model in models:
        Cubulk = read(Path('../initialstructures') / f'Cu-bulk.traj')
        Atombulk = read(Path('../initialstructures') / f'{atom}-bulk.traj')
        Cubulk.calc = mace_mp(model= model, dispersion=False, default_dtype='float64', device='cpu')
        Atombulk.calc = mace_mp(model= model, dispersion=False, default_dtype='float64', device='cpu')
        Cubulk_energy = Cubulk.get_potential_energy()
        Atombulk_energy = Atombulk.get_potential_energy()
        alloy_model = read(f'../RMSD_Zhongwei/Geometries/{surface}/{model}/{model}.traj@-1')
        e_alloyslab = alloy_model.get_potential_energy()
        Cumodel = read(f'../RMSD_Zhongwei/Geometries/CuCu/{model}/{model}.traj@-1')
        e_Cuslab = Cumodel.get_potential_energy()
        with open('Results/CuCuSurface_energies_dispersionoff.csv', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                print('searching row:', row)
                if row[0] == f'{model}' and row[1] == f'{model}':
                    print('found row:', row)
                    e_surfaceCu = float(row[2])
        A = np.linalg.norm(np.cross(alloy_model.cell[0], alloy_model.cell[1]))
        surface_energy = e_surfaceCu + ((e_alloyslab + Cubulk_energy - e_Cuslab - Atombulk_energy)/float(A))
        with open(f'Results/{surface}Surface_energy_initial.csv', 'a', newline='') as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=',')
            csvwriter.writerow([f'{model}', surface_energy])