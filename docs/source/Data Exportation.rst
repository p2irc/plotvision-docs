Data Exportation
=====================================

How to Export
------------------------------------------

There are two buttons that can bring you to your results after a segmentation has been processed. The basic choise is to use the Data Export button on the left toolbar. This opens a popup where Trials and Missions can be selected. Bulk Exports are also possible from this popup, and downloading from multiple missions at once is usually quicker from here.

.. image:: /images/exports/bulk_export.png
    :width: 600

If data is only needed from a specific mission that you’ve already found in the dashboard, the export buttons from the mission panel are also an option. From here the same panel where you can export the orthomosaic, DSM, and CSV file will open.

.. image:: /images/exports/mission_export.png
    :width: 600

CSV File Metrics
-------------------------------------

This is the information for all current PlotVision computed per-plot metrics, as exported in the results CSV. All CSV file metrics require `Plot Extraction`_ to generate. For each metric, the associated column names in the results CSV are detailed. See also `Bands Specification`_ and `List of Indices`_ below. All metrics are based upon the individual plot image & plot Digital Surface Model (DSM) extracted from the trial orthomosaic image & DSM. Thus all metrics are calculated from the ortho-rectified overhead perspective, and should only be evaluated in that context. Unstitched raw images are not currently included in analysis.

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

This section details all the various images available to export in PlotVision. The Orthomosaic and DSM exports are the most basic, and do not require `Plot Extraction`_, but all other images do. Any image that requires plot extraction first should be found within a Bulk Export. Further, during plot extraction, the check box asking to generate the data should also have been checked.

Orthomosaic and DSM
^^^^^^^^^^^^^^^^^^^

The orthomosaic and DSM are the two most basic exports PlotVision provides. They require no extra input beyond the raw UAV images themselves (please look at `Pre-Flight Information`_ before imaging a research trial). Every mission will have the orthomosaic and DSM available for export from the dashboard as soon as stitching has completed.

The orthomosaic will be in .tif format, and have a number of channels equal to the input image. For example, for a RedEdge orthomosaic, the shape of the image will be (WIDTH, HEIGHT, 5), because a RedEdge camera captures 5 colour channels. RGB cameras cameras capture 3 channels. The DSM is a greyscale floating point image, where each pixel represents an altitude. The borders of both of these images will have a non-zero value to represent `null`, or a non-existant pixel value, usually set at the max possible value for the image type. If viewing these images in ArcGIS or QGIS, it is recommended to scale the image values.

Cropped Orthomosaic Images
^^^^^^^^^^^^^^^^^^^^^^^^^^

Cropped orthomosaic images are only available to export after a segmentation in which plot images were selected is finished processing. For each plot in the segmentation, the orthomosaic will be cropped to contain only that plot, named according to the plot name, and be saved in the same image format as the orthomosaic. These images are available for download in the Bulk Export section of the export popup, at the bottom. In the case of non-RGB orthomosaics, a "viewable\_" version of the image should also be available. This would contain only the RGB channels of the image, and is designed only to be used by humans inspecting the data for accuracy.

Beyond this, the same orthomosaic with various spectral indices and metrics applied is also available for download. These images will usually be a greyscale version of the orthomosaic with the given metric applied. These images can be downloaded at the bottom of the export popup, under the options in a Bulk Export.

Cropped Index Images
^^^^^^^^^^^^^^^^^^^^

Similar to the cropped orthomosaic images, these are only available after a successful segmentation in which plot images were chosen to be generated. These images will be in greyscale, and are simply the orthomosaic with the given spectral indices applied, then cropped to the plot.

Cropped _Segmented Index Images
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Masked images. Same as normal cropped images, but non-plant pixels have been blacked out using our proprietary vegetation segmentation algorithm.

Correlations
------------

Creating correlations and heatmaps is currently a work in progress for PlotVision development. It is not automatically included in any export. However, you can contact anyone on the PlotVision team and we'll see what we can do for you.

Plot Workspace
--------------

A tool for visualizing metrics, visualizing plot data, viewing plot images before downloading, and viewing the images with metrics applied.