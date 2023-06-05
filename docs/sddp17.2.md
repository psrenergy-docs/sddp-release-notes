---
title: "SDDP 17.2"
nav_order: 2
---

# SDDP 17.2.5rc4

📅 Date: 2023-06-05<br>
🔗 Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.2.5rc4-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.2.5rc4-setup-linux.zip)

## New features and improvements

* Model
  * adjusts the joint reserve output to not be limited to the reserve requirement when
    the reserve is defined with a >= sign


# SDDP 17.2.5rc3

📅 Date: 2023-05-26<br>
🔗 Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.2.5rc3-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.2.5rc3-setup-linux.zip)

## Fixed bugs

* Model
  * Hourly representation
    * adjusted the target storage integration in chronological blocks execution


# SDDP 17.2.5rc2

📅 Date: 2023-05-25<br>
🔗 Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.2.5rc2-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.2.5rc2-setup-linux.zip)

## Fixed bugs

* Model
  * included the hydro bypass flow in the minimum/maximum total outflow constraints for the
    hydro plant FROM

* GUI
  * included missing attributes in the export/import of the fuel contract configuration


# SDDP 17.2.5rc1

📅 Date: 2023-05-22<br>
🔗 Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.2.5rc1-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.2.5rc1-setup-linux.zip)

## Fixed bugs

* Model
  * fixed an issue in cases with integral fuel contracts modeled with unlimited fuel contracted amount
    and without Take-or-Pay amount


# SDDP 17.2.4

📅 Date: 2023-05-19<br>
🔗 Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.2.4-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.2.4-setup-linux.zip)

Official release


# SDDP 17.2.4rc4

📅 Date: 2023-05-12<br>
🔗 Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.2.4rc4-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.2.4rc4-setup-linux.zip)

## Fixed bugs

* Model
  * fixed the writing of the risk aversion curve limit when the maximum turbining of an existing plant was zero


# SDDP 17.2.4rc3

📅 Date: 2023-05-12<br>
🔗 Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.2.4rc3-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.2.4rc3-setup-linux.zip)

## New features and improvements

* Model
  * new outputs in the hourly model: total inelastic load per class, maximum load of each class and maximum load 
    of each bus

* GUI
  * included the import/export of general constraints


# SDDP 17.2.4rc2

📅 Date: 2023-05-08<br>
🔗 Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.2.4rc2-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.2.4rc2-setup-linux.zip)

## Fixed bugs

* Model
  * fixed an error in the execution of stochastic cases without hydro reservoirs and with other
    types of state variable


# SDDP 17.2.4rc1

📅 Date: 2023-05-02<br>
🔗 Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.2.4rc1-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.2.4rc1-setup-linux.zip)

## Fixed bugs

* Model
  * fixed the application of the chronological sensitivity inflow factors when the simulation
    horizon starts after the beginning of the policy horizon


# SDDP 17.2.3

📅 Date: 2023-04-14<br>
🔗 Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.2.3-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.2.3-setup-linux.zip)

## New features and improvements

* Model
  * relaxed the concavity validation for some hydro tables, to result in a warning
    rather than an error (storage x production, storage x area, storage x infiltration,
    storage x elevation). The concavity validation continues to be tightened for the
    following tables: inflow x turb. and storage x maximum turb. 


# SDDP 17.2.3rc3

📅 Date: 2023-04-13<br>
🔗 Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.2.3rc3-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.2.3rc3-setup-linux.zip)

## New features and improvements

* Model
  * Hourly representation
    * added the system stored energy 65% U.S. output

## Fixed bugs

* Model
  *  fixed execution error with Python 3 in Linux


# SDDP 17.2.3rc2

📅 Date: 2023-04-10<br>
🔗 Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.2.3rc2-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.2.3rc2-setup-linux.zip)

## New features and improvements

* Model
  * added CSP nominal capacity output


# SDDP 17.2.3rc1

📅 Date: 2023-04-10<br>
🔗 Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.2.3rc1-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.2.3rc1-setup-linux.zip)

## Fixed bugs

* Model
  * improved the validation for cases with a reserve area and without network 
    representation


# SDDP 17.2.2

📅 Date: 2023-04-03<br>
🔗 Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.2.2-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.2.2-setup-linux.zip)

## Fixed bugs

* GUI
  * fixed thermal maintenance data loading issue


# SDDP 17.2.2rc6

📅 Date: 2023-03-30<br>
🔗 Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.2.2rc6-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.2.2rc6-setup-linux.zip)

## Fixed bugs

* Model
  * improved the concavity validation for hydro tables


# SDDP 17.2.2rc5

📅 Date: 2023-03-29<br>
🔗 Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.2.2rc5-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.2.2rc5-setup-linux.zip)

## New features and improvements

* Model
  * removed an unnecessary validation of the storage x maximum turbining table


# SDDP 17.2.2rc4

📅 Date: 2023-03-29<br>
🔗 Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.2.2rc4-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.2.2rc4-setup-linux.zip)

## New features and improvements

* Model
  * Hourly representation
    * added the thermal single reserve and the hydro single reserve outputs


# SDDP 17.2.2rc3

📅 Date: 2023-03-28<br>
🔗 Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.2.2rc3-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.2.2rc3-setup-linux.zip)

## Fixed bugs

* GUI
  * fixed a specific issue in the creation of demand scenarios in weekly cases
  * fixed the selection of the "general" option for the flexible demand data resolution


# SDDP 17.2.2rc2

📅 Date: 2023-03-17<br>
🔗 Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.2.2rc2-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.2.2rc2-setup-linux.zip)

## Fixed bugs

* GUI
  * fixed the data visualization of non-thermolelectrical gas demand


# SDDP 17.2.2rc1

📅 Date: 2023-03-16<br>
🔗 Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.2.2rc1-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.2.2rc1-setup-linux.zip)

## Fixed bugs

* Model
  * fixed the application of the thermal minimum generation constraint when the
    constraint requirement is defined as a percentage of the nominal capacity


# SDDP 17.2.1

📅 Date: 2023-03-13<br>
🔗 Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.2.1-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.2.1-setup-linux.zip)

## Fixed bugs

* Model
  * fixed the application of the thermal minimum generation constraint when the
    constraint requirement is defined as a percentage of the nominal capacity


# SDDP 17.2.1rc23

📅 Date: 2023-03-09<br>
🔗 Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.2.1rc23-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.2.1rc23-setup-linux.zip)

## New features and improvements

* Model
  * improved the representation of the hydro turbining x inflow table constraints


# SDDP 17.2.1rc22

📅 Date: 2023-03-08<br>
🔗 Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.2.1rc22-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.2.1rc22-setup-linux.zip)

## Fixed bugs

* Model
  * fixed the initial iteration for the application of the non-convexity representation
    and the hybrid stage resolution in the policy, for cases with rolling horizon or
    coordinated operative mode


# SDDP 17.2.1rc21

📅 Date: 2023-03-07<br>
🔗 Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.2.1rc21-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.2.1rc21-setup-linux.zip)

## Fixed bugs

* Model
  * fixed the print of total number of problems in parallel execution
  * Hourly representation
    * fixed the application of the hydro maximum turbining chronological data


# SDDP 17.2.1rc20

📅 Date: 2023-03-06<br>
🔗 Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.2.1rc20-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.2.1rc20-setup-linux.zip)

## Fixed bugs

* Model
  * fixed specific encoding related issue in Linux execution


# SDDP 17.2.1rc19

📅 Date: 2023-03-01<br>
🔗 Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.2.1rc19-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.2.1rc19-setup-linux.zip)

## Fixed bugs

* Model
  * adjusted the application of the spillage penalty for hydro plants with the representation of
    turbining as a function of the inflow


# SDDP 17.2.1rc18

📅 Date: 2023-03-01<br>
🔗 Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.2.1rc18-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.2.1rc18-setup-linux.zip)

## Fixed bugs

* Model
  * Hourly representation
    *  adjusted the hydro spilled energy and the system spilled energy outputs for future plants


# SDDP 17.2.1rc17

📅 Date: 2023-02-15<br>
🔗 Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.2.1rc17-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.2.1rc17-setup-linux.zip)

## Fixed bugs

* GUI
  * fixed the import/export of the hydro plant non-controllable spillage field

* Model
  * fixed MIP solution strategy to avoid infeasibility due to solver numerical precision issues
  * Hourly representation
    * included the representation of the gas network non-thermoelectrical demand


# SDDP 17.2.1rc16

📅 Date: 2023-02-13<br>
🔗 Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.2.1rc16-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.2.1rc16-setup-linux.zip)

## Fixed bugs

* Model
  * fixed the writing of the hydro capacity by plant without outages output in
    hourly executions


# SDDP 17.2.1rc15

📅 Date: 2023-02-08<br>
🔗 Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.2.1rc15-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.2.1rc15-setup-linux.zip)

## New features and improvements

* Setup
  * included the possibility to download model add-ins during installation


# SDDP 17.2.1rc14

📅 Date: 2023-02-02<br>
🔗 Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.2.1rc14-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.2.1rc14-setup-linux.zip)

## Fixed bugs

* Model
  * fixed the selection of outputs for writing in hourly cases


# SDDP 17.2.1rc13

📅 Date: 2023-01-31<br>
🔗 Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.2.1rc13-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.2.1rc13-setup-linux.zip)

## Fixed bugs

* GUI
  * fixed the import/export of the thermal operating constraints screen


# SDDP 17.2.1rc12

📅 Date: 2023-01-30<br>
🔗 Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.2.1rc12-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.2.1rc12-setup-linux.zip)

## Fixed bugs

* Model
  * fixed the writing of the hydro capacity by plant without outages output in
    hourly executions


# SDDP 17.2.1rc11

📅 Date: 2023-01-25<br>
🔗 Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.2.1rc11-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.2.1rc11-setup-linux.zip)

## Fixed bugs

* GUI
  * included the failure duration field in the import/export of the renewable plant
    configuration, thermal plant configuration and hydro plant configuration screens


# SDDP 17.2.1rc10

📅 Date: 2023-01-17<br>
🔗 Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.2.1rc10-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.2.1rc10-setup-linux.zip)

## Fixed bugs

* Model
  * Hourly representation
    * included the new hourly solution status (linearized solution) in the dashboard


# SDDP 17.2.1rc9

📅 Date: 2023-01-17<br>
🔗 Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.2.1rc9-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.2.1rc9-setup-linux.zip)

## Fixed bugs

* Model
  * removed unnecessary validation of the last year for inflow parameters estimation against
    the historical inflow data horizon


# SDDP 17.2.1rc8

📅 Date: 2023-01-17<br>
🔗 Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.2.1rc8-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.2.1rc8-setup-linux.zip)

## Fixed bugs

* Model
  * Hourly representation
    * fixed an issue in the application of the hydro/thermal plant maintenance schedule


# SDDP 17.2.1rc7

📅 Date: 2023-01-12<br>
🔗 Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.2.1rc7-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.2.1rc7-setup-linux.zip)

## New features and improvements

* Model
  * included the possibility to select the directory in which the TSL renewable
    scenario file (gndforh.dat) is located


# SDDP 17.2.1rc6

📅 Date: 2022-01-11<br>
🔗 Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.2.1rc6-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.2.1rc6-setup-linux.zip)

## New features and improvements

* Model
  * improved the agent names in the active security constraint flag output


# SDDP 17.2.1rc5

📅 Date: 2022-01-11<br>
🔗 Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.2.1rc5-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.2.1rc5-setup-linux.zip)

## Fixed bugs

* Model
  * Hourly representation
    * fixed the writing of the active security constraint flag output


# SDDP 17.2.1rc4

📅 Date: 2023-01-05<br>
🔗 Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.2.1rc4-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.2.1rc4-setup-linux.zip)

## New features and improvements

* Model
  * extended the joint reserve constraints to allow multi-fuel thermal plants with
    different capacities


# SDDP 17.2.1rc3

📅 Date: 2023-01-04<br>
🔗 Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.2.1rc3-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.2.1rc3-setup-linux.zip)

## Fixed bugs

* Model
  * fixed an specific issue involving the presence of non-existent renewable plants
    in the renewable modification data


# SDDP 17.2.1rc2

📅 Date: 2022-12-28<br>
🔗 Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.2.1rc2-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.2.1rc2-setup-linux.zip)

## New features and improvements

* Model
  * unified the gas pipeline flow --> and the gas pipeline flow <-* outputs in a single
    output representing the net flow in the gas pipeline
  * included a validation of the hydro plant maximum storage in the modification data

## Fixed bugs

* Model
  * fixed the reading of historical inflows in cases with more than 999 hydro plants


# SDDP 17.2.1rc1

📅 Date: 2022-12-22<br>
🔗 Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.2.1rc1-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.2.1rc1-setup-linux.zip)

## New features and improvements

* Model
  * new outputs: renewable capacity scenario (in MW) and renewable O&M unitary cost
  * Hourly representation
    * added the writing of the renewable scenario output


# SDDP 17.2

📅 Date: 2022-12-17<br>
🔗 Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.2-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.2-setup-linux.zip)

Please refer to the [release site](http://psr-energy.com/software/sddp-17.2.html) for further information.