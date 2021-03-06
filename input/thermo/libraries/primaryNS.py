#!/usr/bin/env python
# encoding: utf-8

name = "primaryNS"
shortDesc = u"primaryNS"
longDesc = u"""
Thermo data for various nitrogen and sulfur species
"""

entry(
    index = 1,
    label = "N",
    molecule =
"""
multiplicity 4
1 N u3 p1 c0
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([4.9675,4.9675,4.9675,4.9675,4.9675,4.9674,4.9718],'cal/(mol*K)'),
        H298 = (112.96,'kcal/mol'),
        S298 = (36.6336,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc =
    u"""
    Taken from the GRI-Mech3.0-N library
    """,
)

entry(
    index = 2,
    label = "NH(S)",
    molecule =
"""
1 N u0 p2 c0 {2,S}
2 H u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([6.98,7.00,7.11,7.27,7.60,7.91,8.44],'cal/(mol*K)'),
        H298 = (120.9,'kcal/mol','+|-',0.5),
        S298 = (41.7,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc =
    u"""
    Anthony M. Dean, Joseph W. Bozzelli, Combustion Chemistry of Nitrogen,
    in: Gas-Phase Combustion Chemistry, Editor: W.C. Gardiner, 2000, 125-341,
    doi: 10.1007/978-1-4612-1310-9_2
    """,
)

entry(
    index = 3,
    label = "NNOH",
    molecule =
"""
multiplicity 2
1 N u1 p1 c0 {2,D}
2 N u0 p1 c0 {1,D} {3,S}
3 O u0 p2 c0 {2,S} {4,S}
4 H u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.44,11.42,12.25,13.10,14.32,15.15,16.68],'cal/(mol*K)'),
        H298 = (58.1,'kcal/mol','+|-',0.5),
        S298 = (61.4,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc =
    u"""
    Anthony M. Dean, Joseph W. Bozzelli, Combustion Chemistry of Nitrogen,
    in: Gas-Phase Combustion Chemistry, Editor: W.C. Gardiner, 2000, 125-341,
    doi: 10.1007/978-1-4612-1310-9_2
    """,
)

entry(
    index = 4,
    label = "CH2NN",
    molecule =
"""
1 C u0 p1 c-1 {2,S} {3,S} {4,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 N u0 p0 c+1 {1,S} {5,T}
5 N u0 p1 c0 {4,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.74,13.86,15.60,17.04,19.17,20.67,22.94],'cal/(mol*K)'),
        H298 = (68.5,'kcal/mol','+|-',0.5),
        S298 = (57.96,'cal/(mol*K)'),
    ),
    shortDesc = u"""diazomethyl""",
    longDesc =
    u"""
    Anthony M. Dean, Joseph W. Bozzelli, Combustion Chemistry of Nitrogen,
    in: Gas-Phase Combustion Chemistry, Editor: W.C. Gardiner, 2000, 125-341,
    doi: 10.1007/978-1-4612-1310-9_2
    """,
)

entry(
    index = 5,
    label = "HCNN",
    molecule =
"""
multiplicity 2
1 C u1 p1 c-1 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 N u0 p0 c+1 {1,S} {4,T}
4 N u0 p1 c0 {3,T}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.78,12.19,13.40,14.29,15.68,16.56,17.71],'cal/(mol*K)'),
        H298 = (109.0,'kcal/mol','+|-',0.5),
        S298 = (59.3,'cal/(mol*K)'),
    ),
    shortDesc = u"""diazomethyl radical""",
    longDesc =
    u"""
    Anthony M. Dean, Joseph W. Bozzelli, Combustion Chemistry of Nitrogen,
    in: Gas-Phase Combustion Chemistry, Editor: W.C. Gardiner, 2000, 125-341,
    doi: 10.1007/978-1-4612-1310-9_2
    """,
)

entry(
    index = 6,
    label = "HCN2",
    molecule =
"""
multiplicity 2
1 N u0 p1 c0 {2,D} {3,S}
2 N u0 p1 c0 {1,D} {3,S}
3 C u1 p0 c0 {1,S} {2,S} {4,S}
4 H u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.00,12.02,13.00,13.81,15.30,16.09,17.59],'cal/(mol*K)'),
        H298 = (107.1,'kcal/mol','+|-',0.5),
        S298 = (57.5,'cal/(mol*K)'),
    ),
    shortDesc = u"""diazirine radical""",
    longDesc =
    u"""
    Anthony M. Dean, Joseph W. Bozzelli, Combustion Chemistry of Nitrogen,
    in: Gas-Phase Combustion Chemistry, Editor: W.C. Gardiner, 2000, 125-341,
    doi: 10.1007/978-1-4612-1310-9_2
    """,
)

entry(
    index = 7,
    label = "CH2NNH2",
    molecule =
"""
1 C u0 p0 c0 {2,D} {4,S} {5,S}
2 N u0 p1 c0 {1,D} {3,S}
3 N u0 p1 c0 {2,S} {6,S} {7,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([14.29,17.21,18.24,19.79,25.19,29.11,32.34],'cal/(mol*K)'),
        H298 = (45.5,'kcal/mol','+|-',0.5),
        S298 = (63.1,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc =
    u"""
    Anthony M. Dean, Joseph W. Bozzelli, Combustion Chemistry of Nitrogen,
    in: Gas-Phase Combustion Chemistry, Editor: W.C. Gardiner, 2000, 125-341,
    doi: 10.1007/978-1-4612-1310-9_2
    """,
)

entry(
    index = 8,
    label = "CH3NNH",
    molecule =
"""
1 C u0 p0 c0 {2,S} {4,S} {5,S} {6,S}
2 N u0 p1 c0 {1,S} {3,D}
3 N u0 p1 c0 {2,D} {7,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([13.70,16.20,16.82,18.69,24.40,27.10,31.31],'cal/(mol*K)'),
        H298 = (42.8,'kcal/mol','+|-',0.5),
        S298 = (61.4,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc =
    u"""
    Anthony M. Dean, Joseph W. Bozzelli, Combustion Chemistry of Nitrogen,
    in: Gas-Phase Combustion Chemistry, Editor: W.C. Gardiner, 2000, 125-341,
    doi: 10.1007/978-1-4612-1310-9_2
    """,
)

entry(
    index = 9,
    label = "NCHOH",
    molecule =
"""
multiplicity 2
1 N u1 p1 c0 {2,D}
2 C u0 p0 c0 {1,D} {3,S} {4,S}
3 H u0 p0 c0 {2,S}
4 O u0 p2 c0 {2,S} {5,S}
5 H u0 p0 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([12.50,14.24,15.80,17.16,19.17,20.46,22.39],'cal/(mol*K)'),
        H298 = (13.9,'kcal/mol','+|-',0.5),
        S298 = (62.9,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc =
    u"""
    Anthony M. Dean, Joseph W. Bozzelli, Combustion Chemistry of Nitrogen,
    in: Gas-Phase Combustion Chemistry, Editor: W.C. Gardiner, 2000, 125-341,
    doi: 10.1007/978-1-4612-1310-9_2
    """,
)

entry(
    index = 10,
    label = "NS",
    molecule =
"""
multiplicity 2
1 N u1 p1 c0 {2,D}
2 S u0 p2 c0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.07,8.17,8.26,8.35,8.50,8.62,8.84],'cal/(mol*K)'),
        H298 = (66.4,'kcal/mol','+|-',0.5),
        S298 = (52.76,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc =
    u"""
    Enthalpy is taken from Marshall2002:
    L.R. Peebles, P. Marshall, Chem. Phys. Letters, 2002, 366(5-6), 520-524, doi: 10.1016/S0009-2614(02)01619-6
    Entropy and Cp are taken from Burcat2005:
    Alexander Burcat and Branko Ruscic
    "Third Millennium Ideal Gas and Condensed Phase Thermochemical Database for
    Combustion with updates from Active Thermochemical Tables" TAE # 960; ANL-50/20
    Technion-IIT, Aerospace Engineering, and Argonne National Laboratory, Chemistry
    Division, 2005. http://garfield.chem.elte.hu/Burcat/burcat.html
    """,
)

entry(
    index = 11,
    label = "NSO",
    molecule =
"""
1 N u1 p1 c0 {2,D}
2 S u0 p1 c0 {1,D} {3,D}
3 O u0 p2 c0 {2,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([42.70,46.11,48.85,50.92,53.56,55.04,56.70],'J/(mol*K)'),
        H298 = (175.31,'kJ/mol','+|-',2.092),
        S298 = (262.6,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc =
    u"""
    Taken from the SulfurGlarborgNS library
    H298 is updated from Table 7 in P.A. Denis, J. Sulfur Chem. 2008, 29(3-4), 327-352, doi: 10.1080/17415990802047352
    """,
)

entry(
    index = 12,
    label = "NNS",
    molecule =
"""
1 N u0 p1 c0 {2,T}
2 N u0 p0 c+1 {1,T} {3,S}
3 S u0 p3 c-1 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.48496, 0.00087841, 1.61418e-05, -3.21583e-08, 1.89692e-11, 23801.9, 6.98879],
                Tmin = (10, 'K'),
                Tmax = (573.927, 'K'),
            ),
            NASAPolynomial(
                coeffs = [3.41668, 0.00484707, -3.35932e-06, 1.09773e-09, -1.35956e-13, 23752.2, 6.77912],
                Tmin = (573.927, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (197.894, 'kJ/mol'),
        Cp0 = (29.1007, 'J/(mol*K)'),
        CpInf = (54.0441, 'J/(mol*K)'),
    ),
    shortDesc = u"""CCSD(T)-F12a/cc-pVTZ-f12//M06-2x/cc-pVTZ""",
    longDesc =
    u"""
    SMILES: N#[N+][S-]

    calculated by alongd (xq1161, xc1074) at the CCSD(T)-F12a/cc-pVTZ-f12//M06-2x/cc-pVTZ level of theory
    frequencies calculated at M06-2x/cc-pVTZ

    Thermodynamics for NNS:
        Enthalpy of formation (298 K)   =    49.615 kcal/mol
        Entropy of formation (298 K)    =    54.798 cal/(mol*K)
        =========== =========== =========== =========== ===========
        Temperature Heat cap.   Enthalpy    Entropy     Free energy
        (K)         (cal/mol*K) (kcal/mol)  (cal/mol*K) (kcal/mol)
        =========== =========== =========== =========== ===========
                300       8.916      49.633      54.857      33.176
                400       9.631      50.562      57.523      27.552
                500      10.185      51.554      59.735      21.686
                600      10.602      52.594      61.630      15.616
                800      11.229      54.781      64.772       2.963
               1000      11.657      57.072      67.327     -10.254
               1500      12.212      63.062      72.176     -45.202
               2000      12.480      69.239      75.728     -82.218
               2400      12.647      74.266      78.019    -112.980
        =========== =========== =========== =========== ===========
    """,
)

entry(
    index = 13,
    label = "SO",
    molecule =
"""
multiplicity 3
1 S u1 p2 c0 {2,S}
2 O u1 p2 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([7.22,7.55,7.84,8.08,8.43,8.62,8.95],'cal/(mol*K)'),
        H298 = (1.2,'kcal/mol','+|-',0.3),
        S298 = (53.01,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc =
    u"""
    R.J. Kee, F.M. Rupley, J.A. Miller, The Chemkin Thermodynamic Data Base, Sandia Report SAND87-8215, Sandia National Laboratories, Livermore, California, 1991
    As reported by: P. Glarborg, D. Kubel, K Dam-Johansen, H-M. Chiang, J.W. Bozzelli, Int. J. Chem. Kin., 1996, 28(10), 773-790, doi: 10.1002/(SICI)1097-4601(1996)28:10<773::AID-KIN8>3.0.CO;2-K
    H298 is taken from Table 7 in P.A. Denis, J. Sulfur Chem. 2008, 29(3-4), 327-352, doi: 10.1080/17415990802047352
    """,
)

entry(
    index = 14,
    label = "SO2",
    molecule =
"""
1 S u0 p1 c0 {2,D} {3,D}
2 O u0 p2 c0 {1,D}
3 O u0 p2 c0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([9.54,10.41,11.12,11.71,12.55,13.03,13.61],'cal/(mol*K)'),
        H298 = (-70.94,'kcal/mol','+|-',0.05),
        S298 = (59.29,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc =
    u"""
    R.J. Kee, F.M. Rupley, J.A. Miller, The Chemkin Thermodynamic Data Base, Sandia Report SAND87-8215, Sandia National Laboratories, Livermore, California, 1991
    As reported by: P. Glarborg, D. Kubel, K Dam-Johansen, H-M. Chiang, J.W. Bozzelli, Int. J. Chem. Kin., 1996, 28(10), 773-790, doi: 10.1002/(SICI)1097-4601(1996)28:10<773::AID-KIN8>3.0.CO;2-K
    H298 is taken from Table 7 in P.A. Denis, J. Sulfur Chem. 2008, 29(3-4), 327-352, doi: 10.1080/17415990802047352
    """,
)

entry(
    index = 15,
    label = "SO2(T)",
    molecule =
"""
multiplicity 3
1 O u1 p2 c0 {2,S}
2 S u1 p1 c0 {1,S} {3,D}
3 O u0 p2 c0 {2,D}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.98165, 0.00101162, 1.85563e-05, -3.48567e-08, 1.89672e-11, -567.276, 7.74439],
                Tmin = (10, 'K'),
                Tmax = (628.385, 'K'),
            ),
            NASAPolynomial(
                coeffs = [3.8789, 0.0062633, -4.95469e-06, 1.73009e-09, -2.21003e-13, -645.136, 7.47009],
                Tmin = (628.385, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (-4.72505, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (58.2013, 'J/(mol*K)'),
    ),
    shortDesc = u"""UCCSD(T)-F12a/cc-pVTZ-f12//UM06-2x/cc-pVTZ""",
    longDesc =
    u"""
    SMILES: [O][S]=O

    calculated by alongd (xq1112, xc1063) at the UCCSD(T)-F12a/cc-pVTZ-f12//UM06-2x/cc-pVTZ level of theory
    frequencies calculated at UM06-2x/cc-pVTZ
    (no rotors)

    Thermodynamics for SO2(T):
        Enthalpy of formation (298 K)   =     1.526 kcal/mol
        Entropy of formation (298 K)    =    62.167 cal/(mol*K)
        =========== =========== =========== =========== ===========
        Temperature Heat cap.   Enthalpy    Entropy     Free energy
        (K)         (cal/mol*K) (kcal/mol)  (cal/mol*K) (kcal/mol)
        =========== =========== =========== =========== ===========
                300      10.269       1.547      62.235     -17.124
                400      11.148       2.619      65.314     -23.507
                500      11.834       3.770      67.879     -30.170
                600      12.317       4.979      70.082     -37.070
                800      12.944       7.510      73.719     -51.465
               1000      13.308      10.139      76.650     -66.511
               1500      13.604      16.890      82.121    -106.292
               2000      13.695      23.713      86.046    -148.379
               2400      13.823      29.216      88.554    -183.314
        =========== =========== =========== =========== ===========
    """,
)

entry(
    index = 16,
    label = "OOS(T)",
    molecule =
"""
multiplicity 3
1 O u1 p2 c0 {2,S}
2 O u0 p2 c0 {1,S} {3,S}
3 S u1 p2 c0 {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.96096, 0.00261375, 2.4909e-05, -6.85964e-08, 5.17961e-11, 32260.3, 8.78751],
                Tmin = (10, 'K'),
                Tmax = (482.017, 'K'),
            ),
            NASAPolynomial(
                coeffs = [4.54997, 0.00476677, -3.70181e-06, 1.2788e-09, -1.62367e-13, 32121.7, 5.52727],
                Tmin = (482.017, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (268.22, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (58.2013, 'J/(mol*K)'),
    ),
    shortDesc = u"""UCCSD(T)-F12a/cc-pVTZ-f12//UM06-2x/cc-pVTZ""",
    longDesc =
    u"""
    SMILES: [O]O[S]

    calculated by alongd (xq1116, xc1067) at the UCCSD(T)-F12a/cc-pVTZ-f12//UM06-2x/cc-pVTZ level of theory
    frequencies calculated at UM06-2x/cc-pVTZ
    (no rotors)

    Thermodynamics for OOS(T):
        Enthalpy of formation (298 K)   =    66.900 kcal/mol
        Entropy of formation (298 K)    =    65.052 cal/(mol*K)
        =========== =========== =========== =========== ===========
        Temperature Heat cap.   Enthalpy    Entropy     Free energy
        (K)         (cal/mol*K) (kcal/mol)  (cal/mol*K) (kcal/mol)
        =========== =========== =========== =========== ===========
               300      11.038      66.922      65.126      47.385
               400      11.780      68.066      68.411      40.702
               500      12.236      69.269      71.092      33.722
               600      12.584      70.510      73.355      26.497
               800      13.081      73.081      77.049      11.441
              1000      13.377      75.729      80.003      -4.274
              1500      13.642      82.502      85.492     -45.735
              2000      13.729      89.344      89.428     -89.511
              2400      13.829      94.856      91.940    -125.799
        =========== =========== =========== =========== ===========
    """,
)

entry(
    index = 17,
    label = "SO3",
    molecule =
"""
1 S u0 p0 c0 {2,D} {3,D} {4,D}
2 O u0 p2 c0 {1,D}
3 O u0 p2 c0 {1,D}
4 O u0 p2 c0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([12.17,13.76,15.05,16.07,17.45,18.16,19.02],'cal/(mol*K)'),
        H298 = (-94.6,'kcal/mol'),
        S298 = (61.34,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc =
    u"""
    R.J. Kee, F.M. Rupley, J.A. Miller, The Chemkin Thermodynamic Data Base, Sandia Report SAND87-8215, Sandia National Laboratories, Livermore, California, 1991
    As reported by: P. Glarborg, D. Kubel, K Dam-Johansen, H-M. Chiang, J.W. Bozzelli, Int. J. Chem. Kin., 1996, 28(10), 773-790, doi: 10.1002/(SICI)1097-4601(1996)28:10<773::AID-KIN8>3.0.CO;2-K
    """,
)

entry(
    index = 18,
    label = "HSO",
    molecule =
"""
multiplicity 2
1 S u1 p1 c0 {2,S} {3,D}
2 H u0 p0 c0 {1,S}
3 O u0 p2 c0 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,700,1000,1300,2000],'K'),
        Cpdata = ([36.15,38.6,41.4,45.8,50.1,52.7,55.6],'J/(mol*K)'),
        H298 = (-5.2,'kcal/mol','+|-',0.5),
        S298 = (57.65,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc =
    u"""
    A. Goumri, D. Laakso, J‐D R. Rocha, C.E. Smith, P. Marshall
    The Journal of Chemical Physics 102, 161 (1995)
    doi: 10.1063/1.469387
    Table V.
    Cp(200K) = 33.7; Cp(300K) interpolated
    H298 is taken from Table 7 in P.A. Denis, J. Sulfur Chem. 2008, 29(3-4), 327-352, doi: 10.1080/17415990802047352
    """,
)

entry(
    index = 19,
    label = "HOS",
    molecule =
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {3,S}
2 S u1 p2 c0 {1,S}
3 H u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,700,1000,1300,2000],'K'),
        Cpdata = ([36.85,39.6,42.0,45.3,48.6,50.9,54.2],'J/(mol*K)'),
        H298 = (-1.6,'kcal/mol','+|-',0.5),
        S298 = (57.48,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc =
    u"""
    A. Goumri, D. Laakso, J‐D R. Rocha, C.E. Smith, P. Marshall
    The Journal of Chemical Physics 102, 161 (1995)
    doi: 10.1063/1.469387
    Table VI.
    Cp(200K) = 34.1; Cp(300K) interpolated
    H298 is taken from Table 7 in P.A. Denis, J. Sulfur Chem. 2008, 29(3-4), 327-352, doi: 10.1080/17415990802047352
    """,
)

entry(
    index = 20,
    label = "HSS",
    molecule =
"""
multiplicity 2
1 S u1 p1 c0 {2,D} {3,S}
2 S u0 p2 c0 {1,D}
3 H u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([9.62,10.30,10.80,11.19,11.80,12.26,12.98],'cal/(mol*K)'),
        H298 = (25.0,'kcal/mol','+|-',0.5),
        S298 = (60.95,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc =
    u"""
    Taken from the SulfurGlarborgH2S library with comment:
    Zhou - K. Sendt, B.S. Haynes, J. Phys. Chem. A 109 (2005) 8180 to 8186;
    K. Sendt, M. Jazbec, B.S. Haynes, Proc. Combust. Inst. 29 (2003) 2439-2446.
    25.84  60.94
    H298 is taken from Table 7 in P.A. Denis, J. Sulfur Chem. 2008, 29(3-4), 327-352, doi: 10.1080/17415990802047352
    """,
)

entry(
    index = 21,
    label = "HSSH",
    molecule =
"""
1 S u0 p2 c0 {2,S} {3,S}
2 S u0 p2 c0 {1,S} {4,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.63,12.90,13.84,14.57,15.73,16.62,18.02],'cal/(mol*K)'),
        H298 = (3.70,'kcal/mol','+|-',0.5),
        S298 = (61.62,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc =
    u"""
    Taken from the SulfurGlarborgH2S library with comment:
    Zhou - K. Sendt, B.S. Haynes, J. Phys. Chem. A 109 (2005) 8180 to 8186;
    K. Sendt, M. Jazbec, B.S. Haynes, Proc. Combust. Inst. 29 (2003) 2439-2446.
    3.70  61.61
    H298 (updated uncertainty) is taken from Table 7 in P.A. Denis, J. Sulfur Chem. 2008, 29(3-4), 327-352, doi: 10.1080/17415990802047352
    """,
)

entry(
    index = 22,
    label = "HSOH",
    molecule =
"""
1 O u0 p2 c0 {2,S} {3,S}
2 S u0 p2 c0 {1,S} {4,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([49.66,56.19,60.09,64.27,68.62,71.38,75.68],'J/(mol*K)'),
        H298 = (-118.83,'kJ/mol','+|-',4.2),
        S298 = (270.4,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc =
    u"""
    UMP2=full/6-31G+
    A. Goumri, J-D.R. Rocha, D. Laakso, C.E. Smith, P. Marshall
    The Journal of Chemical Physics 101, 9405 (1994); doi: http://dx.doi.org/10.1063/1.467971
    As reported by: M.U. Alzueta, R. Bilbao, P. Glarborg, Comb. Flame, 2001, 127(4) 2234-2251, doi: 10.1016/S0010-2180(01)00325-X
    H298 is taken from Table 7 in P.A. Denis, J. Sulfur Chem. 2008, 29(3-4), 327-352, doi: 10.1080/17415990802047352
    This is significantly different that the value reported  by Marshall 1994 (-236.3 kJ/mol),
    but in agreement with SulfurGlargotgBozzelli library that took it from a currently untraceable source.
    Also in agreement with Table 8 in P.A. Denis, Molecular Physics 2008, 106(21-23), 2557-2567, doi: 10.1080/00268970802603523
    """,
)

entry(
    index = 23,
    label = "H2SO",
    molecule =
"""
1 S u0 p1 c0 {2,D} {3,S} {4,S}
2 O u0 p2 c0 {1,D}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([9.53,11.13,12.66,13.95,15.82,17.00,18.44],'cal/(mol*K)'),
        H298 = (-12.5,'kcal/mol','+|-',1),
        S298 = (57.26,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc =
    u"""
    H.M. Chiang, J.W. Bozzelli, Quantum Rice–Ramsberger–Kassel (QRRK) Analysis on Reaction of HSO + O, H + SO2, and OH + SO; HO2 and HOSO Formation and Dissociation
    As reported by: P. Glarborg, D. Kubel, K Dam-Johansen, H-M. Chiang, J.W. Bozzelli, Int. J. Chem. Kin., 1996, 28(10), 773-790, doi: 10.1002/(SICI)1097-4601(1996)28:10<773::AID-KIN8>3.0.CO;2-K
    H298 is taken from Table 7 in P.A. Denis, J. Sulfur Chem. 2008, 29(3-4), 327-352, doi: 10.1080/17415990802047352
    """,
)

entry(
    index = 24,
    label = "HSO2",
    molecule =
"""
multiplicity 2
1 O u0 p2 c0 {2,D}
2 S u1 p0 c0 {1,D} {3,D} {4,S}
3 O u0 p2 c0 {2,D}
4 H u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.94,13.68,14.99,15.97,17.28,18.05,18.98],'cal/(mol*K)'),
        H298 = (-33.8,'kcal/mol'),
        S298 = (63.68,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc =
    u"""
    H.M. Chiang, J.W. Bozzelli, Quantum Rice–Ramsberger–Kassel (QRRK) Analysis on Reaction of HSO + O, H + SO2, and OH + SO; HO2 and HOSO Formation and Dissociation
    As reported by: P. Glarborg, D. Kubel, K Dam-Johansen, H-M. Chiang, J.W. Bozzelli, Int. J. Chem. Kin., 1996, 28(10), 773-790, doi: 10.1002/(SICI)1097-4601(1996)28:10<773::AID-KIN8>3.0.CO;2-K
    Also available from:
    A. Goumri, J-D.R. Rocha, D. Laakso, C.E. Smith, P. Marshall, J. Phys. Chem. A, 1999, 103, 11328-11335, doi: 10.1021/jp9924070; Table 3; MP2=FULL/6-31G(d)
    """,
)

entry(
    index = 25,
    label = "HOSHO",
    molecule =
"""
1 O u0 p2 c0 {2,S} {4,S}
2 S u0 p1 c0 {1,S} {3,D} {5,S}
3 O u0 p2 c0 {2,D}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([13.58,15.84,17.65,19.01,20.82,21.95,23.54],'cal/(mol*K)'),
        H298 = (-64.5,'kcal/mol'),
        S298 = (64.48,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc =
    u"""
    H.M. Chiang, J.W. Bozzelli, Quantum Rice–Ramsberger–Kassel (QRRK) Analysis on Reaction of HSO + O, H + SO2, and OH + SO; HO2 and HOSO Formation and Dissociation
    As reported by: P. Glarborg, D. Kubel, K Dam-Johansen, H-M. Chiang, J.W. Bozzelli, Int. J. Chem. Kin., 1996, 28(10), 773-790, doi: 10.1002/(SICI)1097-4601(1996)28:10<773::AID-KIN8>3.0.CO;2-K
    """,
)

entry(
    index = 26,
    label = "HOSO2",
    molecule =
"""
multiplicity 2
1 S u0 p1 c0 {2,S} {3,D} {4,S}
2 O u0 p2 c0 {1,S} {5,S}
3 O u0 p2 c0 {1,D}
4 O u1 p2 c0 {1,S}
5 H u0 p0 c0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([16.74,18.76,20.13,21.07,22.22,22.94,24.02],'cal/(mol*K)'),
        H298 = (-89.4,'kcal/mol','+|-',0.72),
        S298 = (70.72,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc =
    u"""
    H.M. Chiang, J.W. Bozzelli, Quantum Rice–Ramsberger–Kassel (QRRK) Analysis on Reaction of HSO + O, H + SO2, and OH + SO; HO2 and HOSO Formation and Dissociation
    As reported by: P. Glarborg, D. Kubel, K Dam-Johansen, H-M. Chiang, J.W. Bozzelli, Int. J. Chem. Kin., 1996, 28(10), 773-790, doi: 10.1002/(SICI)1097-4601(1996)28:10<773::AID-KIN8>3.0.CO;2-K
    H298 is calculated at fc-CCSD(T)/cc-pV(T+d)Z and taken from W. Klopper, D.P. Tew, N. Gonzalez-Garcia, M. Olzmann, J. Chem. Phys. 2008, 129, 114308, doi: 10.1063/1.2973637
    """,
)

entry(
    index=27,
    label="HSOO",
    molecule=
    """
    multiplicity 2
    1 S u0 p2 c0 {2,S} {4,S}
    2 O u0 p2 c0 {1,S} {3,S}
    3 O u1 p2 c0 {2,S}
    4 H u0 p0 c0 {1,S}
    """,
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.86474, 0.0135584, -2.40972e-05, 2.93163e-08, -1.55426e-11, 14275.4, 9.88043],
                Tmin = (10, 'K'),
                Tmax = (448.899, 'K'),
            ),
            NASAPolynomial(
                coeffs = [4.48696, 0.00801407, -5.57065e-06, 1.8022e-09, -2.19497e-13, 14219.5, 7.37697],
                Tmin = (448.899, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (118.694, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (78.9875, 'J/(mol*K)'),
    ),
    shortDesc=u"""CCSD(T)-F12a/cc-pVTZ-f12//B3LYP/6-311G(2d,d,p)""",
    longDesc=
    u"""
    SMILES: SO[O]

    calculated by alongd (xq1174, xc1086) at the CCSD(T)-F12a/cc-pVTZ-f12//B3LYP/6-311G(2d,d,p) level of theory
    frequencies calculated at B3LYP/6-311G(2d,d,p)
    rotor calculated at B3LYP/6-311G(2d,pd)

    Thermodynamics for HSOO:
        Enthalpy of formation (298 K)   =    31.531 kcal/mol
        Entropy of formation (298 K)    =    69.744 cal/(mol*K)
        =========== =========== =========== =========== ===========
        Temperature Heat cap.   Enthalpy    Entropy     Free energy
        (K)         (cal/mol*K) (kcal/mol)  (cal/mol*K) (kcal/mol)
        =========== =========== =========== =========== ===========
               300      12.776      31.557      69.830      10.608
               400      13.733      32.884      73.641       3.427
               500      14.532      34.298      76.794      -4.099
               600      15.204      35.786      79.504     -11.917
               800      16.227      38.935      84.028     -28.287
              1000      16.917      42.255      87.728     -45.473
              1500      17.776      50.965      94.780     -91.205
              2000      18.159      59.955      99.950    -139.944
              2400      18.412      67.271     103.283    -180.610
        =========== =========== =========== =========== ===========
    """,
)

entry(
    index = 28,
    label = "HOSO",
    molecule =
"""
multiplicity 2
1 O u0 p2 c0 {2,S} {4,S}
2 S u1 p1 c0 {1,S} {3,D}
3 O u0 p2 c0 {2,D}
4 H u0 p0 c0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,700,1000,1300,2500],'K'),
        Cpdata = ([53.4,57.1,60.1,64.3,68.3,71.1,74.7],'J/(mol*K)'),
        H298 = (-241.4,'kJ/mol'),
        S298 = (282.3,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc =
    u"""
    Table 4
    MP2=FULL/6-31G(d)
    A. Goumri, J-D.R. Rocha, D. Laakso, C.E. Smith, P. Marshall
    J. Phys. Chem. A, 1999, 103, 11328-11335, doi: 10.1021/jp9924070
    also available from:
    H.M. Chiang, J.W. Bozzelli, Quantum Rice–Ramsberger–Kassel (QRRK) Analysis on Reaction of HSO + O, H + SO2, and OH + SO; HO2 and HOSO Formation and Dissociation
    As reported by: P. Glarborg, D. Kubel, K Dam-Johansen, H-M. Chiang, J.W. Bozzelli, Int. J. Chem. Kin., 1996, 28(10), 773-790, doi: 10.1002/(SICI)1097-4601(1996)28:10<773::AID-KIN8>3.0.CO;2-K
    """,
)

entry(
    index = 29,
    label = "HSOS",
    molecule =
"""
multiplicity 2
1 S u0 p2 c0 {2,S} {4,S}
2 O u0 p2 c0 {1,S} {3,S}
3 S u1 p2 c0 {2,S}
4 H u0 p0 c0 {1,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.76439, 0.0252802, -0.000110467, 2.55957e-07, -2.17671e-10, 13066.9, 9.29384],
                Tmin = (10, 'K'),
                Tmax = (362.811, 'K'),
            ),
            NASAPolynomial(
                coeffs = [4.59981, 0.00798713, -5.55392e-06, 1.77626e-09, -2.13294e-13, 13059.5, 6.84355],
                Tmin = (362.811, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (108.638, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (78.9875, 'J/(mol*K)'),
    ),
    shortDesc = u"""UCCSD(T)-F12a/cc-pVTZ-f12//UM06-2x/cc-pVTZ""",
    longDesc =
    u"""
    SMILES: SO[S]

    calculated by alongd (xq1112, xc1063) at the UCCSD(T)-F12a/cc-pVTZ-f12//UM06-2x/cc-pVTZ level of theory
    frequencies calculated at UM06-2x/cc-pVTZ
    rotor calculated at ub3lyp/6-311++g(df,pd)

    Thermodynamics for HSOS:
        Enthalpy of formation (298 K)   =    29.290 kcal/mol
        Entropy of formation (298 K)    =    69.944 cal/(mol*K)
        =========== =========== =========== =========== ===========
        Temperature Heat cap.   Enthalpy    Entropy     Free energy
        (K)         (cal/mol*K) (kcal/mol)  (cal/mol*K) (kcal/mol)
        =========== =========== =========== =========== ===========
               300      13.024      29.316      70.031       8.306
               400      13.939      30.664      73.905       1.102
               500      14.732      32.099      77.103      -6.452
               600      15.398      33.606      79.849     -14.303
               800      16.409      36.794      84.427     -30.748
              1000      17.082      40.147      88.166     -48.019
              1500      17.883      48.926      95.274     -93.985
              2000      18.194      57.953     100.466    -142.979
              2400      18.395      65.271     103.801    -183.851
        =========== =========== =========== =========== ===========
    """,
)

entry(
    index = 30,
    label = "O2ScycOO",
    molecule =
"""
1 O u0 p2 c0 {2,D}
2 S u0 p0 c0 {1,D} {3,D} {4,S} {5,S}
3 O u0 p2 c0 {2,D}
4 O u0 p2 c0 {2,S} {5,S}
5 O u0 p2 c0 {2,S} {4,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.93153, 0.00394097, 6.00801e-05, -1.23616e-07, 7.28108e-11, -35195.9, 8.63709],
                Tmin = (10, 'K'),
                Tmax = (593.33, 'K'),
            ),
            NASAPolynomial(
                coeffs = [4.45657, 0.0166144, -1.29477e-05, 4.4926e-09, -5.7278e-13, -35543.6, 3.97325],
                Tmin = (593.33, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (-292.664, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (108.088, 'J/(mol*K)'),
    ),
    shortDesc = u"""CCSD(T)-F12a/cc-pVTZ-f12//M06-2x/cc-pVTZ""",
    longDesc =
    u"""
    SMILES: O=S1(=O)OO1

    calculated by alongd (xq1112, xc1063) at the CCSD(T)-F12a/cc-pVTZ-f12//M06-2x/cc-pVTZ level of theory
    frequencies calculated at M06-2x/cc-pVTZ
    (no rotors)

    Thermodynamics for O2ScycOO:
        Enthalpy of formation (298 K)   =   -66.629 kcal/mol
        Entropy of formation (298 K)    =    67.427 cal/(mol*K)
        =========== =========== =========== =========== ===========
        Temperature Heat cap.   Enthalpy    Entropy     Free energy
        (K)         (cal/mol*K) (kcal/mol)  (cal/mol*K) (kcal/mol)
        =========== =========== =========== =========== ===========
               300      15.447     -66.598      67.530     -86.857
               400      18.030     -64.919      72.343     -93.856
               500      19.913     -63.016      76.582    -101.307
               600      21.184     -60.957      80.332    -109.156
               800      22.907     -56.534      86.682    -125.880
              1000      23.932     -51.841      91.914    -143.755
              1500      24.857     -39.581     101.844    -192.346
              2000      25.179     -27.074     109.037    -245.149
              2400      25.544     -16.931     113.660    -289.714
        =========== =========== =========== =========== ===========
    """,
)

entry(
    index = 31,
    label = "cycOOS",
    molecule =
"""
1 O u0 p2 c0 {2,S} {3,S}
2 O u0 p2 c0 {1,S} {3,S}
3 S u0 p2 c0 {1,S} {2,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [4.05319, -0.00458038, 4.32509e-05, -7.36568e-08, 3.97671e-11, 19631.5, 7.5508],
                Tmin = (10, 'K'),
                Tmax = (616.814, 'K'),
            ),
            NASAPolynomial(
                coeffs = [3.74301, 0.00630752, -4.81298e-06, 1.62255e-09, -2.00437e-13, 19500.9, 7.52857],
                Tmin = (616.814, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (163.223, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (58.2013, 'J/(mol*K)'),
    ),
    shortDesc = u"""CCSD(T)-F12a/cc-pVTZ-f12//M06-2x/cc-pVTZ""",
    longDesc =
    u"""
    SMILES: O1OS1

    calculated by alongd (xq1119, xc1070) at the CCSD(T)-F12a/cc-pVTZ-f12//M06-2x/cc-pVTZ level of theory
    frequencies calculated at M06-2x/cc-pVTZ

    Thermodynamics for cycOOS:
        Enthalpy of formation (298 K)   =    41.515 kcal/mol
        Entropy of formation (298 K)    =    60.861 cal/(mol*K)
        =========== =========== =========== =========== ===========
        Temperature Heat cap.   Enthalpy    Entropy     Free energy
        (K)         (cal/mol*K) (kcal/mol)  (cal/mol*K) (kcal/mol)
        =========== =========== =========== =========== ===========
               300       9.747      41.534      60.926      23.256
               400      10.821      42.564      63.882      17.011
               500      11.633      43.689      66.389      10.495
               600      12.160      44.881      68.560       3.745
               800      12.832      47.385      72.158     -10.341
              1000      13.234      49.996      75.069     -25.073
              1500      13.585      56.727      80.522     -64.057
              2000      13.671      63.540      84.442    -105.344
              2400      13.788      69.031      86.945    -139.636
        =========== =========== =========== =========== ===========
    """,
)

entry(
    index = 32,
    label = "cycOOSS",
    molecule =
"""
1 O u0 p2 c0 {2,S} {4,S}
2 O u0 p2 c0 {1,S} {3,S}
3 S u0 p2 c0 {2,S} {4,S}
4 S u0 p2 c0 {1,S} {3,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.93391, 0.00383934, 4.67573e-05, -1.03421e-07, 6.33246e-11, 27935.9, 9.35695],
                Tmin = (10, 'K'),
                Tmax = (591.303, 'K'),
            ),
            NASAPolynomial(
                coeffs = [5.28612, 0.0101553, -8.49195e-06, 3.09661e-09, -4.09322e-13, 27505.6, 1.2579],
                Tmin = (591.303, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (232.245, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (83.1447, 'J/(mol*K)'),
    ),
    shortDesc = u"""CCSD(T)-F12a/cc-pVTZ-f12//M06-2x/cc-pVTZ""",
    longDesc =
    u"""
    SMILES: O1OSS1

    calculated by alongd (xq1118, xc1069) at the CCSD(T)-F12a/cc-pVTZ-f12//M06-2x/cc-pVTZ level of theory
    frequencies calculated at M06-2x/cc-pVTZ

    Thermodynamics for cycOOSS:
        Enthalpy of formation (298 K)   =    58.656 kcal/mol
        Entropy of formation (298 K)    =    67.966 cal/(mol*K)
        =========== =========== =========== =========== ===========
        Temperature Heat cap.   Enthalpy    Entropy     Free energy
        (K)         (cal/mol*K) (kcal/mol)  (cal/mol*K) (kcal/mol)
        =========== =========== =========== =========== ===========
               300      13.939      58.684      68.059      38.267
               400      15.804      60.176      72.338      31.241
               500      17.036      61.824      76.009      23.819
               600      17.762      63.566      79.185      16.056
               800      18.667      67.218      84.430      -0.327
              1000      19.150      71.005      88.654     -17.649
              1500      19.457      80.688      96.502     -64.065
              2000      19.579      90.438     102.111    -113.784
              2400      19.817      98.317     105.702    -155.367
        =========== =========== =========== =========== ===========
    """,
)

entry(
    index = 33,
    label = "H2SO4",
    molecule =
"""
1 S u0 p0 c0 {2,D} {3,D} {4,S} {5,S}
2 O u0 p2 c0 {1,D}
3 O u0 p2 c0 {1,D}
4 O u0 p2 c0 {1,S} {6,S}
5 O u0 p2 c0 {1,S} {7,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {5,S}
""",
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.82425, 0.0119047, 0.000109424, -3.15925e-07, 2.47803e-10, -91732.6, 8.87386],
                Tmin = (10, 'K'),
                Tmax = (471.056, 'K'),
            ),
            NASAPolynomial(
                coeffs = [7.04982, 0.0173189, -1.22766e-05, 4.15079e-09, -5.29527e-13, -92400.4, -8.12269],
                Tmin = (471.056, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (-762.735, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (153.818, 'J/(mol*K)'),
    ),
    shortDesc=u"""UCCSD(T)-F12a/cc-pVTZ-f12//B3LYP/6-311G(2d,d,p)""",
    longDesc=
    u"""
    SMILES: OS(=O)(=O)O

    calculated by alongd (xq1173, xc1085) at the UCCSD(T)-F12a/cc-pVTZ-f12//B3LYP/6-311G(2d,d,p) level of theory
    frequencies calculated at B3LYP/6-311G(2d,d,p)
    rotors calculated at B3LYP/6-311G(2d,pd)

    Thermodynamics for H2SO4:
        Enthalpy of formation (298 K)   =  -178.065 kcal/mol
        Entropy of formation (298 K)    =    73.067 cal/(mol*K)
        =========== =========== =========== =========== ===========
        Temperature Heat cap.   Enthalpy    Entropy     Free energy
        (K)         (cal/mol*K) (kcal/mol)  (cal/mol*K) (kcal/mol)
        =========== =========== =========== =========== ===========
               300      21.305    -178.022      73.210    -199.985
               400      24.281    -175.730      79.784    -207.643
               500      26.084    -173.206      85.408    -215.910
               600      27.522    -170.524      90.294    -224.700
               800      29.721    -164.786      98.533    -243.612
              1000      31.226    -158.681     105.337    -264.018
              1500      33.254    -142.490     118.439    -320.149
              2000      34.409    -125.564     128.170    -381.904
              2400      35.202    -111.636     134.517    -434.476
        =========== =========== =========== =========== ===========
    """,
)

entry(
    index=34,
    label="HSO2OO",
    molecule=
    """
multiplicity 2
1 O u0 p2 c0 {2,D}
2 S u0 p0 c0 {1,D} {3,S} {4,D} {5,S}
3 H u0 p0 c0 {2,S}
4 O u0 p2 c0 {2,D}
5 O u0 p2 c0 {2,S} {6,S}
6 O u1 p2 c0 {5,S}
    """,
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.79167, 0.0166396, 5.60531e-05, -1.97213e-07, 1.66845e-10, -28503.7, 11.2581],
                Tmin = (10, 'K'),
                Tmax = (449.043, 'K'),
            ),
            NASAPolynomial(
                coeffs = [5.95215, 0.0173632, -1.30682e-05, 4.43954e-09, -5.57766e-13, -28899, 0.323081],
                Tmin = (449.043, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (-237.008, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (128.874, 'J/(mol*K)'),
    ),
    shortDesc=u"""CCSD(T)-F12a/cc-pVTZ-f12//B3LYP/6-311G(2d,d,p)""",
    longDesc=
    u"""
    SMILES: [O]O[SH](=O)=O

    calculated by alongd (xq1167, xc1079) at the CCSD(T)-F12a/cc-pVTZ-f12//B3LYP/6-311G(2d,d,p) level of theory
    frequencies calculated at B3LYP/6-311G(2d,d,p)
    rotor calculated at B3LYP/6-311G(2d,pd)

    Thermodynamics for HSO2OO:
        Enthalpy of formation (298 K)   =   -52.563 kcal/mol
        Entropy of formation (298 K)    =    77.295 cal/(mol*K)
        =========== =========== =========== =========== ===========
        Temperature Heat cap.   Enthalpy    Entropy     Free energy
        (K)         (cal/mol*K) (kcal/mol)  (cal/mol*K) (kcal/mol)
        =========== =========== =========== =========== ===========
               300      19.584     -52.524      77.426     -75.752
               400      21.990     -50.436      83.416     -83.803
               500      23.621     -48.152      88.506     -92.405
               600      24.944     -45.722      92.933    -101.482
               800      26.874     -40.526     100.394    -120.841
              1000      28.077     -35.021     106.531    -141.552
              1500      29.318     -20.602     118.207    -197.912
              2000      29.803      -5.820     126.709    -259.237
              2400      30.240       6.189     132.181    -311.046
        =========== =========== =========== =========== ===========
    """,
)

entry(
    index=35,
    label="HSO3",
    molecule=
    """
multiplicity 2
1 S u0 p0 c0 {2,S} {3,D} {4,D} {5,S}
2 H u0 p0 c0 {1,S}
3 O u0 p2 c0 {1,D}
4 O u0 p2 c0 {1,D}
5 O u1 p2 c0 {1,S}
    """,
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.92255, 0.0129065, -8.44739e-07, -8.83705e-09, 4.38872e-12, -16579, 8.38917],
                Tmin = (10, 'K'),
                Tmax = (957.734, 'K'),
            ),
            NASAPolynomial(
                coeffs = [6.26213, 0.00958261, -5.73674e-06, 1.59724e-09, -1.69777e-13, -17322.8, -4.34062],
                Tmin = (957.734, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (-137.825, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (108.088, 'J/(mol*K)'),
    ),
    shortDesc=u"""CCSD(T)-F12a/cc-pVTZ-f12//B3LYP/6-311G(2d,d,p)""",
    longDesc=
    u"""
    SMILES: [O][SH](=O)=O

    calculated by alongd (xq1168, xc1080) at the CCSD(T)-F12a/cc-pVTZ-f12//B3LYP/6-311G(2d,d,p) level of theory
    frequencies calculated at B3LYP/6-311G(2d,d,p)

    Thermodynamics for HSO3:
        Enthalpy of formation (298 K)   =   -29.530 kcal/mol
        Entropy of formation (298 K)    =    68.510 cal/(mol*K)
        =========== =========== =========== =========== ===========
        Temperature Heat cap.   Enthalpy    Entropy     Free energy
        (K)         (cal/mol*K) (kcal/mol)  (cal/mol*K) (kcal/mol)
        =========== =========== =========== =========== ===========
               300      14.935     -29.500      68.610     -50.083
               400      16.885     -27.906      73.180     -57.178
               500      18.549     -26.132      77.132     -64.698
               600      19.916     -24.207      80.639     -72.590
               800      21.820     -20.016      86.654     -89.339
              1000      22.923     -15.533      91.652    -107.184
              1500      24.362      -3.655     101.264    -155.551
              2000      24.923       8.686     108.361    -208.035
              2400      25.166      18.707     112.927    -252.319
        =========== =========== =========== =========== ===========
    """,
)

entry(
    index=36,
    label="HOSO3",
    molecule=
    """
multiplicity 2
1 O u1 p2 c0 {2,S}
2 S u0 p0 c0 {1,S} {3,D} {4,D} {5,S}
3 O u0 p2 c0 {2,D}
4 O u0 p2 c0 {2,D}
5 O u0 p2 c0 {2,S} {6,S}
6 H u0 p0 c0 {5,S}
    """,
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.85754, 0.0099495, 8.51696e-05, -2.46189e-07, 1.94906e-10, -63517.7, 11.0751],
                Tmin = (10, 'K'),
                Tmax = (458.746, 'K'),
            ),
            NASAPolynomial(
                coeffs = [5.63474, 0.0171977, -1.28996e-05, 4.40463e-09, -5.5626e-13, -63920.1, 1.27755],
                Tmin = (458.746, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (-528.134, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (128.874, 'J/(mol*K)'),
    ),
    shortDesc=u"""CCSD(T)-F12a/cc-pVTZ-f12//B3LYP/6-311G(2d,d,p)""",
    longDesc=
    u"""
    SMILES: [O]S(=O)(=O)O

    calculated by alongd (xq1170, xc1082) at the CCSD(T)-F12a/cc-pVTZ-f12//B3LYP/6-311G(2d,d,p) level of theory
    frequencies calculated at B3LYP/6-311G(2d,d,p)
    rotor calculated at B3LYP/6-311G(2d,pd)

    Thermodynamics for HOSO3:
        Enthalpy of formation (298 K)   =  -122.350 kcal/mol
        Entropy of formation (298 K)    =    75.536 cal/(mol*K)
        =========== =========== =========== =========== ===========
        Temperature Heat cap.   Enthalpy    Entropy     Free energy
        (K)         (cal/mol*K) (kcal/mol)  (cal/mol*K) (kcal/mol)
        =========== =========== =========== =========== ===========
               300      18.758    -122.313      75.661    -145.011
               400      21.259    -120.302      81.428    -152.873
               500      22.902    -118.090      86.357    -161.269
               600      24.222    -115.732      90.653    -170.124
               800      26.161    -110.679      97.907    -189.005
              1000      27.386    -105.315     103.887    -209.202
              1500      28.729     -91.218     115.300    -264.169
              2000      29.349     -76.697     123.651    -324.000
              2400      29.892     -64.849     129.050    -374.569
        =========== =========== =========== =========== ===========
    """,
)

entry(
    index=37,
    label="SO4(T)",
    molecule=
    """
multiplicity 3
1 O u1 p2 c0 {2,S}
2 S u0 p0 c0 {1,S} {3,D} {4,D} {5,S}
3 O u0 p2 c0 {2,D}
4 O u0 p2 c0 {2,D}
5 O u1 p2 c0 {2,S}
    """,
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.87898, 0.00756363, 7.69807e-05, -1.95254e-07, 1.34821e-10, -32083.1, 9.11986],
                Tmin = (10, 'K'),
                Tmax = (532.188, 'K'),
            ),
            NASAPolynomial(
                coeffs = [6.41676, 0.0136579, -1.11352e-05, 3.99257e-09, -5.21782e-13, -32709.7, -4.87131],
                Tmin = (532.188, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (-266.792, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (108.088, 'J/(mol*K)'),
    ),
    shortDesc=u"""CCSD(T)-F12a/cc-pVTZ-f12//B3LYP/6-311G(2d,d,p)""",
    longDesc=
    u"""
    SMILES: [O]S(=O)(=O)[O]

    calculated by alongd (xq1171, xc1083) at the CCSD(T)-F12a/cc-pVTZ-f12//B3LYP/6-311G(2d,d,p) level of theory
    frequencies calculated at B3LYP/6-311G(2d,d,p)

    Thermodynamics for SO4(T):
        Enthalpy of formation (298 K)   =   -60.081 kcal/mol
        Entropy of formation (298 K)    =    70.415 cal/(mol*K)
        =========== =========== =========== =========== ===========
        Temperature Heat cap.   Enthalpy    Entropy     Free energy
        (K)         (cal/mol*K) (kcal/mol)  (cal/mol*K) (kcal/mol)
        =========== =========== =========== =========== ===========
               300      17.679     -60.046      70.533     -81.206
               400      20.223     -58.141      75.995     -88.539
               500      21.711     -56.037      80.684     -96.379
               600      22.649     -53.817      84.729    -104.654
               800      23.940     -49.147      91.438    -122.297
              1000      24.662     -44.279      96.866    -141.145
              1500      25.203     -31.767     107.005    -192.274
              2000      25.404     -19.124     114.278    -247.680
              2400      25.712      -8.902     118.937    -294.349
        =========== =========== =========== =========== ===========
    """,
)

entry(
    index=37,
    label="HSOOH",
    molecule=
    """
1 S u0 p2 c0 {2,S} {4,S}
2 O u0 p2 c0 {1,S} {3,S}
3 O u0 p2 c0 {2,S} {5,S}
4 H u0 p0 c0 {1,S}
5 H u0 p0 c0 {3,S}
    """,
    thermo = NASA(
        polynomials = [
            NASAPolynomial(
                coeffs = [3.84407, 0.0150566, 5.35225e-05, -3.37418e-07, 4.77338e-10, -5883.48, 7.95668],
                Tmin = (10, 'K'),
                Tmax = (278.49, 'K'),
            ),
            NASAPolynomial(
                coeffs = [5.11563, 0.0116763, -8.43568e-06, 2.80455e-09, -3.4898e-13, -6012.02, 2.41143],
                Tmin = (278.49, 'K'),
                Tmax = (3000, 'K'),
            ),
        ],
        Tmin = (10, 'K'),
        Tmax = (3000, 'K'),
        E0 = (-48.9027, 'kJ/mol'),
        Cp0 = (33.2579, 'J/(mol*K)'),
        CpInf = (99.7737, 'J/(mol*K)'),
    ),
    shortDesc=u"""CCSD(T)-F12a/cc-pVTZ-f12//B3LYP/6-311G(2d,d,p)""",
    longDesc=
    u"""
    SMILES: [O]S(=O)(=O)[O]

    calculated by alongd (xq1175, xc1087) at the CCSD(T)-F12a/cc-pVTZ-f12//B3LYP/6-311G(2d,d,p) level of theory
    frequencies calculated at B3LYP/6-311G(2d,d,p)
    rotors calculated at B3LYP/6-311G(2d,pd)

    Thermodynamics for HSOOH:
        Enthalpy of formation (298 K)   =    -8.025 kcal/mol
        Entropy of formation (298 K)    =    68.926 cal/(mol*K)
        =========== =========== =========== =========== ===========
        Temperature Heat cap.   Enthalpy    Entropy     Free energy
        (K)         (cal/mol*K) (kcal/mol)  (cal/mol*K) (kcal/mol)
        =========== =========== =========== =========== ===========
               300      15.763      -7.993      69.031     -28.702
               400      17.104      -6.348      73.755     -35.850
               500      18.230      -4.580      77.696     -43.428
               600      19.167      -2.708      81.105     -51.371
               800      20.569       1.275      86.825     -68.185
              1000      21.485       5.487      91.521     -86.034
              1500      22.552      16.547     100.475    -134.166
              2000      23.008      27.943     107.029    -186.115
              2400      23.332      37.213     111.253    -229.795
        =========== =========== =========== =========== ===========
    """,
)
