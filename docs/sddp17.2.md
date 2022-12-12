---
layout: default
title: Release notes
nav_order: 1
description: "SDDP release notes"
permalink: /
---

# Version 5.26.a

🔗 [Download](https://www.psr-inc.com/app/link/?t=d&f=ncp-5.26.a-patch.zip)

## New features

* Included the definition of execution horizon with partial times.
* Included the option to select a single / multi stopping criterion of the model execution.
* Extended the hydro station inflow forecast to sub-hourly resolution.
* New output results file:
  * Target storage violation

## Corrections

* Corrected a bug in the electricity production smoothing feature.
* Corrected a bug in multi-fuel thermal units associated to combined cycle plants.
* Corrected a bug in the secondary spinning reserve assignation (downward) of batteries.
* Corrected a bug in the minimum coupling generation of combined cycle plants.

# Version 5.26

🔗 [Download](https://www.psr-inc.com/app/link/?t=d&f=ncp-5.26-setup.zip)

## New features

* Solver updated to the Xpress Suite Optimization 8.14.
* Included the hydro unit inertia representation.
* Included the frequency control ancillary service (FCAS) representation.
* Included the representation of hydro operative average constraints (turbined / spilled / total outflow / storage / forebay / tailwater level).
* Included the forebay elevation x spillway rating curve outflow table with hourly changing factors.
* Included the definition of hill curve chart for hydro units.
* Included the ability to assign different amounts / prices (upward / downward) of secondary reserve in batteries.
* Included the ability to lead with negative market / bus energy prices for revenue maximization criteria.
* Included the ability to bid different amounts / prices (upward / downward) of secondary reserve for a group of plants.
* Included the infiltration x storage table
* Included the bypass valve representation.
* Included the possibility to define smoothing feature penalty.
* Included the representation of daily forebay ramps.
* Included the control to enable / disable individual generation constraints.
* Extended the automatic recovery tool for turbined / spilled initial conditions.
* Extended the convergence report to include the partial executions of the rolling horizon scheme.
* Extended the possibility to define multiple hydro unit generation forbidden zones per forebay level.
* Extended the possibility to define penalties for target storage constraints.
* Extended the maintenance scenario of hydro units to 05/15/30 minutes resolution.
* Maximum number of target generation constraints extended to 50000.
* Maximum number of DC links extended to 5000.
* Hydro unit production modeling reformulated.
* Thermal combined cycle production modeling reformulated.
* Thermal fuel consumption modeling reformulated.
* New output results file:
  * Average elastic demand price
  * Stage resolution
  * Hydro unit inertia
  * Hydro unit synchronous condenser status
  * Hydro unit synchronous condenser start-up / cost
  * Total received outflow
  * Hydro unit FCAS assignation (raise / lower)
  * Bypass valve flow
  * Bypass valve flow (min / max) violation
  * Hydro average limit violation
  * Renewable O&M total cost
  * Renewable curtailment cost

## Corrections

* Corrected a bug in the general minimum total outflow penalty.
* Corrected a bug in the exclusive secondary reserves output.
* Corrected a bug in the energy price and profit output.
* Corrected a bug in the initial condition applied to cold ramp constraints of hydro plants / units.
* Corrected a bug in the sum of circuit flows constraint.
* Corrected a bug in the reading process of missing renewable generation data.
* Corrected a bug in the constant tailwater level representation.

# Version 5.25

🔗 [Download](https://www.psr-inc.com/app/link/?t=d&f=ncp-5.25-setup.zip)

## New features

* NCP can now handle with time steps of 5 minutes.
* NCP can now handle up to 2-month horizon with hourly time steps.
* Added the stochastic hydro plant / unit commitment modelling.
* Graph module updated to the version 4.0.
* Added a new visualization tool for hydro plants (Hydro View).
* Added a new hydro plant's topology viewer.
* Added a new Power View tool for transmission network visualization.
* New secondary reserve requirements type (not shared / exclusive).
* New battery parameters (round-trip efficiency /optimized initial storage).
* Added the possibility to select renewable power plants to attend secondary reserve requirements.
* Added the possibility to define a minimum / maximum limit applied to renewable power plant's secondary reserve.
* Added the possibility to define a price to renewable power plant's secondary reserve offers.
* Added the possibility to define a primary reserve constraint to renewable power plants.
* Added the possibility to define a minimum / maximum limit applied to battery's secondary reserve.
* Added the possibility to define a price to battery's secondary reserve offers.
* Added the possibility to define generation constraints (charge / discharge) for batteries.
* Included the variable tailwater level definition for hydro plants (tide effect).
* Added the possibility to define penalty values to system generation constraints.
* Added import/export data from/to CSV functionality to the Target Generation constraint.
* Included the minimum generation constraint applied to the combined cycle thermal plants while the coupling operation.
* Included the ability to valorize the total outflow (turbined + spiled) in transit.
* Maximum number of target generation constraints extended to 20000.
* New output results file:
  * Renewable secondary reserve (upward / downward)
  * Renewable primary reserve
  * Renewable primary reserve violation
  * Demand and Load per Bus in 5-minute resolution
  * Hydro Plant / Thermal Plant / Hydro Unit / Battery / Renewable exclusive secondary reserve (upward / downward)

## Corrections

* Corrected a bug in the renewable generation constraint.
* Corrected a bug in the forebay elevation output.
* Corrected a bug in the AC circuits maintenance.
* Corrected a bug in the hydro unit power production associated with constant net head.
* Corrected a bug in the DC links flow monitoring selection.
* Corrected a bug in the water in transit valorization of cases with Maximization Revenues criterion.
* Corrected a bug in the Automatic Detection / Correction feature of incoherent transmission losses.
* Corrected a bug in the representation of battery's ramps.
* Corrected a bug in the minimum storage representation of batteries.

# Version 5.24

🔗 [Download](https://www.psr-inc.com/app/link/?t=d&f=ncp-5.24-setup.zip)

## New features

* Solver updated to the Xpress Suite Optimization 8.9.
* Extended the Maintenance Scenario of Hydro Plant / Thermal Plant to 15/30 minutes definition.
* The tailwater elevation x outflow modeling representation was reformulated.
* The forebay elevation x storage modeling representation was reformulated.
* The maximum quality heuristic was tuned to achieve better performance.
* Graph module updated to the version 3.10.
* Included some enhancements associated to thermal fuel consumption modelling.
* The integer representation for AC circuit losses was reformulated.
* Included the option to define the rolling horizon interval for binary decision variables.
* Added the maximum ramp-up / down by generation level of Thermal Plants.
* The maximum number of connections to a bus was extended to 500.
* Included the possibility to define a fuel transition time for Multi-fuel Thermal Power Plants.
* Included the possibility to define a fuel transition cost for Multi-fuel Thermal Power Plants.
* Included the possibility to define a phase-shifting set-point for transformers.
* Included the possibility to select batteries for secondary reserve requirements.
* Included a results comparison method based on the dashboard tool.
* Included the ability to customize the water in transit valorization.
* Added the quadratic losses representation for DC Links.
* Added the maximum regulation time for Batteries.
* Added import/export data from/to CSV functionality to the Battery Registry Data.
* Added the automatic NCP model version update option.
* Added the possibility to select DC Links in the Sum of Circuit Flows data definition screen.
* Added the constraint type (minimum / maximum) to the Renewable Generation Constraint.
* Added the NCP iFeedback option that collects automatically some statistics of each model execution.
* New output results file:
  * Battery secondary reserve (upward/downward)

## Corrections

* Corrected a bug in the post-processing of cases with only hydro plants / units and network representation.
* Corrected a bug in the results aggregator for chronological executions.
* Corrected a bug in the rolling horizon scheme.
* Corrected a bug in the non-controllable spillage constraint.
* Corrected a bug in the cold ramp constraint for Hydro Units.

# Version 5.23

## New features

* Solver updated to the Xpress Suite Optimization 8.8.
* Added the possibility to define an additional minimum power limit for Secondary Spinning Reserve assignation of Hydro Units.
* Added the possibility to define an additional maximum power limit for Secondary Spinning Reserve assignation of Hydro Units.
* Included some enhancements associated to hydro unit production modelling.
* Included the data set path reading using parameters.
* Added the possibility to define integral fuel contracts.
* Added the possibility to define a maximum number of daily start-ups / shutdowns of Hydro Units.
* Dashboard tool updated with a new look and feel.
* Graph module updated to the version 3.07.
* Added an option to disable heuristic methods in the model optimization.
* Added an option to disable / change the presolve application in the optimization.
* Added the Exclusion constraint for Hydro Units dispatch.
* Added import/export data from/to CSV functionality to the Fuel Registry Data.
* Added import/export data from/to CSV functionality to the DC Link Registry Data.
* Power View module (visualization of transmission network and results) updated to the version 1.18.
* New output results file:
  * Circuit flow sum constraint

## Corrections

* Corrected a bug in the Start-up Minimum Time constraint associated with the initial condition for synchronism.
* Corrected a bug in the revenue calculation per bus.
* Corrected a bug in maximum execution time parameter.
* Corrected a bug in the Renewable Plants CSV import tool.
* Corrected a bug in the representation of batteries with only one charge / discharge segment.
* Corrected a bug in the initial storage calculation defined in terms of forebay level.
* Corrected a bug in the multi-fuel thermal plants selection as eligible generators for secondary reserves.

# Version 5.22

## New features

* The hydro unit production modeling considering the elevation x storage and tailwater elevation x outflow variation effects was totally reformulated.
* Added the possibility to define levels of energy bids / prices for Thermal Power Plants with 30 and 15 minutes time steps.
* Added import/export data from/to CSV functionality to the Hydro Power Plants initial condition.
* Added import/export data from/to CSV functionality to the Thermal Power Plants initial condition.
* Added import/export data from/to CSV functionality to the Elastic Demand / Supply Scenario.
* Added import/export data from/to CSV functionality to the Hydro Unit Data.
* Added import/export data from/to CSV functionality to the Penstock Data.
* Power View module (visualization of transmission network and results) updated to the version 1.17.
* The tolerance associated to the circuits reactance was updated to 0.05%.
* Added the Forebay Fill-up ramp constraint for Hydro Plants.
* Added the Forebay Draw-down ramp constraint for Hydro Plants.
* Graph module updated to the version 2.36.
* Added the possibility to import maximum operative storage constraints of a SDDP mid-long term planning study for the chronological execution option.
* Added the possibility to import minimum spillage constraints of a SDDP mid-long term planning study for the chronological execution option.
* Added the possibility to select both the future cost function and target generation as Terminal Function for the chronological execution option.
* New output results file:
  * Tailwater elevation
  * Hydro unit production factor
  * Elastic transaction revenue

## Corrections

* Corrected a bug in the revenue calculation in cases with elastic supply representation.
* Corrected a bug in the maximum available power of future pumped storage plants.
* Corrected a bug in the automatic calculation of forbidden zones of hydro power plants.
* Corrected a bug in the Elastic Demand / Supply scenarios in cases with 30 and 15 minutes time steps.
* Corrected a bug associated with different reserve bids (upward/downward) of hydro units.
* Corrected a bug associated with system demand scenario selection in chronological execution.
* Corrected a bug associated with renewable configuration / modification file versions.
* Corrected a bug associated with hydro plant modification file versions.
* Corrected a bug associated with hydro unit representation in chronological execution.
* Corrected a bug associated with penstock friction losses output.
* Corrected a bug associated with thermal plants selection in target generation screen.
* Corrected a bug in the reservoir initial storage data conversion.
* Corrected a bug associated with null inelastic demand with Maximization Revenues criterion.
* Corrected a bug associated with combined cycle plants with must-run constraint.

# Version 5.21

## New features

* Solver updated to the Xpress Suite Optimization 8.5.
* Added a heuristic option to retrieve automatically the initial conditions of turbined outflow for Water Travel Time constraint.
* Added the possibility to define levels of energy bids / prices for Thermal Power Plants.
* Added import/export data from/to CSV functionality to the Thermal Energy Bids / Prices Data.
* Added import/export data from/to CSV functionality to the Bus Configuration.
* Added import/export data from/to CSV functionality to the Circuit Configuration.
* Power View module (visualization of transmission network and results) updated to the version 1.14.
* Added the possibility to view the convergence report output (ncpconv.csv).
* Added the possibility to view the objective function terms report output (ncpcope.csv).
* Added import/export data from/to CSV functionality to all AC Power Flow Scenarios / Constraints.
* Added import/export data from/to CSV functionality to the Electrical Areas Limits Constraint.
* Added import/export data from/to CSV functionality to the Null Water Value Scenario.
* Added import/export data from/to CSV functionality to the System Cold Reserve Constraint.
* Added import/export data from/to CSV functionality to the Secondary Spinning Reserve Price Scenario.
* Added import/export data from/to CSV functionality to the System Generation Constraint.
* Added the possibility to define negative prices applied to Secondary Spinning Reserve offers.
* Added the possibility to change the Secondary Spinning Reserve constraint type.
* Added the option to clean up the data set by removing all the model output files.
* Added the option to compact the data set for technical support purposes.

## Corrections

* Corrected a bug in the reading process of initial conditions for Water Travel Time constraint.
* Corrected a bug in the Water Travel Time graphical interface.
* Corrected a bug regarding the benefit Thermal Power plant representation.
* Corrected a bug in the Forced Secondary Reserve based on its Generation constraint.
* Corrected a bug in the Water Value and Hydro Opportunity Cost reports for plants with Target Storage constraints.
* Corrected a bug in the Water Travel Time constraint.
* Corrected a bug in the method to reproduce a previous solution based on the convergence report output.
* Corrected a bug when deleting Electrical Areas.
* Corrected a bug when changing rapidly from different data sets.
* Corrected a bug in the Start-up Minimum Time constraint.
* Corrected a bug in the Secondary Spinning Reserve assignation for mixed offers of hydro plants and hydro units.
* Corrected a bug in the Import/Export limits for Electrical Areas constraint.
* Corrected a bug in the Hydro Unit Maintenance scenario.
* Corrected a bug in the option to value water in transit.
* Corrected a bug regarding the penalty applied to non-controllable spillage plants.
* Corrected a bug in the Fast Response Energy Storage model.

# Version 5.20

## New features

* Added an automatic converter of a SDDP data set with several systems to a NCP data set.
* Extended the automatic infeasibility detector for the optimization process.
* Included the student version for academic testing purposes.
* Included the slack variable for System Cold Reserve requirement.
* Added the possibility to define Operation and Maintenance Cost for Renewable Plants.
* Added the possibility to define Operation and Maintenance Cost for Batteries.
* Added the possibility to define Transmission Costs for DC Links.
* Added a new method to reproduce a previous solution based on the convergence report output.
* Added a new definition unit (MW) to the Renewable Generation Constraint.
* Power View module (visualization of transmission network and results) updated to the version 1.10.
* Added the maximum number of iterations applied to the Automatic Detection / Correction feature of incoherent transmission losses.
* Graph module updated to the version 2.14.
* Reformulated the Water Travel Time modeling of Hydro Power Plants.
* Included an automatic tool to update the NCP user license.
* Dashboard panel updated with new download options.
* New output results file:
  * Thermal commercial revenue

## Corrections

* Corrected a bug in the minimum limit of Secondary Reserve assignation defined in MW.
* Corrected a bug in the reading process of Renewable Plant modification data.
* Corrected a bug in the reading process of System Cold Reserve data.
* Corrected a bug in the reading process of Sum of Circuit Flows for chronological execution.
* Corrected a bug in the reading process of Fuel Costs for Thermal Plants with null first segment of consumption.
* Corrected a bug in the reading process of Future Cost Functions with excedent decimal numbers.
* Corrected a bug in the Sum of Circuit Flows data definition screen.
* Corrected a bug in the System Cold Reserve data definition screen.
* Corrected a bug in the Renewable Generation CSV import tool.
* Corrected a bug in the Quadratic losses output.
* Corrected a bug in the Circuit loading output.
* Corrected a bug in the reading process of Circuit Losses Individual penalty.
* Corrected a bug in the reading process of inflow scenarios for stochastic execution.
* Corrected a bug in the Reservoir elevation output.
* Corrected a bug in the Combined Cycle configuration screen.
* Corrected a bug in the Circuit marginal cost output.
* Corrected a bug in the Minimum spillage constraint.

# Version 5.19

## New features

* Added the possibility to define a set of plants to have an assignation of Forced Secondary Reserve based on its Generation.
* Added the Circuit Losses Representation (linear / integer) in 15/30/60 minutes.
* Added the Circuit Losses Penalty (active / inactive) in 15/30/60 minutes.
* Added the possibility to define more than one type of Individual Generation Constraints for Hydro Plants.
* Added the possibility to define more than one type of Individual Generation Constraints for Hydro Units.
* Added the possibility to define more than one type of Individual Generation Constraints for Thermal Plants.
* Added the Precedence Order Constraint for Thermal Power Plants.
* Added the Automatic Detection / Correction feature of incoherent transmission losses.
* Graph module updated to the version 2.12.
* Added import/export data from/to CSV functionality to the Circuit Losses Representation Scenario.
* Added import/export data from/to CSV functionality to the Circuit Losses Penalty Scenario.
* Added import/export data from/to CSV functionality to the Circuit Maintenance Scenario.
* Added import/export data from/to CSV functionality to the Thermal Forced Units Constraint.
* Added import/export data from/to CSV functionality to the Cold Reserve of Hydro Plants.
* Added import/export data from/to CSV functionality to the Cold Reserve of Thermal Plants.

## Corrections

* Corrected a bug in the Maximum Number of Start-ups for Hydro Units.
* Corrected a bug in the Generation Constraint Violation output.
* Corrected a bug in the Chronological Execution with half-hourly / quarter-hourly representation regarding System Demand data.
* Corrected a bug in the Graph module associated with the selection of the year.
* Corrected a bug in the automatic calculation of Minimum Operative Storage penalty.
* Corrected a bug regarding the penalty applied to non-controllable spillage plants.
* Corrected a bug in the Cold Reserve constraint.

# Version 5.18

## New features

* Added the possibility to define an additional minimum power limit for Secondary Spinning Reserve assignation of Thermal Plants.
* Added the possibility to define an additional minimum power limit for Secondary Spinning Reserve assignation of Hydro Plants.
* Added the possibility to define an additional maximum power limit for Secondary Spinning Reserve assignation of Hydro Plants.
* Added the possibility to define different ways (upward/downward) for Primary Reserve of Hydro and Thermal Plants.
* Added the possibility to define a Maintenance Scenario for DC Links in 15/30/60 minutes.
* Added the possibility to import fuel availability constraints of a SDDP mid-long term planning study for the chronological execution option.
* Power View module (visualization of transmission network and results) updated to the version 1.7 with new colorful animation option.
* Graph module updated to the version 2.11 with new features regarding definition of horizon profiles for selected graphs.
* Several improvements and new developments in the Chronological Execution applied to Cloud Computing, such as automatic restart, decomposition heuristics, infeasibility detector, among others.
* Added import/export data from/to CSV functionality to the Hydro Unit Secondary Spinning Reserve Constraint.
* Added import/export data from/to CSV functionality to the Hydro Unit Maintenance Scenario.
* Added import/export data from/to CSV functionality to the Reservoir Operation Constraint.
* Added import/export data from/to CSV functionality to the Renewable Generation Constraint.
* New output results file:
  * Quadratic losses
  * Circuit loading

## Corrections

* Corrected a bug in the import/export tool from/to CSV of Renewable Plants generation.
* Corrected a bug in the second bid level representation for Secondary Spinning Reserve Constraint.
* Corrected a bug in the Nominal Power of Renewable Plants output.
* Corrected a bug in the Start-up Minimum Time constraint associated with the initial condition for synchronism.
* Corrected a bug in the Marginal Cost of Sum of Circuit flow output.
* Corrected a bug in the Fuel Contracts graphical interface.
* Corrected a bug in the Secondary Spinning Reserve output for non-commitment plants.
* Corrected a bug in the Fuel Emission Factors representation.
* Corrected a bug in the Pumped Storage Maintenance for chronological execution.
* Corrected a bug in the Minimum Up-time constraint associated with Forced Thermal Generation.

# Version 5.17

## New features

* Solver updated to the Xpress Suite Optimization 8.0.
* Added the possibility to define fuel contracts with daily duration (fuel tranches).
* Added the possibility to import fuel contract results of a SDDP mid-long term planning study for the chronological execution option.
* Extended the Individual Generic Generation Constraints of Hydro Plant / Hydro Unit / Thermal Plant to 15/30 minutes definition.
* Added the possibility to define a second bid level for Secondary Spinning Reserve Constraint of Hydro Plant / Hydro Unit / Thermal Plant / Group of Plants.
* Extended the automatic infeasibility detector for the optimization process.
* Reformulated the unit commitment representation of thermal plants.
* Power View module (visualization of transmission network and results) updated to the version 1.5 with animation recording tool.
* Added the possibility to define an additional maximum power limit for Secondary Spinning Reserve assignation of Thermal Plants.
* Improved the memory allocation of some variables/constraints.
* Extended the possibility to define more than 365 days of data at once in chronological grids.
* Added the new format (linear / tabular) for CSV import/export tool data in System Demand and System Market Price screens.
* Added import/export data from/to CSV functionality to the Individual Generic Generation Constraints of Hydro Plant / Hydro Unit / Thermal Plant.
* Extended the NCP Cloud Computing mode to run chronological executions.
* Extended the convergence report output (ncpconv.csv) to register partial execution times.
* Included the functionality to remove one or more scenarios at once in chronological grids.
* Included the functionality to remove one or more days at once in chronological grids.
* Added import/export data from/to CSV functionality to the System Secondary Spinning Reserve.
* Included the functionality to open the data directory in Windows Explorer or copy it to the clipboard by clicking on the directory bar.

## Corrections

* Corrected a bug in the Secondary Spinning Reserve constraint for the chronological option.
* Corrected a bug in the Secondary Spinning Reserve assignation for run of river plants.
* Corrected a bug in the Cold Reserve constraint.
* Corrected a bug in the Data Directory selection.
* Corrected a bug in the Deficit output for the chronological option.
* Corrected a bug in the Selling operation based on the System Secondary Reserve Price.
* Corrected a bug in the Start-up Minimum Time constraint.
* Corrected a bug in the Secondary Spinning Reserve Costs output for a group of plants.
* Corrected a bug in the option to not consider a circuit in the study.
* Corrected a bug in the Elastic Offer/Demand graphical interface.
* Corrected a bug when opening more than one instance of graphical interface.

# Version 5.16

## New features

* Added the possibility to define different bids and/or limits for Hydro Plant / Hydro Unit / Thermal Plant Secondary Spinning Reserve ways (upward/downward).
* Added the possibility to define different ways (upward/downward) for System Secondary Spinning Reserve requirements.
* Added the possibility to define control range limit for Hydro Plant / Hydro Unit / Thermal Plant Secondary Spinning Reserve.
* Added the possibility of definition for System Market Energy Prices in 15/30 minutes.
* Added the possibility to import system marginal prices of a MAXREV mid-long term planning study for the chronological execution option.
* Added the DC Link Configuration definition.
* Added the possibility of definition for Bus Energy Prices in 15/30/60 minutes.
* Power View tool (visualization of transmission network and results) updated to the version 1.3.
* Added a new convergence report output (ncpconv.csv).
* Extended the maximum number of stages to 1488.
* Added the variable minimum spill constraint for Hydro Power Plants.
* Extended the maximum fuel availability constraint to consider a minimum fuel usage amount.
* Included the ability to use more than one fuel simultaneously for Multi-fuel Thermal Power Plants.
* Included the Amazon Simple Storage Service (Amazon S3) integration to the NCP Cloud Computing mode.
* New output results files:
  * Hydro Plant / Hydro Unit / Thermal Plant secondary spinning reserve (upward/downward)
  * Hydro Plant / Hydro Unit / Thermal Plant secondary spinning cost (upward/downward)
  * System secondary spinning reserve purchase (upward/downward)
  * Bus energy price
  * Bus revenue
  * Minimum spillage violation
  * Generation constraint violation

## Corrections

* Corrected a bug in the System Demand graphical interface.
* Corrected a bug in the Hydro Unit Secondary Spinning Reserve graphical interface.
* Corrected a bug in the Minimum Turbined Outflow constraint.
* Corrected a bug in the Sum of Circuit Flows constraint for the chronological option.
* Corrected a bug in the Electrical Area Import/Export constraint for the chronological option.
* Corrected a bug in the Renewable Plant Modification Data for the chronological option.
* Corrected a bug in the Automatic Infeasibility Detector for the optimization process.
* Corrected a bug in the Fuel Availability constraint.
* Corrected a bug in the Hydro Plant Minimum Generation constraint.

# Version 5.15

## New features

* Solver updated to the Xpress Suite Optimization 7.9.
* Added the Stochastic Execution Mode with the definition of multi-scenarios such as renewable generation, inflows, system load, demand by bus and energy prices.
* Power View tool (visualization of transmission network and results) updated to the version 1.1.
* Included the Power View User Manual.
* Included an automatic infeasibility detector for the optimization process.
* Included a dashboard panel with summarized results.
* Added the possibility of definition for Secondary Spinning Reserve Limits and Offers in 15/30 minutes for a group of plants.
* Added the possibility to import fuel costs of a SDDP mid-long term planning study for the NCP chronological execution option.
* Included new parameters to the Fast Response Energy Storage Configuration definition.
* Added import/export data from/to CSV functionality to the Market Energy Price Scenario.
* Improved the selection of data origin for chronological execution.
* Fully compatible with SDDP 14.0.2 (last released version).
* Improved the memory allocation of several constraints.
* New output graphs for Chronological Execution.
* New output graphs for Stochastic Execution.
* New output results file:
  * Sum of circuit flow marginal cost

## Corrections

* Corrected a bug in the Discrete Generation constraint.
* Corrected a bug in the Maximum Number of Power Inflections constraint.
* Corrected a bug in the Null Water Value constraint.
* Corrected a bug in the Hydro Unit Precedence constraint.
* Corrected a bug in the Minimum Downtime constraint.
* Corrected a bug in the Hydro Energy Bid constraint.
* Corrected a bug in the Terminal Function (Target Storage) for the chronological option.
* Corrected a bug regarding some Reservoir Operation output files.

# Version 5.14

## New features

* Solver updated to the Xpress Suite Optimization 7.8.
* Added a new heuristic method: hot-start (save and load initial solutions for new instances).
* Added the possibility to interrupt an execution and return the best solution available with the command CTRL + C.
* Added the representation of pumped storage as hydro units.
* Included an updated version of outputs visualization tool for the cases with network representation, with an option to create automatically the geographical coordinates.
* Added the possibility of definition for Secondary Spinning Reserve Limits and Offers in 15/30 minutes for hydro power plants and units.
* Added the possibility of definition for Secondary Spinning Reserve Limits and Offers in 15/30 minutes for thermal power plants.
* Added the possibility to import system secondary spinning reserve requirements of a SDDP mid-long term planning study for the chronological execution option.
* Added the possibility to import circuit’s violation limits of a SDDP mid-long term planning study for the chronological execution option.
* Added import/export data from/to CSV functionality to the Sum of Circuits Flow.
* Extended some model dimensions such as maximum number of circuits, buses and renewable power plants.
* Improved the memory allocation of network constraints

## Corrections

* Corrected a bug regarding the maximum number of startups for hydro units.
* Corrected a bug regarding the minimum pumping requirements for pumped storage.
* Corrected a bug regarding the generation constraint requirements for pumped storage.
* Corrected a bug regarding the rolling horizon execution.

# Version 5.13

## New features

* Solver updated to the Xpress Suite Optimization 7.7.
* Added the variable minimum turbined outflow constraint for Hydro Power Plants.
* Added the individual attendance option for System Secondary Spinning Reserve.
* Added the definition of groups of plants to meet the secondary spinning reserve requirements.
* Added the minimum up-time for individual attendance of System Secondary Spinning Reserve.
* Added the initial condition definition of plants and groups for individual attendance of System Secondary Spinning Reserve.
* Added a new heuristic method: rolling horizon.
* Included the possibility to define a maximum availability constraint for a set of fuels.
* Added the possibility to aggregate commitment decisions intra-hourly for a specific range.
* Added the maximum number of shutdowns for Thermal Power Plants.
* Included the functionality to copy a Hydro Plant on the Hydro Plant configuration screen.
* Included the functionality to copy a Thermal Plant on the Thermal Plant configuration screen.
* Added import/export data from/to CSV functionality to the Renewable Sources Configuration.
* Extended some model dimensions such as maximum number of circuits and buses.
* Several improvements and new developments applied to Cloud Computing mode, such as Hadoop / Amazon Redshift integration and multi-scenarios graphing tool.
* New output results file:
  * Thermal generation marginal cost

## Corrections

* Corrected a bug in the Renewable Power Plants Configuration screen.
* Corrected a bug in the Circuits Configuration screen.
* Corrected a bug regarding the penalty value for Primary Reserve.

# Version 5.12

## New features

* Added the possibility to import alert storage constraints of a SDDP mid-long term planning study for the chronological execution option.
* Added the possibility to import flood control storage constraints of a SDDP mid-long term planning study for the chronological execution option.
* Added the possibility to import minimum operative storage constraints of a SDDP mid-long term planning study for the chronological execution option.
* Added the possibility to import minimum total outflow constraints of a SDDP mid-long term planning study for the chronological execution option.
* Added the possibility to import irrigation constraints of a SDDP mid-long term planning study for the chronological execution option.
* Added the possibility to import hydro maintenance schedule of a SDDP mid-long term planning study for the chronological execution option.
* Added the possibility to import thermal maintenance schedule of a SDDP mid-long term planning study for the chronological execution option.
* Added the possibility to import hydro spinning reserve constraints of a SDDP mid-long term planning study for the chronological execution option.
* Added the possibility to import thermal spinning reserve constraints of a SDDP mid-long term planning study for the chronological execution option.
* Added the possibility to import generation system constraints of a SDDP mid-long term planning study for the chronological execution option.
* Added the possibility to import sum of circuits flow constraints of a SDDP mid-long term planning study for the chronological execution option.
* Added the possibility to import maximum export/import between electrical areas constraints of a SDDP mid-long term planning study for the chronological execution option.
* Added the possibility to define initial / final scenarios and initial / final stages based on the SDDP execution for the chronological execution option.
* Added the Fast Response Energy Storage Configuration definition.
* Added import/export data from/to CSV functionality to the Hydro Spinning Reserve Data.
* Added import/export data from/to CSV functionality to the Thermal Spinning Reserve Data.
* Added import/export data from/to CSV functionality to the Hydro Energy Bid Data.
* Added the possibility to represent thermal plants gas emissions and respective emission costs (CO2, NOx and SOx).
* Added the extension of generation damping option to be applied for all plants or plants type.
* New Spanish and English versions of User’s Manual.
* Included a beta version of outputs visualization tool for the cases with network representation, based on geographical coordinates.
* Added a new possibility of definition of chronological data based on a predefined set of days.
* New output results file:
  * Battery net generation
  * Battery storage
  * CO2 Emissions
  * NOx Emissions
  * SOx Emissions

## Corrections

* Corrected a bug in the future cost function option as terminal function to disaggregate the mid-long term planning study in hourly time steps.

# Version 5.11

## New features

* Added the possibility to import:
  * system demand data of a SDDP mid-long term planning study for the chronological execution option.
  * bus demand data of a SDDP mid-long term planning study for the chronological execution option.
  * inflow data of a SDDP mid-long term planning study for the chronological execution option.
  * renewable generation data of a SDDP mid-long term planning study for the chronological execution option.
* Included an option for retrieving, aggregating, filtering and graphing NCP results scattered throughout the temporary directories of a chronological execution.
* Added import/export data from/to CSV functionality to the Renewable Generation Data.
* Extended some model dimensions such as maximum number of circuits and buses.

## Corrections

* Corrected a bug in the target storage option as terminal function to disaggregate the mid-long term planning study in hourly time steps.
* Fixed an issue with the memory allocation of individual hydro/thermal plants generation constraints.
* Corrected a bug regarding the Minimum Time for Startup of Thermal Plants.
* Corrected a bug regarding the Total Minimum Outflow requirements of Hydro Plants.
* Corrected a bug regarding the Minimum Turbined Outflow requirements of Hydro Plants.

# Version 5.10

## New features

* Added the Discrete Generation for Hydro Power Plants.
* Added the possibility of definition for System Secondary Spinning Reserve Requirements in 15/30 minutes.
* Added the individual Generic Generation Constraints for:
  * Hydro Power Plants
  * Thermal Power Plants
* Added the Warm Startup Cost field for Thermal Power Plants.
* Added the Startup Minimum Time for Warm State of Thermal Power Plants.
* Added the option to only consider coupled generation of Combined Cycle Plants.
* Reformulated the Startup Minimum Time Modeling of Thermal Power Plants.
* Added the possibility of definition for System Generic Generation Constraints in % of the total demand.
* Added import/export data from/to CSV functionality to:
  * Hydro Secondary Spinning Reserve
  * Thermal Secondary Spinning Reserve
* New output results file:
  * Thermal warm start-up cost
  * Thermal warm start-up decision
  * Thermal cold start-up decision

## Corrections

* Corrected a bug in the Combined Cycle Modeling of Thermal Power Plants.
* Corrected a bug in the option to disaggregate the mid-long term planning study in hourly time steps.

# Version 5.9.9

## New features

* Added the option to disaggregate the mid-long term planning study in hourly time steps based on the refinement of SDDP results using a weekly or monthly stage SDDP simulation. The objective of this feature is to present results chronologically using hourly time steps. With such procedure, for instance, a SDDP 1-year run with weekly time steps will be refined to 8,760 hours results obtained by 52 consecutive sequential (chronological) NCP executions of 1 week each.
* Added the combined cycle generators coupling modeling with minimum time and coupling cost representation.
* Reformulated the Cold Reserve Screen for Hydro and Thermal Power Plants.
* Reformulated the Energy Bid Screen for Hydro Power Plants.
* Solver updated to the Xpress Suite Optimization 7.4.
* New output results file:
  * Thermal shutdown cost
  * Thermal cold start-up cost
  * Thermal start-up cost
  * Combined cycle generator coupling cost
  * Combined cycle generator coupling

## Corrections

* Corrected the measure unit for irrigation violation output file.
* Corrected a bug in the Thermal Forced Units screen.
* Corrected a bug in the System Generation Constraints screen.

# Version 5.9.8

## New features

* Added the Combined Cycle Configuration definition.
* Added the Fuel Consumption Coefficients definition for Thermal Plants.
* Added the Fuel Consumption Function definition for Thermal Plants.
* Added the Integer Representation for Circuit Losses.
* Added the Maximum Operative Storage Constraint for Hydro Plants.
* Added the Overloading penalty field for Renewable Sources.
* Added the Total Outflow Maximum Ramp-up constraint for Hydro Plants.
* Added the Total Outflow Maximum Ramp-down constraint for Hydro Plants.
* Added the Shutdown Cost field for Thermal Plants.
* Added the Cold Startup Cost field for Thermal Plants.
* Added the Generation Constraint as a % of total load for Renewable Sources.
* Added the possibility to define time steps of 15 and 30 minutes for Renewable Sources Generation.
* Added import/export data from/to CSV functionality to:
  * Hydro Plants Configuration
  * Thermal Plants Configuration
  * Bus Configuration
  * Circuit Configuration
* Added the automatic unit conversion in Target Storage screen.
* Added a new language in the graphical interface (French).
* Deprecated the option to define hourly/daily production factor for hydro plants.
* Added the possibility to define the constraints of the thermal plants startup minimum time screen in floating point numbers.
* New output results file:
  * Maximum operative storage violation
  * Thermal shutdown
  * Renewable over generation
  * Thermal operative average cost

## Corrections

* Corrected a bug regarding the Minimum Time for Startup of Thermal Plants.
* Corrected some general labels in the graphical interface.
* Corrected a bug regarding definition of new elements (grey labels).

# Version 5.9.7

## New features

* Added the circuits selection to be considered for losses penalty.
* Added the possibility of fuel changing during the horizon for multi-fuel plants.
* Solver updated to the Xpress Suite Optimization 7.3.
* Definition of number of cores to be used in NCP Mixed-Integer Programming Solver.
* New output results file:
  * Hydro secondary reserve cost
  * Thermal secondary reserve cost
  * Hydro unit secondary reserve cost
  * Hydro energy bid cost

## Corrections

* Corrected a bug regarding the representation of elevation x storage variation.
* Corrected a bug regarding the variable hourly production factor.
* Corrected a bug regarding the Renewable Source Generation Data.
* Corrected a bug regarding the bus selection for Renewable Sources.
* Corrected a bug regarding the minimum generation of commitment hydro plants.

# Version 5.9.6

## New features

* Added the Renewable Source Configuration definition.
* Added the Renewable Source Generation constraint.
* Added the Minimum Generation field for Hydro Plants.
* Added the Forbidden Zone constraint for Thermal Plants.
* Added the NCP Dimensions screen in the menu bar.
* Added the Secondary Spinning Reserve Bid Prices definition for Hydro Units.
* New output results file:
  * Non-dispatchable generation

## Corrections

* Corrected a bug regarding the Temperature effects data for Thermal Plants.

# Version 5.9.5

## New features

* Added an option to value the water lagging between hydro plants in the end of horizon.

## Corrections

* Corrected a bug regarding Cold Ramp constraint for Hydro Plants and Hydro Units.
* Corrected a bug regarding Concave Specific Consumption Curve of Thermal Plants.
* Corrected a bug regarding Self Consumption and Thermal Plants with Minimum Generation.
* Corrected a bug in the Maintenance data writing process for Hydro and Thermal Plants.

# Version 5.9.4

## New features

* Added the Generation Limits per Elevation for hydro units.
* New output results file:
  * Hydro unit opportunity cost.
  * Available hydro (capacity - generation)
  * Available thermal (capacity - generation)
  * Available hydro unit (capacity - generation)
  * Available hydro unit capacity

## Corrections

* Corrected a bug in the Bus Demand data writing process for 15 and 30 minutes time steps.
* Corrected a bug regarding future reservoirs.
* Corrected a bug regarding hydro units maintenance.
* Corrected a bug regarding Null Water Value.
* Corrected a bug regarding initial condition of CHP thermal plants.

# Version 5.9.3

## New features

* Added the Maintenance Scenario for hydro units.

## Corrections

* Corrected a bug in the Electrical Areas data reading.
* Corrected a bug in the Sum of Circuit Flows data reading process.
* Corrected a bug in the Bus Configuration graphical interface.
* Corrected a bug in the Circuits Configuration graphical interface.
* Corrected a bug in the Elastic Load/Supply graphical interface.

# Version 5.9.2

## New features

* Added the Precedence Order Constraint for hydro units.
* Utilization of future benefit function generated by MAXREV (maximize revenues criterion).

## Corrections

* Fixed an issue with a memory allocation error causing the tree search to be reported as finished.
* Fixed an issue when deleting nodes from the global file in parallel MIP.
* Reduced the amount of memory needed to store active nodes for a MILP.

# Version 5.9.1

## New features

* Added new Optimization option: enable/disable parallel execution.
* Added the Problem Representation option: do not allow deficit for economic reasons.

## Corrections

* Corrected a bug in the Secondary Spinning Reserve data screen were the select button of the Hydro Plants list was not being enabled even when there were available hydro plants for selection.
* Corrected a bug in the Secondary Spinning Reserve maximum limit for thermal power plant.
* Corrected a bug in the Sum of Circuit Flows modeling.

# Version 5.9

## New features

* Added the new Secondary Spinning Reserve modeling with possibility of definition of minimum and maximum reserve limits and offers per hydro unit.
* Added the Generation Constraint modeling per hydro unit.
* Added the Initial Status modeling per hydro unit.
* Added the Ramps Constraints (cold and warm) modeling per hydro unit.
* Added the Maximum Number of Start-ups modeling per hydro unit.
* Added the Forbidden Zone modeling per hydro unit.
* Added the Ramps Constraints (cold) modeling per hydro plant.
* Added the Null Water Value definition per hydro plant.
* Added the Elastic Load/Supply modeling
* Added the Electrical Areas Configuration
* Added the Import/Export limits for Electrical Areas.
* Added the Maximum Number of Variations for thermal plants with minimum time in constant power.
* Included the functionality to copy a Bus on the Bus configuration screen.
* Included the functionality to copy a Circuit on the Circuit configuration screen.

# Version 5.8.3

## New features

* NCP Mixed-Integer Programming Solver (Xpress) fully exploits multi-core machines, which can greatly reduce the computational time with distributed computing.
* A NCP 64-bit version is now available; A big advantage of this setting is the overcoming of the 2GB RAM memory limitation of the 32-bit system.
* Dynamic allocation of memory, which sets the amount of memory required by running NCP to the minimum required.

# Version 5.8.2

## New features

* NCP can now handle paths containing white spaces.
* NCP User's Manual now contains the output file names description.

## Corrections

* Corrected a bug in the model regarding Target Generation constraint when the used time step was 15 or 30 minutes.
* Corrected a bug in the CSV module regarding maintenance entry data.
* Corrected a bug in the Sum of Circuits flows data screen.

# Version 5.8.1

## New features

* Future cost function (FCF) reading changed to allow different numbers of reservoirs between the function and data set.

## Corrections

* Corrected a bug that was preventing the DC-Link Circuits type to be saved.
* Corrected a bug regarding the Hydro and Thermal Secondary spinning reserve data screen.
* Corrected a bug that occurs when the user starts a new case from scratch.

# Version 5.8

## New features

* Improved data loading and navigation performance.
* Added the attribute 'DC-Link Circuit type' on the Circuit Configuration data screen.
* Added the attribute 'Associated Reservoir' to the Hydro Configuration data screen.
* Added the new Secondary Spinning Reserve modeling with possibility of definition of minimum and maximum reserve limits and offers per plant.

# Version 5.7.1

## New features

* NCP can now handle time steps of 30 minutes or 15 minutes. All input data and constraints will remain on an hourly basis, except for the demand (both the system level or in each bus bar, if the transmission network is modeled)

## Corrections

* Corrected a bug regarding alert storage and minimum storage.

# Version 5.7

## New features

* Input/output data unit converter.
* New output results file:
  * Revenue

## Corrections

* Corrected a bug regarding hydro generating unit data entry.

# Version 5.6.1

## New features

* New output results file:
  * Maximum available turbined outflow
  * Evaporation

## Corrections

*  Corrected a bug regarding maximum available turbined outflow.

# Version 5.6

## New features

* Removed the columns 'constant Power Period (H)' and 'Previous Load Condition' from the Hydro Initial Status screen.

## Corrections

* Corrected a bug that was preventing the bus configuration file to be updated when a change was made on a multi fuel thermal plant
* Corrected a bug on NCP's mathematical model regarding evaporation.
* Corrected a bug on NCP's mathematical model regarding controllable spill.

# Version 5.5

## New features

* Added the ability to customize the label of the tree-view data elements. This functionality is available on the Preferences Screen.
* Added the Hydro Cold Reserve Bid chronological data screen.
* Added the Thermal Cold Reserve Bid chronological data screen.
* Added the System Cold Reserve chronological data screen.
* Added new execution option: 'Use generation damping'. 
* 'Spinning Reserve' label has been updated to 'Primary Reserve'
* 'Auxiliar Consumption' label has been updated to 'Self Consumption'.
* 'Reserve bid' label has been updated to 'Operative spinning reserve bid'
* 'Generation Reserve' label has been updated to 'Secondary Spinning Reserve'
* 'Power reserve' label has been updated to 'Operative spinning reserve bid'
* 'Power reserve price' label has been updated to 'Operative spinning reserve price'
* New output results file:
  * Hydro cold reserve bid
  * Thermal cold reserve bid
  * Reserve bid marginal cost

# Version 5.4

## New features

* The definition of the fuels used by the thermal plants is more user friendly.
* Added the Power reserve price chronological data screen (only for maximization of revenues).
* Added new execution option: variable production factor (hourly/daily).
* New output results file:
  * Target generation marginal cost
  * Secondary reserve marginal cost
  * Availability fuel marginal cost

# Version 5.3

## New features

* Added the voltage field to the Bus Configuration screen.
* Added the Shunt capacitor/reactor chronological data screen.
* Added the Voltage limits chronological data screen.
* Added the Hydro reactive generation chronological data screen.
* Added the Thermal reactive generation chronological data screen.
* Added the Power factor chronological data screen.
* New output results file:
  * Minimum outflow violation
  * Alert storage violation
  * Minimum storage violation
  * Minimum total outflow violation
  * Maximum total outflow violation
  * Irrigation violation
  * Terminal function marginal cost
  * Values of the objective function terms

# Version 5.2

## New features

* Added the parameter 'relative convergence tolerance' to the Optimization Options panel of the Execution Parameters screen.
* Added the ability to define the configuration of the Generating Units of the Hydro Plants 
* Incorporated the DrawHydro module to the Hydro configuration screen

# Version 5.1.2

## Corrections

* Corrected a bug on the Hydro definition screen which occurred whenever a user tried to delete any value from the evaporation coefficient table.
* Corrected a bug on NCP's mathematical model regarding evaporation.

# Version 5.1.1

## New features

* Added import/export data from/to CSV functionality to:
  * Hydro Maintenance chronological data screen.
  * Thermal Maintenance chronological data screen.
  * Inflows chronological data screen
  * System Demand chronological data screen
  * Fuel Price chronological data screen
* NCP's mathematical model is now taking into consideration the Reservoir's Controllable Spill flag of the Hydro configuration data screen.
* NCP's mathematical model is now taking into consideration the Reservoir's Evaporation Coefficients of the Hydro configuration data screen.
* New output results file:
  * Marginal cost per circuit

# Version 5.1

## New features

* Added import/export data from/to CSV functionality to the Demand by bus chronological data screen.
* Added daily maximum number of start-ups constraint to the Thermal and Hydroelectric Maximum Number of Start-ups screen.

## Corrections

* A bug was corrected in the routine which updates the sddp.dat file.

# Version 5.0

## New features

* Included the ability to add/remove data series values on the Power Reserve constraint screen.
* Included the ability to add/remove data series values on the Energy Price Scenario screen.
* Included the Combined Cycle option on the Thermal configuration screen.

## Corrections

* A bug that prevented the sort functionality to work properly on numeric columns has been corrected.
* A bug was corrected on the Fuel Configuration screen which prevented the price attribute to be saved.
* A bug was corrected on the Hydro Configuration screen which prevented the list of Hydro Sites to be re-populated after an Add or Remove operation on a Hydro Site.
* Included the Start-up cost field on the Thermal plants configuration screen.
* A bug was corrected on the load routine of Thermal Configuration data that was preventing the loading of the alternative fuels data.
