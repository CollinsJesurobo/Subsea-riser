                Lazy wave riser analysis automation tool.
Tools used:
- Orcaflex
- Python

code/standard used:
- DNVOSF201

Description:

This project involves building an analysis tool with ORCAFLEX-Python API to automate subsea lazywave riser modelling, analysis and postprocessing. The entire process from preprocessing to postprocessing was automated in Python.This method can also be applied to umbilicals, hoses.

The riser is similar to a catenary riser but with a distribued buoyancy module placed along a section of the riser to form a lazy configuration. The EndA is connected to FPSO at the topside and EndB anchored to the seabed. The response of the riser due to  hydrodynamics loading(wave,current), vessel RAOs, pipe self waight and content are simulated to determine the worst values for effective tension(top and bottom), bending moment, stresses, maximum combined loading on the riser. The allowable limits for effective tension, stresses, are computed from DNVOSF201 recommended practice taking into consideration the LRFD methodology, design factors and material strength. 

The analysis results are compared to the allowable limits to determine if the response is acceptable or not. The maximum combined load unity checks due to combined effect of effective tension, bending moment and pressure effects are also automatically extracted from the analysis.

1) The Preprocess.py builds the model:
- import OrcFxAPI  - OrcFxAPI is the Python-orcaflex API 

General
- setting of units
- stagecount, stagedurations and number of iterations

Environment:
- set the waterdepth
- seawater temperature
- wave type, wave direction,significant waveheight,and peak period
- set variable current values at corresponding water depths

Dragloads:
- variable drag coefficient as a function of Reynolds number

Vessel:
- set the vessel length,type and end boundary connection
- set the vessel position (translation and rotation)
- this project uses default Orcaflex vesselRAO, for real life project, the typical vessel FPSO RAO will be used

Line:
- create number of sections
- section length and targetsegmentlength
- Connect EndA to vessel and anchore EndB to seabed
- set the position and orientation of each End

Buoyancy module:
- line with float 
- create a section along the length of the pipe
- set the float properties(name,category,OD,ID,length,pitch,drag coefficients

Pipe material and dimension:
- set linepipe category (general,homogenous,equivalent)
- apply the linewizard
- specify material type (steel,Al,Ti,user specified)
- set outside diameter, wall thickness, content density
- wizard will automatically calculate the axial submerged weight, stiffness,bending stiffnnes and torsional stiffness


Code design factors
- select the applicable code and standards to be used
- set the design factors

Save model
- save as .dat (binary file)
- save as .yml (text file)


2) Postprocess.py
- import OrcFxAPI,numpy and pandas -they necessary modules for postprossing this application
- load the .dat file that was saved previously to have access to all objects within it
- open line, vessel and lintype objects
- compute the formula for the allowable load limits,and allowable stress limits according to codes/standard
- perform analysis( statics first followed by dynamics)
- extract the analysis results (toptension,bottom tension, minlinetension, bending moment,vonMises stress, 
  maxcombined loading,  maxcombined loading unity check, codesstress check)
- compare the analysis results and allowable limits, check for code compliance
- End of postprocessing