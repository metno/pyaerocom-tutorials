Tutorials
---------

pyaerocom tutorials and examples. All content displayed here is based on the
official pyaerocom tutorials which are not part of the 
`pyaerocom <https://github.com/metno/pyaerocom>`__ GitHub
repository but are available through the
`pyaerocom-tutorials repo <https://github.com/metno/pyaerocom-tutorials>`__.

All tutorials are jupyter notebooks.

.. note::

  The tutorials are currently undergoing revision, as the initial set of
  tutorial notebooks cannot be interactively executed from the outside world,
  since they relied on access to internal data servers of the Norwegian
  Meteorological Institute.

  These *old* tutorials can be found below in Section "Outdated tutorials".
  They are still mostly valid and provide a comprehensive introduction into
  pyaerocom and its main features.

  All other tutorials, that are shown in the following rely on publicly
  available example data, and can thus, be run interactively.

Getting started
===============

.. toctree::
   :hidden:

   getting_started_setup.ipynb
   getting_started_analysis.ipynb

This section contains tutorials that are meant to help you getting started
quickly with pyaerocom.


- `Setup and data access <getting_started_setup.html>`__ | *getting_started_setup.ipynb*
- `Basic data analysis <getting_started_analysis.html>`__ | *getting_started_analysis.ipynb*

Outdated tutorials
==================

.. toctree::
   :hidden:

   obsolete/tut00_get_started.ipynb
   obsolete/tut01_intro_regions.ipynb
   obsolete/tut02_intro_ReadGridded.ipynb
   obsolete/tut04_intro_class_GriddedData
   obsolete/tut05_intro_ungridded_reading
   obsolete/tut06_intro_UngriddedData_and_StationData_classes
   obsolete/tut07_intro_colocation
   obsolete/add04_stationdata_merging
   obsolete/tut08_trends_computation
   obsolete/add03_ebas_database_browser
   obsolete/add02_read_ebas_nasa_ames

.. note::

  These are old tutorials that are not tested against the latest pyaerocom version.
  Thus, some of the notebooks may not work properly anymore with the most recent
  pyaerocom version.

  Also, most of these tutorials rely on access to internal servers of the Norwegian
  Meteorological institute and can, thus, not be executed interactively from the
  outside world.

  However, the tutorials provide a comprehensive introduction into pyaerocom and
  most of the introduced features will work with the current pyaerocom version.
  Thus they are a useful addition to the updated notebooks above, which rely
  on publicly accessible data and can thus be run interactively.

   - `Getting started <obsolete/tut00_get_started.html>`__ | *tut00_get_started.ipynb*
   - `Regions in pyaerocom <obsolete/tut01_intro_regions.html>`__ | *tut01_intro_regions.ipynb*
   - `Reading of gridded data <obsolete/tut02_intro_ReadGridded.html>`__ | *tut02_intro_ReadGridded.ipynb*
   - `Working with gridded data <obsolete/tut04_intro_class_GriddedData.html>`__ | *tut04_intro_class_GriddedData.ipynb*
   - `Reading of ungridded data <obsolete/tut05_intro_ungridded_reading.html>`__ | *tut05_intro_ungridded_reading.ipynb*
   - `Working with ungridded observations <obsolete/tut06_intro_UngriddedData_and_StationData_classes.html>`__ | *tut06_intro_UngriddedData_and_StationData_classes.ipynb*
   - `Colocation of models and observations <obsolete/tut07_intro_colocation.html>`__ | *tut07_intro_colocation.ipynb*
   - `Merging of StationData <obsolete/add04_stationdata_merging.html>`__ | *add04_stationdata_merging.ipynb*
   - `Computation of trends <obsolete/tut08_trends_computation.html>`__ | *tut08_trends_computation.ipynb*
   - `EBAS data: finding the right data files <obsolete/add03_ebas_database_browser.html>`__ | *add03_ebas_database_browser.ipynb*
   - `EBAS data: low-level reading of NASA Ames files <obsolete/add02_read_ebas_nasa_ames.html>`__ | *add02_read_ebas_nasa_ames.ipynb*
