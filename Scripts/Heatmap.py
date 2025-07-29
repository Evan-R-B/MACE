import matplotlib.pyplot as plt
import numpy as np
import csv
from matplotlib.colors import TwoSlopeNorm

surface = 'CuCu'
bulk_models = ['small', 'medium', 'large', 'medium-mpa-0', 'small-0b', 'medium-0b', 'small-0b2', 'medium-0b2', 'medium-0b3', 'large-0b2', 'medium-omat-0']
slab_models = ['small', 'medium', 'large', 'medium-mpa-0', 'small-0b', 'medium-0b', 'small-0b2', 'medium-0b2', 'medium-0b3', 'large-0b2', 'medium-omat-0']

def get_e_surface(bulk_model, slab_model):
    with open(f'Results/{surface}Surface_energies_dispersionoff.csv', newline='') as csvfile_1:
        reader = csv.reader(csvfile_1)
        for row in reader:
           if row[0] == f'{slab_model}' and row[1] == f'{bulk_model}':
              return (abs(0.098 - float(row[2])))
        return None

error1 = np.array([[get_e_surface(bulk_models[0], slab_models[0]), get_e_surface(bulk_models[1], slab_models[0]), get_e_surface(bulk_models[2], slab_models[0]), get_e_surface(bulk_models[3], slab_models[0]), get_e_surface(bulk_models[4], slab_models[0]), get_e_surface(bulk_models[5], slab_models[0]), get_e_surface(bulk_models[6], slab_models[0]), get_e_surface(bulk_models[7], slab_models[0]), get_e_surface(bulk_models[8], slab_models[0]), get_e_surface(bulk_models[9], slab_models[0]), get_e_surface(bulk_models[10], slab_models[0])],
                  [get_e_surface(bulk_models[0], slab_models[1]), get_e_surface(bulk_models[1], slab_models[1]), get_e_surface(bulk_models[2], slab_models[1]), get_e_surface(bulk_models[3], slab_models[1]), get_e_surface(bulk_models[4], slab_models[1]), get_e_surface(bulk_models[5], slab_models[1]), get_e_surface(bulk_models[6], slab_models[1]), get_e_surface(bulk_models[7], slab_models[1]), get_e_surface(bulk_models[8], slab_models[1]), get_e_surface(bulk_models[9], slab_models[1]), get_e_surface(bulk_models[10], slab_models[1])],
                  [get_e_surface(bulk_models[0], slab_models[2]), get_e_surface(bulk_models[1], slab_models[2]), get_e_surface(bulk_models[2], slab_models[2]), get_e_surface(bulk_models[3], slab_models[2]), get_e_surface(bulk_models[4], slab_models[2]), get_e_surface(bulk_models[5], slab_models[2]), get_e_surface(bulk_models[6], slab_models[2]), get_e_surface(bulk_models[7], slab_models[2]), get_e_surface(bulk_models[8], slab_models[2]), get_e_surface(bulk_models[9], slab_models[2]), get_e_surface(bulk_models[10], slab_models[2])],
                  [get_e_surface(bulk_models[0], slab_models[3]), get_e_surface(bulk_models[1], slab_models[3]), get_e_surface(bulk_models[2], slab_models[3]), get_e_surface(bulk_models[3], slab_models[3]), get_e_surface(bulk_models[4], slab_models[3]), get_e_surface(bulk_models[5], slab_models[3]), get_e_surface(bulk_models[6], slab_models[3]), get_e_surface(bulk_models[7], slab_models[3]), get_e_surface(bulk_models[8], slab_models[3]), get_e_surface(bulk_models[9], slab_models[3]), get_e_surface(bulk_models[10], slab_models[3])],
                  [get_e_surface(bulk_models[0], slab_models[4]), get_e_surface(bulk_models[1], slab_models[4]), get_e_surface(bulk_models[2], slab_models[4]), get_e_surface(bulk_models[3], slab_models[4]), get_e_surface(bulk_models[4], slab_models[4]), get_e_surface(bulk_models[5], slab_models[4]), get_e_surface(bulk_models[6], slab_models[4]), get_e_surface(bulk_models[7], slab_models[4]), get_e_surface(bulk_models[8], slab_models[4]), get_e_surface(bulk_models[9], slab_models[4]), get_e_surface(bulk_models[10], slab_models[4])],
                  [get_e_surface(bulk_models[0], slab_models[5]), get_e_surface(bulk_models[1], slab_models[5]), get_e_surface(bulk_models[2], slab_models[5]), get_e_surface(bulk_models[3], slab_models[5]), get_e_surface(bulk_models[4], slab_models[5]), get_e_surface(bulk_models[5], slab_models[5]), get_e_surface(bulk_models[6], slab_models[5]), get_e_surface(bulk_models[7], slab_models[5]), get_e_surface(bulk_models[8], slab_models[5]), get_e_surface(bulk_models[9], slab_models[5]), get_e_surface(bulk_models[10], slab_models[5])],
                  [get_e_surface(bulk_models[0], slab_models[6]), get_e_surface(bulk_models[1], slab_models[6]), get_e_surface(bulk_models[2], slab_models[6]), get_e_surface(bulk_models[3], slab_models[6]), get_e_surface(bulk_models[4], slab_models[6]), get_e_surface(bulk_models[5], slab_models[6]), get_e_surface(bulk_models[6], slab_models[6]), get_e_surface(bulk_models[7], slab_models[6]), get_e_surface(bulk_models[8], slab_models[6]), get_e_surface(bulk_models[9], slab_models[6]), get_e_surface(bulk_models[10], slab_models[6])],
                  [get_e_surface(bulk_models[0], slab_models[7]), get_e_surface(bulk_models[1], slab_models[7]), get_e_surface(bulk_models[2], slab_models[7]), get_e_surface(bulk_models[3], slab_models[7]), get_e_surface(bulk_models[4], slab_models[7]), get_e_surface(bulk_models[5], slab_models[7]), get_e_surface(bulk_models[6], slab_models[7]), get_e_surface(bulk_models[7], slab_models[7]), get_e_surface(bulk_models[8], slab_models[7]), get_e_surface(bulk_models[9], slab_models[7]), get_e_surface(bulk_models[10], slab_models[7])],
                  [get_e_surface(bulk_models[0], slab_models[8]), get_e_surface(bulk_models[1], slab_models[8]), get_e_surface(bulk_models[2], slab_models[8]), get_e_surface(bulk_models[3], slab_models[8]), get_e_surface(bulk_models[4], slab_models[8]), get_e_surface(bulk_models[5], slab_models[8]), get_e_surface(bulk_models[6], slab_models[8]), get_e_surface(bulk_models[7], slab_models[8]), get_e_surface(bulk_models[8], slab_models[8]), get_e_surface(bulk_models[9], slab_models[8]), get_e_surface(bulk_models[10], slab_models[8])],
                  [get_e_surface(bulk_models[0], slab_models[9]), get_e_surface(bulk_models[1], slab_models[9]), get_e_surface(bulk_models[2], slab_models[9]), get_e_surface(bulk_models[3], slab_models[9]), get_e_surface(bulk_models[4], slab_models[9]), get_e_surface(bulk_models[5], slab_models[9]), get_e_surface(bulk_models[6], slab_models[9]), get_e_surface(bulk_models[7], slab_models[9]), get_e_surface(bulk_models[8], slab_models[9]), get_e_surface(bulk_models[9], slab_models[9]), get_e_surface(bulk_models[10], slab_models[9])],
                  [get_e_surface(bulk_models[0], slab_models[10]), get_e_surface(bulk_models[1], slab_models[10]), get_e_surface(bulk_models[2], slab_models[10]), get_e_surface(bulk_models[3], slab_models[10]), get_e_surface(bulk_models[4], slab_models[10]), get_e_surface(bulk_models[5], slab_models[10]), get_e_surface(bulk_models[6], slab_models[10]), get_e_surface(bulk_models[7], slab_models[10]), get_e_surface(bulk_models[8], slab_models[10]), get_e_surface(bulk_models[9], slab_models[10]), get_e_surface(bulk_models[10], slab_models[10])]])

plt.figure(figsize=(6, 5))
#im = plt.imshow(error1, origin='lower', cmap='plasma', norm=TwoSlopeNorm(vmin=-3.5, vcenter=-1.75, vmax=0))
#im = plt.imshow(error1, origin='lower', cmap='viridis', norm=TwoSlopeNorm(vmin=0, vcenter=0.01, vmax=0.22))
im = plt.imshow(error1, origin='lower', cmap='viridis', norm=TwoSlopeNorm(vmin=-0.03, vcenter=0, vmax=0.03))

plt.xticks(np.arange(len(bulk_models)), bulk_models, rotation=45, ha='right')
plt.yticks(np.arange(len(slab_models)), slab_models)

plt.xlabel('Bulk model')
plt.ylabel('Slab model')
plt.title('Copper Slab Surface‑Energy Error')

cbar = plt.colorbar(im)
cbar.set_label('Surface-Energy Error (eV/Å²)')

plt.tight_layout()
plt.savefig('ErrorHeatmap.png', dpi=300)
plt.show()
