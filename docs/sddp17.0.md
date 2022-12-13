---
layout: default
title: "SDDP 17.0"
nav_order: 4
description: "SDDP 17.0 (detailed changelog)"
#permalink: "/:collection/:path/"
---

# SDDP 17.0.5 (2022-05-13)

🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.0.5-setup.zip) | [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.0.5-setup-linux.zip)

## New features and improvements

* Graph module
  * updated to version 3.1.3


# SDDP 17.0.5rc17 (2022-05-09)

🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.0.5rc17-setup.zip) | [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.0.5rc17-setup-linux.zip)

## New features and improvements

* Model
  * changed compiler options to ensure deterministic floating-point
    operations in different architectures

## Fixed bugs

* Model
  * fixed uninitialized variable for cases with Markov representation
  * fixed the calculation of penalties and bounds for hydro plants with
    production coefficient represented as a function of reservoir and
    variable tailwater elevation. This issue could cause non-deterministc
    results in parallel executions.


# SDDP 17.0.5rc16 (2022-04-29)

🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.0.5rc16-setup.zip) | [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.0.5rc16-setup-linux.zip)

## Fixed bugs

* Model
  * included memory deallocation for some structures


# SDDP 17.0.5rc15 (2022-04-28)

🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.0.5rc15-setup.zip) | [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.0.5rc15-setup-linux.zip)

## New features and improvements

* Model
  * Hourly resolution
    * new output: Minimum joint reserve requirement


# SDDP 17.0.5rc14 (2022-04-19)

🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.0.5rc14-setup.zip) | [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.0.5rc14-setup-linux.zip)

## New features and improvements

* Model
  * included the possibility to select the directory in which the FCF file
    is located for a simulation


# SDDP 17.0.5rc13 (2022-04-18)

🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.0.5rc13-setup.zip) | [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.0.5rc13-setup-linux.zip)

## New features and improvements

* PSRIO
  * updated to version 0.11.0

## Fixed bugs

* Model
  * fixed an issue in the NetPlan integration associated to power injetions


# SDDP 17.0.5rc12 (2022-04-11)

🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.0.5rc12-setup.zip) | [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.0.5rc12-setup-linux.zip)

## New features and improvements

  * Hourly representation
    * included the application of sensitivity factors for the
      interconnection capacities

## Fixed bugs

* Model
  * fixed an issue in the OptGen integration with hourly simulation


# SDDP 17.0.5rc11 (2022-04-05)

🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.0.5rc11-setup.zip) | [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.0.5rc11-setup-linux.zip)

## Fixed bugs

* Model
  * fixed a specific issue in the opening of output files


# SDDP 17.0.5rc10 (2022-04-01)

🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.0.5rc10-setup.zip) | [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.0.5rc10-setup-linux.zip)

## New features and improvements

* Model
  * Hourly representation
    * included a protection in the writing of outputs regarding emission
      budgets when there are no constraints defined


# SDDP 17.0.5rc9 (2022-03-31)

🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.0.5rc9-setup.zip) | [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.0.5rc9-setup-linux.zip)

## New features and improvements

* Model
  * Hourly representation
    * new output: renewable O&M cost


# SDDP 17.0.5rc8 (2022-03-29)

🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.0.5rc8-setup.zip) | [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.0.5rc8-setup-linux.zip)

## Fixed bugs

* Model
  * Hourly representation
    * fixed the modeling of DC links with quadratic losses representation


# SDDP 17.0.5rc7 (2022-03-28)

🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.0.5rc7-setup.zip) | [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.0.5rc7-setup-linux.zip)

## New features and improvements

* Model
  * included the application of the circuit rating power factor constant 
    in databases with NetPlan integration


# SDDP 17.0.5rc6 (2022-03-22)

🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.0.5rc6-setup.zip) | [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.0.5rc6-setup-linux.zip)

## New features and improvements

* Model
  * Hourly representation
    * new output: flag for active security constraint and start-up cost

## Fixed bugs

* Model
  * Hourly representation
    * fixed the consideration of the thermal chronological start-up cost
	

# SDDP 17.0.5rc5 (2022-03-09)

🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.0.5rc5-setup.zip) | [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.0.5rc5-setup-linux.zip)

## Fixed bugs

* Model
  * fixed a specific issue in the reading of the sum of circuit flow constraint modifications
  * Hourly representation
    * fixed the execution of cases with chronological blocks and without slicing


# SDDP 17.0.5rc4 (2022-03-09)

🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.0.5rc4-setup.zip) | [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.0.5rc4-setup-linux.zip)

## Fixed bugs

* Model
  * improved the representation of emission budget constraints, to avoid degenerate solutions
* Dashboard
  * fixed the breakdown of total operating costs chart to consider the discount rate


# SDDP 17.0.5rc3 (2022-03-08)

🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.0.5rc3-setup.zip) | [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.0.5rc3-setup-linux.zip)

## New features and improvements

* Model
  * changed the name of the thermal emissions per plant output from "emiter.csv/bin" to "teremi.csv/bin"


# SDDP 17.0.5rc2 (2022-03-07)

🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.0.5rc2-setup.zip) | [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.0.5rc2-setup-linux.zip)

## Fixed bugs

* Model
  * Hourly representation
    * fixed the reading of joint reserve constraints with dc links as backed elements


# SDDP 17.0.5rc1 (2022-03-03)

🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.0.5rc1-setup.zip) | [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.0.5rc1-setup-linux.zip)

## Fixed bugs

* Model
  * fixed the display of error messages in the inflow generation mode


# SDDP 17.0.4 (2022-02-24)

🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.0.4-setup.zip) | [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.0.4-setup-linux.zip)

Official release


# SDDP 17.0.4rc6 (2022-02-23)

🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.0.4rc6-setup.zip) | [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.0.4rc6-setup-linux.zip)

## New features and improvements

* Model
  * Hourly representation
    * new output: Load per class * supplied

## Fixed bugs

* Model
  * fixed hot-start execution with tolerance outlier convergence criterion


# SDDP 17.0.4rc6 (2022-02-17)

🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.0.4rc6-setup.zip) | [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.0.4rc6-setup-linux.zip)

## New features and improvements

* GUI
  * new strategy for filtering large datasets

## Fixed bugs

* Dynamic Probabilistic Reserve calculator
  * minor fixes


# SDDP 17.0.4rc5 (2022-02-16)

🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.0.4rc5-setup.zip) | [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.0.4rc5-setup-linux.zip)

## New features and improvements

* PSRIO
  * updated to version 0.10.2

## Fixed bugs

* Dynamic Probabilistic Reserve calculator
  * fixed the horizon of the dashboard file


# SDDP 17.0.4rc4 (2022-02-14)

🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.0.4rc4-setup.zip) | [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.0.4rc4-setup-linux.zip)

## New features and improvements

* Model
  * Hourly representation
    * improved representation of target storages in weekly studies
* GUI
  * updated installation process of the extensions
* PSRIO
  * updated to version 0.10.0

## Fixed bugs

* Inflow estimation
  * fixed warning messages


# SDDP 17.0.4rc3 (2022-02-02)

🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.0.4rc3-setup.zip) | [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.0.4rc3-setup-linux.zip)

## New features and improvements

* GUI
  * included log files in the zip file generated by the compact case data option


# SDDP 17.0.4rc2 (2022-01-31)

🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.0.4rc2-setup.zip) | [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.0.4rc2-setup-linux.zip)

## New features and improvements

* Model
  * changed the power injection representation to allow negative price values
* GUI
  * added the export/import functions for the sum of interconnection
    modification screen

## Fixed bugs

* GUI
  * fixed the name of the energy load hourly scenarios file in weekly cases
  * fixed an specific issue in the saving of implicit sensitivity factors
  * fixed an issue that allowed simulations of one scenario to be executed
    in parallel mode


# SDDP 17.0.4rc1 (2022-01-12)

🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.0.4rc1-setup.zip) | [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.0.4rc1-setup-linux.zip)

## New features and improvements

* GUI
  * added the export/import functions for the thermal emission
    coefficient screen

## Fixed bugs

  * fixed the name of the hour-block remap file in weekly cases


# SDDP 17.0.3 (2022-01-04)

🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.0.3-setup.zip) | [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.0.3-setup-linux.zip)

## New features and improvements

* Model
  * Hourly representation
    * new outputs: percentage of system stored energy and potential
      hydro spilled energy
    * enabled export/import outputs for electrical areas without
      defined limits
* GUI
  * added the export/import functions for the geographical location of
    buses


# SDDP 17.0.3rc7 (2021-12-28)

🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.0.3rc7-setup.zip) | [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.0.3rc7-setup-linux.zip)

## New features and improvements

* Model
  * Hourly representation
    * included security constraints on AC transmission

## Fixed bugs

* Dashboard
  * fixed an issue in the convergence map in deterministic cases


# SDDP 17.0.3rc6 (2021-12-20)

🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.0.3rc6-setup.zip) | [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.0.3rc6-setup-linux.zip)

## New features and improvements

* Model
  * Hourly representation
    * translation of objective function element names
* GUI
  * added the export/import functions for the penalties of hydro single
    reservoir constraints

## Fixed bugs

* GUI
  * fixed the saving of renewable scenarios for large amount of data
  * fixed the selection of electrification nodes of different systems


# SDDP 17.0.3rc5 (2021-12-09)

🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.0.3rc5-setup.zip) | [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.0.3rc5-setup-linux.zip)

## New features and improvements

* Model
  * Hourly representation
    * added the battery generation x bus marginal cost output


# SDDP 17.0.3rc4 (2021-12-06)

🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.0.3rc4-setup.zip) | [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.0.3rc4-setup-linux.zip)

## Fixed bugs

* Model
  * fixed the participation of batteries and electrification
    producers in the circuit flow limit constraints


# SDDP 17.0.3rc3 (2021-12-06)

🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.0.3rc3-setup.zip) | [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.0.3rc3-setup-linux.zip)

## Fixed bugs

* Model
  * fixed an issue in the OptGen integration with deterministic
    scenarios and binary outputs


# SDDP 17.0.3rc2 (2021-12-03)

🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.0.3rc2-setup.zip) | [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.0.3rc2-setup-linux.zip)

## Fixed bugs

* Model
  * Hourly representation
    * fixed the consideration of the thermal chronological
      minimum generation constraint violation penalty


# SDDP 17.0.3rc1 (2021-11-23)

🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.0.3rc1-setup.zip) | [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.0.3rc1-setup-linux.zip)

## Fixed bugs

* Model
  * includes a validation of the connection between batteries
    and buses in databases with NetPlan integration


# SDDP 17.0.2 (2021-11-19)

🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.0.2-setup.zip) | [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.0.2-setup-linux.zip)

## New features and improvements

* Model
  * new option for ensuring that the policy will be stopped when
    the gap is negative and greater than the tolerance


# SDDP 17.0.2rc2 (2021-11-18)

🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.0.2rc2-setup.zip) | [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.0.2rc2-setup-linux.zip)

## Fixed bugs

* Model
  * fixed the block aggregation of the power injection price data


# SDDP 17.0.2rc1 (2021-11-18)

🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.0.2rc1-setup.zip) | [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.0.2rc1-setup-linux.zip)

## New features and improvements

* Model
  * updated the version of PSRIO


# SDDP 17.0.1 (2021-11-11)

🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.0.1-setup.zip) | [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.0.1-setup-linux.zip)

## New features and improvements

* GUI
  * added the export/import functions for the fuel availability and
    consumption rate constraints chronological data


# SDDP 17.0.1rc6 (2021-11-09)

🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.0.1rc6-setup.zip) | [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.0.1rc6-setup-linux.zip)

## Fixed bugs

* Model
  * fixed the type of aggregation of the renewable dispatch factor output
* GUI
  * fixed the importation of load weekly data
  * fixed the saving of the joint reserve level


# SDDP 17.0.1rc5 (2021-11-07)

🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.0.1rc5-setup.zip) | [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.0.1rc5-setup-linux.zip)

## Fixed bugs

* GUI
  * fixed a specific error in the reading of the circuit modification data


# SDDP 17.0.1rc4 (2021-11-05)

🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.0.1rc4-setup.zip) | [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.0.1rc4-setup-linux.zip)

## Fixed bugs

* Model
  * Hourly representation
    * fixed the consideration of user-defined penalties for hydro operative
      storage constraints


# SDDP 17.0.1rc3 (2021-10-28)

🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.0.1rc3-setup.zip) | [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.0.1rc3-setup-linux.zip)

## Fixed bugs

* Model
  * considers the hydro production factor calculated after the solution of
    the problem for the writing of outputs of hydro plants with representation
    of the production factor as a function of the reservoir and variable
    tailwater elevation


# SDDP 17.0.1rc2 (2021-10-25)

🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.0.1rc2-setup.zip) | [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.0.1rc2-setup-linux.zip)

## Fixed bugs

* Model
  * Hourly representation
    * fixed an error in the representation of thermal plants with
      commitment and outage sampling


# SDDP 17.0.1rc1 (2021-10-13)

🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.0.1rc1-setup.zip) | [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.0.1rc1-setup-linux.zip)

## Fixed bugs

* Model
  * Hourly representation
    * fixed the network losses calculation 


# SDDP 17.0 (2021-10-06)

🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.0-setup.zip) | [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-17.0-setup-linux.zip)

Please refer to the "SDDP 17.0 Readme" file for the release notes:
* [English](https://www.psr-inc.com/wp-content/uploads/softwares/sddp/SddpReleaseNotesEng-17.0.pdf)
* [Español](https://www.psr-inc.com/wp-content/uploads/softwares/sddp/SddpReleaseNotesEsp-17.0.pdf)
* [Português](https://www.psr-inc.com/wp-content/uploads/softwares/sddp/SddpReleaseNotesPor-17.0.pdf)