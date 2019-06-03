
Gridded model profile data: how AeroCom “ModelLevel” files should be prepared
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This notebook shows an example 4D AeroCom model data file that contains
aerosol extinction coefficients and how such files should be prepared,
such that pyaerocom can convert the model levels to altitude levels.

.. code:: ipython3

    import pyaerocom as pya


.. parsed-literal::

    Initating pyaerocom configuration
    Checking database access...
    Checking access to: /lustre/storeA
    Access to lustre database: True
    Init data paths for lustre
    Expired time: 0.025 s


.. code:: ipython3

    model_reader = pya.io.ReadGridded('GISS-MATRIX_GLOFIR0p5') 
    print(model_reader)


.. parsed-literal::

    
    Pyaerocom ReadGridded
    ---------------------
    Model ID: GISS-MATRIX_GLOFIR0p5
    Data directory: /lustre/storeA/project/aerocom/aerocom-users-database/AEROCOM-PHASE-III/GISS-MATRIX_GLOFIR0p5/renamed
    Available experiments: ['GISS-MATRIX_GLOFIR0p5']
    Available years: [2008]
    Available frequencies ['3hourly', 'daily', 'monthly']
    Available variables: ['abs550aer', 'abs550aercs', 'dh', 'drybc', 'drydust', 'drynh4', 'dryno3', 'dryoa', 'dryso2', 'dryss', 'ec550aer', 'emibc', 'emidms', 'emidust', 'emioa', 'emiso2', 'emiso4', 'emisoa', 'emiss', 'hus', 'mmrbc', 'mmrdust', 'mmrnh4', 'mmrno3', 'mmroa', 'mmrso4', 'mmrss', 'od550aer', 'od550aercs', 'ps', 'rh', 'ta', 'ts', 'uas', 'vas', 'was', 'wetbc', 'wetdust', 'wetnh4', 'wetno3', 'wetoa', 'wetso2', 'wetso4', 'wetss']


.. code:: ipython3

    data = model_reader.read_var('ec550aer', ts_type='daily', vert_which='ModelLevel')
    print(data)


.. parsed-literal::

    /home/jonasg/anaconda3/lib/python3.6/site-packages/iris/fileformats/cf.py:1069: UserWarning: Ignoring formula terms variable 'ps' referenced by data variable 'b_bnds' via variable 'lev': Dimensions ('time', 'lat', 'lon') do not span ('lev', 'bnds')
      warnings.warn(msg)
    /home/jonasg/anaconda3/lib/python3.6/site-packages/iris/fileformats/cf.py:1069: UserWarning: Ignoring formula terms variable 'ps' referenced by data variable 'a_bnds' via variable 'lev': Dimensions ('time', 'lat', 'lon') do not span ('lev', 'bnds')
      warnings.warn(msg)
    /home/jonasg/anaconda3/lib/python3.6/site-packages/iris/fileformats/netcdf.py:599: UserWarning: Unable to find coordinate for variable 'ps'
      '{!r}'.format(name))
    /home/jonasg/anaconda3/lib/python3.6/site-packages/iris/fileformats/netcdf.py:599: UserWarning: Unable to find coordinate for variable 'ps'
      '{!r}'.format(name))


.. parsed-literal::

    pyaerocom.GriddedData: GISS-MATRIX_GLOFIR0p5
    Grid data: Aerosol Extinction @550nm                                (time: 365; atmosphere_hybrid_sigma_pressure_coordinate: 40; latitude: 90; longitude: 144)
         Dimension coordinates:
              time                                                x                                                 -             -              -
              atmosphere_hybrid_sigma_pressure_coordinate         -                                                 x             -              -
              latitude                                            -                                                 -             x              -
              longitude                                           -                                                 -             -              x
         Auxiliary coordinates:
              surface_air_pressure                                x                                                 -             x              x
              hybrid sigma coordinate A coefficient for layer     -                                                 x             -              -
              hybrid sigma coordinate B coefficient for layer     -                                                 x             -              -
              vertical pressure                                   -                                                 x             -              -
         Derived coordinates:
              air_pressure                                        x                                                 x             x              x
         Scalar coordinates:
              reference pressure for hybrid sigma coordinate: 100000.0 Pa
         Attributes:
              Conventions: CF-1.3
              associated_files: gridspecFile: gridspec_REALM_fx_GISS-MATRIX-GLOFIR0p5_r0i0p0.nc
              branch_time: 0.0
              cmor_version: 2.5.7
              contact: Kenneth Lo (cdkkl@giss.nasa.gov)
              creation_date: 2017-03-09T23:41:42Z
              experiment: GLOFIR0p5
              experiment_id: GLOFIR0p5
              forcing: N/A
              frequency: day
              history: 2017-03-09T23:41:42Z altered by CMOR: replaced missing value flag (-1e+30)...
              initialization_method: 1
              institute_id: NASA-GISS
              institution: NASA/GISS (Goddard Institute for Space Studies) New York, NY
              invalid_standard_name: volume_extinction_coeffcient_in_air_due_to_ambient_aerosol_particles
              model_id: GISS-MATRIX-GLOFIR0p5
              modeling_realm: REALM
              original_name: ec550aer
              parent_experiment: N/A
              parent_experiment_id: N/A
              parent_experiment_rip: N/A
              physics_version: 1
              product: output
              project_id: AEROCOM-ACC
              realization: 1
              references: http://data.giss.nasa.gov/modelE/ar5
              source: GISS-MATRIX-GLOFIR0p5-MATRIXEQSAM_AEROBB2s Atmosphere: GISS-E2; Ocean:...
              table_id: Table 3D-D (July 2009) 6053da228d695447dc6f66720d2bf9f8
              title: GISS-MATRIX-GLOFIR0p5 model output prepared for AEROCOM-ACC GLOFIR0p5
              tracking_id: 10b022b3-0597-490f-8d97-24c074853a57
         Cell methods:
              mean: time

