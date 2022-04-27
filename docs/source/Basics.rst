Basics
=====

What is PlotVision
-----------------

PlotVision is a SaaS for processing high throughput phenotyping data, specifically captured from UAV/drones. Found at www.plotvision.usask.ca, a user can upload images taken from a UAV flight on research plots, and PlotVision will stitch them into an orthomosaic. From there, a user can segment the separate research plots, and obtain calculated phenotypes.

Analytics
^^^^^^^^^

- Spectral Indices
- Vegetation-segmented spectral indices
- Canopy height, ground cover, and volume
- Canola flower area
- All of the above over time

Termonology
------------

trial
    A single in-field agricultural experiment, consisting of some number of plots and reps in a specific layout.

plot
    The experimental atomic unit of a trial. Each plot has a specific variety or treatment of the same crop, and has a unique plot ID.

range
    A group of plots within a trial, arranged in a line.

bloc
    A group of ranges within a trial. Usually corrosponds to a single rep.

rep
    "Replications" of a single plot. Used to accomodate for environmental variability in a trial.

row
    A single line of seeded plants within a trial. Can span ranges. Multiple rows of the same treatment form a plot.

field
    The physical location containing experimental trials. Can contain more than one trial.

mission
    A single flight or group of images of a field. Can contain multiple trials within. Can only have one sensor type.

sensor type
    The camera used to image during a mission.

trial map
    Details of a trial layout specifying the dimensions and cardinal directions of a given trial, used for plot segmentation.

ground control points (GCPs)
    Physical markers than can be perminately placed in a field. These markers can be RTK GPSed for precise georeferencing without the need of a sensor with GPS. These markers are very specific and can be automatically detected by our software.







