from pathlib import Path
from ase.optimize import BFGS
from mace.calculators import mace_mp
from ase.io import read

surfaces = ['CuCu', 'CuGa', 'CuIr', 'CuNi', 'CuOs', 'CuPd', 'CuPt', 'CuRh', 'CuRu', 'CuZn']
models = ['small', 'medium', 'large', 'medium-mpa-0', 'small-0b', 'medium-0b', 'small-0b2', 'medium-0b2', 'medium-0b3', 'large-0b2', 'medium-omat-0']

for surface in surfaces:
    slab_base = read(filename=f'../initialstructures/{surface}-SAA.traj', index=0)
    for model in models:
        slab = slab_base.copy()
        folder = Path(f'Geometries/{surface}/{model}')
        folder.mkdir(parents=True, exist_ok=True)
        trajectory_save = folder/f'{model}.traj'
        logfile_save = folder/f'{model}.log'
        slab.calc = mace_mp(model=model, dispersion= False, default_dtype="float64", device='cpu') #run true for rmsd
        opt = BFGS(slab, trajectory=str(trajectory_save), logfile=str(logfile_save))
        opt.run(fmax=0.01)