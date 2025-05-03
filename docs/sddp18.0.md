---
title: "SDDP 18.0"
nav_order: 10
---

# SDDP 18.0 – Integrated Energy System Planning Platform

📅 Date: 2025-05-19 _(to be released)_<br>
🔗 Download:
[Windows](https://www.psr-inc.com/app/link/?t=d&f=sddp-18.0-setup.zip)
\|
[Linux](https://www.psr-inc.com/app/link/?t=d&f=sddp-18.0-setup-linux.zip)

Please visit the [release site](https://psr-energy.com/software/sddp-18.0.html) to explore the highlights of this release.

## 🚀 A unified experience across all planning horizons

This release marks a major milestone. **SDDP 18.0 introduces a unified platform** for operation and expansion planning, reliability analysis and maintenance scheduling — offering a seamless experience, from graphical interface to execution and results analysis.

## 🔷 Graphical interface

The new interface delivers a fully redesigned and unified environment for energy system planning. All modules — operation (SDDP), expansion (OptGen), reliability (CORAL) and maintenance — are now accessible from a single platform, offering a consistent, responsive, and user-friendly experience.

### 🌐 Unified layout and planning integration

- **Single platform** for configuration, execution, and analysis of all SDDP-based models.
- Fully integrated environment for operation and expansion planning, reliability analysis and maintenance scheduling.
- **No need for external tools or switching contexts** — everything is accessible in one place.

### 🗂️ Flexible data interaction

- **Bulk data edition**: tabular views support editing, grouping, and filtering of all input data.
- **Smart filters**: dynamic grouping by system, region, technology, or other dimensions.
- **Inline charting**: visualize key relationships (e.g., volume × production) directly within data grids.
- **Excel integration**: import/export supported for all input data and output results.
- **Mass-editable grids**: scrollable, filterable tables provide a full overview of modeling data.

### 🗺️ Georeferenced system visualization

- Interactive visualization of **hydraulic cascades**, **transmission networks**, and **energy supply chains**.
- Unified topology maps with integrated spatial and operational data.
- **Multiple visualization modes**, including:
  - Animated flows on circuits and cascades;
  - Scaled node representation (e.g., capacity, cost, stored energy);
  - Contour plots for marginal costs, generation, and energy balance.

### 📊 Built-in dashboards and result analysis

- **Interactive charting** through the graphical interface: point-and-click customization of dashboards by selecting variables, time horizons, scenarios, and filters.
- **Automated dashboards with PSRIO**: customized post-processing dashboards are generated automatically after each execution, supporting standardized and collaborative workflows.
- **Built-in dashboard**: each case includes a ready-to-use dashboard summarizing solution quality, convergence, cost and revenue breakdowns, constraint violations, results by region, marginal costs, execution times, and key information.
- **Comparative dashboards**: analyze multiple cases side-by-side, either with the built-in comparison view or fully customized dashboards via PSRIO.

### 📚 Help system and support

- New **integrated help platform**, the **PSR Knowledge Hub**, with direct access to:
  - Interface guide  
  - Methodological documentation  
  - Mathematical modeling references  
  - Troubleshooting articles

## ⚡ Energy system modeling

### 🔗 Energy supply chains

Detailed modeling of energy supply chains, enabling integrated planning of electricity, natural gas, hydrogen, biomass, Power-to-X, X-to-Y, and more.

- **Comprehensive supply chain modeling**: represent the full cycle of energy transformation, including production, transport, conversion, storage, and demand.
- **Multiple energy carriers**: define energy networks for fuels such as natural gas, hydrogen, methanol, biogas, electricity, and synthetic products.
- **System-wide integration**: energy supply chains are directly linked to the power system through converters, fuel-consuming units, and electrification modules.
- **Element types**:
  - **Producers** (e.g., gas wells, steam reformers, anaerobic digesters)
  - **Converters** (e.g., electrolyzers, methanol synthesis, biogas purifiers)
  - **Storage facilities** (e.g., hydrogen tanks, gas cylinders, long-term storage)
  - **Transport links** between nodes with capacity, cost, and losses
  - **Demands**, elastic or inelastic, at any node in the chain
- **Applications**:
  - **Natural gas**: from gas wells to thermal plants and households via pipelines and storage
  - **Hydrogen**: production from electrolysis or reforming; distribution and use in vehicles or industry
  - **Biomass**: conversion to biogas, biomethane, and electricity, with links to transport and heat sectors
  - **Power-to-X and X-to-Y**: enabling sector coupling between power, mobility, heat, and synthetic fuels

### 💡 Energy efficiency

Modeling of energy efficiency programs as investment decisions that reduce or reshape energy demand across the system.

- **Explicit representation of efficiency programs**: each program is linked to a specific demand class and represents an improvement that reduces energy consumption.
- **Flexible modeling structure**:
  - Allows modeling demand reductions across different time resolutions, reflecting seasonal or intraday efficiency impacts.
  - Supports varying levels of efficiency adoption over time, enabling the representation of progressive program deployment.
- **Endogenous investment decisions**: the level of deployment can be optimized considering cost-effectiveness in both **operation** and **expansion** planning.
- **Typical applications** include more efficient lighting in public infrastructure, industrial equipment retrofits, and residential upgrades such as improved air conditioning or heating systems.
- **Expansion planning integration**: efficiency programs are treated as investment alternatives with costs, constraints, and impacts on system needs — alongside traditional generation and transmission projects.

<!-- ### 🔀 Hybrid chronology

- Combines **typical days and chronological blocks** in a single run.
- Enables short-term modeling of renewable variability and intraday storage cycles while preserving computational efficiency. -->

## 🏗️ Expansion planning

### 📈 Efficient frontier analysis

- **Multi-criteria optimization** to identify portfolios that minimize cost while managing risk in expansion planning.
- Allows decision-makers to explore the trade-off between total cost and risk, selecting robust and cost-effective energy mixes.
- Accounts for uncertainty sources like fuel prices, climate variability, and policy shifts.
- Compatible with complex system interdependencies, including **energy supply chains and technology interactions**.
- Supports the **visualization of optimal and sub-optimal portfolios**, enhancing understanding of planning alternatives.

### 🛠️ Maintenance planning

Enables the **explicit and high-resolution modeling of maintenance schedules**, allowing users to move beyond simplified capacity derating and achieve more accurate planning results.

- Particularly valuable in contexts where **hourly dynamics and short-term constraints** matter for both operation and expansion planning—helping avoid distortions caused by average availability assumptions.
- Also supports **system operators and coordination agents** in approving, aggregating, or rescheduling maintenance requests under reliability and feasibility criteria.
- Maximizes the **system reserve margin** by identifying and protecting the most critical periods using risk-based metrics.
- Captures key operational constraints, including **minimum up/down times**, **ramp limits**, **precedence and association between maintenance requests**, **non-coincident maintenance** rules, and **forbidden periods or priority preferences**.
- Fully integrated into the broader planning methodology, complementing **operation planning with SDDP** and **expansion planning with OptGen**.

## 🗼 Transmission representation

A detailed transmission model is essential for accurately representing key aspects of modern energy systems — such as renewable integration, curtailment management, and operational flexibility. This enhanced modeling capability supports both operation and expansion planning with a high level of electrical and spatial granularity.

- Supports a wide range of **AC and DC components**: lines, 2- and 3-winding transformers, LCC and VSC converters, shunt devices, SVCs, and synchronous compensators  
- Includes advanced attributes such as electrical parameters, flow capacities, fault probabilities, tap settings, and voltage/reactive power control  
- Represents corridor constraints, contingency conditions, and flexible network topologies  
- Compatible with standard power flow databases and allows import from **PSS®E**, **PSLF**, and **other formats**

<!-- ## ⚙️ Modeling improvements

- **Multi-stage generic constraints** now supported, enabling long-horizon policies with flexible rules.
- **Group contingencies**: multiple circuits affected in a single event.
- **Unit-based modeling** of generation: each generator can have its own constraints, status, and reserve contribution.
- **Reserve representation** extended for CSP, batteries, and renewables.
- **Hourly flexibility** for demand, outages, and network status (e.g., DC link operational states). -->

<!-- ## 🧪 Execution and performance

- **Execution flags and configuration logic restructured** for better usability and control.
- **Support for skipping redundant constraint checks**, improving performance. -->

## 🧩 Compatibility and migration

- Internal architecture restructured to unify all models under one execution framework.
- Discontinued legacy files and input formats. Migration tools and warnings guide the transition.

