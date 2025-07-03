---
title: "Release notes"
parent: "SDDP 17.3"
nav_order: 1
layout: default
---

# SDDP 17.3

🌐 Please refer to the [release site](http://psr-energy.com/software/sddp-17.3.html) and check out the most important features
developed on this release.
📝 For the detailed changelog and download links, please visit [this page](sddp17.3-changelog.md).

## New features and improvements

* GUI
  * Discontinuation of Graph 3 interface, replaced by Graph 4
  * Discontinuation of DrawHydro, replaced by Topology Viewer
  * Discontinuation of 32-bit version  
* Model
  * Hourly representation
    * Hydro commitment
    * Risk aversion curve (RAC) included in the model
    * Enhanced energy transference window of flexible demand modeling
  * The hydroelectric storage data now allows the definition of explicit limits for run-of-river plants, which are used in the chronological blocks, typical days and hourly representation for intra-stage modulation
    * Aiming to provide an automatic transition to the new representation, a data conversion process has been incorporated into the 17.3 interface:
      * The ror_operative_storage.dat file that contains the storage limits for hourly executions has been discontinued with the information being incorporated in the registry data
      * Run-of-river plants with 0 hm3 of useful storage had their limits recalculated according to its modulation capacity. The new limits are determined as Vmax = Vmin + 2 * (1 - regulation factor). Minimum storage Vmin remains unchanged.
    * Added option to allow automatic classification of hydroelectric plants based on its regularization capacity (useful storage and turbining capacity ratio, given in hours) 
  * Typical days modeling
    * Intra-stage modulation for small storages (run-of-river, batteries, CSPs...)
    * Thermal operating constraints: generation ramps, minimum downtime, minimum uptime, maximum uptime
    * Hydro operating constraints: generation ramps and outflow ramps
    * New flexible demand modeling for typical days representation (following new hourly modeling)
    * Typical days with aggregated block strategy in policy phase
    * Detailed and profile typical days mapping options
    * Automatic typical days clusterization based on the demand stage profile through PSRClustering (only for detailed mapping)
  * Network contingency representation. This feature includes an option to enable contigencies representation from a specific iteration in the policy
  * Post-contingency network report
  * Operational status of DC link
  * Custom modeling
    * Generic interpolation constraints non-linear functions modeling
    * Generic variables, allowing its use with internal SDDP variables through generic linear and interpolation constraints
    * New variables in generic constraints: initial hydro volume, battery charge and discharge, demand, and electrical consumption for electrification
  * New dashboard and result comparator based on PSRIO
  * Hourly maintenance for hydro, thermal, and battery as well as stage-wise battery maintenance
  * Execution option to not apply the forced outage factor
  * Generation reserve features
    * Quantity and price of joint battery and CSP reserve offer
    * Joint renewable reserve
    * Maximum offer per generator-reserve
    * Reserve sharing
    * Absolute reserve + dynamic probabilistic reserve option
    * Allow maximum joint reserve offer as percentage of nominal available capacity for hydro and thermal plants
  * Battery Operation & Maintenance cost
  * Modification data of hydroelectric Operation & Maintenance cost
  * Dynamic line rating for the representation of environment conditions (such as temperature) influence over transmission lines capacities 
  * Execution options interface reorganization
  * Xpress solver update to version 9.1

