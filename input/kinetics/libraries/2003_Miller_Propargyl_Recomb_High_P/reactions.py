#!/usr/bin/env python
# encoding: utf-8

name = "2003_Miller_Propargyl_Recomb_High_P"
shortDesc = u"Propargyl Radical Recombination to form Fulvene and Benzene"
longDesc = u"""
TST rates calculated from QM calculations of:
Miller, J. A.; Klippenstein, S. J., The Recombination of Propargyl Radicals and Other Reactions on a C6H6 Potential. 
J. Phys. Chem. A 2003, 107, 7783-7799.
"""
entry(
    index = 1,
    label = "I <=> II",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.873e+11, 's^-1'), n=0.278, Ea=(35.198, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 2,
    label = "II <=> III",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.606e+11, 's^-1'), n=0.285, Ea=(29.433, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 3,
    label = "II <=> A",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.056e+11, 's^-1'), n=0.183, Ea=(38.65, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 4,
    label = "A <=> IV",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8.067e+10, 's^-1'), n=0.649, Ea=(8.03, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 5,
    label = "II <=> VIII",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.086e+09, 's^-1'), n=1.038, Ea=(39.326, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 6,
    label = "IV <=> VI",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.676e+10, 's^-1'), n=1.256, Ea=(85.885, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 7,
    label = "B <=> IX",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.45e+12, 's^-1'), n=0.194, Ea=(32.274, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 8,
    label = "V <=> VI",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.55e+11, 's^-1'), n=-0.049, Ea=(30.306, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 9,
    label = "IX <=> VII",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.454e+12, 's^-1'), n=0.178, Ea=(0.205, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 10,
    label = "VIII <=> IX",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.994e+12, 's^-1'), n=0.197, Ea=(51.841, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 11,
    label = "VIII <=> X",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.587e+11, 's^-1'), n=0.108, Ea=(37.209, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 12,
    label = "X <=> IX",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.865e+11, 's^-1'), n=0.577, Ea=(29.169, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)

entry(
    index = 13,
    label = "X <=> XI",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.392e+10, 's^-1'), n=0.782, Ea=(34.256, 'kcal/mol'), T0=(1, 'K')),
    longDesc = 
u"""
Originally from reaction library: Unclassified
""",
)
