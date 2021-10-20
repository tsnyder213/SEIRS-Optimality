# An Optimal Control Experiment for an SEIRS Epidemiological Model

### What does it do?

This script takes a variety of parameters into account to find an optimal control solution for an SEIRS epidemic. Optimal in this case means maintaining control of the number of infected individuals at the cheapest cost of control (whether it be doses of a vaccine or some other control). The script has values for the initial (S)usceptible population, initial (I)nfected population, the maximum amount of control that can be applied, the rate of change in the population (from natural deaths/births/immigation/emigration), and how transmittible the disease is depending on control administered. It will run calculations obtaining the number of those infected but not infectious (E), those that are removed from the population via infection related deaths (R), and those that will be newly infected depending on the control rate at each time step. It will then make a decision at each time step on what rate of control to apply to keep these numbers in check while keeping cost as low as possible. It determines cost based on a cost function that uses the rate of control, cost of a newly infected individual, and cost to treat the currently infected as factors.

### How does it work?

The script runs through every possible scenario for each discrete time step, creating a decision tree. When it finds a branch that is more optimal than another, it prunes the less optimal and continues on the new path. It does this repeatedly until the end of the dictated time period and results in a treatment plan that keeps the infection under control while costing the least amount possible. At the end, it prints a graph of the treatment plan or the number of infectives.

### How do I use it?

To use the script, you can use as-is or input your own parameters. You can tweak bmin and bmax (minimal transmission rate and maximum tranmission rate depending on control applied), S (number of initial susceptible individuals), I (number of initial infected individuals), CI (cost of an infected individual), population growth rate (currently hard-coded at 1.02 based on U.S. Census data), and more. At the end, you can choose to plot either y (treatment plan) or y2 (number of infective individuals) in relation to the time period.

**Created with [readmegenerator.com](https://readmegenerator.com) -- build a beautiful ReadMe!**