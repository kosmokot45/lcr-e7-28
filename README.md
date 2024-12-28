### GUI app for controlling the immittance meter E7-28, conducting experiments, measurements, plotting graphs and saving results in different formats.

**Protocol**

**rs232**;  baud rate: 9600; paritet: false; stop: 1

app->lcr 0xAA, NUM_COMMAND, [parameters]

lcr->app 0xAA, NUM_COMMAND, [parameters]

**Commads**

| Command | APP ask | LCR answer | Info|
|---------|---------|------------|--|
| lcr name| 0xAA, 64    | 0xAA, 64, "E728"     |
| turn on avp | lcr (0xAA, 65)     | lcr (0xAA, 65)      |
| turn off avp | (0xAA, 66)    | (0xAA, 66)     |
| set frequency | (0xAA, 67, f4, f3, f2, f1)    | (0xAA, 67)      |f1, f2, f3, f4 - 4 bytes of integer number |
| set bias | (0xAA, 70, U1, U0)    |  (0xAA, 70)     | U1, U0 - 2 bytes (int16) * 10|
| reset | (0xAA, 71)    | (0xAA, 71)     ||
| get info | lcr (0xAA, 72, 0)    | (0xAA, 72, flags, mode, slow, diap, U1, U0, f3..f0, Z3..Z0,fi3..fi0)     | see below \\/|
| ... | ...    | ...     | ... |


**Get info command**

    flags: bits
        0 - AVP
        1 - Current (not available)
        2 - Restart
        3 - Parameter autoset
        4 - Equivalence circuit (1-parallel, 0-series)
        7 - The measurement cycle is complete
    mode: parameter from leyboard?
        0- F1..3- F2
    slow: measurement speed
        0 - fast
        1 - normal
        2 - averaging over 10
    diap: measurement range
        0 - 10 MOm
        1 - 1 MOm
        2 - 100 kOm
        3 - 10 kOm
        4 - 1 kOm
        5 - 100 Om
        6 - 10 Om
        7 - 1 Om
    Uсм1, Uсм0: 2 bytes (int16) * 10
    f3..f0: 4 bytes (int32) working frequency
    f3..f0: 4 bytes (float) complex impedance module for the final equivalent circuit
    fi3..fi0: 4 bytes (float) phase angle for the last equivalent circuit
real, float is transferred to radians (fi*57.2957795)

    |Y| = 1/|Z|; fiy = -fiz(parallel equivalent circuit)
    Rs = |Z|*Cos(fiz); Xs = |Z|*Sin(fiz)
    Gp = |Y|*Cos(fiy); Bp = |Z|*Sin(fiy)
    Rp = 1/Gp; Xp = 1/Bp
    Gs = 1/Rs; Bs = 1/Xs
    C = 1/2*pi*f*X; L = 2*pi*f*X

TODO:
- [ x ] - connection with simple script
- [ ] - collect all byte-commands
- [ ] - draw simple gui with main functional
- [ ] - mode switcher
- [ ] - plots

to be continue...

--------

`pyside`

```bash
# run qt-designer
pyside6-designer
```

```bash
# convert ui to python code
pyside6-uic main.ui -o ui_main.py
```