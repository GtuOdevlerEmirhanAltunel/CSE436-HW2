# CSE436 Assignment 1 Report

> Name: Emirhan Altunel
> Student ID: 200104004035

## How you designed the layouts?

### 2-input Carry Ripple Adder

First i create a full adder layout, then i connect first full adder's carry output to the second full adder's carry input. In this way, i create a 2-input carry ripple adder.

To create a full adder, i only use NAND gates. Because using different gates would be more complex and harder to design.

My full adder layout:

<img src="./assets/first.png" style="width: 40%">

> I know it is not quite clear but it will be more clear with the next diagram.

It is basically redesigned version of the bottom diagram.

<img src="./assets/full.png" style="width: 40%">

In magic layout tool:

<img src="./assets/full_mag.png" style="width: 60%">

> I have to redesign my nand gates, because i have to connect them to each other. As you can see bottom part of the each nand gate is moved to the left side.

## How you extracted the netlist and set up the simulation?

When i finished my design, i use these command in magic layout tool to extract:

```bash
extract all
ext2spice
```

.include /output/tsmc_cmos025

Then, i add these lines to the extracted spice file:

```spice
* Include the technology file
.include /output/tsmc_cmos025

* Set the voltage difference between vdd and gnd
V0 vdd gnd 2.5V


* Define the A1 and A2 as input signals
V1 a1 gnd PULSE(0 2.5 0ns 0ns 0ns 20ns 40ns)
V3 a2 gnd PULSE(0 2.5 0ns 0ns 0ns 60ns 120ns)

* Define the B1 and B2 as input signals
V2 b1 gnd PULSE(0 2.5 0ns 0ns 0ns 40ns 80ns)
V4 b2 gnd PULSE(0 2.5 0ns 0ns 0ns 120ns 240ns)

* Define the carry in signal
V5 cin gnd PULSE(0 2.5 0ns 0ns 0ns 240ns 480ns)


* Add capacitors to the output
* I increased the capacitance to decrease the spikes
CL0 s1 0 20fF
CL1 s2 0 20fF
CL2 cout 0 20fF

* Set the simulation length as 100ns
* I also decreased the time step to 10ps, it makes the simulation more clear
.TRAN 10ps 1000ns

* Add models otherwise it doesnt work
.model nfet NMOS
.model pfet PMOS

* Export the data to file, i use python to plot the data
* But ngspice can plot the data too
* .plot v(a1) v(a2) v(b1) v(b2) v(cin) v(s1) v(s2) v(cout)
.control
run
wrdata output_file.dat v(a1) v(a2) v(b1) v(b2) v(cin) v(s1) v(s2) v(cout)
.endc
```

## Plots

<img src="./assets/full2.png" style="width: 40%">

> Seperated outputs

<img src="./assets/full2_sum.png" style="width: 40%">

> I combine A1 and A2, B1 and B2, S1 and S2 and Cout

As you can see, the output gives sum of A and B and the carry in.
