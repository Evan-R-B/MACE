import matplotlib.pyplot as plt

models = ['small', 'large', 'small-0b', 'medium-0b']
surfaces = ['CuCu', 'CuGa', 'CuIr', 'CuNi', 'CuOs', 'CuPd', 'CuPt', 'CuRh', 'CuRu', 'CuZn']

rmsd_values = {'small' : [0.12761355319815273, 0.13308986404812256, 0.1272728811301354, 0.12190276729950085, 0.1269113463291335, 0.1232847565159814, 0.12496595237853635, 0.1251042686505073, 0.12865573323423013, 0.12786432327776895],
               'large' : [0.14181674783776904, 0.14541300246209685, 0.13487691799081533, 0.13568368657365584, 0.13873318040600802, 0.13568749146743467, 0.1380523187110648, 0.13407869329841676, 0.12756933247263047, 0.14507991319221578],
               'small-0b' : [0.09917006726225061, 0.11115389665159017, 0.11574317863681903, 0.08595461653996775, 0.10184860277764929, 0.10898435062146848, 0.10580591375693546, 0.10119972628424946, 0.10506282239345262, 0.10836225550881204],
               'medium-0b' : [0.1281757336499702, 0.1302551692602755, 0.124148234520653, 0.12648143334770257, 0.12283796979784853, 0.13226146023281063, 0.12682765583581068, 0.12202522124787142, 0.13572273028917317, 0.1257296409638479]}

plt.figure(figsize=(6, 8))

cmap = plt.get_cmap('tab10')
colors = [cmap(i) for i in range(len(surfaces))]

for j, slab in enumerate(surfaces):
    x_vals = []
    y_vals = []
    for i, model in enumerate(models):
        x_vals.append(i)
        y_vals.append(rmsd_values[model][j])
    plt.scatter(x_vals, y_vals, label=slab, color=colors[j])

plt.xlabel('Model')
plt.ylabel('RMSD (Å)')
plt.title('RMSD for Best Models')
plt.xticks(ticks=range(len(models)), labels=models, rotation=45)
plt.legend(title='Slab', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig('GroupedScatterRes.png', dpi=600)
plt.show()