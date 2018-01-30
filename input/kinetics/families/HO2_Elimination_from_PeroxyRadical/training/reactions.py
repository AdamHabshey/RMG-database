#!/usr/bin/env python
# encoding: utf-8

name = "HO2_Elimination_from_PeroxyRadical/training"
shortDesc = u"Kinetics used to train group additivity values"
longDesc = u"""
Put kinetic parameters for reactions to use as a training set for fitting
group additivity values in this file.
"""
entry(
    index = 1,
    label = "C2H3O3 <=> C2H2O + HO2",
    degeneracy = 3,
    kinetics = Arrhenius(
        A = (2.6e+09, 's^-1', '*|/', 2.51189),
        n = 1.2,
        Ea = (34.1, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ["J. W. Allen", "C. F. Goldsmith", "W. H. Green"],
        title = u'Automatic Estimation of Pressure-Dependent Rate Coefficients',
        journal = "Phys. Chem. Chem. Phys.",
        volume = "14",
        pages = """1131-1155""",
        year = "2012",
    ),
    referenceType = "theory",
    shortDesc = u"""CFG VTST calculations at RQCISD(T)/CBS//B3LYP/6-311++G(d,p) level""",
    longDesc = 
u"""
Quantum chemistry calculations at the RQCISD(T)/CBS//B3LYP/6-311++G(d,p) level
using Gaussian 03 and MOLPRO. High-pressure-limit rate coefficient computed
using Variflex.
DOI: 10.1039/C1CP22765C
""",
)
entry(
    index = 2,
    label = "MPO1QJ <=> MPO1Star + HO2",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.034e10, 's^-1'),
        n = 1.109,
        Ea = (30.611, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    shortDesc = u"""G4 calculation""",
    longDesc = 
u"""
G4 calculation with 1-D HR by Lintao Bu at Nrel
""",
)
    
entry(
    index = 3,
    label = "MPO1Q3QJ <=> MPO1Q2Star + HO2",
    degeneracy = 2,
    kinetics = Arrhenius(
        A = (1.132e13, 's^-1'),
        n = -0.199,
        Ea = (28.052, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 3,
    shortDesc = u"""G4 calculation""",
    longDesc = 
u"""
G4 calculation with 1-D HR by Lintao Bu at Nrel
""",
)
