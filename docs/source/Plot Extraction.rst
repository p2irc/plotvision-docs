Plot Extraction
=================

Overview/Basics
---------------

The purpose of a segmentation is to obtain per-plot metrics such as NDVI, heights, or cropped images. A basic segmentation in PlotVision has three steps:

1. Create the segmentation
2. Fit the Edges of the Trial
3. Adjust Plot boxes

Step 1: Creating a Segmentation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To create a segmentation, a Trial Map must be uploaded first. This is most commonly done during the Upload Step 2 (Uploading Metadata), but can also be uploaded afterwards, in the Trial Manager.

First, select a mission from the Trial Dashboard, and select the first button to enter the Segmentation Dashboard for that mission.

.. image:: /images/segmentation/entry.png
    :width: 600

From here, begin a new Segmentation, and name it. If this is the first segmentation for the mission, and it completes successfully, it will automatically become the Default Segmentation for the mission.

.. image:: /images/segmentation/start.png
    :width: 600

.. image:: /images/segmentation/name.png
    :width: 600

Step 2: Fit Edges of Trial
^^^^^^^^^^^^^^^^^^^^^^^^^^

In this step, the user will need to select the four corners of the trial using Ctrl+Click. It’s important that the corners selected in this step are performed in order. Please follow the instructions on the left as to which corner order to click in. After this step, the orthomosaic will be cropped and rotated so that (a) only the plots are visible and (b) the first plot is in the top left corner. If this is not true, please double check the uploaded Trial Map, and the order in which you clicked corners.

.. image:: /images/segmentation/select_corners.png
    :width: 600

.. image:: /images/segmentation/crop_and_rotate.png
    :width: 600

Step 3: Adjust Plot Boxes
^^^^^^^^^^^^^^^^^^^^^^^^^

At this point, plot boxes should be automatically placed onto the orthomosaic according to the dimensions specified by the Trial Map. However, small adjustments are often needed on the plots to get a perfect segmentation. One can simply click and drag plot boxes around as required. Boxes can also have their size changed. Multiple plots can be selected at one time using a Ctrl+Click.

.. image:: /images/segmentation/moving.gif
    :width: 600

.. image:: /images/segmentation/adjust_size.gif
    :width: 600

Advanced Tooltips
-----------------

- Clicking a plot will move the yellow box to that plot
- Shift+Click on a plot to select all plots between the yellow plot and the clicked plot
- Space will select the entire range the yellow plot is in
- Moving the first and last plot of a range to fit, then selecting all the plots and Vertically Auto-Adjusting

Multi-Select and using Shift Click are the most basic of the Advanced Tools, and makes for quick work of some nasty segmentations

.. image:: /images/segmentation/multiselect.gif
    :width: 600

Selecting the entire range that the yellow plot is located in is also powerful, but it’s main use is when combined with other tools

.. image:: /images/segmentation/move_range.gif
    :width: 600

The most common use case of the Advanced Tools is when the plots extend beyond the range at the bottom of the orthomosaic. Instead of manually moving each plot one by one up a little bit to the correct location, try a combination of

1. Correctly positioning the top plot and the bottom plot of a range
2. Using the range selection tool to highlight every plot in the range
3. Using the Vertical Distribution tool to position every plot correctly

.. image:: /images/segmentation/accordian.gif
    :width: 600


Propagating to Future Missions
------------------------------

Shapefiles
------------
