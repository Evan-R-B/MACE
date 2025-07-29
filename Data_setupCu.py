from ase.io import read
from pathlib import Path
from mace.calculators import mace_mp
import csv
import numpy as np
# Select best model and remove for loops, only calculate with 1 model

models = ['small', 'medium', 'large', 'medium-mpa-0', 'small-0b', 'medium-0b', 'small-0b2', 'medium-0b2', 'medium-0b3', 'large-0b2', 'medium-omat-0']
results = Path(f'../RMSD_Zhongwei/Geometries/CuCu')
bulk = read(f'../initialstructures/Cu-bulk.traj')

#Slab and bulk energy for each model

for model in models:
    bulk.calc = mace_mp(model=model, dispersion=False, default_dtype='float64', device='cpu')
    e_bulk = bulk.get_potential_energy()
    atoms_model = read(results / model / f'{model}.traj@-1')
    e_model = atoms_model.get_potential_energy()
    with open('Results/CuCuBulkoff_and_slaboff_energies.csv', 'a', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        csvwriter.writerow([model, f'{e_bulk}', f'{e_model}'])

#Functions for retrieving energies from csv file

def get_bulk(model1):
    with open('Results/CuCuBulkoff_and_slaboff_energies.csv', newline='') as csvfile_1:
        reader = csv.reader(csvfile_1)
        for row in reader:
           if row[0] == f'{model1}':
              return float(row[1])
        return None


def get_slab(model2):
    with open('Results/CuCuBulkoff_and_slaboff_energies.csv', newline='') as csvfile_2:
        reader = csv.reader(csvfile_2)
        for row in reader:
           if row[0] == f'{model2}':
              return float(row[2])
        return None

#Calculate all possible combinations of models for surface energy

n = 63

for model_slab in models:
    slab_energy = get_slab(model_slab)
    traj_path = results / model_slab / f'{model_slab}.traj@-1'
    atoms_model = read(traj_path)
    A = np.linalg.norm(np.cross(atoms_model.cell[0], atoms_model.cell[1]))
    for model_bulk in models:
        bulk_energy = get_bulk(model_bulk)
        surface_energy = (slab_energy - n * bulk_energy) / (2 * float(A))
        with open('Results/CuCuSurface_energies_dispersionoff.csv', 'a', newline='') as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=',')
            csvwriter.writerow([model_slab, model_bulk, surface_energy])