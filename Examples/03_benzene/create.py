from pysimm import system, lmps, forcefield

# use a smiles string to query the pubchem search database and read the mol file returned from the http request
s = system.read_pubchem_smiles('c1=cc=cc=c1')

# the resulting system (benzene) has alternating double bonds
# we want pysimm to recognize the ring as aromatic, so we define each bond in the ring to be bond order 'A'
for b in s.bonds:
  if b.a.elem=='C' and b.b.elem=='C':
    b.order='A'

# the resulting system has sufficient information to type with a forcefield, here we will use the GAFF2 force field
# we will also determine partial charges using the gasteiger algorithm
s.apply_forcefield(forcefield.Gaff2(), charges='gasteiger')

# we'll perform energy minimization using the fire algorithm in LAMMPS
lmps.quick_min(s, min_style='fire')

# write a few different file formats
s.write_xyz('benzene.xyz')
s.write_yaml('benzene.yaml')
s.write_lammps('benzene.lmps')
s.write_chemdoodle_json('benzene.json')
