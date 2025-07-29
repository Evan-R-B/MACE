import matplotlib.pyplot as plt
import numpy as np
import csv
from matplotlib.colors import TwoSlopeNorm

models = ['small', 'medium', 'large', 'medium-mpa-0', 'small-0b', 'medium-0b', 'small-0b2', 'medium-0b2', 'medium-0b3', 'large-0b2', 'medium-omat-0']
surfaces = ['CuIr', 'CuNi', 'CuPd', 'CuPt', 'CuRh']

def get_error(surface, model):
    with open(f'Results/{surface}Surface_energy_lattice.csv', newline='') as csvfile_1:
        reader = csv.reader(csvfile_1)
        for row in reader:
           if row[0] == f'{model}':
            if surface == 'CuIr':
                return abs(0.117 - float(row[1]))
            elif surface == 'CuNi':
                return abs(0.104 - float(row[1]))
            elif surface == 'CuPd':
                return abs(0.090 - float(row[1]))
            elif surface == 'CuPt':
                return abs(0.091 - float(row[1]))
            elif surface == 'CuRh':
                return abs(0.106 - float(row[1]))
        return None


error = np.array([[get_error(surfaces[0], models[0]), get_error(surfaces[1], models[0]), get_error(surfaces[2], models[0]), get_error(surfaces[3], models[0]), get_error(surfaces[4], models[0])],
                  [get_error(surfaces[0], models[1]), get_error(surfaces[1], models[1]), get_error(surfaces[2], models[1]), get_error(surfaces[3], models[1]), get_error(surfaces[4], models[1])],
                  [get_error(surfaces[0], models[2]), get_error(surfaces[1], models[2]), get_error(surfaces[2], models[2]), get_error(surfaces[3], models[2]), get_error(surfaces[4], models[2])],
                  [get_error(surfaces[0], models[3]), get_error(surfaces[1], models[3]), get_error(surfaces[2], models[3]), get_error(surfaces[3], models[3]), get_error(surfaces[4], models[3])],
                  [get_error(surfaces[0], models[4]), get_error(surfaces[1], models[4]), get_error(surfaces[2], models[4]), get_error(surfaces[3], models[4]), get_error(surfaces[4], models[4])],
                  [get_error(surfaces[0], models[5]), get_error(surfaces[1], models[5]), get_error(surfaces[2], models[5]), get_error(surfaces[3], models[5]), get_error(surfaces[4], models[5])],
                  [get_error(surfaces[0], models[6]), get_error(surfaces[1], models[6]), get_error(surfaces[2], models[6]), get_error(surfaces[3], models[6]), get_error(surfaces[4], models[6])],
                  [get_error(surfaces[0], models[7]), get_error(surfaces[1], models[7]), get_error(surfaces[2], models[7]), get_error(surfaces[3], models[7]), get_error(surfaces[4], models[7])],
                  [get_error(surfaces[0], models[8]), get_error(surfaces[1], models[8]), get_error(surfaces[2], models[8]), get_error(surfaces[3], models[8]), get_error(surfaces[4], models[8])],
                  [get_error(surfaces[0], models[9]), get_error(surfaces[1], models[9]), get_error(surfaces[2], models[9]), get_error(surfaces[3], models[9]), get_error(surfaces[4], models[9])],
                  [get_error(surfaces[0], models[10]), get_error(surfaces[1], models[10]), get_error(surfaces[2], models[10]), get_error(surfaces[3], models[10]), get_error(surfaces[4], models[10])]])

plt.figure(figsize=(5, 5))
im = plt.imshow(error, origin='lower', cmap='viridis', norm=TwoSlopeNorm(vmin=0, vcenter=0.02, vmax=0.04))

plt.xticks(np.arange(len(surfaces)), surfaces, rotation=45, ha='right')
plt.yticks(np.arange(len(models)), models)

plt.xlabel('Slab')
plt.ylabel('Model')
plt.title('Alloy Surface Energy Error with Lattice Constant')

cbar = plt.colorbar(im)
cbar.set_label('Absolute Surface Energy Error (eV/Å²)')

plt.tight_layout()
plt.savefig('AlloySurfaceErrorLattice.png', dpi=300)
plt.show()
