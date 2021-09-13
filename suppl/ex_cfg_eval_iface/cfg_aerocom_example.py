#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Config file for AeroCom PhaseIII optical properties experiment
"""

from pyaerocom.aeroval import VAR_MAPPING

CFG = dict(
#: Project ID
proj_id = 'aerocom',

#: ID and name of experiment
exp_id = 'example',
exp_name = 'Pyaerocom example experiment',
    
# the parent directory of data_new needs to have the gitlab aeroval repository
# cloned if you wish to look at the data
out_basedir = '/home/jonasg/github/aerocom_evaluation/data_new/json/',
add_methods_file = './cube_read_methods.py',
# directory where colocated data files are supposed to be stored
basedir_coldata = '/home/jonasg/MyPyaerocom/colocated_data/',

# if True, existing colocated data files will be ignored and recomputed
reanalyse_existing = False,

# if True, the analysis will stop whenever an error occurs (else, errors that 
# occurred will be written into the logfiles)
raise_exceptions = False,

# Regional filter for analysis
filter_name = 'WORLD-noMOUNTAINS',

ts_type = 'daily',

# default start / stop of considered intercomparison. Leave stop None in order
# to analyse a single year
start = 2010,
stop = None,

# Option: outlier removal
# If True, outliers are removed from observations before colocation with models.
# Outlier ranges are taken from variables.ini file that is part of pyaerocom
# installation, e.g.
# low = pyaerocom.const.VARS.od550aer.minimum
# high = pyaerocom.const.VARS.od550aer.maximum
# or may be specified observation or model specific below in individual entries
# of obs_config or model_config, using keyword "var_outlier_ranges" (cf. entry
# for MODIS6-terra)
remove_outliers=False,
harmonise_units=True,

obs_config = {

'AeronetSun'        :   dict(obs_id='AeronetSunV3Lev2.daily',
                             obs_vars=['ang4487aer', 'od550aer'],
                             obs_filters=dict(remove_outliers=True,
                                              latitude=[20, 60],
                                              longitude=[5, 30]),
                             var_outlier_ranges = {'od550aer' : [0, 1]},
                             obs_vert_type='Column'),
                             
'AeronetSDA'        :   dict(obs_id='AeronetSDAV3Lev2.daily',
                             obs_vars=['od550lt1aer', 'od550gt1aer'],
                             obs_vert_type='Column'),
                             
'EBAS-Lev3'         :   dict(obs_id='EBASMC', 
                             obs_vars=['absc550aer', 'scatc550dryaer'], 
                             vert_scheme='surface',
                             obs_vert_type='Surface'),
                             
'MODIS6-terra'      :   dict(obs_id='MODIS6.terra',
                             obs_vars=['od550aer'],
                             regrid_res_deg=5,
                             obs_vert_type='Column',
                             ts_type='daily',
                             harmonise_units=False,
                             var_outlier_ranges=dict(od550aer=[0,10])),
'AATSR4.3-SU'       :   dict(obs_id='AATSR_SU_v4.3',
                            obs_vars=['od550aer', 'ang4487aer', 'od550lt1aer',
                                      'od550gt1aer', 'abs550aer'],
                            regrid_res_deg=5,
                            ts_type='daily',
                            obs_vert_type='Column')
},

obs_ignore = [],

# setup of models for this experiment (name and specs)
model_config = {
    'GFDL-AM4'          : dict(
            
            model_id='GFDL-AM4-met2010_AP3-CTRL',
            start=2010,
            model_ts_type_read='daily',
            model_read_aux={
                    'od550gt1aer'   : dict(
                            vars_required=['od550dust', 'od550ss'],
                            fun='add_cubes'),
                    'ang4487aer'    : dict(
                            vars_required=['od550aer', 'od870aer'],
                            fun='calc_ae')
                    },
            
    ),
            
    'OsloCTM3-2010'      :   dict(
        
            model_id='OsloCTM3v1.01',
            start=2010,
            model_ts_type_read='daily',
            model_use_vars={'absc550aer' : 'abs550aer'},
            model_read_aux={
                'scatc550dryaer': {'vars_required' : ['ec550dryaer', 
                                                      'abs550dryaer'],
                                   'fun': 'subtract_cubes'}
            },
    
    ),
            
    'ECMWF-REAN-2010'       :   dict(
    
            model_id='ECMWF_CAMS_REAN', 
            start=2010,
            model_ts_type_read='daily',
            model_use_vars={'abs550aer'      : 'od550bc'},
            model_read_aux={
                    'od550gt1aer': {'vars_required' : ['od550dust', 'od550ss'],
                                    'fun':'add_cubes'}}
    )
},


#: this will be evaluated when creating the menu.json
model_ignore = [],
var_mapping = VAR_MAPPING, 
# =============================================================================
# #: Names of variables and categories displayed in menu of website
# var_mapping = {'od550aer'       : ['AOD', '2D'],
#                'od550lt1aer'    : ['AOD<1um', '2D'],
#                'od550gt1aer'    : ['AOD>1um', '2D'],
#                'abs550aer'      : ['AAOD', '2D'],
#                'ang4487aer'     : ['AE', '2D'],
#                'scatc550dryaer' : ['Scat. coef. (dry)', '3D'],
#                'absc550aer'     : ['Abs. coef.', '3D']},  
# =============================================================================

var_order_menu = ['ang4487aer', 'od550aer', 'od550lt1aer', 'od550gt1aer',
                  'abs550aer', 'absc550aer', 'scatc550dryaer'],

clear_existing_json=True      
)
                                
if __name__ == '__main__':

    from pyaerocom.aeroval import AerocomEvaluation
    
    stp = AerocomEvaluation(**CFG)
    stp.to_json('.') # update json config
    
    stp.run_evaluation()
    #stp.make_info_table_web()
    stp.update_menu()
    #stp = AerocomEvaluation(proj_id='aerocom', exp_id='PIII-CTRL2019')
    #stp.update_menu(ignore_experiments='PIII-test')
    
    #d = stp.to_json('.')
    
    
    #stp.run_evaluation()
    #print(stp.__dict__.keys())

    #print(stp)
    
    #stp.get_custom_read_method_model('dummy')()
    #print(stp.get_custom_read_method_model('add_cubes'))
