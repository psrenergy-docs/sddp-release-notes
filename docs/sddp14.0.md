---
title: "SDDP 14.0"
nav_order: 8
---

# SDDP 14.0.19rc2

📅 Date: 2017-12-28<br>
🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.19rc2-setup.zip) \| [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.19rc2-setup-linux.zip)

## New Features and Improvements

* Model
  * new option to represent inflow correlation matrix per season
* Graph (updated from version 2.19 to 2.21)


# SDDP 14.0.19rc1

📅 Date: 2017-12-15<br>
🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.19rc1-setup.zip) \| [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.19rc1-setup-linux.zip)

## Fixed Bugs

* Model
  * fixed a validation error that disabled users to define tables of inflow x turbining with less than 5 points
* GUI
  * fixed an error that occured when deleting more than one element in modification data screens
  * fixed an error that occured when editing modification data of circuits that had their name altered using the importing tool


# SDDP 14.0.18

📅 Date: 2017-12-08<br>
🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.18-setup.zip) \| [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.18-setup-linux.zip)

## Fixed Bugs

* Model
  * fixed the unit of "Interchange sum marginal cost" output from k$/MWh to k$/MW
  * fixed the representation of turbining as a function of inflows constraints
    in case of repeated points informed in the table
* GUI
  * fixed an error while updating the multi-fuel column in Thermal configuration
    screen


# SDDP 14.0.18rc3

📅 Date: 2017-11-28<br>
🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.18rc3-setup.zip) \| [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.18rc3-setup-linux.zip)

## New Features and Improvements

* GUI
  * number of decimal places increased for sensitivity factors

## Fixed Bugs

* Model
  * fixed the unit of "Interchange sum marginal cost" output from k$/MWh to k$/MW
  * fixed the hardkey verification scheme in parallel executions
* GUI
  * fixed an error while copying maximum generation of multi-fuel thermal
    plants


# SDDP 14.0.17

📅 Date: 2017-11-16<br>
🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.17-setup.zip) \| [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.17-setup-linux.zip)

## New Features and Improvements

* Graph (updated from version 2.17 to 2.19)
* PowerView
  * implementation of new map interface control that are independent from
    third-party map providers

## Fixed Bugs

* Model
  * fixed an error in the type of aggregation per block for results below.
    The correct aggregation per block is the sum of the values of each block
    within the stages instead of weighted averaged by block duration.
    * Export&Import limits per area
    * Bus voltage angle
    * Interchange sum upper bound
    * Interchange sum lower bound
    * Violation minimum turb. outflow
    * Violation generation reserve
    * Interchange Cost
    * Deficit (% of load)        
    * Deficit per bus (% of load)
    * Thermal generation in MW
    * Flag for active security ctr.
  * fixed an error in the calculation of FCF cut coefficients for cases with 
    Markov inflow model representation
  * fixed an error in dynamic memory allocation for simulations with horizon that
    are different than policy horizon
* GUI
  * fixed an error while importing data of agents with same names but
    in different systems from Excel
  * fixed the integration with the PowerView tool
  * fixed an error while ordering columns and filtering elements by system in
    another screen


# SDDP 14.0.16

📅 Date: 2017-10-09<br>
🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.16-setup.zip) \| [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.16-setup-linux.zip)

## New Features and Improvements

* Model
  * improved some error messages and labels
  * improvement in the Markov inflow model to enhance convergence
* PSRCloud (updated to version 4.4.1)
  * it is now possible to run multiple instances simultaneously
* Graph (updated from version 2.15 to 2.17)
  * new option to use chart titles in the definition of file names.
    If selected, more meaningful file names will be used instead of the
    standard GRAF####.csv output file names.

## Fixed Bugs

* Model
  * fixed an error in the type of aggregation per block for results below.
    The correct aggregation per block is the sum of the values of each block
    within the stages instead of weighted averaged by block duration.
    * Marg. cost generation reserve
    * Marg. cost hydro spinning reserve
    * Marg. cost therm spinning reserve
* GUI
  * fixed an error while loading detailed data per block for renewable scenarios
  * fixed an error while opening the GUI in modification screen


# SDDP 14.0.15

📅 Date: 2017-09-12<br>
🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.15-setup.zip) \| [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.15-setup-linux.zip)

## Fixed Bugs

* GUI
  * fixed an error while showing the combined cycle thermal plants in 
    "Thermal plants > Operative state of combined cycle" screen
  * fixed the integration with the PowerView tool


# SDDP 14.0.14

📅 Date: 2017-08-31<br>
🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.14-setup.zip) \| [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.14-setup-linux.zip)

## Fixed Bugs

* GUI
  * fixed an error in the Demand configuration screen while filtering demands
    for systems without demands
  * fixed an error while importing demands if there are demands with same code
* Graph (updated from version 2.14 to 2.15)


# SDDP 14.0.14rc3

📅 Date: 2017-08-23<br>
🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.14rc3-setup.zip) \| [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.14rc3-setup-linux.zip)

## Fixed Bugs

* Model
  * fixed an error in the iterative circuit monitoring algorithm for cases with
    circuits with 5-digit codes


# SDDP 14.0.14rc2

📅 Date: 2017-08-22<br>
🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.14rc2-setup.zip) \| [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.14rc2-setup-linux.zip)

## Fixed Bugs

* Model
  * fixed an error in the iterative losses algorithm for cases with circuits with
    5-digit codes
  * fixed an error in the reserve violation cost printed in the 'Operation costs'
    report (sddpcope.csv)
* GUI
  * fixed an error when exporting bus data for Excel in the presence of buses without
    generators
  * fixed an error in the date field of sum of circuit flows modification screen when
    adding new modifications
  * fixed some translations


# SDDP 14.0.14rc1

📅 Date: 2017-07-24<br>
🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.14rc1-setup.zip) \| [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.14rc1-setup-linux.zip)

## Fixed Bugs

* Model
  * fixed an error in the automatic calculation of the risk aversion curve penalty
    for cases with transmission network representation
* GUI
  * fixed an error when updating generation constraints after deleting a thermal plant
  * fixed an error when deleting a renewable source plant without scenarios
  * fixed some errors in the import/export from/to CSV files functionality
  * fixed an error when saving annual profile of hourly renewable scenarios
  * fixed some translations
* Graph (updated from version 2.11 to 2.13)
  * fixed an error when copying graphics with horizon different from study
  * fixed an error when selecting initial or final stages if final or initial
    stages were not defined
  * fixed an error when copying graphics: the horizon type was not copied
    correctly
  * fixed an error when saving chart types different from standard


# SDDP 14.0.13

📅 Date: 2017-06-23<br>
🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.13-setup.zip) \| [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.13-setup-linux.zip)

## New Features and Improvements

* Model
  * the "Turbine capacity marg. cost" output has been changed to avoid positive
    values which indicate that there would be some benefit to have artificial
    negative turbined outflows
* PowerView (updated from version 1.8 to 1.10)
  * new functionality to automatically show results in MW instead of GWh
  * change in the graphical exhibition of generation to improve the perception
    of small changes in generation

## Fixed Bugs

* Model
  * fixed an error related to maximum turbining outflow constraint: the model
    was considering the minimum value of all previous stages instead of the
    current value defined in chronological data
* GUI
  * fixed an error while adding new reneweable scenarios
* PowerView (updated from version 1.8 to 1.10)
  * fixed an error in the visualization of future and disconnected circuits


# SDDP 14.0.13rc2

📅 Date: 2017-06-09<br>
🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.13rc2-setup.zip) \| [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.13rc2-setup-linux.zip)

## New Features and Improvements

* Model
  * new additional convergence criterion that rejects the convergence in
    case the ratio between the tolerance of the current iteration and the
    minimum tolerance obtained in the previous iterations is greater than
    a pre-defined threshold. This criterion is now activated by default.
* GUI
  * import/export from/to CSV files (Excel integration) extended to
    interconnection cost data

## Fixed Bugs

* GUI
  * fixed an error while handling (adding or removing) levels of elastic
    demands in demand configuration data
  * fixed an error in the search function in thermal configuration
    with combined cycle


# SDDP 14.0.13rc1

📅 Date: 2017-05-15<br>
🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.13rc1-setup.zip) \| [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.13rc1-setup-linux.zip)

## New Features and Improvements

* GUI
  * import/export from/to CSV files (Excel integration) extended to
    hydro and thermal maintenance data

## Fixed Bugs

* Model
  * fixed an error in "Thermal cost (oper+CO2 emission)" output: the total
    value was not accumulated correctly over the consumption segments and
    blocks
  * fixed an error in "CO2 emission cost by thermal" output: the emission
    coefficient was not considered in the calculation


# SDDP 14.0.12

📅 Date: 2017-04-29<br>
🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.12-setup.zip) \| [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.12-setup-linux.zip)

## New Features and Improvements

* GUI
  * "Import" feature improved to trim empty data at the begining and
    end of the chronological data

## Fixed Bugs

* Model
  * fixed the memory allocation of an internal structure that could
    consume a large ammount of memory and prevent model execution
    in cases with large number of stages and forward scenarios
* GUI
  * fixed an error in the detection of changes for saving data
    in circuit modification screen
  * fixed an error while saving hourly demand data
  * fixed an error updating list of elements information after importing
    external CSV file


# SDDP 14.0.11rev1

📅 Date: 2017-04-19<br>
🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.11rev1-setup.zip) \| [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.11rev1-setup-linux.zip)

## Fixed Bugs

* GUI
  * fixed an error in the calculation of the thermal operative costs


# SDDP 14.0.11

📅 Date: 2017-04-19<br>
🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.11-setup.zip) \| [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.11-setup-linux.zip)

## New Features and Improvements

* GUI
  * new "File > Import..." feature to import several CSV files at once
  * import/export from/to CSV files (Excel integration) extended to:
    * load per bus configuration
    * interconnection modification

## Fixed Bugs

* Model
  * fixed an error in the Markov inflow model
  * fixed an error related to the initialization of state variables related
    to fuel contracts that was causing infeasibilities in some specific cases
* GUI
  * fixed an error while editing fuel contract duration


# SDDP 14.0.11rc13

📅 Date: 2017-04-03<br>
🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.11rc13-setup.zip) \| [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.11rc13-setup-linux.zip)

## Fixed Bugs

* Model
  * fixed an error in fuel contract initialization for first iteration that
    could lead to infeasibilities


# SDDP 14.0.11rc12

📅 Date: 2017-03-31<br>
🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.11rc12-setup.zip) \| [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.11rc12-setup-linux.zip)

## New Features and Improvements

* Model
  * change in fuel contract modelling to avoid prevent fuel "spilling" before
    the end of the contract


# SDDP 14.0.11rc11

📅 Date: 2017-03-22<br>
🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.11rc11-setup.zip) \| [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.11rc11-setup-linux.zip)

## New Features and Improvements

* Model
  * new Markov inflow model

## Fixed Bugs

* GUI
  * fixed an error while saving secondary reserve prices data


# SDDP 14.0.11rc10

📅 Date: 2017-03-14<br>
🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.11rc10-setup.zip) \| [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.11rc10-setup-linux.zip)

## Fixed Bugs

* Model
  * fixed an error for cases with risk aversion curve and transmission network
    losses representation
* GUI
  * fixed an error in the search function in thermal secondary reserve screen


# SDDP 14.0.11rc9

📅 Date: 2017-03-06<br>
🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.11rc9-setup.zip) \| [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.11rc9-setup-linux.zip)

## New Features and Improvements

* Model
  * new input data option: detailed data per block for renewable scenarios (model
    only * to be included in GUI)


# SDDP 14.0.11rc8

📅 Date: 2017-03-06<br>
🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.11rc8-setup.zip) \| [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.11rc8-setup-linux.zip)

## Fixed Bugs

* Model
  * fixed an error that was activating the Markov inflow model by mistake when
    the the demand-inflow correlation feature was activated


# SDDP 14.0.11rc7

📅 Date: 2017-02-27<br>
🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.11rc7-setup.zip) \| [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.11rc7-setup-linux.zip)

## New Features and Improvements

* Model
  * New modelling: demand-inflow correlation
  * New sensitivity factors for interconnection capacities
  * New chronological data for single reservoir constraint: maximum turbining outflow
* GUI
  * import/export from/to CSV files (Excel integration) extended to
    DC link modification data

## Fixed Bugs

* Model
* GUI
  * fixed an error while importing gauging stations with names with more
    than 12 characters
  * fixed an error while creating new years for inflow data: new values were
    set to zero instead to blank values


# SDDP 14.0.11rc6

📅 Date: 2017-02-15<br>
🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.11rc6-setup.zip) \| [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.11rc6-setup-linux.zip)

## New Features and Improvements

* Model
  * New output: Stored energy per hydro plant


# SDDP 14.0.11rc5

📅 Date: 2017-01-30<br>
🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.11rc5-setup.zip) \| [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.11rc5-setup-linux.zip)

## New Features and Improvements

* GUI
  * new field in fuel contract screen to explicitly inform the duration of
    integral contracts

## Fixed Bugs

* Model
  * fixed an error in the representation of fuel contracts in policy phase when
    using aggregation of blocks
  * fixed OptGen integration for cases in which the hydro plant production factor
    was changed from zero to any a greater value
  * fixed an error while reading external initial inflows file for coordinated cases
* GUI
  * fixed an error while importing renewable scenarios per block from Excel


# SDDP 14.0.11rc4

📅 Date: 2017-01-13<br>
🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.11rc4-setup.zip) \| [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.11rc4-setup-linux.zip)

## Fixed Bugs

* Model
  * fixed an error in the representation of fuel availability constraint
    in hourly representation


# SDDP 14.0.11rc3

📅 Date: 2016-12-27<br>
🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.11rc3-setup.zip) \| [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.11rc3-setup-linux.zip)

## New Features and Improvements

* Model
  * redefinition of Xpress solver parameters to improve solution time of
    large-scale mixed integer problems in SDDP deterministic scenarios
    option, when used integrated with Optgen as operation model


# SDDP 14.0.11rc2

📅 Date: 2016-12-15<br>
🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.11rc2-setup.zip) \| [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.11rc2-setup-linux.zip)

## Fixed Bugs

* Model
  * fixed specific error in thermal plant capacity representation in
    policy phase
  * fixed OptGen integration for cases with excess of forced generation
    (minimum generation and/or renewable sources)


# SDDP 14.0.11rc1

📅 Date: 2016-12-08<br>
🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.11rc1-setup.zip) \| [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.11rc1-setup-linux.zip)

## New Features and Improvements

* Model
  * improvement in the modelling of secondary reserve involving DC links
    in order to avoid degenerated solutions with flows in both directions
    of DC links
* PowerView
  * update to version 1.8

## Fixed Bugs

* Model
  * fixed the integration with OptGen model for cases with secondary reserve


# SDDP 14.0.10

📅 Date: 2016-12-04<br>
🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.10-setup.zip) \| [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.10-setup-linux.zip)

## New Features and Improvements

* Model
  * Secondary reserve price
* Graph
  * update to version 2.10

## Fixed Bugs

* GUI
  * fixed an error associated to the reading of secondary reserve data that
    caused freezing while loading data


# SDDP 14.0.10rc12

📅 Date: 2016-11-23<br>
🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.10rc12-setup.zip) \| [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.10rc12-setup-linux.zip)

## Fixed Bugs

* Model
  * internal error in the definition of sequential renewable scenarios in hourly
    cases with less renewable scenarios than number of scenarios in study
* GUI
  * error adding demand hourly data to the begining of datatable


# SDDP 14.0.10rc11

📅 Date: 2016-11-11<br>
🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.10rc11-setup.zip) \| [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.10rc11-setup-linux.zip)

## Fixed Bugs

* Model
  * fixed the integration with OptGen model for cases with dead storage
    representation


# SDDP 14.0.10rc10

📅 Date: 2016-11-08<br>
🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.10rc10-setup.zip) \| [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.10rc10-setup-linux.zip)

## New Features and Improvements

* Model
  * change in the definition of seecondary reserve constraints that compensate
    DC links. All DC links involved in the constraint are now considered as a
    unique asset and the constraint requirement is redefined to the total flow
    above the emergency limit.
  * change in primary and secondary reserve outputs for hydro and thermal plants.
    The calculation has been changed to allow reserves to be greater than zero if
    generation is zero. For thermal plants with commitment, the reserve will be
    equal to zero if the plant is not committed.
* GUI
  * secondary reserve: DC links cannot be part of the backing group anymore


# SDDP 14.0.10rc9

📅 Date: 2016-11-01<br>
🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.10rc9-setup.zip) \| [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.10rc9-setup-linux.zip)

## New Features and Improvements

* Model
  * secondary reserve outputs extended to show results for each model constraint,
    related to each element in backed group
* GUI
  * new option in secondary reserve file indicating that the requirement is
    per plant or per unit


# SDDP 14.0.10rc8

📅 Date: 2016-10-28<br>
🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.10rc8-setup.zip) \| [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.10rc8-setup-linux.zip)

## New Features and Improvements

* Model
  * new option in secondary reserve file indicating that the requirement is
    per plant or per unit


# SDDP 14.0.10rc7

📅 Date: 2016-10-27<br>
🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.10rc7-setup.zip) \| [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.10rc7-setup-linux.zip)

## Fixed Bugs

* Model
  * fixed hydro and thermal secondary reserve output: reserve is now defined as zero
    for plants that don't participate in any of the reserve constraints
* Graph
  * update to version 2.10


# SDDP 14.0.10rc6

📅 Date: 2016-10-25<br>
🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.10rc6-setup.zip) \| [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.10rc6-setup-linux.zip)

## New Features and Improvements

* Model
  * automatic renewable generation spillage for cases without network representation or
    transmission represented by interconnection model
  * new outputs:
    * Renewable generation spillage
    * Circuit income (>0)
  * new maximum secondary reserve per plant constraint
  * new check to avoid negative values for hourly demand data
* GUI
  * import/export from/to CSV files (Excel integration):
    * extended to renewable sources scenarios
    * included renewable source plants network connection in bus configuration data


# SDDP 14.0.10rc5

📅 Date: 2016-10-03<br>
🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.10rc5-setup.zip) \| [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.10rc5-setup-linux.zip)

## New Features and Improvements

* Model
  * generation reserve output extended for all types of constraints (absolute and compensation)
    * generation reserve limit
    * generation reserve
    * marginal cost generation reserve
    * violation generation reserve
    * violation cost of generation reserve
  * new feature in generation reserve constraints: multiplicative and additive factors

## Fixed Bugs

* Model
  * possibe error when using DC Links in generation reserve constraints with block aggregation in
    policy phase
* GUI
  * error erasing hydro plants
  * error exporting empty Hour-Block mapping file to Excel


# SDDP 14.0.10rc4

📅 Date: 2016-09-22<br>
🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.10rc4-setup.zip) \| [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.10rc4-setup-linux.zip)

## New Features and Improvements

* Graph (update to version 2.8)
  * new subtitle indicating graph horizon
  * new options to define graph horizon:
    * study horizon (automatic)
    * custom horizon (user defined)
    * inherit horizon from other graph
  * new function to "copy horizon" from one graph to another

## Fixed Bugs

* GUI
  * error importing bus configuration and demand price data from CSV files


# SDDP 14.0.10rc3

📅 Date: 2016-09-15<br>
🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.10rc3-setup.zip) \| [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.10rc3-setup-linux.zip)

## New Features and Improvements

* Reliability analysis model (Coral)
  * performance improvement for problems with interconnection and transmission representation

## Fixed Bugs

* Reliability analysis model (Coral)
  * error when executing without renewable sources


# SDDP 14.0.10rc2

📅 Date: 2016-09-09<br>
🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.10rc2-setup.zip) \| [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.10rc2-setup-linux.zip)

## Fixed Bugs

* Model
  * error in the validation of mean production factor for future hydro plants with
    dead storage fill-up and production factor representation as a function of
    reservoir elevation


# SDDP 14.0.10rc1

📅 Date: 2016-09-08<br>
🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.10rc1-setup.zip) \| [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.10rc1-setup-linux.zip)

## New Features and Improvements

* GUI
  * generation reserve:
    * reformulated screen for selection of agents in constraint
    * new type of constraint: compensates individual outages of agents in defined group


# SDDP 14.0.9

📅 Date: 2016-09-05<br>
🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.9-setup.zip) \| [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.9-setup-linux.zip)

## New Features and Improvements

* Model
  * new attribute for DC links: emergency flow limit. This attribute will be used in
    a new type of generation reserve constraint involving DC links that will be released soon.
  * new macro-agent TotalDCLink: sum of DC link results in Graph module,
    useful for summarizing losses in DC links
* Reliability analysis model (Coral)
  * improvement of the analisys of base case contingency (i.e. without generation outages)
    for cases with renewable sources: the average generation scenario is now considered
    instead of their maximum capacity
  * change in scenario sampling scheme to avoid possible bias
* Power View (updated to version 1.5)
  * new functionality to record videos directly from the screen

## Fixed Bugs

* Model
  * error in transmission losses estimation in policy phase for cases running
    in parallel model
* GUI
  * error handling hourly annual profile scenarios of renewables
* Reliability analysis model (Coral)
  * error in the calculation of Benders cuts in the integration with OptGen
  * error in the selection of plants and circuits participating in the outage sampling: all elements
    with outage rate greater than zero were considered
* Power View (updated to version 1.5)
  * error for cases with 21 blocks


# SDDP 14.0.9rc9

📅 Date: 2016-08-16<br>
🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.9rc9-setup.zip) \| [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.9rc9-setup-linux.zip)

## Fixed Bugs

* GUI
  * error in generation reserve for constraints involving multi-fuel thermal plants
* Reliability analysis model (Coral)
  * internal error while using 'SDDP hydro capacity limit' that contains negative values


# SDDP 14.0.9rc8

📅 Date: 2016-08-01<br>
🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.9rc8-setup.zip) \| [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.9rc8-setup-linux.zip)

## New Features and Improvements

* Model
  * new worksheet outputs:
    * future cost at each stage and scenario: for each system (coordinated studies) or
      total (integrated studies)
    * immediate cost per system at each stage and scenario
    * costs per category at each stage and scenario
  * delete (remaining) working files at the end of execution
* GUI
  * new function to clean model output files from old runs in current directory
  * new execution scheme to avoid concurrency problems and allows automatic execution
    of user-defined processes after a successful SDDP run

## Fixed Bugs

* Model
  * error in "Hydro Capacity (no outages)" output for hydro pumped storage stations
* Reliability analysis model (Coral)
  * error in the calculation of system's maximum available power in cases with hydro pumped
    storage stations


# SDDP 14.0.9rc7

📅 Date: 2016-07-25<br>
🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.9rc7-setup.zip) \| [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.9rc7-setup-linux.zip)

## Fixed Bugs

* Reliability analysis model (Coral)
  * error in parallel executions with large number of stages/blocks


# SDDP 14.0.9rc6

📅 Date: 2016-07-21<br>
🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.9rc6-setup.zip) \| [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.9rc6-setup-linux.zip)

## New Features and Improvements

* GUI
  * improved integration between GUI and model in order to avoid concurrency errors
    when running multiple instances

## Fixed Bugs

* Model
  * internal error on generation reserve constraints involving DC links for some cases


# SDDP 14.0.9rc5

📅 Date: 2016-07-19<br>
🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.9rc5-setup.zip) \| [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.9rc5-setup-linux.zip)

## New Features and Improvements

* GUI
  * new column for filtering multi-fuel thermal plants in configuration data

## Fixed Bugs

* Reliability analysis model (Coral)
  * error in SDDP integration for integrated OptGen-SDDP-Coral optimization
    during OptGen iterations
  * error in the type of aggregation per block for LOLE results


# SDDP 14.0.9rc4

📅 Date: 2016-07-14<br>
🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.9rc4-setup.zip) \| [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.9rc4-setup-linux.zip)

## New Features and Improvements

* Model
  * generation reserve extended to allow securing the net flow
    imported via DC links
* GUI
  * new columns for filtering circuit configuration data:
    * FROM bus system
    * TO   bus system
    * Tie-line indicator (FROM bus system different from TO bus system)

## Fixed Bugs

* Model
  * included the effect of active network security constraints in bus
    marginal costs report
* Reliability analysis model (Coral)
  * error in case of multi-fuel thermal plants: the generation capacity
    considered was duplicated
  * error in case of hourly representation selected for economic dispatch
* GUI
  * error when opening more than one instance
  * error when filtering load per bus data for very large number of records


# SDDP 14.0.9rc3

📅 Date: 2016-07-06<br>
🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.9rc3-setup.zip) \| [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.9rc3-setup-linux.zip)

## New Features and Improvements

* Model
  * delete working files at the end of execution

## Fixed Bugs

* Model
  * included the effect of active network security constraints in bus
    marginal costs report
* Reliability analysis model (Coral)
  * error in execution for cases with hourly representation


# SDDP 14.0.9rc2

📅 Date: 2016-06-25<br>
🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.9rc2-setup.zip) \| [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.9rc2-setup-linux.zip)

## New Features and Improvements

* Model
  * new reserve modelling

## Fixed Bugs

* GUI
  * error while opening two or more instance of the graphical interface


# SDDP 14.0.9rc1

📅 Date: 2016-06-20<br>
🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.9rc1-setup.zip) \| [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.9rc1-setup-linux.zip)

## Fixed Bugs

* Model
  * error in the initial values of fuel contracts for backward recursion
    that could result in infeasibilities if case contains future contracts


# SDDP 14.0.8

📅 Date: 2016-06-16<br>
🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.8-setup.zip) \| [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.8-setup-linux.zip)

## New Features and Improvements

* Model
  * agents in "Thermal consumption via contracts" output are now restricted
    to thermal with contracts only (the result for all others equals to zero
    by definition)
* Parallel execution
  * change to use local instead of network directories
* GUI
  * number of decimal places are now free in data grids (instead of fixed)
* Hydrology > Parameter estimation
  * error message for invalid model now identifies the station by name


# SDDP 14.0.8rc2

📅 Date: 2016-06-08<br>
🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.8rc2-setup.zip) \| [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.8rc2-setup-linux.zip)

## New Features and Improvements

* Model
  * automatic memory allocation for some of the fuel contract internal
    data structures

## Fixed Bugs

* Model
  * internal error while adding names for new losses constraints
  * error introduced in version 14.0.8rc1 for cases with transmission
    network with losses representation
* Power View (updated to version 1.4)
  * error for hourly cases when using binary format
  * error in the detection of case output format (binary x CSV)
  * error in the detection of renewable source outputs


# SDDP 14.0.8rc1

📅 Date: 2016-05-31<br>
🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.8rc1-setup.zip) \| [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.8rc1-setup-linux.zip)

## New Features and Improvements

* Model
  * new macro-agent TotalCirc: sum of circuit results in Graph module,
    useful for summarizing total system transmission losses
  * internal code optimization to speed-up some operations

## Fixed Bugs

* Reliability analysis model (Coral)
  * error in some network calculations for cases without changes in transmission
    configuration from one stage to another
* GUI
  * error saving changes in load per bus configuration data
  * error when deleting all circuits of the case
  * translations


# SDDP 14.0.7

📅 Date: 2016-05-23<br>
🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.7-setup.zip) \| [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.7-setup-linux.zip)

## New Features and Improvements

* Model
  * New output: Lerner index for transmission system (buses)


# SDDP 14.0.7rc5

📅 Date: 2016-05-18<br>
🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.7rc5-setup.zip) \| [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.7rc5-setup-linux.zip)

## New Features and Improvements

* GUI
  * increased the number of decimal places in minimum and maximum hydro
    storage constraints screen
  * check the internet connection availability before checking for version updates
    to avoid freezing while waiting for connectivity
* Graph
  * update to version 2.6
  * compiler version updated to Intel 2015

## Fixed Bugs

* Model
  * error in the calculation of infiltration for hydro reservoirs with representation
    of storage x infiltration table and minimum storage equal to zero. This problem
    could lead to an internal error that reflect in model infeasibility
* GUI
  * error in the importing process of demand data from CSV files. The data
    was imported in wrong order
* Graph
  * error while generating graphics for hourly cases with large horizon


# SDDP 14.0.7rc4

📅 Date: 2016-05-03<br>
🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.7rc4-setup.zip) \| [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.7rc4-setup-linux.zip)

## Fixed Bugs

* Model
  * error in the representation of thermal plants with concave consumption costs
    with 3 segments


# SDDP 14.0.7rc3

📅 Date: 2016-05-02<br>
🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.7rc3-setup.zip) \| [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.7rc3-setup-linux.zip)

## New Features and Improvements

* GUI
  * changed the behavior when editing downstrean plant for filtration and
    stored energy calculation

## Fixed Bugs

* Model
  * error in simulations of selected forward scenarios for cases that consider
    sampling of renewable generation scenarios
  * error in security constraints: dynamic parameters' information were
    not being considered in the coefficients of post-contingent flow
    constraints


# SDDP 14.0.7rc2

📅 Date: 2016-04-22<br>
🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.7rc2-setup.zip) \| [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.7rc2-setup-linux.zip)

## New Features and Improvements

* Model
  * extension to represent thermal plants with concave consumption curve
    with 3 segments
* GUI
  * new columns for filtering circuit configuration data: selected for contingency

## Fixed Bugs

* Model
  * possible internal error for cases with more than 744 stages
* GUI
  * possible error while retrieving the updated licence file from PSR's server


# SDDP 14.0.7rc1

📅 Date: 2016-04-07<br>
🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.7rc1-setup.zip) \| [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.7rc1-setup-linux.zip)

## Fixed Bugs

* Model
  * possible internal error for cases with more than 744 stages
* GUI
  * possible error while retrieving the updated licence file from PSR's server


# SDDP 14.0.6

📅 Date: 2016-04-02<br>
🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.6-setup.zip) \| [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.6-setup-linux.zip)

## New Features and Improvements

* Model
  * new output report: flag for active security constraint in optimal solution
  * improvements in reserve output reports:
    * agents in output reports shows only reserve constraints of absolute type
    * unit of "Generation reserve" and "Generation reserve limit" outputs
      changed from GWh to MW
    * "Generation reserve" output maximum value is now limited by the reserve input
      value defined for the corrsponding stage/block in chronological data table
    * redefinition of output report names:
      * Thermal generation reserve -> Thermal capacity margin
      * Hydro   generation reserve -> Hydro   capacity margin
* GUI
  * minor label changes in:
    * execution options screen
    * hydro configuration screen


# SDDP 14.0.6rc4

📅 Date: 2016-03-30<br>
🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.6rc4-setup.zip) \| [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.6rc4-setup-linux.zip)

## New Features and Improvements

* Model
  * rolled back of the default strategy of version 14.0.5 to solve power flow
    with quadratic losses for problems involving integer variables (thermal
    plants with commitment, hydro plants with non-controllable spillage, etc)
* GUI
  * import/export from/to CSV files (Excel integration) extended to
    single reservoir constraints

## Fixed Bugs

* Model
  * fixed changes in optimization solver routines that resulted in performance
    degradation introduced in version 14.0.5


# SDDP 14.0.6rc3

📅 Date: 2016-03-22<br>
🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.6rc3-setup.zip) \| [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.6rc3-setup-linux.zip)

## New Features and Improvements

* Dongle
  * updated driver software to version 7.6.8 (Windows only)

## Fixed Bugs

* Model
  * fixed solver parameters that resulted in problems during solution in
    simulation for some cases
  * fixed compilation options that resulted in performance degradation
    in version 14.0.5
  * fixed output description that exceeded maximum length


# SDDP 14.0.6rc2

📅 Date: 2016-03-17<br>
🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.6rc2-setup.zip) \| [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.6rc2-setup-linux.zip)

## New Features and Improvements

* Model
  * new default strategy to solve power flow with quadratic losses: it improves
    the circuit losses representation while ensures the correct calculation of
    bus marginal costs.


# SDDP 14.0.6rc1

📅 Date: 2016-03-15<br>
🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.6rc1-setup.zip) \| [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.6rc1-setup-linux.zip)

## New Features and Improvements

* Model
  * maximum number of circuit contingencies increased from 10 to 20


# SDDP 14.0.5

📅 Date: 2016-03-08<br>
🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.5-setup.zip) \| [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.5-setup-linux.zip)

## New Features and Improvements

* Model
  * redefinition of Xpress solver parameters for improve solution time of large-scale problems
  * new output report: island of each bus in each stage (different islands indicates network split)
  * maximum number of buses increased from 3,000 to 4,000 on standard version
  * error reading the historical data of climatic variable when it has more data than
    the historical inflow data
  * new attributes for DC links:
    * status: connected or disconnected
* GUI
  * added possibility to change bus names while importing data from a CSV file
  * import/export from/to CSV files (Excel integration) extended to:
    * demand and price data
    * circuit modification data
    * fuel price data
    * renewable source modification data
  * new columns for filtering circuit configuration data:
    * type: existing or future
    * status: connected or disconnected
    * monitored: yes or no
* Power View
  * changed the maps provider from Google Maps to Microsoft Bing

## Fixed Bugs

* Model
  * minimum and maximum total outflow constraints must not be considered to future hydro plants
  * error in reading routine of gas data
  * error for hard problems with integer variable representation and single node output
  * error checking plants in joint reservoir constraints for coordinated studies
* GUI
  * error aligning elements with numeric names
  * error saving downstream plant for stored energy calculation in cases it is equal to downstream for turbining
  * error on grid control and area configuration when exists element with code equal zero (0)
* Hydrology > Parameter estimation
  * updated the internal threshold for the detection of constant inflows


# SDDP 14.0.4

📅 Date: 2016-01-13<br>
🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.4-setup.zip) \| [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.4-setup-linux.zip)

## New Features and Improvements

* Model documentation
  * modelling of climatic variables
  * parallel execution
* GUI
  * export to CSV functionality now exports an empty template file to be filled.
    This is useful when importing data from scratch.
  * default value set to 1.0 for "Weighting factor" of climatic variable in
    "Hydrology > Parameters estimation"
  * new option to import initial condition of the hydrology file in binary format in
    "Economic dispath > Solution strategy > Initial inflows" option

## Fixed Bugs

* GUI
  * error choosing the correct number of blocks at the directory selection screen
    for some particular cases
  * field "mean tailwater level" is now disabled when the information will not be used by SDDP
  * error importing initial storage file in binary format from a different directory
  * error opening the Dashboard for cases in a path containing spaces
  * error filtering data by system in single reservoir constraints


# SDDP 14.0.3rc1

📅 Date: 2015-12-11<br>
🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.3rc1-setup.zip) \| [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.3rc1-setup-linux.zip)

## Fixed Bugs

* Model
  * possible error starting parallel executions


# SDDP 14.0.3

📅 Date: 2015-12-09<br>
🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.3-setup.zip) \| [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.3-setup-linux.zip)

## New Features and Improvements

* Model
  * new option for load shedding in buses: "none"
  * new output reports related to fuel reservoir:
    * marginal value of fuel in reservoir
    * marginal value of fuel reservoir capacity
  * added type (existing/future) for DC links
  * evaporation effect on hydro plants is now considered since the beginning of the
    dead storage fill-up (if considered)
  * new option to consider at least one loss linearization for all circuits, which may be necessary
    to ensure differentiation between the marginal costs on the terminal buses of circuits with low losses.
    This option may increase the computational time and should be used only when necessary.
  * removed the limitation of 20 processes per computer in parallel execution
  * update Xpress optimization solver to version 7.9 to improve numerical stability in some cases
* GUI
  * new field for the definition of fixed penalty for the flood control energy constraint
    of joint reservoir constraints
  * increased the precision of fixed duration of blocks data to avoid round problems in the sum
  * new feature to adapt interface to computer's regional settings
  * new option to import initial storage file in binary format in the
    "Economic dispath > Solution strategy > Initial storages" option
  * new column describing the type of generation constraint: lower or upper limit
  * new column describing fuel contract type: free contract or integral contract
* Hydrology > Parameter estimation
  * report improvement for the estimation of hydro sites with constant intermediate inflows
  * added tolerance for stationarity tests
* Dashboard
  * the chart's style has been updated to a much fancier style: check it out!
* Power View
  * improvements in the responsiveness of map control options such as zoom, scroll, panning.

## Fixed Bugs

* Model
  * possible error in the identification algorithm of excess in renewable generation
    in cases with the representation of the transmission network
  * wrong definition of the type of aggregation per block for the CO2 emission cost outputs
  * possible error in the execution of the model in Windows Server 2012 and Windows XP
  * possible error in cases with excess in renewable generation for relatively large datasets
  * error for parallel execution of cases with spaces in path
* GUI
  * error in the visualization of operative costs for cases with specific consumption
    varying per block
  * error while saving the lower and upper limits for sum of interconnections
  * error while saving load per bus configuration data file with more
    than 32,768 records
  * error while loading fuel contract data with initial date separated by dots instead of slashes
  * error in the copy to Excel function of renewable source scenarios data
  * error activating the use of climatic variables in the inflows
  * error saving bus configuration data after deleting a power plant
  * error saving the climatic variable option
* Graph
  * update to version 2.3
  * problem for cases using binary output and csv (specific case when running SDDP
    with OptGen model)
* Power View
  * error representing the circuit capacities over time. For some particular cases, the exhibited capacity
    did not match with circuit data.
  * error representing existing and future circuits in weekly studies


# SDDP 14.0.2

📅 Date: 2015-07-15<br>
🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.2-setup.zip) \| [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.2-setup-linux.zip)

## Fixed Bugs

* Graph
  * problems in the calculation of weighted average of block values for charts
    starting after the beginning of the study in studies with variable duration of blocks


# SDDP 14.0.1

📅 Date: 2015-07-13<br>
🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.1-setup.zip) \| [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.1-setup-linux.zip)

## New Features and Improvements

* Model
  * new options for monitoring of circuit limits: "tie-lines only" and "none"
  * new output: stored energy at a storage level of 65% of the useful storage
* GUI
  * incremental search filter on bus geographical location screen
  * verification for circuit emergency limit lower than normal limit

## Fixed Bugs

* GUI
  * specific problem while opening Graph module that could wrongly force the exclusion
    of all csv files in the case directory
  * error in the addition of load per bus data for systems without pre-defined load
* Graph
  * problems while saving selected blocks for cases with more than 5 blocks
  * problems in the generation of Excel output when values are aggregated by year
* PowerView
  * translations
  * initialization error of stage label when a new case is loaded
  * wrong column size for units in variable table of selection panel


# SDDP 14.0.1rc1

📅 Date: 2015-06-18<br>
🔗 Download: [Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.1rc1-setup.zip) \| [Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-14.0.1rc1-setup-linux.zip)

## Fixed Bugs

* Model
  * 32-bits version: fixed problems with dll dependencies
* PowerView
  * possible freezing of playback controls in simulation panel
  * missing scenarios when showing variables that vary and don't vary per scenario
  * problems in the aggregation per block
  * problems while reading SDDP binary output files
