# output_dir = <output_dir>"/data"
# coldata_dir = <output_dir>"/coldata"
# exp_pi = <your name>
# proj_id = "tutorial"
# exp_id = "bulk"

output_dir = "./data"
coldata_dir = "./coldata"
exp_pi = "DH"
proj_id = "tutorial"
exp_id = "bulk"

CFG = dict(
    # Output directories
    json_basedir=output_dir,
    coldata_basedir=coldata_dir,

    # Run options
    reanalyse_existing=True,        # if True, existing colocated data files will be deleted
    raise_exceptions=True,          # if True, the analysis will stop whenever an error occurs 
    clear_existing_json=False,      # if True, deletes previous output before running

    # Map Options
    add_model_maps=False,           # Adds a plot of the whole map. Very slow!!!
    only_model_maps=False,          # Adds only plot above, without any other evaluation
    filter_name="ALL-wMOUNTAINS",   # Regional filter for analysis
    map_zoom="Europe",              # Zoom level. For EMEP, Europe is typically used
    regions_how="country",          # Calculates statistics for different regions. Typically "country" is used, but that does not work for satellite data

    # Time and Frequency Options
    ts_type="monthly",              # Colocation frequency (no statistics in higher resolution can be computed)
    freqs=["monthly", "yearly"],    # Frequencies that are evaluated
    main_freq="monthly",            # Frequency that is displayed when opening webpage
    periods=["2017"],               # List of years or periods of years that are evaluated. E.g. "2005" or "2001-2020"
    

    # Statistical Options
    obs_remove_outliers=False,
    model_remove_outliers=False,
    colocate_time=False,
    zeros_to_nan=False,
    weighted_stats=True,
    annual_stats_constrained=True,
    harmonise_units=True,

    # Experiment Metadata
    exp_pi=exp_pi,
    proj_id=proj_id,
    exp_id=exp_id,
    exp_name="Evaluation of EMEP data with bulk variables",
    exp_descr=("Evaluation of EMEP data with bulk variables"),
    public=True,

    var_order_menu=["fraction"], # Adds variable to menu list, so it is visible at webpage 

)

folder_EMEP = "../../data/testdata-minimal/modeldata/EMEP_PM"

EMEP = dict(
        model_id="EMEP",
        model_data_dir=folder_EMEP,
        gridded_reader_id={"model": "ReadMscwCtm"}, # Tells pyaerocom to use the EMEP reader instead of the default aerocom reader
    )

MODELS = {
    "EMEP": EMEP,
}

CFG["model_cfg"] = MODELS


from pyaerocom.variable import Variable
from pyaerocom import const

variables = {
    "fraction": Variable(var_name="fraction", units="1"), # Defines a new variable
}

const.register_custom_variables(variables)
from pyaerocom.io import PyaroConfig


data_id = "nilupmfebas"
url = "../../data/testdata-minimal/obsdata/EBASTutorialData"

config = PyaroConfig(
    name="ebaspyaro",
    reader_id=data_id,
    filename_or_obj_or_url=url,
    filters={
        "variables": {
            "include": [
                "pm10#pm10_mass#ug m-3",
                "pm25#pm25_mass#ug m-3",
            ]
        }
    },
    name_map={
        "pm25#pm25_mass#ug m-3": "concpm25",
        "pm10#pm10_mass#ug m-3": "concpm10",
    },
)

EBAS= dict(
            obs_id=config.name,
            pyaro_config=config,
            web_interface_name="EBAS-m",
            obs_vars=[
                "fraction"
            ],
            obs_vert_type="Surface",
            ts_type="monthly",
            is_bulk=True,
            bulk_options={
            "fraction": dict(
                vars=["concpm25", "concpm10"],
                model_exists=False,
                mode="fraction",
                units="1",
            ),}
            
        )

OBS_CFG = {
    "EBAS-m": EBAS,
}

CFG["obs_cfg"] = OBS_CFG


from pyaerocom.aeroval import EvalSetup, ExperimentProcessor

print(
    const.CACHEDIR
)  # Prints where to find the caching folder. Not needed but this folder should be emptied now and then, so I like to see where it is


stp = EvalSetup(**CFG)  # Makes a setup object from the dict, that PyAeroval can use
ana = ExperimentProcessor(stp)  # Makes an experiment object
res = ana.run()  # Runs the experiment

