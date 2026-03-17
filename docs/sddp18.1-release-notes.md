---
title: "Release notes"
parent: "SDDP 18.1"
nav_order: 1
layout: default
---

# SDDP 18.1 – Advanced transmission modeling, now with AC OPF (OptFlow)

🌐 Please refer to the release site and check out the most important features developed on this release.  
📝 For the detailed changelog and download links, please visit the changelog page.

SDDP 18.1 brings **advanced transmission network assessment with AC optimal power flow (OptFlow)**, **more flexible database naming and coding** (with a modernized file structure), and a set of **GUI and performance refinements** that improve day-to-day workflows.

## 🚀 Highlights

- **OptFlow: AC OPF and voltage security assessment** now incorporated into the **SDDP platform**, expanding network analysis capabilities alongside operation and expansion planning workflows.
- **Longer names and codes in the database**, enabled by a new file structure that improves interoperability and maintainability.
- **Unique identifiers across database elements**, providing a consistent, user-editable identification scheme to support long-term database evolution.
- **Excel import/export feature rebuilt**: import/export redesigned to fully support **relationships**, enabling complete editing workflows through spreadsheets.
- **GUI & analytics upgrades**: new **PSRIO dashboard template** and additional visualization controls.
- **Modeling improvements**: new representations in SDDP (battery stored-energy loss, battery cycle counting, and reserve direction options), and OptGen enhancements (battery capacity degradation, transmission expansion enhancement, and energy efficiency integration).

## 🗼 OptFlow: advanced transmission modeling with AC OPF

OptFlow adds a **steady-state AC optimal power flow (OPF)** layer to the platform, enabling studies to complement linear network representations when assessing operational feasibility—especially for **voltage limits and reactive power adequacy**.

OptFlow is a **mature PSR tool**, already used in multiple studies and countries, and is part of the **NetPlan** suite. In SDDP 18.1, it is now incorporated into the SDDP platform to strengthen integrated studies where transmission performance is a key driver for feasibility, flexibility and cost-effectiveness.

### ⚡ Key capabilities

- **Detailed AC OPF and voltage security assessment**  
  OptFlow performs a steady-state AC OPF analysis to assess reactive power adequacy, verify voltage limit compliance, and capture voltage- and reactive-related operational constraints. It **complements the linear power flow representations already available in the platform for operation and expansion planning**, adding an additional layer of AC feasibility and voltage security assessment when required.

- **Identification of reactive power deficiencies and solutions**  
  The model detects reactive power shortages across different network configurations and dispatch scenarios, and provides locational recommendations for candidate shunt devices to mitigate voltage and reactive power support issues.

- **Integrated with SDDP and OptGen planning workflows**  
  Built into the SDDP environment, OptFlow uses the optimal active power dispatch obtained from SDDP as input, preserving it whenever possible while optionally minimizing active power losses and supporting OptGen expansion planning decisions.

## 📁 Database improvements and migration

### 🏷️ Longer names and codes

SDDP 18.1 expands database flexibility by allowing **longer names and codes** for all elements. This supports clearer models, better alignment with corporate naming conventions and fewer workarounds in large databases.

### 🗂️ Modernized file structure (CSV)

To enable this flexibility and improve interoperability with common tools, most database files are now represented using a **CSV-based structure**.

### 🆔 Unique identifiers

SDDP 18.1 introduces **unique identifiers** across database elements to support robust referencing and database evolution over time.

- When converting a database to SDDP 18.1, the platform automatically creates identifiers based on standard PSR rules.
- Identifiers are **user-editable**, allowing teams to adapt them to internal conventions when needed.

> ⚠️ **Important**: the updated data format is **not compatible** with earlier SDDP versions. It is strongly recommended to create and store a backup copy of your project files before using version 18.1 if you intend to maintain compatibility with previous releases.

## 🔷 Graphical interface and user experience

### 📊 Excel import/export with relationships (redesigned)

The Excel integration was rebuilt to address prior limitations and now supports complete round-trip workflows, including **relational structures**—allowing users to export, edit and re-import data without losing link consistency.

### 📈 PSRIO dashboards: new template and controls

SDDP 18.1 includes a redesigned PSRIO dashboard template and new visualization controls, enabling richer charts and additional options for exploring results.

### 🧩 Add-ins system

A new **add-ins system** was introduced to support more agile delivery and adoption of new model capabilities through the platform.

### ⚡ Performance and robustness

- **Lower memory consumption** through improvements in data handling and core components.
- **Faster loading** through targeted data-loading optimizations.

## ⚙️ Modeling improvements

## ⚡ Operation planning (SDDP)

### 🔋 Battery: stored-energy loss (self-discharge)

A new representation allows modeling **loss of stored energy over time** within a stage due to unintentional discharge.

- Available in all chronological time resolutions.
- A loss factor is applied to the battery’s useful storage (current storage minus minimum storage), producing energy loss regardless of active battery usage.

### ♻️ Battery: cycling (throughput) representation

SDDP now includes a decision variable that represents the **number of battery cycles within each stage**.

- This variable is exposed through **generic modeling**, so users can define flexible limits on cycling.
- Users may constrain cycles **within a week or month** and also over longer horizons (e.g., **annual limits**) using **multi-stage generic constraints**.

We are available and interested in hearing client feedback and practical experiences with battery cycling requirements and degradation modeling, to continue refining this representation. Please reach out to sddp@psr-inc.com with any insights or questions.

### 🛡️ Reserve direction: up, down, or both

Previously, the time block representation only supported reserve provision in the **upward** direction. SDDP 18.1 extends the block model to match the hourly capability, enabling **up**, **down**, or **both** reserve directions.

## 📈 Expansion planning (OptGen)

### 🔋 Battery: capacity degradation

OptGen now supports battery **capacity degradation** modeling for expansion studies, enabling more realistic valuation of storage projects over time.

### 🗺️ Transmission expansion performance: automatic precedences

Performance was improved for transmission expansion cases by introducing **automatic precedence constraints**, reducing overhead in large network build-out studies.

### 💡 Energy efficiency in firm energy/capacity generic constraints

Energy efficiency programs can now be included in **generic firm energy / firm capacity constraints**, improving the consistency of adequacy-style formulations that combine supply-side and demand-side resources.

## 🌤️ Time Series Lab 2.2 (TSL)

- **Bifacial PV panels modeling**  
  New support for representing bifacial PV behavior in renewable generation time series and scenarios.

- **Custom temperature data input**  
  Users can now include customized temperature datasets to enhance weather-driven time series generation and downstream studies.

- **Faster execution through data and results handling improvements**  
  Time Series Lab (TSL) now runs more efficiently thanks to internal optimizations in data processing and results management, reducing runtime in large workflows.
