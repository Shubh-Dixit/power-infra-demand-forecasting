# Dataset Description: Intelligent Forecasting System for Adaptive Material Demand

## Overview
This document describes the inputs and outputs for the "Intelligent Forecasting System for Adaptive Material Demand in Power Transmission and Substation Infrastructure". The goal is to forecast material requirements based on project parameters and environmental conditions.

## Inputs (Features)
These variables characterize the specific infrastructure project or maintenance event.

| Feature Name | Type | Description |
| :--- | :--- | :--- |
| `Date` | Date | Date of the material requisition or project start. |
| `Region` | Categorical | Geographic region (e.g., North, South, East, West) affecting logistics and climate. |
| `Terrain` | Categorical | Terrain type (Urban, Rural, Mountainous, Coastal) affecting construction difficulty. |
| `Infrastructure_Type` | Categorical | Type of asset (e.g., Substation, Transmission Line, Distribution Network). |
| `Project_Category` | Categorical | Nature of work (New Installation, Routine Maintenance, Emergency Repair, grid Upgrade). |
| `Voltage_Level_kV` | Numerical | System voltage (e.g., 33, 66, 132, 220, 400) determining equipment rating. |
| `Route_Length_km` | Numerical | Length of the transmission line or coverage area (0 for substations). |
| `Weather_Condition` | Categorical | Prevailing weather (Clear, Rainy, Storm, Heatwave) influencing immediate repair needs. |
| `Project_Budget_Index` | Numerical | Normalized index indicating the scale of investment. |

## Outputs (Material Demands)
These are the specific materials whose quantities are to be predicted or analyzed.

| Material | Unit | Description |
| :--- | :--- | :--- |
| `ACSR_Conductor` | Meters | Aluminum Conductor Steel Reinforced cables for overhead lines. |
| `Underground_Cable_XLPE` | Meters | Cross-linked polyethylene insulated cables for underground usage. |
| `Towers_Steel` | Tonnes | Structural steel for transmission towers or substation gantries. |
| `Insulators_Disc` | Count | Porcelain or glass insulators for suspension strings. |
| `Insulators_Polymer` | Count | Polymer long-rod insulators (often used in polluted areas). |
| `Circuit_Breakers` | Count | High-voltage switchgear for circuit protection. |
| `Power_Transformers` | Count | Voltage transformation units (usually 0 or 1 per record, unless bulk order). |
| `Concrete` | Cubic Meters | Foundation material for towers and equipment pads. |
| `Control_Cables` | Meters | Low voltage cables for instrumentation and control. |
