#Config file: options for bkg fitting
_year ='2022'
backgroundScriptCfg = {
  # Setup
  'inputWS': '/uscms/home/tsievert/nobackup/XHYbbgg/CombineFits/BoostedRootFiles/ws/2223_Boosted_Data.root',
  'cats':'cat0', # if auto: inferred automatically from (0) workspace
  'ext':'222324_Data',
  'catOffset': 0,
  'year':'combined',   # Use 'combined' if merging all years: not recommended    
  # Job submission options
  'batch':'local',  # ['condor','SGE','IC','local']
  'queue':'espresso'
}
