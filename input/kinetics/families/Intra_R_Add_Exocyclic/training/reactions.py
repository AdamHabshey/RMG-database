#!/usr/bin/env python
# encoding: utf-8

name = "Intra_R_Add_Exocyclic/training"
shortDesc = u"Kinetics used to train group additivity values"
longDesc = u"""
Put kinetic parameters for reactions to use as a training set for fitting
group additivity values in this file.
"""


entry(
    index = 1,
    label = "C7H9 <=> C7H9-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.32e+10, 's^-1'), n=0.35, Ea=(10.3, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: product38 <=> product39
""",
)

entry(
    index = 2,
    label = "C7H9-3 <=> C7H9-4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.95e+12, 's^-1'), n=0.12, Ea=(3, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: product39 <=> product37
""",
)



entry(
    index = 3,
    label = "C10H11 <=> C10H11-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.69e+11, 's^-1'), n=0.22, Ea=(40, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C10H11""",
    longDesc = 
u"""
Taken from entry: pdt18 <=> pdt19
""",
)

entry(
    index = 4,
    label = "C10H11-3 <=> C10H11-4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.19e+11, 's^-1'), n=0.08, Ea=(16.7, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C10H11""",
    longDesc = 
u"""
Taken from entry: pdt14 <=> pdt23
""",
)

entry(
    index = 5,
    label = "C10H11-5 <=> C10H11-6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.02e+11, 's^-1'), n=0.79, Ea=(35.3, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: C10H11""",
    longDesc = 
u"""
Taken from entry: pdt55 <=> pdt58
""",
)



entry(
    index = 6,
    label = "C10H9 <=> C10H9-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.3e+12, 's^-1'), n=0.45, Ea=(25.6, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: naphthalene_H""",
    longDesc = 
u"""
Taken from entry: prod2 <=> prod5
""",
)

entry(
    index = 7,
    label = "C10H9-3 <=> C10H9-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(6.311e+09, 's^-1'), n=0.537, Ea=(2.307, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2016_Mebel_C10H9_highP""",
    longDesc = 
u"""
Taken from entry: W5 <=> W8
""",
)

entry(
    index = 8,
    label = "C10H7 <=> C10H7-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.992e+11, 's^-1'), n=0.67, Ea=(58.336, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/phenyl_diacetylene_effective""",
    longDesc = 
u"""
Taken from entry: i2_trans <=> i3
""",
)

entry(
    index = 9,
    label = "C9H9 <=> C9H9-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.66e+11, 's^-1'), n=0.412, Ea=(27.805, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2016_Mebel_C9H9_highP""",
    longDesc = 
u"""
Taken from entry:
""",
)

entry(
    index = 10,
    label = "C9H9-3 <=> C9H9-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.454e+11, 's^-1'), n=0.447, Ea=(24.536, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2016_Mebel_C9H9_highP""",
    longDesc = 
u"""
Taken from entry:
""",
)

entry(
    index = 11,
    label = "C9H9-5 <=> C9H9-6",
    degeneracy = 2.0,
    kinetics = Arrhenius(A=(1.185e+11, 's^-1'), n=0.586, Ea=(37.614, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2016_Mebel_C9H9_highP""",
    longDesc = 
u"""
Taken from entry:
""",
)

entry(
    index = 12,
    label = "C9H9-7 <=> C9H9-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.241e+10, 's^-1'), n=0.754, Ea=(22.335, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2016_Mebel_C9H9_highP""",
    longDesc = 
u"""
Taken from entry:
""",
)

entry(
    index = 13,
    label = "C9H9-9 <=> C9H9-10",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.932e+07, 's^-1'), n=1.035, Ea=(14.54, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2016_Mebel_C9H9_highP""",
    longDesc = 
u"""
Taken from entry:
""",
)

entry(
    index = 14,
    label = "C9H9-11 <=> C9H9-12",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(4.713e+10, 's^-1'), n=0.481, Ea=(30.309, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2016_Mebel_C9H9_highP""",
    longDesc = 
u"""
Taken from entry:
""",
)

entry(
    index = 15,
    label = "C10H9-5 <=> C10H9-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.54e+10, 's^-1'), n=0.69, Ea=(20.376, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2017_Mebel_C6H5_C4H4_highP""",
    longDesc = 
u"""
Taken from entry:
""",
)

entry(
    index = 16,
    label = "C10H9-7 <=> C10H9-8",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9.423e+09, 's^-1'), n=0.834, Ea=(24.235, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2017_Mebel_C6H5_C4H4_highP""",
    longDesc = 
u"""
Taken from entry:
""",
)

entry(
    index = 17,
    label = "C10H9-9 <=> C10H9-10",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(3.233e+11, 's^-1'), n=0.39, Ea=(35.846, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2017_Mebel_C6H5_C4H4_highP""",
    longDesc = 
u"""
Taken from entry:
""",
)

entry(
    index = 18,
    label = "C10H9-11 <=> C10H9-12",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.126e+14, 's^-1'), n=-0.355, Ea=(28.539, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2017_Mebel_C6H5_C4H4_highP""",
    longDesc = 
u"""
Taken from entry:
""",
)

entry(
    index = 19,
    label = "C10H9-13 <=> C10H9-14",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.881e+08, 's^-1'), n=1.062, Ea=(16.546, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2017_Mebel_C6H5_C4H4_highP""",
    longDesc = 
u"""
Taken from entry:
""",
)

entry(
    index = 20,
    label = "C10H9-15 <=> C10H9-16",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(8.443e+10, 's^-1'), n=0.474, Ea=(23.82, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2017_Mebel_C6H5_C4H4_highP""",
    longDesc = 
u"""
Taken from entry:
""",
)

entry(
    index = 21,
    label = "C6H9 <=> C6H9-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.249e+08, 's^-1'), n=0.846, Ea=(19.298, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: 2015_Buras_C2H3_C4H6_highP""",
    longDesc = 
u"""
Taken from entry:
""",
)

entry(
    index = 22,
    label = "C9H11 <=> C9H11-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.597e+08, 's^-1'), n=0.953, Ea=(15.885, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2017_Buras_C6H5_C3H6_highP""",
    longDesc = 
u"""
Taken from entry:
""",
)

entry(
    index = 23,
    label = "C9H11-3 <=> C9H11-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.732e+09, 's^-1'), n=0.671, Ea=(15.317, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2017_Buras_C6H5_C3H6_highP""",
    longDesc = 
u"""
Taken from entry:
""",
)

entry(
    index = 24,
    label = "C10H7-3 <=> C10H7-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.42e+11, 's^-1'), n=0.258, Ea=(3.797, 'kcal/mol'), T0=(1, 'K')),
    rank = 3,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2017_Mebel_C6H4C2H_C2H2_highP""",
    longDesc = 
u"""
Taken from entry: W1 <=> W3_6
""",
)

