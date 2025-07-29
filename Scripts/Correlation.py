import matplotlib.pyplot as plt
import csv
import numpy as np

surface = 'CuCu'
models = ['small', 'medium', 'large', 'medium-mpa-0', 'small-0b', 'medium-0b', 'small-0b2', 'medium-0b2', 'medium-0b3', 'large-0b2', 'medium-omat-0']
rmsd = []
surface_error = []

for model in models:
    with open(f'RMSD_Zhongwei/RMSDs/{surface}.csv', newline='') as csvfile_1:
        reader = csv.reader(csvfile_1)
        for row in reader:
            if row[0] == f'{model}':
                rmsd.append(float(row[1]))

for model in models:
    with open(f'Surface_Energy/Results/{surface}Surface_energies_dispersionoff.csv', newline='') as csvfile_1:
        reader = csv.reader(csvfile_1)
        for row in reader:
            if row[0] == f'{model}' and row[1] == f'{model}':
                surface_error.append(0.098 - float(row[2]))

plt.figure(figsize=(7, 6))
plt.scatter(rmsd, surface_error)
for i, model in enumerate(models):
    plt.text(rmsd[i], surface_error[i] - 0.0003, model, fontsize=8, ha='center', va='top')
z = np.polyfit(rmsd, surface_error, 1)
p = np.poly1d(z)
x_vals = np.linspace(min(rmsd), max(rmsd), 100)
plt.plot(x_vals, p(x_vals), color='red', linestyle='-')

plt.xlabel('RMSD (Å)')
plt.ylabel('Surface-Energy Error (eV/Å²)')
plt.title('Correlation Between RMSD and Surface Energy Error for Copper')
plt.tight_layout()
plt.savefig('CuCuCorrelation.png', dpi=300)
plt.show()
print(surface_error[0])
print(surface_error[1])
print(surface_error[2])