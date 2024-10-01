your_dir = <your folder>
output_dir = f"{your_dir}/data"
coldata_dir = f"{your_dir}/coldata"
exp_pi =  <your name>
proj_id = "tutorial"
exp_id = "customvar"

# %%
CFG = dict(
    # Output directories
    json_basedir=output_dir,
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
        "2018"
    ],  # List of years or periods of years that are evaluated. E.g. "2005" or "2001-2020"
    # Statistical Options
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
    exp_name="Evaluation of EMEP data",
    exp_descr=("Evaluation of EMEP data"),
    public=True,
)

# %%
DEFAULT_RESAMPLE_CONSTRAINTS = dict(
    yearly=dict(monthly=1),
    monthly=dict(
        daily=1,
        weekly=1,
        hourly=1,
    ),
    daily=dict(hourly=1),
)

CFG["min_num_obs"] = DEFAULT_RESAMPLE_CONSTRAINTS


# %%


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

from pyaerocom.variable import Variable
from pyaerocom import const

variables = {
    "elemental_carbon": Variable(var_name="elementalcarbon", units="ug C m-3"),
    "organic_carbon": Variable(var_name="organiccarbon", units="ug C m-3"),
}

const.register_custom_variables(variables)


# %%
def calc_elecmentalcarbon(concecCoarse, concecFine):

    elementalcarbon = concecCoarse.copy(deep=True) + concecFine.copy(
        deep=True
    )  # Adds the two variables
    elementalcarbon.attrs["units"] = "ug C m-3"  # Make sure the unit is correct
    return elementalcarbon


folder_EMEP = "/lustre/storeB/project/fou/kl/emep/ModelRuns/2021_REPORTING/TRENDS/2018"

EMEP = dict(
    model_id="EMEP",
    model_data_dir=folder_EMEP,
    gridded_reader_id={
        "model": "ReadMscwCtm"
    },  # Tells pyaerocom to use the EMEP reader instead of the default aerocom reader
    model_kwargs={
        "emep_vars": {"organiccarbon": "SURF_ugC_PM_OM25"},
    },
    model_read_aux={
        "elementalcarbon": {
            "vars_required": ["concecCoarse", "concecFine"],
            "fun": calc_elecmentalcarbon,
        }
    },
)


# %%
MODELS = {
    "EMEP": EMEP,
}

CFG["model_cfg"] = MODELS


# %%
EBAS = dict(
    obs_id="EBASMC",  # ID of EBAS in AeroTools
    web_interface_name="EBAS-m",  # The name which is shown on the web interface
    obs_vars=[
        "concpm10",  # Variables to be used
    ],
    obs_vert_type="Surface",  # Observation level
    ts_type="monthly",  # Frequency of read observations. Evaluation can not be finer than this, for this network
    obs_filters=EBAS_FILTER,  # Filters we made before
)

# %%
from pyaerocom.io.pyaro.pyaro_config import PyaroConfig

data_id = "nilupmfebas"
url = "/lustre/storeB/project/aerocom/aerocom1/AEROCOM_OBSDATA/EIMP/EIMPs_winter2017-2018_data/EIMPs_winter_2017_2018_ECOC_Levo/"
config = PyaroConfig(
    name="pmf",
    data_id=data_id,
    filename_or_obj_or_url=url,
    filters={
        "variables": {
            "include": [
                "pm10#elemental_carbon#ug C m-3",
                "pm10#organic_carbon#ug C m-3",
            ]
        }
    },
    name_map={
        "pm10#elemental_carbon#ug C m-3": "elementalcarbon",
        "pm10#organic_carbon#ug C m-3": "organiccarbon",
    },
)


# %%
PYARO = dict(
    obs_id=config.name,  # Must be set to the name found in the config
    obs_config=config,  # The pyaro config
    web_interface_name="Pyaro-m",  # Name that is displayed on the webpage
    obs_vars=[
        "elementalcarbon",
        "organiccarbon",
    ],  # List of variables that is to be evaluated
    obs_vert_type="Surface",  # Observation level
    ts_type="monthly",  # Frequency of read observations. Evaluation can not be finer than this, for this network
)


# %%
OBS_CFG = {
    "Pyaro-m": PYARO,
    # "EBAS-m": EBAS,
}  # "EEA-m": EEA}

CFG["obs_cfg"] = OBS_CFG


# %%
from pyaerocom.aeroval import EvalSetup, ExperimentProcessor
from pyaerocom import const

print(
    const.CACHEDIR
)  # Prints where to find the caching folder. Not needed but this folder should be emptied now and then, so I like to see where it is


stp = EvalSetup(**CFG)  # Makes a setup object from the dict, that PyAeroval can use
ana = ExperimentProcessor(stp)  # Makes an experiment object
res = ana.run()  # Runs the experiment


#
