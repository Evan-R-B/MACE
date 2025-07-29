import matplotlib.pyplot as plt
import numpy as np
import csv
from matplotlib.colors import TwoSlopeNorm

models = ['small', 'medium', 'large', 'medium-mpa-0', 'small-0b', 'medium-0b', 'small-0b2', 'medium-0b2', 'medium-0b3', 'large-0b2', 'medium-omat-0']
surfaces = ['CuCu', 'CuGa', 'CuIr', 'CuNi', 'CuOs', 'CuPd', 'CuPt', 'CuRh', 'CuRu', 'CuZn']

def get_rmsd(surface, model):
    with open(f'RMSDs/{surface}.csv', newline='') as csvfile_1:
        reader = csv.reader(csvfile_1)
        for row in reader:
           if row[0] == f'{model}':
              return float(row[1])
        return None

RMSD = np.array([[get_rmsd(surfaces[0], models[0]), get_rmsd(surfaces[1], models[0]), get_rmsd(surfaces[2], models[0]), get_rmsd(surfaces[3], models[0]), get_rmsd(surfaces[4], models[0]), get_rmsd(surfaces[5], models[0]), get_rmsd(surfaces[6], models[0]), get_rmsd(surfaces[7], models[0]), get_rmsd(surfaces[8], models[0]), get_rmsd(surfaces[9], models[0])],
                  [get_rmsd(surfaces[0], models[1]), get_rmsd(surfaces[1], models[1]), get_rmsd(surfaces[2], models[1]), get_rmsd(surfaces[3], models[1]), get_rmsd(surfaces[4], models[1]), get_rmsd(surfaces[5], models[1]), get_rmsd(surfaces[6], models[1]), get_rmsd(surfaces[7], models[1]), get_rmsd(surfaces[8], models[1]), get_rmsd(surfaces[9], models[1])],
                  [get_rmsd(surfaces[0], models[2]), get_rmsd(surfaces[1], models[2]), get_rmsd(surfaces[2], models[2]), get_rmsd(surfaces[3], models[2]), get_rmsd(surfaces[4], models[2]), get_rmsd(surfaces[5], models[2]), get_rmsd(surfaces[6], models[2]), get_rmsd(surfaces[7], models[2]), get_rmsd(surfaces[8], models[2]), get_rmsd(surfaces[9], models[2])],
                  [get_rmsd(surfaces[0], models[3]), get_rmsd(surfaces[1], models[3]), get_rmsd(surfaces[2], models[3]), get_rmsd(surfaces[3], models[3]), get_rmsd(surfaces[4], models[3]), get_rmsd(surfaces[5], models[3]), get_rmsd(surfaces[6], models[3]), get_rmsd(surfaces[7], models[3]), get_rmsd(surfaces[8], models[3]), get_rmsd(surfaces[9], models[3])],
                  [get_rmsd(surfaces[0], models[4]), get_rmsd(surfaces[1], models[4]), get_rmsd(surfaces[2], models[4]), get_rmsd(surfaces[3], models[4]), get_rmsd(surfaces[4], models[4]), get_rmsd(surfaces[5], models[4]), get_rmsd(surfaces[6], models[4]), get_rmsd(surfaces[7], models[4]), get_rmsd(surfaces[8], models[4]), get_rmsd(surfaces[9], models[4])],
                  [get_rmsd(surfaces[0], models[5]), get_rmsd(surfaces[1], models[5]), get_rmsd(surfaces[2], models[5]), get_rmsd(surfaces[3], models[5]), get_rmsd(surfaces[4], models[5]), get_rmsd(surfaces[5], models[5]), get_rmsd(surfaces[6], models[5]), get_rmsd(surfaces[7], models[5]), get_rmsd(surfaces[8], models[5]), get_rmsd(surfaces[9], models[5])],
                  [get_rmsd(surfaces[0], models[6]), get_rmsd(surfaces[1], models[6]), get_rmsd(surfaces[2], models[6]), get_rmsd(surfaces[3], models[6]), get_rmsd(surfaces[4], models[6]), get_rmsd(surfaces[5], models[6]), get_rmsd(surfaces[6], models[6]), get_rmsd(surfaces[7], models[6]), get_rmsd(surfaces[8], models[6]), get_rmsd(surfaces[9], models[6])],
                  [get_rmsd(surfaces[0], models[7]), get_rmsd(surfaces[1], models[7]), get_rmsd(surfaces[2], models[7]), get_rmsd(surfaces[3], models[7]), get_rmsd(surfaces[4], models[7]), get_rmsd(surfaces[5], models[7]), get_rmsd(surfaces[6], models[7]), get_rmsd(surfaces[7], models[7]), get_rmsd(surfaces[8], models[7]), get_rmsd(surfaces[9], models[7])],
                  [get_rmsd(surfaces[0], models[8]), get_rmsd(surfaces[1], models[8]), get_rmsd(surfaces[2], models[8]), get_rmsd(surfaces[3], models[8]), get_rmsd(surfaces[4], models[8]), get_rmsd(surfaces[5], models[8]), get_rmsd(surfaces[6], models[8]), get_rmsd(surfaces[7], models[8]), get_rmsd(surfaces[8], models[8]), get_rmsd(surfaces[9], models[8])],
                  [get_rmsd(surfaces[0], models[9]), get_rmsd(surfaces[1], models[9]), get_rmsd(surfaces[2], models[9]), get_rmsd(surfaces[3], models[9]), get_rmsd(surfaces[4], models[9]), get_rmsd(surfaces[5], models[9]), get_rmsd(surfaces[6], models[9]), get_rmsd(surfaces[7], models[9]), get_rmsd(surfaces[8], models[9]), get_rmsd(surfaces[9], models[9])],
                  [get_rmsd(surfaces[0], models[10]), get_rmsd(surfaces[1], models[10]), get_rmsd(surfaces[2], models[10]), get_rmsd(surfaces[3], models[10]), get_rmsd(surfaces[4], models[10]), get_rmsd(surfaces[5], models[10]), get_rmsd(surfaces[6], models[10]), get_rmsd(surfaces[7], models[10]), get_rmsd(surfaces[8], models[10]), get_rmsd(surfaces[9], models[10])]])

plt.figure(figsize=(6, 5))
im = plt.imshow(RMSD, origin='lower', cmap='viridis', norm=TwoSlopeNorm(vmin=0.05, vcenter=0.145, vmax=0.2))

plt.xticks(np.arange(len(surfaces)), surfaces, rotation=45, ha='right')
plt.yticks(np.arange(len(models)), models)

plt.xlabel('Slab')
plt.ylabel('Model')
plt.title('Slab Relaxation RMSD')

cbar = plt.colorbar(im)
cbar.set_label('RMSD (Å)')

plt.tight_layout()
#plt.savefig('RMSDHeatmap.png', dpi=300)
plt.show()
