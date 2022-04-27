Data Exportation
=====================================

CSV File Metrics
-------------------------------------

This is the information for all current PlotVision computed per-plot metrics, as exported in the results CSV. For each metric, the associated column names in the results CSV are detailed. See also `Bands Specification`_ and `List of Indices`_ below. All metrics are based upon the individual plot image & plot Digital Surface Model (DSM) extracted from the trial orthomosaic image & DSM. Thus all metrics are calculated from the ortho-rectified overhead perspective, and should only be evaluated in that context. Unstitched raw images are not currently included in analysis.

Included metrics:

- Spectral Indices
- Vegetation-segmented Spectral Indices
- Canopy Height
- Canopy Area
- Canopy Volume
- Canola Flower Area

Spectral Indices
^^^^^^^^^^^^^^^^

A variety of spectral indices are computed for every plot image, depending on the available image bands. First, a single-band plot index array is computed, with the same dimensions as the plot image, where each pixel is a computed index value. Next, the index values are aggregated into scalar summary values over the whole image. Currently, the mean and standard deviation of the plot index array are computed.

CSV column names
   | *mean_{INDEX NAME}*: The mean value of all pixels in the plot index array.
   | *std_{INDEX NAME}*: The standard deviation of all pixels in the plot index array.

*INDEX NAME* is specified separately for each index (see `List of indices`_).

Vegetation-Segmented Spectral Indices
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

These values are calculated in the same way as Spectral Indices, with one extra step. Prior to aggregating the index into summary values, a vegetation segmentation is computed for the
plot image, separating the image into vegetation and non-vegetation pixels. Then the summary values for the index are computed for the vegetation pixels only.

CSV column names
   | *mean_{INDEX NAME}_segmented*: The mean value of all vegetation pixels in the plot index array. This is an image that has been masked so that only vegetation pixels are included in the mean calculation.
   | *std_{INDEX NAME}_segmented*: The standard deviation of all vegetation pixels in the plot index array.

*INDEX NAME* is specified separately for each index (see `List of indices`_).



Canopy Height
^^^^^^^^^^^^^

Only available for georeferenced missions. Canopy height is calculated by first computing a vegetation segmentation for the plot image, separating the image into vegetation and non-vegetation pixels. Then summary height values in meters are aggregated based upon the Digital Surface Model elevation values corresponding to the ortho-rectified overhead vegetation pixels.

CSV column names
   | *mean_crop_height_m_{INDEX NAME FOR VEGETATION SEGMENTATION}-based*: mean plot canopy height in meters.
   | *median_crop_height_m_{INDEX NAME FOR VEGETATION SEGMENTATION}-based*: median plot canopy height in meters.
   | *max_crop_height_m_{INDEX NAME FOR VEGETATION SEGMENTATION}-based*: max plot canopy height in meters.
   | *std_crop_height_m_{INDEX NAME FOR VEGETATION SEGMENTATION}-based*: standard deviation of plot canopy height in meters.


Canopy Area
^^^^^^^^^^^

Only available for georeferenced missions. Canopy area is calculated by first computing a vegetation segmentation for the plot image, separating the image into vegetation and non-vegetation pixels. Then vegetation area in square meters is derived from GPS information.

CSV column names
    *crop_area_m2_{INDEX NAME FOR VEGETATION SEGMENTATION}-based*: plot canopy area in square meters, computed from the ortho-rectified overhead perspective.

Canopy Volume
^^^^^^^^^^^^^

Only available for georeferenced missions. Canopy volume is calculated by first computing av egetation segmentation for the plot image, separating the image into vegetation and non-vegetation pixels. Then vegetation volume in square meters is derived from GPS information.

CSV column names
   | *crop_volume_m3_{INDEX NAME FOR VEGETATION SEGMENTATION}-based*: plot canop volume in meters cubed.
   | *ground_dilation_pix_{INDEX NAME FOR VEGEATION_SEGMENTATION}-based*: value used for internal debugging. Can be ignored.

Canola Flower Area
^^^^^^^^^^^^^^^^^^

The area in meters squared covered by flowering canola from the ortho-rectified overhead perspective. Only relevant or included in crop that have flowering processes designed (such as canola).

CSV column names
   | *flower_area_m2*: The area in meters squared covered by flowering canola from the ortho-rectified overhead perspective.
   | *flower_fraction_of_plot_area*: the fraction of the total area of the plot (soil included) that is covered by flowers.


Bands Specification
^^^^^^^^^^^^^^^^^^^

Metrics are currently calculated according to named colour bands, not by exact wavelength values. So two different cameras can have a different wavelength for "Red", and PlotVision will naively treat them the same for the purposes of index calculations. Thus the onus is on the user to account wavelength differences between sensors. Nevertheless, a specification of roughly expected wavelengths follows:

.. list-table:: Band Specification
   :widths: 25 25 50
   :header-rows: 1

   * - Abbr.
     - Band
     - Colour Spectrum Range
   * - B
     - Blue
     - 443nm - 507nm
   * - G
     - Green
     - 533nm - 587nm
   * - R
     - Red
     - 654nm - 682nm
   * - RE
     - RedEdge
     - 705nm -729nm
   * - NIR
     - Near Infrared
     - 785nm - 899nm

List of indices
^^^^^^^^^^^^^^^

All current **Spectral Indices** and **Vegetation-Segmented Spectral Indices** for PlotVision. See `Bands Specification`_ for definitions of colour bands within formulas. *INDEX NAME* defines the name used for the index in the results CSV. It is very easy to add to this list. See `here <https://www.indexdatabase.de/db/i.php>`_ for suggestions. If you want an index to be added, please contact anyone on the PlotVision team.

**Anthocyanin reflectance index (ARI)**
   | formula: 1 / G - 1 / RE
   | INDEX NAME: ari


**custom chlorophyll index (non-standard)**
   | Formula: 1 / RE - 1 / NIR
   | INDEX NAME: chl


**Excess Green (ExG)**
   | Formula: 2G - B - R
   | INDEX NAME: excess_green


**Normalized Difference RedEdge Index (NDRE)**
   | Formula: (NIR - RE) / (NIR + RE)
   | INDEX NAME: ndre


**Normalized Difference Vegetation Index (NDVI)**
   | formula: (NIR - R) / (NIR + R)
   | INDEX NAME: ndvi


**Normalized Difference Yellowness Index (NDYI)**
   | formula: (G - B) / (G + B)
   | INDEX NAME: ndyi


**Sentera NDVI**
   | formula: Custom NDVI formula for Sentera sensors
   | INDEX NAME: sentera_ndvi


**Sentera NDRE**
   | formula: Custom NDRE formula for Sentera sensors
   | INDEX NAME: sentera_ndre


Image Exports
--------------

Correlations
------------

Plot Workspace
--------------
