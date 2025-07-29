import numpy as np
import matplotlib.pyplot as plt
import csv

models = ['small', 'medium', 'large', 'medium-mpa-0', 'small-0b', 'medium-0b', 'small-0b2', 'medium-0b2', 'medium-0b3', 'large-0b2', 'medium-omat-0']
surfaces = ['CuCu', 'CuGa', 'CuIr', 'CuNi', 'CuOs', 'CuPd', 'CuPt', 'CuRh', 'CuRu', 'CuZn']
rmsd_values = {model: [] for model in models}

for surface in surfaces:
    with open(f'RMSDs/{surface}.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            model = row[0]
            if model in rmsd_values:
                rmsd_values[model].append(float(row[1]))

mean_rmsd = [np.mean(rmsd_values[model]) for model in models]
std_rmsd = [np.std(rmsd_values[model]) for model in models]

plt.figure(figsize=(8, 5))
plt.bar(models, mean_rmsd, yerr=std_rmsd, capsize=5, color='teal')
plt.ylabel('Mean RMSD (Å)')
plt.xlabel('Model')
plt.title('Mean RMSD with Error Bars per Model')
plt.xticks(rotation=45, ha='right', fontsize = 9)
plt.tight_layout()
#plt.savefig('BarGraph.png', dpi=300)
plt.show()
maxim = max(rmsd_values['small'])
minim = min(rmsd_values['small'])
average = np.mean(rmsd_values['medium-mpa-0'])
print(maxim, minim)
print(maxim-minim)
print(average)