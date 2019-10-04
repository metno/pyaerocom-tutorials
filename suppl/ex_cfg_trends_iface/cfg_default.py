#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SETUP to run conversion for Aerosol trends interface

Based on original notebook from A. Mortier and adapted for usage with pyaerocom.

NOTE: This is a BETA version, please report any errors to the developers.

Contact: jonasg@met.no, augustinm@met.no
"""

from collections import OrderedDict as od
from pyaerocom.web import VAR_MAPPING
import os

# default variable mapping dictionary, you may add variables if you like
var_mapping=VAR_MAPPING

NAME = 'default'
CFG = dict(
        
        name = NAME,
        obs_config = od([
              
        ('GAW-TAD-EANET',   dict(
                obs_vars            = ['sconcso4pr', 'sconcso4', 'sconcso2'],
                obs_vert_type       = 'Surface',
                obs_id              = 'GAWTADsubsetAasEtAl')
        ),
        ('AERONET-Sun',  dict(
                obs_vars            = ['od550aer', 'ang4487aer'],
                obs_id              = 'AeronetSunV3Lev2.daily',
                models              = ['ECMWF-Rean'],
                obs_vert_type       = 'Column')
        ),
        ('AERONET-SDA',  dict(
                obs_vars            = ['od550lt1aer', 'od550gt1aer'],
                obs_id              = 'AeronetSDAV3Lev2.daily',
                models              = ['ECMWF-Rean'],
                obs_vert_type       = 'Column')
        ),
               
        ('EBAS-Lev3',       dict(
                obs_vars            = ['scatc550dryaer', 'scatc550aer',
                                       'absc550aer', 'sconco3', 
                                       'sconcpm10', 'sconcpm25'],
                obs_id              = 'EBASMC',
                obs_vert_type       = 'Surface',
                obs_filters         = dict(remove_outliers = True,
                                           set_flags_nan   = True,
                                           data_level      = 2),
                var_outlier_ranges  = dict(scatc550dryaer   = [-10, 1000],
                                           scatc550aer      = [-10, 1000],
                                           absc550aer       = [-1, 100]))
        ), 
        ('EBAS-Lev2',       dict(
                obs_vars            = ['scatc550aer', 'absc550aer',
                                       'sconco3', 'sconcpm10', 'sconcpm25'],
                obs_id              = 'EBASMC',
                obs_vert_type       = 'Surface',
                obs_filters         = dict(data_level      = 2))),
        ('EBAS-RAW',        dict(   
                obs_vars            = ['scatc550aer', 'absc550aer', 'sconco3', 
                                       'sconcpm10', 'sconcpm25'],
                obs_id              = 'EBASMC',
                obs_vert_type       = 'Surface')),
        ('EARLINET',        dict(
                obs_vars            = ['bscatc532aer', 'ec532aer'],
                obs_id              = 'EARLINET',
                obs_vert_type       = 'Profile',
                min_dim             = 0)),
    ]),
         
    model_config = {
            
        'ECMWF-Rean'       :   dict(
                model_id            = 'ECMWF_CAMS_REAN',
                model_ts_type_read  = 'daily',
                mtype               = 'model')
    },
    # basic output directory for json files (files will be stored in 
    # designated subdirectories ts and map)
    out_basedir = os.path.abspath('../{}/'.format(NAME)),
    
    # additional regions other than the pyaerocom default regions
    _add_regions = {'Arctic'     :   dict(lon_range=[-180, 180],
                                          lat_range=[70, 90])},
    
    # periods that are supposed to be used for the analysis
    periods = ["1995-2014",
               "2001-2010",
               "2002-2012",
               "1995-2017",
               "2002-2017",
               "1980-2019"],

    # significance of slope (.68 corresponds to 1sigma)
    slope_alpha = 0.68,
    # minimum number of days per month
    min_dim = 5,
    
    # how is timeseries supposed to be averaged when aggregating
    avg_how = 'mean', # 'median'
    
    obs_order_menu_cfg = True,
    # delete outdated json files that may exist and are not part of this
    # configuration
    delete_outdated = True,
    
    # Delete existing json files before rerunning
    clear_existing_json = True, 
    
    # Write logfiles for outliers, errors and files that were created in 
    # analysis
    write_logfiles = True,
    
    # directory where logfiles are stored (only relevant if logging is 
    # active, cf. prev. option)
    #logdir = './logfiles/',
    logdir = os.path.abspath('../{}/logfiles/'.format(NAME)),
    
    var_mapping = var_mapping,
    var_order_menu = list(var_mapping)
)
        
if __name__ == '__main__':
   #print(var_mapping)
   from pyaerocom.web.trends_evaluation import TrendsEvaluation
   
   t = TrendsEvaluation(**CFG)
   t.to_json('.')
   t.update_menu()
   #t.run_evaluation('GAW-TAD-EANET')
   #t.run_evaluation('TEST-AERONET')   
   #t.run_evaluation('TEST-EBAS')
   
   #t.delete_outdated_json_files()
   #t#.update_menu()