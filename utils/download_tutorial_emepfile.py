import requests
import xarray as xr
from pathlib import Path

EMEP_URL = "https://thredds.met.no/thredds/fileServer/data/EMEP/2024_Reporting/EMEP01_rv5.3_month.1999met_1999emis_rep2024.nc"
DOWNLOAD_OUTNAME = "Base_month_full.nc"
DOWNLOAD_PATH = Path("./tmp/") / DOWNLOAD_OUTNAME

Path("./tmp").mkdir(exist_ok=True)

NEW_OUTNAME = "Base_month.nc"
NEW_PATH = Path("./tmp/") / NEW_OUTNAME

if not DOWNLOAD_PATH.exists():
    print("Downloading EMEP data")
    query_parameters = {"downloadformat": "nc"}

    response = requests.get(EMEP_URL, params=query_parameters)

    with open(DOWNLOAD_PATH, mode="wb") as f:
        f.write(response.content)


data = xr.open_dataset(DOWNLOAD_PATH)

min_lat, max_lat = 57, 72
min_lon, max_lon = 3, 24

LatIndexer, LonIndexer = "lat", "lon"
slicedata = data.sel(
    **{LatIndexer: slice(min_lat, max_lat), LonIndexer: slice(min_lon, max_lon)}
)

variables = ["SURF_ug_PM10_rh50", "SURF_ppb_O3"]


reduceddata = slicedata[variables]


reduceddata.to_netcdf(NEW_PATH)
