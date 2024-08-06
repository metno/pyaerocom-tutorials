output_dir = <output_dir>
exp_pi = <your name>

data_dir = output_dir + "/data"
coldata_dir = output_dir + "/coldata"
proj_id = "tutorial"
exp_id = "emep-trends"


DEFAULT_RESAMPLE_CONSTRAINTS = dict(
    yearly=dict(monthly=9),
    monthly=dict(
        daily=1,
        weekly=1,
    ),
    daily=dict(hourly=1),
)


CFG = dict(
    # Output directories
    json_basedir=data_dir,
    coldata_basedir=coldata_dir,
    # Run options
    reanalyse_existing=True,  # if True, existing colocated data files will be deleted
    raise_exceptions=True,  # if True, the analysis will stop whenever an error occurs
    clear_existing_json=False,  # if True, deletes previous output before running
    # Map Options
    add_model_maps=False,  # Adds a plot of the whole map. Very slow!!!
    only_model_maps=False,  # Adds only plot above, without any other evaluation
    filter_name="ALL-wMOUNTAINS",  # Regional filter for analysis
    map_zoom="Europe",  # Zoom level. For EMEP, Europe is typically used
    regions_how="country",  # Calculates statistics for different regions. Typically "country" is used, but that does not work for satellite data
    # Time and Frequency Options
    ts_type="monthly",  # Colocation frequency (no statistics in higher resolution can be computed)
    freqs=["monthly", "yearly"],  # Frequencies that are evaluated
    main_freq="monthly",  # Frequency that is displayed when opening webpage
    periods=[
        "2000-2010"
    ],  # List of years or periods of years that are evaluated. E.g. "2005" or "2001-2020"
    # Statistical Options
    min_num_obs=DEFAULT_RESAMPLE_CONSTRAINTS,
    obs_remove_outliers=False,
    model_remove_outliers=False,
    colocate_time=True,
    zeros_to_nan=False,
    weighted_stats=True,
    annual_stats_constrained=True,
    harmonise_units=True,
    resample_how={
        "vmro3max": {"daily": {"hourly": "max"}}
    },  # How to handle Ozone. Used all the time in EMEP
    # Experiment Metadata
    exp_pi=exp_pi,
    proj_id=proj_id,
    exp_id=exp_id,
    exp_name="Evaluation of EMEP data, with trends",
    exp_descr=("Evaluation of EMEP data, with trends"),
    public=True,
)


BASE_FILTER = {
    "latitude": [30, 82],
    "longitude": [-30, 90],
    "altitude": [-200, 5000],
}

EBAS_FILTER = {
    **BASE_FILTER,
    "data_level": [None, 2],
    "set_flags_nan": True,
}

CFG["obs_cfg"] = {
    "EBAS-tc": dict(
        obs_id="EBASMC",
        web_interface_name="EBAS",
        obs_vars=[
            "concpm10",
            "concpm25",
        ],
        obs_vert_type="Surface",
        colocate_time=True,
        ts_type="monthly",
        obs_filters=EBAS_FILTER,
    )
}


# Dir where emep data is found
folder_EMEP = f"/lustre/storeB/project/fou/kl/emep/ModelRuns/2021_REPORTING/TRENDS/"

# Setup for models used in analysis
CFG["model_cfg"] = {
    "EMEP": dict(
        model_id="EMEP",
        model_data_dir=folder_EMEP,
        gridded_reader_id={"model": "ReadMscwCtm"},
        model_use_vars={"vmro3": "vmro3max"},
        model_rename_vars={"vmro3max": "vmro3"},
        model_ts_type_read="daily",
    ),
}


CFG.update(
    dict(
        add_trends=True,
        avg_over_trends=True,
        obs_min_yrs=7,
        stats_min_yrs=7,
        sequential_yrs=False,
    )
)


if __name__ == "__main__":
    from pyaerocom.aeroval import EvalSetup, ExperimentProcessor
    from pyaerocom import const

    print(
        const.CACHEDIR
    )  # Prints where to find the caching folder. Not needed but this folder should be emptied now and then, so I like to see where it is

    stp = EvalSetup(**CFG)  # Makes a setup object from the dict, that PyAeroval can use
    ana = ExperimentProcessor(stp)  # Makes an experiment object
    res = ana.run()  # Runs the experiment
