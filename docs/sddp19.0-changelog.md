---
title: "Detailed changelog"
parent: "SDDP 19.0"
nav_order: 2
layout: default
---

# SDDP 19.0

📅 Date: to be announced<br>
🔗 Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-19.0-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-19.0-setup-linux.bin)

This page lists every change you will notice when moving from **SDDP 18.0.x** to **SDDP 19.0**. Fixes that were already delivered in 18.0.x hotfixes are not repeated here; see the [SDDP 18.0 changelog](sddp18.0-changelog) for those. For an overview of the main features, see the [release notes](sddp19.0-release-notes).

**Contents**

- [Before you upgrade](#before-you-upgrade)
- [Installation and platform](#installation-and-platform)
- [Database and file structure](#database-and-file-structure)
- [Graphical user interface](#graphical-user-interface)
- [Operation Planning Module (SDDP)](#operation-planning-module-sddp)
- [Expansion Planning Module (OptGen)](#expansion-planning-module-optgen)
- [Short-term model (NCP)](#short-term-model-ncp)
- [Transmission network: OptNet, NetPlan and Network Report](#transmission-network-optnet-netplan-and-network-report)
- [Reliability Module (Coral)](#reliability-module-coral)
- [Maintenance Planning Module (OptMain)](#maintenance-planning-module-optmain)
- [Results post-processing (PSRIO 5.0)](#results-post-processing-psrio-50)
- [Documentation: the new Knowledge Hub](#documentation-the-new-knowledge-hub)
- [Coming in future releases](#coming-in-future-releases)
- [Removed and discontinued features](#removed-and-discontinued-features)
- [Fixed issues](#fixed-issues)

---

## Before you upgrade

SDDP 19.0 changes the study database format and its installation requirements. Please read these points before you convert any production case.

| Topic | What changes in 19.0 | What you should do |
|---|---|---|
| **Data format** | Cases are converted to a new CSV-based format with unique element identifiers. **SDDP 18.0 cannot open a converted case.** | The GUI makes a timestamped backup automatically (`Backup\Backup_yyyyMMdd_HHmmss`). Keep your own copy as well if you still need to run the case in 18.0. |
| **Side-by-side install** | 19.0 installs into its own folder and Start-menu group. It does not replace 18.0. | You can keep both versions installed while you migrate. |
| **Windows version** | The minimum is now **Windows 10 1607 / Windows Server 2016**. Windows 8.1 and Server 2012 R2 are no longer supported. | Upgrade the operating system first, if needed. |
| **.NET 9** | The **.NET 9 Desktop Runtime** is a new prerequisite (the updater, the Add-in Manager, the CSV Editor and TMS Preview use it). | The online installer downloads it, and the offline installer includes it. |
| **MPI** | **MPICH2 is no longer supported on Windows**. Only MS-MPI is used. | Move multi-machine Windows setups to MS-MPI. |
| **Licensing** | The hardware-key (dongle) license was removed. Only the PSR software license is used. NCP needs its own "NCP 7.0" license feature. | Contact PSR if you still rely on a dongle. |
| **Add-ins** | Some tools are now **add-ins** that you install from the Add-in Manager: OptNet, NetPlan AC optimal power flow (formerly OptFlow), PSRNetworkReport and PSRClustering. | Install the add-ins you use after installing SDDP 19.0. |
| **Removed features** | The gas network, legacy CO2 emission factor, POCP target storage, quarterly stages and other options were removed (see [Removed and discontinued features](#removed-and-discontinued-features)). | Most are converted automatically. Check the table for the ones that need manual action. |
| **Changed defaults** | OptGen 1 now includes additional years in Benders cuts by default. Scenario probabilities in SDDP-OptGen runs must now be requested explicitly. | Review these if you compare 19.0 results with 18.0 (see the [SDDP](#simulation-and-integration-with-optgen) and [OptGen](#changed-behaviour-and-defaults) sections). |

---

## Installation and platform

### New features and improvements
- **Side-by-side installation**: SDDP 19.0 has its own installation and Start-menu group. 18.0 stays installed and keeps working.
- **In-app updates**: SDDP 19.0 can be updated from inside the GUI without running a new setup:
  - Updates follow release channels that come from the installed version: a final release receives *Stable* updates, and a beta or RC receives *Preview* updates. A stable installation is never overwritten by a beta. A new major or minor version is offered as a separate installation.
  - A background check covers both SDDP and the installed add-ins and shows a single notification, from which you can update directly.
  - Before closing SDDP to apply an update, the updater checks for unsaved work and brings the save prompt to the front.
  - Downloads run in parallel, skip optional components you did not install (help, examples), never overwrite the example cases, and only delete files the updater installed itself.
  - Your license file is never touched by an update.
  - Downloads use your PSR account session: if you are not signed in, the updater asks you to sign in to SDDP first.
- **Add-in system and Add-in Manager**: a new **Add-in Manager**, available from the GUI, lists the add-ins that PSR publishes for your SDDP version:
  - It can install, update and uninstall several add-ins at once, and shows a maturity label (Beta, RC) and a changelog link for each one.
  - Only digitally signed add-ins compatible with the installed SDDP version are installed.
  - When you run a tool whose add-in is missing, the Add-in Manager opens automatically.
  - The SDDP uninstaller asks whether installed add-ins should also be removed.
  - Add-ins available for 19.0: **OptNet**, **NetPlan – AC optimal power flow** (formerly OptFlow), **PSRNetworkReport** (formerly built into the installation) and **PSRClustering** (formerly an optional installer component).
- **New in the installation**: the NCP short-term model (see [NCP](#short-term-model-ncp)) and bin3csv, a new command-line result converter (see [below](#new-tools)).
- **Example cases** have been re-saved in the 19.0 data format. They can no longer be opened with 18.0.
- The installer now checks that the components it downloads are signed by PSR.

### Linux
- The Linux distribution now includes **NCP**.
- **Coral on Linux now checks the license**, the same way as on Windows. Before, the Linux build ran unlicensed.
- Coral on Linux uses Xpress 9.1, and OptGen and NCP use Xpress 9.9.

### Changed requirements
- The minimum Windows version is now Windows 10 1607 / Windows Server 2016 (18.0 accepted Windows 8.1 / Server 2012 R2).
- The .NET 9 Desktop Runtime is a new prerequisite.
- The MPI selection page was removed from the installer: SDDP and OptGen always use MS-MPI, which is installed if missing.

---

## Database and file structure

### Longer names and codes
- **Names are no longer limited to 12 characters**. This applies to all elements, in input files, terminal FCF files, logs, reports and output files. Output agent names can be up to 1000 characters, in SDDP and in bin2csv.
- **Element codes can have up to 9 digits** (they had 4 before).
- Long names are supported across SDDP, OptGen 1 and 2, NCP, the hourly representation and the GUI.

### New CSV-based file structure
- **About 60 input files moved to a CSV format**, with a version line and a header row instead of fixed-width columns. This includes the configuration of systems, hydro and thermal plants, fuels, interconnections, batteries, reserves and fuel contracts.
- Modification files now use separate year, month and day columns instead of a single date column.
- Chronological per-plant files (minimum and maximum storage, outflow limits, irrigation, fuel costs, demand and others) no longer repeat the plant name, and the plant code field is wider.
- Saving a case is now **atomic**: each file is written to a temporary file and then renamed over the original. If SDDP crashes, the network drops or the disk fills up during a save, the existing input files are no longer left half-written.
- Names that contain commas are quoted correctly in CSV files, so they no longer corrupt the case on the next save.
- Case paths with non-ASCII (UTF-8) characters are supported.

### Unique identifiers
- **Each element now has a unique, user-editable identifier**, stored in a new file of the case.
- When a case is converted, identifiers are generated automatically from the element type, name and code.
- When you add an element in the GUI, the identifier is filled in automatically. You can also type your own, and duplicate identifiers are rejected.
- The identifiers are what mark a case as SDDP 19.0 data. SDDP 19.0 stops with an error if they are missing, so older databases must be converted by the GUI first.

### Automatic conversion of older cases
When you open a case from SDDP 18.0 or an earlier version, the GUI asks for confirmation, creates a timestamped backup in `Backup\Backup_yyyyMMdd_HHmmss` and converts the case. The conversion:
- rewrites the input files in the 19.0 format and generates the unique identifiers;
- converts the legacy **CO2 emission data** (the system carbon cost plus the CO2 emission factor of each fuel) into explicit CO2 emission elements;
- converts the legacy **gas network** into the **Energy Supply Chain** representation, including OptGen gas projects, constraints that refer to gas nodes or pipelines, and user expansion plans;
- converts the OptGen hydro inflow scenarios to the new format (see [OptGen](#changed-behaviour-and-defaults));
- converts saved graph configurations into charts in the new **Results** tab;
- creates the case's time-series database.

The conversion cannot be undone. Older SDDP 17 cases without a network, NetPlan cases and legacy NCP cases are also converted directly. The recent cases list shows the data version of each case ("ver. 19.0", "ver. 18.0", "ver. 17.x or older").

### Time-series database
- Each case can now have a **time-series database**. It registers CSV time-series files and links them to elements. New and converted cases get one automatically. It is used mainly for short-term (NCP) chronological data.
- **One file, any resolution**: before, NCP data had to be entered again for each resolution (one table for hourly, another for 30, 15 or 5 minutes). Now a series is entered once, at the resolution you already have, and the model upscales or downscales it to the resolution of the run, down to 1 minute. You choose how each series is converted (for example distribute, forward or backward fill, take first or last, step, or linear interpolation).
- **Flexible CSV format**: the layout is inferred from the header, any delimiter can be used, and a series can be split across several files. Data can be entered in four ways:
  - **absolute**: one value per timestamp, as before;
  - **sparse**: only the date parts at which the value changes (for example, year and month), with the gaps filled automatically;
  - **periodic**: leave out the major date parts to make a profile that repeats (for example, a daily profile by hour);
  - **date patterns**: declare when a value applies, for example from January to March, from 9:00 to 18:00. This is useful for peak and off-peak values, holidays or maintenance.

### New input data
The 19.0 database adds the following input data. The models that use each item are shown in italics, and the features are described in the module sections:
- **Inertia**: an inertia constant for hydro and thermal plants, and inertia requirement elements. *SDDP (including the hourly representation), NCP.*
- **Batteries**: a stored-energy loss factor, the cycle-counting option, reserve direction parameters and battery generation offers. *SDDP (including the hourly representation), OptGen 2, NCP.*
- **Reserves**: a reserve direction (up, down or both) for joint and primary reserves. Lines and transformers can have a maximum secondary reserve that can be shared through them, and a price for it. *SDDP (including the hourly representation), NCP.*
- **Data centers / large loads**: flexible demands can be marked as data centers, with an existing flag and a deployment level over time. *SDDP (including the hourly representation), OptGen 1 and 2.*
- **Fuels and fuel contracts**: hourly fuel price scenarios, hourly fuel-contract availability, a minimum offtake rate per stage, a take-or-pay cost that varies over time, and SOx/NOx emission factors. *SDDP (including the hourly representation); time-varying take-or-pay also in OptGen 2.*
- **Energy supply chain**: hourly demand scenarios, and a balance coefficient for thermal plants. *SDDP (including the hourly representation).*
- **Interconnections**: capacity, losses and cost each have their own dates per direction, and interconnection-sum constraints have their own lower and upper bounds. *SDDP.*
- **Generation and generic constraints**: a flag to disable them, a constraint unit and a constraint type. *SDDP (including the hourly representation).*
- **Hydro**: fractional travel times (fractions of an hour), mean forebay level, a unit precedence order, and tables with any number of points. *SDDP (including the hourly representation), NCP.*
- **Thermal**: installed capacity with its own date index, self-consumption, and combined-cycle options. *SDDP, NCP.*
- **OptGen projects**: a degradation factor by year of operation, and resilience days. *OptGen 1 and 2 (resilience days: C++ engine of OptGen 2 only).*
- **AC network**: per-plant reactive-power limits, voltage control data and short-circuit data. *NetPlan – AC optimal power flow.*
- **Short-term data**: the detailed short-term data of each element (hydro units and hill curves, start-up types, forbidden zones, initial conditions, terminal functions and others). *NCP.*
- **Georeference**: plants, systems and circuits can be georeferenced. *Graphical interface (Energy map).*

### Performance
- Cases load and save faster and use less memory: indexes speed up element lookup, many memory leaks were fixed, and a long text line full of empty fields no longer takes seconds to read.

---

## Graphical user interface

### Home page and navigation
- **New Home page** with pinned and recent cases, a filter, a case summary (study period, dimensions in use, last opened), copy path and **delete case** (to the Recycle Bin, optionally keeping a zipped backup).
- The new-case panel uses cards (blank case, import a case, and options added by add-ins).
- A **command palette** (Ctrl+Shift+P, also on the Tools tab) finds and runs any GUI command by name, including commands added by add-ins. **Go to element** has its own shortcut, Ctrl+G.
- A redesigned splash screen and account card.
- **Display scaling**: per-monitor DPI, Compact or System scaling, and an experimental fixed zoom mode.
- **Optional sign-in with your PSR account**, done in your default web browser. You can open the GUI without signing in. Online actions (add-ins, license, updates, PSR Cloud) ask for it when needed, and if the service cannot be reached you can choose to open SDDP offline.
- If the license file is missing at start-up, the GUI tries to update or download it in the background.

### Run tab
- **Redesigned Run tab** with an **active model** selector (SDDP, OptGen, NCP, NetPlan, OptNet, Coral), a "Prepare" step and a data status ("Case ready to run" / "Data not checked yet").
- Pre-simulation tools (Estima, Clustering) and case actions are now global groups shown before the model selector. Add-ins can add buttons to them.
- **Clean case**: replaces the SDDP-only "Clean" button. A window lists, by category, what can be removed from the case folder: model results, logs, temporary files, files not recognised by any model, and the operating policy (off by default). Selected files are moved to a quarantine folder from which they can be restored. Input data and time-series CSVs registered in the case are never removed, and you can add your own rules.
- The execution window has an **Execution issues** button that lists the warnings of the run, and errors and warnings are coloured as in a terminal.

### Results tab (charts and dashboards)
- **New Results tab**, replacing the legacy Graph tool. You build charts, dashboards and PSRIO scripts and save them inside the case (`<case>\psrplot\`):
  - **Variables**: choose model outputs (only outputs that exist in the case are offered), pick agents from a searchable grid, and set the unit, chart type and number of decimals.
  - **Aggregation**: over agents, stages, blocks and scenarios, using sum, average, weighted average, standard deviation, standard error, first/last, max/min, percentile or CVaR (1–99). Profiles are available per month, quarter, semester or year, or as a typical month, quarter, semester or year. Scenario and block ranges are selected by dragging.
  - **Chart types**: line, column, stacked column, percent column, area, stacked area, percent area, range area, area spline, pie and histogram.
  - **Dashboards**: combine charts and Markdown notes in tabs, with drag and drop from the tree. Charts are linked by reference, so a change to a chart updates every dashboard that uses it (you are warned when this happens).
  - **PSRIO scripts**: edit them in an embedded editor and run them, including scripts that write CSV output. You can also see the PSRIO script behind any chart.
  - **Publishing**: export charts and dashboards to standalone HTML files.
  - Charts are regenerated automatically after a successful run.
- When a case is converted, its saved graph configurations become charts in the Results tab.

### Energy map and single-line diagram
- **New Energy map** (now out of beta). It replaces the old network map (PowerView):
  - **Layers**: buses, circuits, AC interconnections, DC links, 2- and 3-winding transformers, series capacitors, converters, synchronous compensators and loads, on a choice of base maps (vector tiles, satellite, country background).
  - **Labels and search**: labels by name or attribute ("Name [code]" by default), search and go to element, zoom to an area, and the mouse latitude/longitude in the footer.
  - **Results on the map**: each output can be shown as a value label, as the size or colour of the symbol, or as an animated flow direction on lines. Colour scales can be fixed, by range or by category, with several palettes.
  - **Result panel and playback**: a result panel keeps the values of selected elements, and **Play** animates the results over stages. Scenarios and blocks can be selected or aggregated, and a global unit selection converts the values.
  - **Presets and settings**: loading presets for operation, NetPlan AC optimal power flow and OptNet results, and map settings saved per case.
  - **Edit mode**: drag buses to change their coordinates, and edit element properties directly on the map.
  - **Diagram mode**: an automatic layout, opened directly when the buses have no coordinates.
- **Single-line diagram**: opened from the map for a selected bus ("Open single line diagram", "Draw neighbors"). It shows buses, lines, transformers, generators by type, loads, shunts, series capacitors, converters and interconnections, with the map's result values and flow arrows. Candidate circuits are drawn with a distinct line style.

### Data entry
- **Excel import and export rebuilt, with relationships.** You can export data to Excel, edit it and re-import it without losing links between elements. This covers registry, modification, interval, seasonal, chronological (hourly, daily, yearly), interpolation and element-dimension tables, as well as children and related elements.
  - Import is validated, with clear messages in English, Spanish and Portuguese: invalid keys and references, missing tabs or columns, duplicated or missing years, stages, days or hours, invalid dates, and the code format.
  - Rows whose numeric cells cannot be read are rejected and reported, instead of being imported as empty values.
- **Excel-like editing in grids**: a fill handle (including series), Ctrl+D, Ctrl+R, Ctrl+Enter, Delete, undo/redo, and cell-by-cell paste.
- **Define horizon**: replaces "Add chronological data". You set the initial and final year of a chronological table and choose **Update** to grow or shrink it, or **Remove all**.
- **Restricted maintenance dates** are now entered on a calendar for each plant: drag to paint, Shift+click to select a range, or click a header to fill a whole year or column.
- **Time-series screens**: link CSV time-series files to elements, see which elements use a series, and remove series (optionally deleting their files) when you save.
- **CSV Editor and TMS Preview**: companion applications to create, edit, chart and preview time-series CSV files, with resolutions from 5 minutes to 6 hours.
- **New validations**: duplicate dates in modification tables, inline checks of from/to dates, tables whose rows must add up to a given value, and tables that must be complete when a flag is set.
- A redesigned stage settings dialog, and a hill-curve table with a heat map for NCP hydro generators.
- Smaller additions: copy an attribute's value to the clipboard, the plant's fuel shown in the emission-coefficient screen, a window to remove scenarios, and units in time-series headers and chart axes.

### Data manager (version control)
- The "Version control" tab is now the **Data manager**. It replaces the practice of copying case folders for every change, which leads to redundant copies, wasted storage and no single source of truth. Besides local Git versioning, it can store case versions in **PSR Cloud**, so a team shares one organized history of the case. Access is controlled by your PSR account, and every version records who changed what and when:
  - publish a case, register versions, create and switch branches, pull, restore a version and discard local changes;
  - see whether the cloud workspace has unsaved changes, and the current repository and branch in the status bar.
- **Comparing versions**: Ctrl+Click two versions in the history to compare them. The comparison shows a chart of the differences in a series, and enum values are translated.
- The **case comparator** can compare two case folders directly. It can load only the files that differ, and it covers OptGen, NCP and OptMain data as well as SDDP.
- Comparisons are much faster, and they only run when you open the Data manager tab. Before, opening a case with tens of thousands of elements could freeze the GUI for several minutes.

### Add-ins in the GUI
- Add-ins can add buttons to the **Tools** and **Run** tabs, entries to the **New case / Import / Export** menus, and commands to the command palette.
- Add-ins can also run inside the GUI with their own tool windows, with the permissions they declare.
- **Factory Workbench** is the first add-in of this kind: a **macro recorder** that turns your edits in the GUI into a PSR Factory script.

### Support
- **Screen recorder and support package**: record the SDDP window, another window, a region or the whole screen, optionally with narration from the microphone. The recording can then be packaged with a description of the problem, the logs of SDDP and the tools you ran and, optionally, the case input data, ready to send to PSR support.
- Crashes during start-up are now recorded in a log file, which helps PSR support find the cause.

### Performance
- Screens open faster (for example, the hydro plant screen opens in about 1.35 s instead of 2.5 s).
- Selecting an element with very many modifications is much faster (in one case, 358,000 renewable modifications went from 12–15 s to 0.2 s).
- GUI memory leaks when closing or reloading a case were fixed.
- The Energy map no longer reloads when only the displayed output changes.

### Removed
- The legacy **Graph** tab and graph module (replaced by the Results tab).
- The old **PowerView** network map (replaced by the Energy map).
- The "publish to S3" option of the case comparator.

### New tools
- **bin3csv**: a command-line converter between CSV, HDR/BIN and single-file binary result formats. It can also compare result files within a tolerance and pack or unpack HDR/BIN pairs. It accepts the same syntax as bin2csv.

---

## Operation Planning Module (SDDP)

### Batteries
- **Stored-energy loss (self-discharge)**: a battery can lose a fraction of its useful energy (current storage minus minimum storage) every hour, even when it is idle. It is set per battery as a loss factor in p.u. per hour. The factor can change over time through battery modifications. It is available in every chronological resolution, including the hourly representation and OptGen 2.
- **Battery cycle counting**: battery degradation depends on how intensively the battery is used, so SDDP now counts **equivalent full cycles** in each stage: charged plus discharged energy, divided by twice the useful storage capacity. Partial cycles count in proportion to their depth, so several shallow cycles add up to fewer full ones. This linear approximation keeps the optimization efficient. It is turned on per battery.
- **Battery cycle limits**: the number of cycles is a new term of generic constraints: for example, to limit cycles within a weekly or monthly stage, or over a year or any other period with multi-stage generic constraints. Constraints that use it must have stage resolution.
- **New outputs**: battery cycles per stage, battery charge (energy drawn from the grid, including charging losses) and battery discharge (energy delivered to the grid after discharging losses).
- In chronological resolutions, a battery's reserve offer is now limited by its stored energy: up-reserve by the energy above minimum storage, and down-reserve by the free storage.

### Reserves
- **Reserve direction: up, down or both**. Secondary (joint) reserve requirements have a new direction: up (the default, same as 18.0), down or both. This was already possible in the hourly model and is now available in the block model too.
  - Hydro (with and without unit commitment), thermal (including multi-fuel) and battery plants can provide down-reserve.
  - Renewable and CSP plants cannot take part in requirements that include down-reserve.
  - All requirements in a reserve-sharing group must have the same direction, and reserve sharing cannot be combined with requirements in both directions.
- **Reserve limited by ramp rates** in chronological block and typical-day runs, as in the hourly model: up-reserve by the ramp-up rate, and down-reserve by the ramp-down rate.
- **Reserve sharing through circuits**: lines and transformers can have a maximum secondary reserve that can be shared through them, and a price for it.
- In the hourly representation, shared and non-shared (exclusive and non-exclusive) reserve requirements were reformulated, and reserve constraints on AC circuits, interconnections and DC links were adjusted.

### Inertia (new)
As renewables displace synchronous generators, systems have less inertia and frequency deviations after a disturbance develop faster. SDDP now co-optimizes energy, reserves and inertia, so the dispatch is both cost-effective and frequency-aware.
- **Inertia requirements**: a new element defines a minimum system inertia (MW·s) per block or per hour, with a violation penalty. Hydro and thermal plants have an **inertia constant** and can be assigned as providers. For each requirement, the sum of the providers' inertia constants, weighted by their commitment decisions, must be at least the required value. Providers are added to the unit commitment representation automatically.
- New outputs: inertia violation, its cost and marginal cost, and the inertia provided by hydro and thermal plants. Inertia violations also appear in the SDDP dashboard.

### Large loads and data centers (new)
- Flexible demands can be marked as **data centers**. A data center can shift load between blocks or hours within limits around its reference profile. Instead of a deficit, its curtailment is unlimited and penalized at its willingness to pay. Its existence status and deployment level can change over time.
- New outputs: supplied load, curtailment, and the maximum, minimum and reference load of large loads. The hourly model reports a "Revenue: Large load" objective term.
- Data centers can also be expansion candidates in OptGen.

### Fuels and fuel contracts
- **Minimum offtake rate per stage** for fuel contracts (chronological data), with a penalized violation. New outputs for the violation and its cost, also shown in the dashboard.
- **Hourly availability of fuel contracts** limits the total offtake from a contract in each hour. It requires the hour-block mapping.
- **Hourly fuel price scenarios**: they are averaged into block prices, or used hour by hour in the hourly representation.
- The take-or-pay cost of fuel contracts can now change over time, and is defined per year.
- Duplicate fuel names are now allowed (codes must still be unique within a system).

### Energy supply chain
- New execution option **"Use energy supply chain modelling"** (on by default). Turn it off to ignore the energy supply chain data in the case.
- New generic-constraint terms: supply-chain transport flow and supply-chain final storage.
- **Hourly demand scenarios** for supply-chain demands.
- Thermal plants have a **balance coefficient** in the supply-chain node balance.
- The energy supply chain replaces the legacy gas network, which was removed (cases are converted automatically).

### Hydro and inflows
- **Inflow model estimated from an hourly inflow history**: ESTIMA can read the history in hourly resolution and aggregate it to stage values. Each station can use its own resolution. ESTIMA also accepts the case path as a command-line argument.
- **Modifications in additional years**: new execution option (off by default). When it is on, configuration modifications and dead-storage fill-ups dated in the additional years are applied (before, they stopped at the end of the study horizon).
- Water travel times can be fractions of an hour (for example 0.5 h), so they can be represented exactly in 15- or 30-minute runs.
- The outflow × tailwater table is no longer limited to 5 points.
- New hourly output: tailwater elevation.
- Inflows are no longer generated for gauging stations that are not linked to any hydro plant. In cases with such stations, the synthetic inflows of the other stations may differ from 18.0.

### Network
- New option for the representation of the 2nd Kirchhoff law: it can be represented for every circuit except those tied to an expansion project. It is not allowed with the complete network model.
- **New outputs by device type**: flow, capacity, available capacity, marginal cost, losses, flow under contingency and loading for AC interconnections, DC lines, LCC converters and VSC converters. Also new: loading of AC lines, transformers, series capacitors and 3-winding transformers, and the phase-shifter angle of 2- and 3-winding transformers. The generic circuit flow, circuit loading, DC link flow and DC link loading outputs are no longer offered in the output selection.
- The DC link transmission cost output was renamed to **AC interconnection transmission cost**.
- New execution option **"Generate outputs for NetPlan/OptNet"** (off by default) produces the outputs that a later NetPlan AC optimal power flow or OptNet run needs.
- Network calculations are now always done by PSRNetwork, so the option to choose them was removed. Features that the complete network model does not support are rejected with a clear message.
- In the hourly representation, transformer, capacitor and AC line flow outputs are now also produced when losses are not modelled (before, they required modelling losses).

### Generic constraints
- Interpolation constraints can be **disabled** individually. Older files without this field still load.
- New terms: battery cycles, and supply-chain transport flow and final storage.

### Penalty-free SDDP with feasibility cuts (beta)
Real-world cases have constraints that are hard to meet. They are usually handled with slack variables penalized in the objective function, but the penalty values are hard to calibrate: they mix artificial costs with real operating costs and can distort prices. The penalty-free approach first seeks a feasible operation and then reports the constraints that are truly infeasible.
- SDDP co-optimizes the **future cost function** (optimality cuts) and a **future feasibility function** (feasibility cuts, which approximate the region where the future operation is feasible). Constraints that are truly infeasible are detected automatically.
- In a test with a deterministic case of the Brazilian hydrothermal system, the penalty-free approach matched the benchmark violations almost exactly. The methodology is described in [arXiv:2512.03739](https://arxiv.org/abs/2512.03739).
- Feasibility cuts are turned on with an execution option. In 19.0:
  - they are also computed and added in the **forward** phase (new option, on by default);
  - a new option (off by default) uses feasibility constraints instead of fixing the bounds of slack variables;
  - the convergence criterion takes feasibility cuts into account, cuts can be relaxed, and the discount rate is applied to the future feasibility function;
  - the feasibility-cut file is read once per stage and new cuts are appended, instead of rewriting the file;
  - when feasibility cuts are on, the option for the future feasibility function of the final simulation is ignored.
- This feature is in **beta**: work on its performance continues, because cases can generate a large number of feasibility cuts.

Cut dominance filtering no longer normalizes cuts.

### Simulation and integration with OptGen
- **Scenario probabilities in runs chained with OptGen**: they are now read only when the new execution option **"Consider scenario probability data"** is on. In 18.0 they were read automatically.

### Outputs and dashboard
- **SDDP dashboard**:
  - new violation categories: inertia, and fuel-contract minimum offtake per stage;
  - a table describing the execution nodes and processes;
  - "Lower bound", "Upper bound" and "Tolerance" labels in the convergence chart, in each interface language;
  - "k$" in the final cost table;
  - faster generation of the generation report.
- Post-processed outputs no longer include the additional (buffer) years, unless additional years are selected for the final simulation.
- The infeasibility report shows each constraint's short code next to its description (for example "HGuideC: Hydro plant - Guide curve").
- A new **electrical losses analysis** report shows losses in total and per bus, for AC circuits, DC lines, transformers and series capacitors.
- The **DPR** dashboard uses the current dashboard layout.

### Performance and security
- **Redesigned cut management engine**: in the policy phase, the time per iteration grows with the number of stages, scenarios and state variables, and with the cuts accumulated in the future cost function, so performance degrades as iterations go on. The engine that stores and manages cuts was fully redesigned to make building the future cost function faster and more scalable. This makes it practical to run more scenarios and iterations, which improves policy quality. In a preliminary benchmark on a Brazilian case (165 hydro plants, 116 stages, about 1,080 state variables, 2,000 forward scenarios, 12 iterations), the total policy time fell by about 40%.
  > ⚠️ **Pending confirmation:** this engine is still being finalized in a separate development branch and is not yet part of the 19.0 release branch. The 40% figure is a preliminary result.
- Lower memory use: output buffers are sized to the case instead of a fixed maximum.
- The system calls that copy, rename and delete files and launch runs were hardened against command injection. Paths with spaces in the MPI configuration now work.

---

## Expansion Planning Module (OptGen)

### OptGen 1
- **Capacity degradation of batteries and solar PV**: equipment such as batteries and solar panels deliver less as they age. For an existing plant this can be entered as yearly modifications, but for a project the entrance date is itself an OptGen decision, so its degradation must follow the date that OptGen chooses. A project can now have an "Operation factor" table (degradation factor in p.u. by year of operation), edited in a dedicated screen, and its available capacity follows that factor from its entrance date onwards. This avoids biasing investment decisions in favour of these technologies. It cannot be combined with an entrance unit schedule for the same project. This is also available in OptGen 2.
- **Automatic precedence constraints for transmission expansion**: when the network is represented, candidate circuits that link the same two buses and have the same impedance are grouped automatically, and precedence constraints are created among them. This avoids exploring equivalent solutions and reduces solution time. Nothing needs to be set. This is also available in OptGen 2.
- **Convergence improvements for cases with a detailed network**: two changes to the OptGen–SDDP Benders decomposition target the hardest integrated generation and transmission studies, where they can make the difference between converging and not converging.
  - **Sensitivity cuts from a relaxed network** (new option "Generate sensitivity cuts from relaxed network model"): at each iteration, OptGen also runs an SDDP simulation in which the 2nd Kirchhoff law of candidate circuits is relaxed. The relaxed cuts guide the investment problem early on, and the exact cuts tighten the bound.
  - **Regularization strategy** (with a regularization weight and a starting iteration): keeps successive expansion plans close to the best plan found so far, which stabilizes the investment problem. Unlike a user-defined expansion plan, this reference plan is only a guide and is not mandatory. Available in a new "Regularization strategy" group of the OptGen configuration.
- **Warm start from a given plan**: the plan is used as the initial solution and checked for feasibility in a first run.
- **Data center expansion**: data centers (see [SDDP](#large-loads-and-data-centers-new)) can be expansion candidates, with a new "Data Center" project type in reports and the dashboard.
- **Xpress 9.9** for the investment module (was 8.13). The maximum MIP time can be set to unlimited.
- Benders cut coefficients smaller than 1e-8 are set to zero, which avoids numerical difficulties in the MIP.

### OptGen 2
- **Battery stored-energy loss**: the battery loss factor is also taken into account, with a new battery leakage output.
- **Data center agents and projects**, with investment and O&M costs and a willingness-to-pay revenue.
- The capacity degradation factor and automatic precedence constraints are available (see OptGen 1).
- **Automatic firm capacity of renewables (PFCA)**: the firm capacity of each renewable candidate is computed automatically, year by year. OptGen 2 identifies the most critical hours of the year (the hours with the highest net demand, that is, demand minus renewable generation) and averages each candidate's available generation over those hours. The firm capacity therefore adapts to the system and to the renewable mix being built. For example, as more solar is built, the critical hours move into the evening and the firm capacity of new solar plants falls. Previously in beta, the option is now available in the OptGen configuration screen, together with the number of critical hours (100 by default).
- **Ward network reduction**: in studies with a detailed network, the network is split into an internal area (the buses of the monitored circuits), its boundary, and the external area. The external area is replaced by an equivalent network with the same electrical behaviour at the boundary, but far fewer buses and circuits. This makes integrated generation and transmission studies with realistic topologies tractable in OptGen 2. Methodology: Castro et al., "Ward reduction in unit-commitment problems", *Electric Power Systems Research*, 2024.
- The take-or-pay cost of fuel contracts can vary over time.
- **New C++ engine (preview)**: SDDP 19.0 also includes a new C++ implementation of OptGen 2. The Julia engine is still the one used by default. The C++ engine does not yet support every OptGen 2 feature, and it is the only engine that supports **resilience (stress) days** (new "Resilience days" option and screen). Resilience days model the hourly operation of selected critical days (peak net demand, lowest renewable generation and similar) alongside the base case. With the default Julia engine, the resilience-days option has no effect.

### OptGen 2 operational results in the Results tab
- The operational module of OptGen 2 writes a family of results (dispatch, reserves, battery use and more), which help explain why the model chooses one technology over another. Until now, reading them required custom scripts. A dedicated module of the [Results tab](#results-tab-charts-and-dashboards) loads these files, so you can chart and browse them interactively, in the same way as SDDP results.
  > ⚠️ **Pending confirmation:** this module was announced at the PSR User Meeting 2026, but we could not yet confirm it in the 19.0 code.

### New expansion planning dashboard
- A new expansion planning dashboard replaces the previous one. It has the following tabs:
  - Summary;
  - Expansion plan, with project details and events;
  - Capacity: added, cumulative, retired, installed, network and interconnection expansion;
  - Costs: NPV, CAPEX, fixed O&M, largest investments, levelized cost by project, and reduced costs of candidates that were not selected;
  - Firm capacity and energy, broken down by technology, including batteries;
  - Economics;
  - Constraints;
  - OptGen 2 reports;
  - Risk frontier;
  - Convergence.
- You can filter by system and technology, switch chart types, rearrange and resize panels, zoom, export to Excel and save charts as images. It is available in English, Spanish and Portuguese.
- The dashboard needs **internet access** to load its chart and Excel libraries.
- The PSRIO log is now kept in the case folder.

### Changed behaviour and defaults
- **Additional years in Benders cuts are now considered by default.** A new option excludes them, replacing the previous option that included them. Another new option also lets OptGen build projects in the additional years. This changes the results of cases with additional years compared with 18.0.
- **Hydro inflow scenarios have a new format**: one file per scenario plus a probability table are replaced by a single binary file with all scenarios and a scenario-weight table, enabled by the new option **"Use scenarios data"**. Converted cases get this option turned on automatically. A new **Hydro inflow scenarios** window (under expansion "Scenarios data") generates them: number of scenarios, include the long-term average scenario, initial year and probability per scenario, and set negative incremental inflows to zero.
- For hydro plants with firm energy or firm capacity given in p.u., the value is now multiplied by the **installed capacity**. Before, it was multiplied by the smaller of the installed capacity and the maximum turbining times the production factor.
- A project whose plant belongs to a generator group is now rejected with an error.
- Legacy gas projects must be energy supply chain projects (the case conversion handles this).
- OptGen 1 reads the new 19.0 database and no longer cuts names to 12 characters in reports and logs.

---

## Short-term model (NCP)

- **NCP 7.0 (beta) is now part of the SDDP platform.** NCP is PSR's short-term hydrothermal unit commitment and dispatch model, used for more than 20 years in dispatch centers, utilities and system operators worldwide. It was previously distributed separately. In 19.0 it uses the same database and GUI as SDDP and is installed with SDDP on Windows and Linux.
- **One platform, two horizons**: the generators, network, contracts and costs are defined once. SDDP computes the stochastic policy and water values for the medium and long term, and NCP turns them into short-term decisions through the SDDP future cost function. Typical uses are day-ahead scheduling, redispatch after forecast deviations or outages, and refining the SDDP operation at a finer time step.
- **Time step from 60 minutes down to 1 minute** (1-minute steps are new). The resolution is a setting, not a change to the model: hourly for week-ahead and day-ahead planning, 15 minutes for intraday operation, 5 minutes or less for real-time redispatch and reserve activation. Input data can be given at any resolution, see [Time-series database](#time-series-database).
- **Same study, new NCP tab**: short-term data is entered in the same case, in an NCP data tab with its own screens. These cover configuration, system, demand, thermal, hydro (including hydro units, hill curves and the power grid), hydrology, renewables, batteries, power injections, fuels, reserves, generic constraints, electrification, interconnections, buses and the electric network.
- **Running NCP**: select NCP as the active model on the Run tab, then use **Check data** and **Run NCP**. After the run, the NCP dashboard and the execution report open in the GUI.
- **Main options**: dates, stage duration and number of stages (sub-hourly steps are supported), MIP tolerance and maximum time, parallel processing, reading an SDDP future cost function to value water at the end of the horizon, deficit options, network losses, and individual switches for ramps, minimum up/down times, start-up limits and forbidden zones.
- **Modelling**: the shorter horizon allows a more detailed representation of each element:
  - **Hydro**:
    - unit-level generation as a function of net head and turbined flow, including hill curves;
    - hydraulic losses in units and penstocks, and in-line, parallel or cascaded unit arrangements;
    - synchronous condenser mode, which provides reactive power and inertia without active generation;
    - terminal functions (target generation, storage or turbined outflow) or the SDDP future cost function;
    - precedence between units, and average flow, storage and generation limits;
    - forbidden zones (cavitation, vibration) and generation limits that depend on the reservoir level;
    - spillway rating curves and water in transit.
  - **Thermal**:
    - non-linear fuel consumption, given as a table or a polynomial;
    - combined cycles at unit and configuration level, with coupling time and coupling cost;
    - cogeneration (steam supplied to non-electric demands);
    - start-up costs and minimum times that depend on the thermal state (hot, warm, cold);
    - synchronous condenser mode and forbidden zones;
    - alternative fuels.
  - **Renewables and storage**:
    - hybrid plants (solar, wind and storage dispatched as one asset with a shared connection);
    - battery arbitrage between energy and reserves within the hour;
    - renewable curtailment precedence;
    - round-trip losses and target storage;
    - price-quantity energy and reserve bids.
  - **Reserves**:
    - nested primary, secondary and tertiary reserves with explicit response times;
    - inertia as an instantaneous service;
    - reserve as a percentage of the current generation;
    - asymmetric up/down reserves and units that provide only one direction;
    - reserve offers per requirement;
    - joint, exclusive and non-spinning reserves.
  - **Also inherited from SDDP**: interchanges between systems, fuel contracts and fuel reservoirs, energy supply chains, CSP plants, reserve sharing, flexible demand and water desalination.
- **Legacy NCP cases are converted** to the integrated SDDP 19.0 format when opened. Their chronological data goes to the case's time-series database, and the old NCP files are removed (after a backup).
- NCP requires its own **"NCP 7.0" license** feature. An SDDP license alone is not enough.

---

## Transmission network: OptNet, NetPlan and Network Report

The transmission planning tools of the standalone NetPlan environment now run inside the SDDP platform. In 18.0, NetPlan was used next to SDDP, and the shared data had to be converted and kept up to date in both. Since SDDP 18.0, the full network data (AC/DC buses, circuits, transformers, FACTS, reactive devices, monitoring and contingencies) is part of the SDDP database. In 19.0, the Energy map and the optimization models are added, so a single database serves every application, with no duplication or conversion:
- active-power (DC) transmission expansion: **OptNet**, together with OptGen;
- AC power flow analysis: the **NetPlan** suite, which starts with the AC optimal power flow (formerly OptFlow).

### NetPlan – AC optimal power flow (formerly OptFlow; new, add-in)
- The steady-state AC optimal power flow can now be configured and run from the SDDP interface. It takes the SDDP case and dispatch scenarios and solves an AC OPF for each selected stage, scenario and block, hour or typical day.
- It represents reactive power, voltages, transformer taps, FACTS and DC link controls, which are not represented by the linear (DC) power flow used in SDDP and OptGen. It assesses voltage limits and reactive-power adequacy, finds reactive-power deficiencies, and recommends shunt support and control adjustments per dispatch scenario. N-1 contingencies can be considered.
- Typical workflow: compute the generation and transmission expansion plan with OptGen and SDDP, generate the dispatch scenarios with SDDP, then use the AC OPF to check whether reactive support is needed to keep voltages within their limits.
- It is installed as the **optflow add-in** from the Add-in Manager and run from **Run > NetPlan > AC optimal power flow**.
- A new options group has four screens:
  - **Horizon**: stages, scenarios, blocks, hours or typical days, and systems.
  - **Objective function**: minimize reactive injection, deviation from the SDDP active dispatch, active losses and load shedding, plus convergence parameters.
  - **Controls**: converters, series capacitors, phase shifters, transformer taps, generator P and Q, synchronous condensers, SVCs and shunts, plus the initial OptGen plan, flow limits and constraints.
  - **Contingencies and monitoring**: no contingencies, selected contingencies or N-1, normal or emergency limits, and monitored buses and circuits.
- The Run tab has **Check** and **Run** (in parallel with MPI) commands, plus the execution, summary and validation reports.
- The **NetPlan – AC OPF dashboard** covers solution quality (convergence, mismatches, execution times, costs) and results: reactive injection, generation by technology, load shedding, deviations from the SDDP dispatch, and a voltage profile with a heatmap, critical buses and voltage safety margins.
- In SDDP, turn on "Generate outputs for NetPlan/OptNet" to produce the outputs the AC OPF needs. Its results can also be displayed on the Energy map.

### OptNet: transmission expansion (new, add-in)
- OptNet, part of the OptGen family of expansion tools, finds the lowest-cost set of transmission reinforcements that keeps the network operating under the dispatch scenarios produced by SDDP (per block, per typical day or hourly).
  - It uses a linearized (DC) power flow and combines a heuristic with a Benders decomposition, so that the plan is found with practical computing times.
  - Candidates can be any branch between two buses: AC lines, transformers, series capacitors, flow controllers and DC links.
  - N-1 contingencies can be considered.
- **Typical uses**:
  - a hierarchical approach: expand generation with OptGen, run SDDP without network constraints to get dispatch scenarios, then use OptNet to remove overloads and load shedding;
  - pruning the candidate circuit list before an integrated generation and transmission expansion with OptGen;
  - complementing an OptGen transmission plan to remove residual overloads or load shedding.
- OptNet uses the same input data as SDDP and OptGen, with its own section in the configuration screen. It is installed as the **OptNet add-in** and run from **Run > Run OptNet**.
- **Licensing**: OptNet is repositioned as part of the OptGen family, and every user with an OptGen license will have access to it.
  > ⚠️ **Pending confirmation:** this was announced at the PSR User Meeting 2026. The licensing terms still need to be confirmed.
- Results: the execution report, the expansion plan, binary outputs in the usual SDDP format, and the OptNet dashboard (investment decisions, capacity and cost, circuit loading, an N-1 redundancy check, and deviations).

### PSR Network Report (now an add-in)
- PSRNetworkReport (the post-contingency and power-flow analysis tool) is now installed as the **psrnetwork-report add-in** and is no longer part of the SDDP installation. Since 18.0 it gained a power-flow analysis dashboard, an option to analyse only selected circuits, and better identification of circuits that share the same code.

---

## Reliability Module (Coral)

- Coral reads the SDDP 19.0 database, including long names and codes and unique identifiers.
- **Load sensitivities** defined in the new sensitivity groups of the 19.0 GUI are applied in Coral runs.
- Coral **output selection** is now available in the GUI, and Coral results can be browsed like the results of other models.
- **Licensing**: Coral now uses the same license library as SDDP and OptGen, so your existing SDDP license still covers it.
  - Without a valid license, Coral runs cases within the former trial limits instead of stopping with an error. Above those limits it lists each dimension that exceeds them.
  - With a valid license, the Coral report shows the licensed user.
- Coral uses Xpress 9.1.
- The Coral report shows a version hash, which helps PSR support.

---

## Maintenance Planning Module (OptMain)

- OptMain 3.0.1 reads the SDDP 19.0 database. The maintenance scheduling workflow is unchanged.

---

## Results post-processing (PSRIO 5.0)

SDDP 19.0 ships **PSRIO 5.0** (18.0.x shipped 4.0.x).

### New features and improvements
- **PSRIO runs inside the GUI**: PSRIO is now also a library that the GUI loads directly, so dashboards and charts are produced without starting a separate process.
- **New script functions**:
  - `select_stages_by_year_period`;
  - `aggregate_blocks` and `aggregate_scenarios` restricted to selected blocks or scenarios;
  - `filter_blocks`, which keeps the time dimension and leaves gaps for blocks that are not selected;
  - `select_scenarios_by_simulation_index`;
  - `select_agents` with a name separator, to group agents by a prefix of their name;
  - aggregation of weekly stages into months, quarters and other profiles.
- **New aggregators**: `BY_EXCLUDING`, `BY_MAX_EXCLUDING`, `BY_MIN_EXCLUDING`, and `*_EXCLUDING_KEEP_NAN` variants that return NaN instead of 0 when every value is excluded.
- **New collections**: `Shunt`, `StaticVarCompensator`, `SynchronousCompensator`, LCC and VSC converters, and the `generator_group_count` attribute.
- **Output settings**: `set_global_digits` sets the number of decimals for every chart and table, and `set_save_as_csv` switches output to CSV from within a script.
- **Time resolution**: sub-hourly results, a semester profile, and a new command-line option that reads block durations from the model results, so the case's block definition is not needed.
- **Charts**:
  - a Y-axis range control;
  - horizontal legends with automatic pagination;
  - per-block error bars;
  - units in data table columns;
  - gaps shown for missing values;
  - stable series colours during playback;
  - faster rendering of large dashboards (charts are drawn only when they become visible).
- **Performance**: faster scenario operations, and a new command-line option that speeds up reading large outputs.

### Changed behaviour
- **Unit-aware default aggregation**: when `aggregate_blocks()` or `aggregate_stages()` is called without an aggregation function, the function now depends on the unit: average for rates, sum for energies. Scripts that relied on the previous fixed default may give different numbers.
- Several command-line options were removed: the old dashboard template, the number of threads (parallel operations always use all available hardware cores), the debug log, multiple S3 loading, and the list of outputs not found.
- Direct reading from and writing to Amazon S3 was removed.

---

## Documentation: the new Knowledge Hub

The [PSR Knowledge Hub](https://docs.psr-inc.com/knowledge/index.html) has been restructured. It is available online, separately from the SDDP installer:
- **Organized by product**: documentation is grouped by product (SDDP, OptGen, NCP, Time Series Lab and others) rather than by manual type (user manual, methodology manual, input file manual). It has about 600 articles across more than 10 products.
- **The same learning path for every product**: Get started, Interface guide, How-to articles (for example, how to model a hybrid plant in SDDP), Methodology, and Sample cases.
- **Better search**: it tolerates typos, can be filtered by product, topic and article type, and shows results as you type.
- **Short video tutorials**: task-focused videos of up to 5 minutes, published progressively.
- Articles follow a common editorial standard, and the hub can be read on computers, tablets and phones.
- **Coming next**: an AI chatbot that answers product questions in natural language, a video library for every product, and sign-in with company credentials (SSO).

> ⚠️ **Pending confirmation:** video publishing and the "coming next" items follow the plan announced at the PSR User Meeting 2026.

---

## Coming in future releases

> ⚠️ **Not part of SDDP 19.0.** The following developments were announced at the PSR User Meeting 2026 for upcoming releases. Their scope and dates may change.

- **NetPlan suite**:
  - **Reactive power expansion planning** (formerly OptVAr): optimizes the reactive support investments (capacitors and reactors) needed over the planning horizon.
  - **SDDP to PSS/E and Anarede**: export of transmission data and AC optimal power flow set points to other database formats.
- **NCP**:
  - **Time Series Lab integration**: stochastic renewable and inflow scenarios from TSL fed directly to NCP.
  - **Probabilistic dynamic reserve**: reserves sized from forecast distributions instead of fixed margins.
  - **Maintenance optimizer**: maintenance schedules co-optimized with the short-term dispatch.
  - **AC optimal power flow** inside the dispatch, for voltage, reactive support and losses.
  - **Stochastic dispatch**: short-term decisions that hedge against renewable and demand uncertainty.
  - **N-1 contingencies**: security analysis at every dispatch interval.

---

## Removed and discontinued features

| Model / module | Feature (18.0.x) | Status in 19.0 | Replacement / action |
|---|---|---|---|
| SDDP (including the hourly representation) and OptGen | Gas network (gas nodes, pipelines, gas outputs, OptGen gas cuts and gas projects) | Removed | Energy Supply Chain. Converted automatically. |
| SDDP (including the hourly representation) | Legacy CO2 emission factor per fuel, system carbon cost and their CO2 cost and emission outputs | Removed | Emission elements. Converted automatically. |
| SDDP (including the hourly representation) | POCP target storage ("Nível Meta") and its outputs | Removed | — |
| SDDP | 13-month policy grouping | Removed | — |
| SDDP | Quarterly stages | Removed | Monthly or weekly stages. |
| SDDP (ESTIMA) | Principal-components inflow model and non-parametric inflow model | Removed | Standard inflow model in ESTIMA. |
| SDDP | FCF cycles option | Removed | — |
| SDDP | Network calculations without PSRNetwork | Removed | PSRNetwork is always used. |
| SDDP | DC link transmission cost output | Renamed | AC interconnection transmission cost. |
| SDDP | Generic circuit and DC link flow and loading outputs in the output selection | No longer offered | New outputs by device type. |
| SDDP | Convergence screen (SDDPScr) and its command-line option | Removed | Progress shown in the execution window. |
| SDDP | Multi-disk architecture option | Removed | — |
| SDDP and PSRIO | Direct output to Amazon S3, and the PSRIO S3 options | Removed | — |
| OptGen 1 | Option to include additional years in Benders cuts | Replaced | Considered by default; a new option excludes them. |
| OptGen | Inflow scenarios with one file per scenario | Replaced | Single scenario file plus a scenario-weight table. Converted automatically. |
| PSRIO | Old dashboard template and number-of-threads options | Removed | — |
| Graphical interface | Legacy Graph tab / graph module | Removed | Results tab. Saved graphs are converted. |
| Graphical interface | PowerView network map | Removed | Energy map and single-line diagram. |
| Database (all models) | Old file formats (results before the single-binary format, the initial chronological sensitivity format, and legacy fixed-width files) | No longer read | Convert the case through the GUI. |
| Licensing (all models) | Hardware-key (dongle) license | Removed | PSR software license. |
| Installation (SDDP and OptGen) | MPICH2 on Windows | Removed | MS-MPI. |
| Installation | Windows 8.1 / Server 2012 R2 | Not supported | Windows 10 1607 / Server 2016 or newer. |
| Installation | PSRNetworkReport and PSRClustering in the installation | Moved | psrnetwork-report and psrclustering add-ins. |

---

## Fixed issues

These issues existed in SDDP 18.0.x and are fixed in 19.0.

### Database and graphical interface
- Fixed names containing commas, which could corrupt CSV files on the next save and make a case reload silently with missing data.
- Fixed a value too wide for a fixed column overflowing into the next column when saving.
- Fixed malformed case or result files crashing the GUI or the model. They are now rejected with a message.

### Operation Planning Module (SDDP)
- Losses are ranked by absolute value when circuits are selected for loss representation.
- Fixed the battery storage percentage output.
- In dashboard charts, labels and tooltips now show the original scenario and block numbers after a selection, instead of their position in the selection.

### Expansion Planning Module (OptGen)
- OptGen 1:
  - Fixed the accumulation of previous-decision capacity for projects with a fixed date before the study horizon.
  - Fixed the index of projects ignored because of precedence constraints.
  - Fixed a memory error when reading exclusivity constraints.
  - Fixed the "Existing" flag of flow controllers.
  - Fixed the minimum/maximum storage mapping and the storage modifications of batteries.
  - Removed warnings that were repeated at every iteration.
- OptGen 2: a missing battery charge or discharge efficiency is now taken as 1. Before, future batteries could produce invalid bounds.

### Reliability Module (Coral)
- Fixed generation being counted twice for plants that already have explicit generator units.
- Fixed non-hourly outputs being written twice in parallel runs.
