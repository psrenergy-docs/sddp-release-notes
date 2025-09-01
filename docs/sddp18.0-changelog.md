---
title: "Detailed changelog"
parent: "SDDP 18.0"
nav_order: 2
layout: default
---

# SDDP 18.0.4rc1
📅 Date: 2025-09-01<br>
🔗 Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-18.0.4rc1-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-18.0.4rc1-setup-linux.zip)

## Expansion Planning Module (OptGen)
###  Fixed issues
####  OptGen 1
  * Fixed an issue related to the execution of coordinated cases

# SDDP 18.0.3
📅 Date: 2025-08-29<br>
🔗 Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-18.0.3-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-18.0.3-setup-linux.zip)

## Operation Planning Module (SDDP)
### New features and improvements
  * Changed header of CSV output files to always be in english

###  Fixed issues
  * Fixed a possible infinite loop in cases with circuit projects in OptGen integration
  * Hourly representation
    * Fixed an issue introduced in recent versions in the correct consideration of thermal plant operation mode (standard or must-run)
  
## Expansion Planning Module (OptGen)
###  Fixed issues
####  OptGen 2
  * Fixed an issue with the Firm Capacity Automatic Calculation (PFCA,1) feature
  * Fixed an issue with multi-fuel thermal plants with fuel exclusive generation


# SDDP 18.0.3rc6
📅 Date: 2025-08-27<br>
🔗 Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-18.0.3rc6-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-18.0.3rc6-setup-linux.zip)

## Operation Planning Module (SDDP)
### New features and improvements
  * Added transformer flow and DC line flow variables to generic constraints
  * New output: energy efficiency applied

###  Fixed issues
  * Compatibilized the maximum battery charging capacity between the hourly and block models. Now, the
    maximum charging capacity is applied to the energy inside the battery in the block model, as previously
    done in the hourly model
  * Fixed the application of an hourly energy efficiency defined in p.u. to an hourly demand
  * Fixed an issue in the representation of the Markov infow model in a simulation execution
  * Fixed multi-fuel thermal plant association to electrical bus for cases created in version 18
  
## Graphical user interface
###  Fixed issues
  * Fixed an issue that prevented the use of the hot-start option
  * Fixed the thermal operation mode field definition


# SDDP 18.0.3rc5
📅 Date: 2025-08-25<br>
🔗 Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-18.0.3rc5-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-18.0.3rc5-setup-linux.zip)

## Operation Planning Module (SDDP)
###  Fixed issues
  * Fixed sum of circuit flow constraint unlimited lower bound option


# SDDP 18.0.3rc4
📅 Date: 2025-08-24<br>
🔗 Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-18.0.3rc4-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-18.0.3rc4-setup-linux.zip)

## Expansion Planning Module (OptGen)
###  Fixed issues
####  OptGen 1
  * Fixed an issue with post processing tool (PSRIO)
  * Fixed an issue with resilience planning and rolling horizons


# SDDP 18.0.3rc3
📅 Date: 2025-08-19<br>
🔗 Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-18.0.3rc3-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-18.0.3rc3-setup-linux.zip)

## Operation Planning Module (SDDP)
###  Fixed issues
  * Fixed an specific issue that prevented the execution when using the Markov inflow model
  * Included the representation of the start-up cost for hydro plants with commitment
    representation in the block resolution

## Graphical user interface
###  Fixed issues
  * Fixed import/export of blank values in the historical inflow data per stage
  * Fixed file format of the hourly historical inflow data


# SDDP 18.0.3rc2
📅 Date: 2025-08-13<br>
🔗 Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-18.0.3rc2-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-18.0.3rc2-setup-linux.zip)

## Maintenance Planning Module (OptMain)
###  Fixed issues
  * Fixed an error related to weekly stages cases

# SDDP 18.0.3rc1
📅 Date: 2025-08-07<br>
🔗 Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-18.0.3rc1-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-18.0.3rc1-setup-linux.zip)

## Operation Planning Module (SDDP)
###  Fixed issues
  * Fixed the loading of CSP bus connection

## Expansion Planning Module (OptGen)
### Fixed Issues
#### OptGen 2
  * Fixed an error related to the installed capacity of future projects in min/max investment constraints
  * Fixed an error in generic operative constraints including demand segment variables
  * Fixed an error related to operative generic  constraints
  * Fixed an error in generic operative constraints including demand segment variables

### New features and improvements
#### OptGen 2
  * Improve warning message of excess generation infeasibility showing the name of each bus/area/system where it occurs


# SDDP 18.0.2
📅 Date: 2025-08-01<br>
🔗 Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-18.0.2-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-18.0.2-setup-linux.zip)

## Operation Planning Module (SDDP)
###  Fixed issues
  * Fixed the writing of some outputs in typical days execution with aggregation in the policy phase
  * Hourly representation
    * Fixed the consideration of generation offers

## Expansion Planning Module (OptGen)
### Fixed Issues
#### OptGen 1
  * Fixed an error with energy efficiency projects with data defined in p.u of the demand
  * Fixed an error when there are generic investment constraints and no min/max constraint
  * Fixed errors when running OptGen with PSRCloud 5.4
  
#### OptGen 2
  * Fixed data validation issues when running with TSL scenarios
  * Fixed an error related to reserve requirement constraints backing DC Links
  * Fixed an error related to the DPR calculations when there are renewable projects being backed

### New features and improvements
#### OptGen 2
  * Added debug output files to generic investment constraints (opt2_genericlhs.csv, opt2_genericrhs.csv, opt2_genericagents.csv, opt2_genericdbg.csv)

# SDDP 18.0.2rc8
📅 Date: 2025-07-29<br>
🔗 Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-18.0.2rc8-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-18.0.2rc8-setup-linux.zip)

## Operation Planning Module (SDDP)
###  Fixed issues
  * Adjustment in hydro capacity output (phidsf.csv) to consider piecewise functions involving maximum turbining


# SDDP 18.0.2rc7
📅 Date: 2025-07-23<br>
🔗 Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-18.0.2rc7-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-18.0.2rc7-setup-linux.zip)

## Operation Planning Module (SDDP)
###  New features and improvements
  * New output: generic linear constraint value


# SDDP 18.0.2rc6
📅 Date: 2025-07-17<br>
🔗 Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-18.0.2rc6-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-18.0.2rc6-setup-linux.zip)

## Operation Planning Module (SDDP)
###  Fixed issues
  * Fixed a memory invasion issue in coordinated cases


# SDDP 18.0.2rc5
📅 Date: 2025-07-15<br>
🔗 Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-18.0.2rc5-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-18.0.2rc5-setup-linux.zip)

## Operation Planning Module (SDDP)
###  Fixed issues
  * Added missing dependencies to Linux setup
  * Fixed energy efficiency OptGen cuts when defined in per-unit (pu)
  * Fixed generic constraints and thermal emissions consideration in coordinated policy execution

## Graphical user interface
###  Fixed issues
  * Fixed registration of multi-fuel thermal plants
  * Fixed database conversion when battery modification file contains non-existent elements


# SDDP 18.0.2rc4
📅 Date: 2025-07-14<br>
🔗 Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-18.0.2rc4-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-18.0.2rc4-setup-linux.zip)

## Operation Planning Module (SDDP)
###  Fixed issues
  * Fixed coordinated execution with network representation

## Graphical user interface
###  Fixed issues
  * Changed column type for thermal plant maximum generation to enable proper filtering


# SDDP 18.0.2rc3
📅 Date: 2025-07-12<br>
🔗 Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-18.0.2rc3-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-18.0.2rc3-setup-linux.zip)

## Graphical user interface
###  New features and improvements
  * Reduced minimum installation requirements to Windows 8.1 and Windows Server 2012 R2. For versions
    below Windows 10 and Windows Server 2016, it will be necessary update the WebView2 component
    during SDDP's installation


# SDDP 18.0.2rc2
📅 Date: 2025-07-11<br>
🔗 Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-18.0.2rc2-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-18.0.2rc2-setup-linux.zip)

## Operation Planning Module (SDDP)
###  Fixed issues
  * Fixed the consideration of fuel prices varying per scenario


# SDDP 18.0.2rc1
📅 Date: 2025-07-09<br>
🔗 Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-18.0.2rc1-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-18.0.2rc1-setup-linux.zip)

## Expansion Planning Module (OptGen)
###  Fixed issues
  * Fixed an error related to demand-based requirement constraints


# SDDP 18.0.1

📅 Date: 2025-07-03<br>
🔗 Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-18.0.1-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-18.0.1-setup-linux.bin)

Official release