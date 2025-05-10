# Config file: options for signal fitting

_year = '2022'

signalScriptCfg = {
  # Setup
  'inputWSDir': '/uscms/home/tsievert/nobackup/XHYbbgg/CombineFits/BoostedRootFiles/ws_GluGluToHH',
  'procs':'GluGluToHH', # if auto: inferred automatically from filenames
  'cats':'cat0', # if auto: inferred automatically from (0) workspace
  'ext':'2223_GluGluToHH',#_%s_nGaus'%_year,
  'analysis':'Boosted', # To specify which replacement dataset mapping (defined in ./python/replacementMap.py)
  'year':'combined', # Use 'combined' if merging all years: not recommended
  'massPoints':'125',
  'xvar':'CMS_hgg_mass',
  'skipVertexSplit': '--skipVertexScenarioSplit', #For HH searches, skip this if you are forming single Hgg with split vertex
    #Photon shape systematics  
  'scales':'',#'Scale', # separate nuisance per year
  'scalesCorr':'', # correlated across years
  'scalesGlobal':'', # affect all processes equally, correlated across years
  'smears':'',#'Smearing', # separate nuisance per year

  # Job submission options
  'batch':'local', # ['condor','SGE','IC','local']
  'queue':'espresso'

}
