# import FWCore.ParameterSet.Config as cms

from FWCore.ParameterSet.VarParsing import VarParsing
# import copy
# from pdb import set_trace

###############################
####### Parameters ############
###############################

options = VarParsing ('analysis')

options.register('runOnData', False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "Run this on real data"
)
options.register('outFilename', 'JetTreeHLT',
    VarParsing.multiplicity.singleton,
    VarParsing.varType.string,
    "Output file name"
)
options.register('reportEvery', 10,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.int,
    "Report every N events (default is N=1)"
)
options.register('wantSummary', False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "Print out trigger and timing summary"
)
options.register('useCalo', False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "Use Calo"
)
options.register('usePFchs', True,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "Use PFchs"
)
options.register('usePuppi', False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "Use Puppi"
)
options.register('usePuppiForBTagging', False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "Use Puppi candidates for b tagging"
)
options.register('mcGlobalTag', 'FIXME',
    VarParsing.multiplicity.singleton,
    VarParsing.varType.string,
    "MC global tag, no default value provided"
)
options.register('dataGlobalTag', 'FIXME',
    VarParsing.multiplicity.singleton,
    VarParsing.varType.string,
    "Data global tag, no default value provided"
)
# options.register('runJetClustering', True,
#     VarParsing.multiplicity.singleton,
#     VarParsing.varType.bool,
#     "Cluster jets from scratch instead of using those already present in the event"
# )
options.register('runEventInfo', True,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "Run Event Info"
)
options.register('processStdAK4Jets', True,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "Process standard AK4 jets"
)
options.register('useTTbarFilter', False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "Use TTbar filter"
)
# options.register('remakeAllDiscr', False,
#     VarParsing.multiplicity.singleton,
#     VarParsing.varType.bool,
#     "Remake all b-tag discriminator"
# )
# options.register('useExplicitJTA', False,
#     VarParsing.multiplicity.singleton,
#     VarParsing.varType.bool,
#     "Use explicit jet-track association"
# )
# options.register('jetAlgo', 'AntiKt',
#     VarParsing.multiplicity.singleton,
#     VarParsing.varType.string,
#     "Jet clustering algorithms (default is AntiKt)"
# )
options.register('useTrackHistory', False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "uses track history, for GEN-SIM-RECODEBUG samples only"
)
options.register('produceJetTrackTree', False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "True if you want to run info for tracks associated to jets : for commissioning studies"
)
options.register('produceAllTrackTree', False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "Produce all track tree"
)

options.register('fillPU', True,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "Fill PU"
)
### Options for upgrade studies
# Change hits requirements
options.register('changeMinNumberOfHits', False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    "Change minimum number of tracker hits"
)
options.register('minNumberOfHits', 1,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.int,
    "Minimum number of tracker hits"
)
# Change eta for extended forward pixel coverage
options.register('maxJetEta', 4.5,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.float,
    "Maximum jet |eta| (default is 4.5)"
)
options.register('minJetPt', 20.0,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.float,
    "Minimum jet pt (default is 20)"
)
options.register('usePrivateJEC', False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    'Use JECs from private SQLite files')
options.register('jecDBFileMC', 'FIXME',
    VarParsing.multiplicity.singleton,
    VarParsing.varType.string,
    'SQLite filename for JECs, no default value provided')
options.register('jecDBFileData', 'FIXME',
    VarParsing.multiplicity.singleton,
    VarParsing.varType.string,
    'SQLite filename for JECs, no default value provided')
options.register('isReHLT', False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    '80X reHLT samples')
options.register('JPCalibration', 'FIXME',
    VarParsing.multiplicity.singleton,
    VarParsing.varType.string,
    'JP Calibration pyload to use')
options.register('runJetVariables', True,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    'True if you want to run Jet Variables')
options.register('runTagVariables', True,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    'True if you want to run Tag Variables')
options.register('runQuarkVariables', False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    'True if you want to run c/b quark Variables')
options.register('runHadronVariables', False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    'True if you want to run Hadron Variables')
options.register('runGenVariables', False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    'True if you want to run Gen Variables')
options.register('runCSVTagVariables', True,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    'True if you want to run CSV TaggingVariables')
options.register('runCSVTagTrackVariables', True,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    'True if you want to run CSV Tagging Track Variables')
options.register('runDeepFlavourTagVariables', False,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.bool,
    'True if you want to run DeepFlavour TaggingVariables')
# options.register('runPFElectronVariables', False,
#     VarParsing.multiplicity.singleton,
#     VarParsing.varType.bool,
#     'True if you want to run PF Electron Variables')
# options.register('runPFMuonVariables', False,
#     VarParsing.multiplicity.singleton,
#     VarParsing.varType.bool,
#     'True if you want to run PF Muon Variables')
# options.register('runPatMuons', False,
#     VarParsing.multiplicity.singleton,
#     VarParsing.varType.bool,
#     'True if you want to run Pat Muon Variables')
options.register('defaults', '',
    VarParsing.multiplicity.singleton,
    VarParsing.varType.string,
    'baseline default settings to be used')
options.register('eras', [],
    VarParsing.multiplicity.list,
    VarParsing.varType.string,
    'era modifiers to be used to be used')
options.register('groups', [],
    VarParsing.multiplicity.list,
    VarParsing.varType.string,
    'variable groups to be stored')
options.register(
    'skipEvents', 0,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.int,
    "skip N events"
)

## 'maxEvents' is already registered by the Framework, changing default value
options.setDefault('maxEvents', -1)

options.parseArguments()
if options.defaults:
	from importlib import import_module
	try:
		defaults = import_module('RecoBTag.PerformanceMeasurements.defaults_HLT.%s' % options.defaults)
	except ImportError:
		raise ValueError('The default settings named %s.py are not present in PerformanceMeasurements/python/defaults_HLT/' % options.defaults)
	if not hasattr(defaults, 'common') or not isinstance(defaults.common, dict):
		raise RuntimeError('the default file %s.py does not contain a dictionary named common' % options.defaults)
	items = defaults.common.items()
	if hasattr(defaults, 'data') and options.runOnData:
		if not isinstance(defaults.data, dict):
			raise RuntimeError('the default file %s.py contains an object called "data" which is not a dictionary' % options.defaults)
		items.extend(defaults.data.items())
	if hasattr(defaults, 'mc') and not options.runOnData:
		if not isinstance(defaults.mc, dict):
			raise RuntimeError('the default file %s.py contains an object called "mc" which is not a dictionary' % options.defaults)
		items.extend(defaults.mc.items())
	for key, value in items:
		if key not in options._beenSet:
			raise ValueError('The key set by the defaults: %s does not exist among the cfg options!' % key)
		elif not options._beenSet[key]:
			if key == 'inputFiles' and options.inputFiles: continue #skip input files that for some reason are never considered set
			print 'setting default option for', key
			setattr(options, key, value)

from RecoBTag.PerformanceMeasurements.HLTBTagAnalyzer_cff import *
btagana_tmp = HLTBTagAnalyzer.clone()
print('Storing the variables from the following groups:')
options_to_change = set() #store which swtiches we need on
for requiredGroup in options.groups:
  print(requiredGroup)
  found=False
  for existingGroup in btagana_tmp.groups:
    if(requiredGroup==existingGroup.group):
      existingGroup.store=True
      for var in existingGroup.variables:
        options_to_change.update([i for i in variableDict[var].runOptions])
      found=True
      break
  if(not found):
    print('WARNING: The group ' + requiredGroup + ' was not found')

#change values accordingly
for switch in options_to_change:
  if switch in ["runTagVariablesSubJets","runCSVTagVariablesSubJets"]:
      continue
  elif switch not in options._beenSet:
    raise ValueError('The option set by the variables: %s does not exist among the cfg options!' % switch)
  elif not options._beenSet[switch]:
    print 'Turning on %s, as some stored variables demands it' % switch
    setattr(options, switch, True)


## Use either PFchs or Puppi
if options.usePFchs and options.usePuppi:
    print "WARNING: Both usePFchs and usePuppi set to True. Giving priority to Puppi."
    options.usePFchs = False

print "Running on data: %s"%('True' if options.runOnData else 'False')
print "Using calo: %s"%('True' if options.useCalo else 'False')
print "Using PFchs: %s"%('True' if options.usePFchs else 'False')
print "Using Puppi: %s"%('True' if options.usePuppi else 'False')
print "Using Puppi for b tagging: %s"%('True' if (options.usePuppi and options.usePuppiForBTagging) else 'False')

## Global tag
globalTag = options.mcGlobalTag
if options.runOnData:
    globalTag = options.dataGlobalTag

## Jet energy corrections
# jetCorrectionsAK4 = ('AK4PF', ['L1FastJet', 'L2Relative', 'L3Absolute'], 'None')
# jetCorrectionsAK8 = ('AK8PF', ['L1FastJet', 'L2Relative', 'L3Absolute'], 'None')
# if options.usePFchs:
#     jetCorrectionsAK4 = ('AK4PFchs', ['L1FastJet', 'L2Relative', 'L3Absolute'], 'None')
#     jetCorrectionsAK8 = ('AK8PFchs', ['L1FastJet', 'L2Relative', 'L3Absolute'], 'None')
# if options.usePuppi:
#     jetCorrectionsAK4 = ('AK4PFPuppi', ['L2Relative', 'L3Absolute'], 'None')
#
# if options.runOnData:
#     jetCorrectionsAK4[1].append('L2L3Residual')
#     jetCorrectionsAK8[1].append('L2L3Residual')

trigresults='TriggerResults::HLT'
if options.runOnData: options.isReHLT=False
if options.isReHLT: trigresults = trigresults+'2'


pfjets = "hltAK4PFJets" #original ak4PFJetsCHS
calojets = "hltAK4CaloJets" #original ak4CaloJets
PFDeepCSVTags = "hltDeepCombinedSecondaryVertexBPFPatJetTags" # original: pfDeepCSVJetTags
PFDeepFlavourTags = "hltPFDeepFlavourJetTags" # original: pfDeepFlavourJetTagsSlimmedDeepFlavour
rho = "hltFixedGridRhoFastjetAll" #original fixedGridRhoFastjetAll
hltVertices = "hltVerticesPFFilter" #original offlinePrimaryVertices
hltVerticesSlimmed = "hltVerticesPFFilter" #original offlineSlimmedPrimaryVertices
siPixelClusters = "hltSiPixelClusters" #original siPixelClusters
ecalRecHit = "hltEcalRecHit" #original ecalRecHit
hbhereco = "hltHbhereco" #original hbhereco
hfreco = "hltHfreco" #original hfreco
horeco = "hltHoreco" #original horeco
rpcRecHits = "hltRpcRecHits" #original rpcRecHits
tracks = "hltMergedTracks" #original generalTracks
payload = "AK4PFHLT" #original AK4PFchs




## b-tag infos
# bTagInfos = [
#     # 'pfImpactParameterTagInfos'
#    # ,'pfSecondaryVertexTagInfos'
#    # ,'pfInclusiveSecondaryVertexFinderTagInfos'
#    'hltDeepSecondaryVertexTagInfosPF'
#    # ,'pfSecondaryVertexNegativeTagInfos'
#    # ,'pfInclusiveSecondaryVertexFinderNegativeTagInfos'
#    # ,'softPFMuonsTagInfos'
#    # ,'softPFElectronsTagInfos'
#    # ,'pfInclusiveSecondaryVertexFinderCvsLTagInfos'
#    # ,'pfInclusiveSecondaryVertexFinderNegativeCvsLTagInfos'
#    # ,'pfDeepFlavourTagInfos'
# ]
# bTagInfos_noDeepFlavour = bTagInfos[:-1]
## b-tag discriminators
# bTagDiscriminators = set([
#    #  'pfJetBProbabilityBJetTags'
#    # ,'pfJetProbabilityBJetTags'
#    # ,'pfPositiveOnlyJetBProbabilityBJetTags'
#    # ,'pfPositiveOnlyJetProbabilityBJetTags'
#    # ,'pfNegativeOnlyJetBProbabilityBJetTags'
#    # ,'pfNegativeOnlyJetProbabilityBJetTags'
#    # ,'pfTrackCountingHighPurBJetTags'
#    # ,'pfTrackCountingHighEffBJetTags'
#    # ,'pfNegativeTrackCountingHighPurBJetTags'
#    # ,'pfNegativeTrackCountingHighEffBJetTags'
#    # ,'pfSimpleSecondaryVertexHighEffBJetTags'
#    # ,'pfSimpleSecondaryVertexHighPurBJetTags'
#    # ,'pfNegativeSimpleSecondaryVertexHighEffBJetTags'
#    # ,'pfNegativeSimpleSecondaryVertexHighPurBJetTags'
#    # ,'pfCombinedSecondaryVertexV2BJetTags'
#    # ,'pfPositiveCombinedSecondaryVertexV2BJetTags'
#    # ,'pfNegativeCombinedSecondaryVertexV2BJetTags'
#    # ,'pfCombinedInclusiveSecondaryVertexV2BJetTags'
#    # ,'pfPositiveCombinedInclusiveSecondaryVertexV2BJetTags'
#    # ,'pfNegativeCombinedInclusiveSecondaryVertexV2BJetTags'
#    # ,'softPFMuonBJetTags'
#    # ,'positiveSoftPFMuonBJetTags'
#    # ,'negativeSoftPFMuonBJetTags'
#    # ,'softPFElectronBJetTags'
#    # ,'positiveSoftPFElectronBJetTags'
#    # ,'negativeSoftPFElectronBJetTags'
#    # ,'pfCombinedMVAV2BJetTags'
#    # ,'pfNegativeCombinedMVAV2BJetTags'
#    # ,'pfPositiveCombinedMVAV2BJetTags'
#    # ,'pfCombinedCvsBJetTags'
#    # ,'pfNegativeCombinedCvsBJetTags'
#    # ,'pfPositiveCombinedCvsBJetTags'
#    # ,'pfCombinedCvsLJetTags'
#    # ,'pfNegativeCombinedCvsLJetTags'
#    # ,'pfPositiveCombinedCvsLJetTags'
#     # DeepCSV
#   # , 'pfDeepCSVJetTags:probudsg'
#   # , 'pfDeepCSVJetTags:probb'
#   # , 'pfDeepCSVJetTags:probc'
#   # , 'pfDeepCSVJetTags:probbb'
#    PFDeepCSVTags+':probudsg'
#   , PFDeepCSVTags+':probb'
#   , PFDeepCSVTags+':probc'
#   , PFDeepCSVTags+':probbb'
#   # , 'pfNegativeDeepCSVJetTags:probudsg'
#   # , 'pfNegativeDeepCSVJetTags:probb'
#   # , 'pfNegativeDeepCSVJetTags:probc'
#   # , 'pfNegativeDeepCSVJetTags:probbb'
#   # , 'pfPositiveDeepCSVJetTags:probudsg'
#   # , 'pfPositiveDeepCSVJetTags:probb'
#   # , 'pfPositiveDeepCSVJetTags:probc'
#   # , 'pfPositiveDeepCSVJetTags:probbb'
#     # DeepFlavour
#   # , 'pfDeepFlavourJetTags:probb'
#   # , 'pfDeepFlavourJetTags:probbb'
#   # , 'pfDeepFlavourJetTags:problepb'
#   # , 'pfDeepFlavourJetTags:probc'
#   # , 'pfDeepFlavourJetTags:probuds'
#   # , 'pfDeepFlavourJetTags:probg'
#   # , 'pfNegativeDeepFlavourJetTags:probb'
#   # , 'pfNegativeDeepFlavourJetTags:probbb'
#   # , 'pfNegativeDeepFlavourJetTags:problepb'
#   # , 'pfNegativeDeepFlavourJetTags:probc'
#   # , 'pfNegativeDeepFlavourJetTags:probuds'
#   # , 'pfNegativeDeepFlavourJetTags:probg'
# ])


## Clustering algorithm label
# algoLabel = 'CA'
# if options.jetAlgo == 'AntiKt':
#     algoLabel = 'AK'

# print "Jet clustering: %s"%('True' if options.runJetClustering else 'False')


# bTagDiscriminators_no_deepFlavour = {i for i in bTagDiscriminators if 'DeepFlavourJetTags' not in i}

# if options.runJetClustering:
#     options.remakeAllDiscr = True


## Postfix
# postfix = "PFlow"
## Various collection names
genParticles = 'genParticles'
# jetSource = 'pfJetsPFBRECO'+postfix
# patJetSource = 'selectedPatJets'+postfix
# patJetSource = 'hltSlimmedJets'
patJetSource = 'hltPatJets'
genJetCollection = 'ak4GenJetsNoNu'
# pfCandidates = 'particleFlow'
pfCandidates = 'hltParticleFlow'
# pvSource = 'offlinePrimaryVertices'
pvSource = hltVertices
# svSource = 'inclusiveCandidateSecondaryVertices'
svSource = 'hltDeepInclusiveMergedVerticesPF'
# muSource = 'muons'
# elSource = 'gedGsfElectrons'
# patMuons = 'selectedPatMuons'
# trackSource = 'generalTracks'
trackSource = tracks
# if not options.runJetClustering:
#     jetSource = ('ak4PFJetsCHS' if options.usePFchs else 'ak4PFJets')



from RecoBTag.PerformanceMeasurements.Configs.HLT_dev_CMSSW_11_2_0_GRun_V19_configDump import cms, process
###
### customizations
###
from JMETriggerAnalysis.Common.customise_hlt import *
# process = addPaths_MC_PFClusterJME(process)
process = addPaths_MC_PFPuppiJME(process)
from RecoBTag.PerformanceMeasurements.PATLikeConfig import customizePFPatLikeJets
process = customizePFPatLikeJets(process)


# remove cms.OutputModule objects from HLT config-dump
for _modname in process.outputModules_():
    _mod = getattr(process, _modname)
    if type(_mod) == cms.OutputModule:
       process.__delattr__(_modname)
       # if opts.verbosity > 0:
       #    print '> removed cms.OutputModule:', _modname

# remove cms.EndPath objects from HLT config-dump
for _modname in process.endpaths_():
    _mod = getattr(process, _modname)
    if type(_mod) == cms.EndPath:
       process.__delattr__(_modname)
       # if opts.verbosity > 0:
       #    print '> removed cms.EndPath:', _modname

# remove selected cms.Path objects from HLT config-dump
print '-'*108
print '{:<99} | {:<4} |'.format('cms.Path', 'keep')
print '-'*108
for _modname in sorted(process.paths_()):
    _keepPath = _modname.startswith('MC_') and ('Jets' in _modname or 'MET' in _modname or 'DeepCSV' in _modname)
#    _keepPath |= _modname.startswith('MC_ReducedIterativeTracking')
    if _keepPath:
      print '{:<99} | {:<4} |'.format(_modname, '+')
      continue
    _mod = getattr(process, _modname)
    if type(_mod) == cms.Path:
      process.__delattr__(_modname)
      print '{:<99} | {:<4} |'.format(_modname, '')
print '-'*108

# remove FastTimerService
del process.FastTimerService

# remove MessageLogger
del process.MessageLogger
# if not options.eras:
# 	process = cms.Process("BTagAna")
# else:
# 	from Configuration.StandardSequences.Eras import eras
# 	eras_to_use = []
# 	for era in options.eras:
# 		if hasattr(eras, era):
# 			eras_to_use.append(getattr(eras, era))
# 		else:
# 			raise ValueError('The requested era (%s) is not available' % era)
# 	process = cms.Process("BTagAna", *eras_to_use)


## MessageLogger
# process.load("FWCore.MessageLogger.MessageLogger_cfi")
# If you run over many samples and you save the log, remember to reduce
# the size of the output by prescaling the report of the event number
# process.MessageLogger.cerr.FwkReport.reportEvery = options.reportEvery
# process.MessageLogger.cerr.default.limit = 10

## Input files
# process.source = cms.Source("PoolSource",
#     fileNames = cms.untracked.vstring()
# )
#
# process.source.fileNames = [
#     '/store/mc/PhaseIFall16DR/TT_TuneCUETP8M2T4_13TeV-powheg-pythia8/AODSIM/PhaseIFall16PUFlat20to50_81X_upgrade2017_realistic_v26-v1/50000/0039E945-35E3-E611-AF8D-001E675A6C2A.root'
# ]
# if options.runOnData:
#     process.source.fileNames = [
#         '/store/data/Run2016B/SingleMuon/AOD/PromptReco-v2/000/275/125/00000/DA2EC189-7E36-E611-8C63-02163E01343B.root'
#     ]
# if options.inputFiles:
#     process.source.fileNames = options.inputFiles

## Define the output file name
if options.runOnData :
    options.outFilename += '_data'
else :
    options.outFilename += '_mc'

options.outFilename += '.root'

## Output file
process.TFileService = cms.Service("TFileService",
   fileName = cms.string(options.outFilename)
)

## Events to process
process.source.skipEvents = cms.untracked.uint32(options.skipEvents)
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(options.maxEvents) )

## Options and Output Report
process.options   = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(options.wantSummary),
    # allowUnscheduled = cms.untracked.bool(True)
)

#Set GT by hand:
# process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
# from Configuration.AlCa.GlobalTag import GlobalTag
# process.GlobalTag.globaltag = globalTag
#Choose automatically:
#process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
#from Configuration.AlCa.GlobalTag import GlobalTag
#process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_' + ('data' if options.runOnData else 'mc'))

#Loading calibrations from db file, example of code for any future use
#process.load("CondCore.DBCommon.CondDBSetup_cfi")
#process.BTauMVAJetTagComputerRecord = cms.ESSource("PoolDBESSource",
#    process.CondDBSetup,
#    timetype = cms.string('runnumber'),
#    toGet = cms.VPSet(
#        cms.PSet(
#            record = cms.string('BTauGenericMVAJetTagComputerRcd'),
#            tag = cms.string('MVAJetTags')
#        )
#    ),
#    connect = cms.string('sqlite_fip:RecoBTag/PerformanceMeasurements/data/MVAJetTags.db'),
#    BlobStreamerName = cms.untracked.string('TBufferBlobStreamingService')
#)
#process.es_prefer_BTauMVAJetTagComputerRecord = cms.ESPrefer("PoolDBESSource","BTauMVAJetTagComputerRecord")

# if options.usePrivateJEC:
#
#     from CondCore.DBCommon.CondDBSetup_cfi import *
#     import os
#     dbfile=''
#     if options.runOnData: dbfile=options.jecDBFileData
#     else: dbfile=options.jecDBFileMC
#     print "\nUsing private SQLite file", dbfile, "\n"
#     process.jec = cms.ESSource("PoolDBESSource",CondDBSetup,
# 		    connect = cms.string( "sqlite_fip:RecoBTag/PerformanceMeasurements/data/"+dbfile+'.db'),
# 		    toGet =  cms.VPSet(
# 			    cms.PSet(
# 				    record = cms.string("JetCorrectionsRecord"),
# 				    tag = cms.string("JetCorrectorParametersCollection_"+dbfile+"_AK4PF"),
# 				    label= cms.untracked.string("AK4PF")
# 				    ),
# 			    cms.PSet(
# 				    record = cms.string("JetCorrectionsRecord"),
# 				    tag = cms.string("JetCorrectorParametersCollection_"+dbfile+"_AK4PFchs"),
# 				    label= cms.untracked.string("AK4PFchs")
# 				    ),
# 			    cms.PSet(
# 				    record = cms.string("JetCorrectionsRecord"),
# 				    tag = cms.string("JetCorrectorParametersCollection_"+dbfile+"_AK4PFPuppi"),
# 				    label= cms.untracked.string("AK4PFPuppi")
# 				    ),
# 			    cms.PSet(
# 				    record = cms.string("JetCorrectionsRecord"),
# 				    tag = cms.string("JetCorrectorParametersCollection_"+dbfile+"_AK8PF"),
# 				    label= cms.untracked.string("AK8PF")
# 				    ),
# 			    cms.PSet(
# 				    record = cms.string("JetCorrectionsRecord"),
# 				    tag = cms.string("JetCorrectorParametersCollection_"+dbfile+"_AK8PFchs"),
# 				    label= cms.untracked.string("AK8PFchs")
# 				    ),
# 			    cms.PSet(
# 				    record = cms.string("JetCorrectionsRecord"),
# 				    tag = cms.string("JetCorrectorParametersCollection_"+dbfile+"_AK8PFPuppi"),
# 				    label= cms.untracked.string("AK8PFPuppi")
# 				    ),
# 			    )
# 		    )
#
#     process.es_prefer_jec = cms.ESPrefer("PoolDBESSource",'jec')

### to activate the new JP calibration: using the data base
# trkProbaCalibTag = options.JPCalibration
# process.GlobalTag.toGet = cms.VPSet(
#     cms.PSet(record = cms.string("BTagTrackProbability3DRcd"),
#       tag = cms.string(trkProbaCalibTag),
#       connect = cms.string("frontier://FrontierProd/CMS_CONDITIONS")
#     )
# )

# process.load("Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff")
# process.load("Configuration.Geometry.GeometryRecoDB_cff")
# process.load("SimGeneral.HepPDTESSource.pythiapdt_cfi")

#-------------------------------------
## Output Module Configuration (expects a path 'p')
# from PhysicsTools.PatAlgos.patEventContent_cff import patEventContent
process.out = cms.OutputModule("PoolOutputModule",
    fileName = cms.untracked.string(options.outFilename),
    # save only events passing the full path
    SelectEvents   = cms.untracked.PSet( SelectEvents = cms.vstring('p') ),
    # save PAT Layer 1 output; you need a '*' to
    # unpack the list of commands 'patEventContent'
    # outputCommands = cms.untracked.vstring('drop *', *patEventContent)
)

#-------------------------------------
## PAT Configuration
# jetAlgo="AK4"

# from PhysicsTools.PatAlgos.tools.pfTools import *
# usePF2PAT(process,runPF2PAT=True, jetAlgo=jetAlgo, runOnMC=not options.runOnData, postfix=postfix,
#           jetCorrections=jetCorrectionsAK4, pvCollection=cms.InputTag(pvSource))

## Top projections in PF2PAT
# getattr(process,"pfPileUpJME"+postfix).checkClosestZVertex = False
# getattr(process,"pfNoPileUpJME"+postfix).enable = options.usePFchs
# getattr(process,"pfNoMuonJMEPFBRECO"+postfix).enable = False
# getattr(process,"pfNoElectronJMEPFBRECO"+postfix).enable = False

if options.usePuppi:
    # process.load('CommonTools.PileupAlgos.Puppi_cff')
    # if options.usePuppi:
        # from RecoJets.JetProducers.ak4PFJets_cfi import ak4PFJets
        # _pfJets = ak4PFJets.clone(src = cms.InputTag('puppi'), doAreaFastjet = True, srcPVs = cms.InputTag(pvSource))
        # setattr(process,'pfJetsPFBRECO'+postfix,_pfJets)
    if options.usePuppiForBTagging: pfCandidates = 'puppi'

## Load standard PAT objects (here we only need PAT muons but the framework will figure out what it needs to run using the unscheduled mode)
# process.load("PhysicsTools.PatAlgos.producersLayer1.patCandidates_cff")
# process.load("PhysicsTools.PatAlgos.selectionLayer1.selectedPatCandidates_cff")

# from PhysicsTools.PatAlgos.tools.jetTools import *
## Updated the default jet collection
# updateJetCollection(
#     process,
#     jetSource = cms.InputTag(jetSource),
#     jetCorrections = jetCorrectionsAK4,
#     pfCandidates = cms.InputTag(pfCandidates),
#     pvSource = cms.InputTag(pvSource),
#     svSource = cms.InputTag(svSource),
#     muSource = cms.InputTag(muSource),
#     elSource = cms.InputTag(elSource),
#     btagInfos = bTagInfos,
#     btagDiscriminators = list(bTagDiscriminators),
#     explicitJTA = options.useExplicitJTA,
#     postfix = postfix
# )



#-------------------------------------
# if options.runOnData:
#     # Remove MC matching when running over data
#     from PhysicsTools.PatAlgos.tools.coreTools import removeMCMatching
#     removeMCMatching( process, ['Photons', 'Electrons','Muons', 'Taus', 'Jets', 'METs', 'PFElectrons','PFMuons', 'PFTaus'] )

#-------------------------------------
## Add GenParticlePruner for boosted b-tagging studies
if not options.runOnData:
    process.prunedGenParticlesBoost = cms.EDProducer('GenParticlePruner',
        src = cms.InputTag(genParticles),
        select = cms.vstring(
            "drop  *  ", #by default
            "keep ( status = 3 || (status>=21 && status<=29) ) && pt > 0", #keep hard process particles with non-zero pT
            "keep abs(pdgId) = 13 || abs(pdgId) = 15" #keep muons and taus
        )
    )

#-------------------------------------

## Filter for removing scraping events
process.noscraping = cms.EDFilter("FilterOutScraping",
    applyfilter = cms.untracked.bool(True),
    debugOn = cms.untracked.bool(False),
    numtrack = cms.untracked.uint32(10),
    thresh = cms.untracked.double(0.25)
)

## Filter for good primary vertex
# process.primaryVertexFilter = cms.EDFilter("GoodVertexFilter",
#     vertexCollection = cms.InputTag(pvSource),
#     minimumNDOF = cms.uint32(4) ,
#     maxAbsZ = cms.double(24),
#     maxd0 = cms.double(2)
# )
#-------------------------------------

#-------------------------------------
if options.useTTbarFilter:
    process.load("RecoBTag.PerformanceMeasurements.TTbarSelectionFilter_cfi")
    process.load("RecoBTag.PerformanceMeasurements.TTbarSelectionProducer_cfi")

    if options.isReHLT and not options.runOnData:
        process.ttbarselectionproducer.triggerColl =  cms.InputTag("TriggerResults","","HLT2")

    #electron id
    from PhysicsTools.SelectorUtils.tools.vid_id_tools import *

    process.ttbarselectionproducer.electronColl = cms.InputTag('selectedPatElectrons'+postfix)
    process.ttbarselectionproducer.muonColl     = cms.InputTag('selectedPatMuons'+postfix)
    process.ttbarselectionproducer.jetColl      = cms.InputTag(patJetSource)
    process.ttbarselectionproducer.metColl      = cms.InputTag('patMETs'+postfix)
    switchOnVIDElectronIdProducer(process, DataFormat.AOD)

    # Set up electron ID (VID framework)
    from PhysicsTools.SelectorUtils.tools.vid_id_tools import *
    switchOnVIDElectronIdProducer(process, dataFormat=DataFormat.MiniAOD)
    my_id_modules = ['RecoEgamma.ElectronIdentification.Identification.cutBasedElectronID_Fall17_94X_V2_cff']
    for idmod in my_id_modules:
        setupAllVIDIdsInModule(process,idmod,setupVIDElectronSelection)



    #process.ttbarselectionproducer.isData       = options.runOnData
    #process.ttbarselectionproducer.electronColl = cms.InputTag('selectedPatElectrons'+postfix)
    #process.ttbarselectionproducer.muonColl     = cms.InputTag('selectedPatMuons'+postfix)
    #process.ttbarselectionproducer.jetColl      = cms.InputTag(patJetSource)
    #process.ttbarselectionproducer.metColl      = cms.InputTag('patMETs'+postfix)
    #process.ttbarselectionfilter.select_ee   = True
    #process.ttbarselectionfilter.select_mumu = True
    #process.ttbarselectionfilter.select_emu  = True
    #process.ttbarselectionfilter.Keep_all_events  = False

    ## Change the cone size of muon isolation to 0.3
    #getattr(process,"pfIsolatedMuons"+postfix).isolationValueMapsCharged = cms.VInputTag( cms.InputTag( 'muPFIsoValueCharged03'+postfix ) )
    #getattr(process,"pfIsolatedMuons"+postfix).isolationValueMapsNeutral = cms.VInputTag( cms.InputTag( 'muPFIsoValueNeutral03'+postfix ), cms.InputTag( 'muPFIsoValueGamma03'+postfix ) )
    #getattr(process,"pfIsolatedMuons"+postfix).deltaBetaIsolationValueMap = cms.InputTag( 'muPFIsoValuePU03'+postfix )
    #getattr(process,"pfIsolatedMuons"+postfix).combinedIsolationCut = cms.double(9999.)
    #getattr(process,"pfIsolatedMuons"+postfix).isolationCut = cms.double(9999.)

    #getattr(process,"patMuons"+postfix).isolationValues = cms.PSet(
    #    pfNeutralHadrons = cms.InputTag('muPFIsoValueNeutral03'+postfix),
    #    pfPhotons = cms.InputTag('muPFIsoValueGamma03'+postfix),
    #    pfChargedHadrons = cms.InputTag('muPFIsoValueCharged03'+postfix),
    #    pfChargedAll = cms.InputTag('muPFIsoValueChargedAll03'+postfix),
    #    pfPUChargedHadrons = cms.InputTag('muPFIsoValuePU03'+postfix)
    #)

    ## Change the cone size of electron isolation to 0.3
    #getattr(process,'pfElectrons'+postfix).isolationValueMapsCharged  = cms.VInputTag(cms.InputTag('elPFIsoValueCharged03PFId'+postfix))
    #getattr(process,'pfElectrons'+postfix).deltaBetaIsolationValueMap = cms.InputTag('elPFIsoValuePU03PFId'+postfix)
    #getattr(process,'pfElectrons'+postfix).isolationValueMapsNeutral  = cms.VInputTag(cms.InputTag('elPFIsoValueNeutral03PFId'+postfix), cms.InputTag('elPFIsoValueGamma03PFId'+postfix))

    #getattr(process,'pfIsolatedElectrons'+postfix).isolationValueMapsCharged = cms.VInputTag(cms.InputTag('elPFIsoValueCharged03PFId'+postfix))
    #getattr(process,'pfIsolatedElectrons'+postfix).deltaBetaIsolationValueMap = cms.InputTag('elPFIsoValuePU03PFId'+postfix)
    #getattr(process,'pfIsolatedElectrons'+postfix).isolationValueMapsNeutral = cms.VInputTag(cms.InputTag('elPFIsoValueNeutral03PFId'+postfix), cms.InputTag('elPFIsoValueGamma03PFId'+postfix))
    #getattr(process,'pfIsolatedElectrons'+postfix).combinedIsolationCut = cms.double(9999.)
    #getattr(process,'pfIsolatedElectrons'+postfix).isolationCut = cms.double(9999.)

    ## Electron ID
    #process.load("EGamma.EGammaAnalysisTools.electronIdMVAProducer_cfi")
    #process.eidMVASequence = cms.Sequence( process.mvaTrigV0 + process.mvaNonTrigV0 )

    #getattr(process,'patElectrons'+postfix).electronIDSources.mvaTrigV0    = cms.InputTag("mvaTrigV0")
    #getattr(process,'patElectrons'+postfix).electronIDSources.mvaNonTrigV0 = cms.InputTag("mvaNonTrigV0")
    #getattr(process,'patElectrons'+postfix).isolationValues = cms.PSet(
    #    pfChargedHadrons = cms.InputTag('elPFIsoValueCharged03PFId'+postfix),
    #    pfChargedAll = cms.InputTag('elPFIsoValueChargedAll03PFId'+postfix),
    #    pfPUChargedHadrons = cms.InputTag('elPFIsoValuePU03PFId'+postfix),
    #    pfNeutralHadrons = cms.InputTag('elPFIsoValueNeutral03PFId'+postfix),
    #    pfPhotons = cms.InputTag('elPFIsoValueGamma03PFId'+postfix)
    #)

    ## Conversion rejection
    ## This should be your last selected electron collection name since currently index is used to match with electron later. We can fix this using reference pointer.
    #setattr(process,'patConversions'+postfix) = cms.EDProducer("PATConversionProducer",
        #electronSource = cms.InputTag('selectedPatElectrons'+postfix)
    #)

#-------------------------------------
## Change the minimum number of tracker hits used in the track selection
if options.changeMinNumberOfHits:
    for m in process.producerNames().split(' '):
        if m.startswith('pfImpactParameterTagInfos'):
            print "Changing 'minimumNumberOfHits' for " + m + " to " + str(options.minNumberOfHits)
            getattr(process, m).minimumNumberOfHits = cms.int32(options.minNumberOfHits)

# from PhysicsTools.PatAlgos.tools.pfTools import *
## Adapt primary vertex collection
# adaptPVs(process, pvCollection=cms.InputTag(pvSource))

#-------------------------------------
## Add TagInfos to PAT jets
# for i in ['patJets','updatedPatJetsTransientCorrected']:
#     m = i + postfix
#     if hasattr(process,m) and getattr( getattr(process,m), 'addBTagInfo' ):
#         print "Switching 'addTagInfos' for " + m + " to 'True'"
#         setattr( getattr(process,m), 'addTagInfos', cms.bool(True) )

#-------------------------------------
process.btagana = HLTBTagAnalyzer.clone()
# The following combinations should be considered:
# For b-tagging performance measurements:
#   process.btagana.useTrackHistory      = False (or True for Mistag systematics with GEN-SIM-RECODEBUG samples)
#   options.produceJetTrackTree  = False
#   process.btagana.produceAllTrackTree  = False
# or data/MC validation of jets, tracks and SVs:
#   process.btagana.useTrackHistory      = False
#   options.produceJetTrackTree  = True
#   process.btagana.produceAllTrackTree  = False
# or general tracks, PV and jet performance studies:
#   process.btagana.useTrackHistory      = False
#   options.produceJetTrackTree  = False
#   process.btagana.produceAllTrackTree  = True
#------------------
#Handle groups
for requiredGroup in process.btagana.groups:
   for storedGroup in btagana_tmp.groups:
     if (requiredGroup.group == storedGroup.group):
       requiredGroup.store = storedGroup.store

process.btagana.MaxEta                = options.maxJetEta ## for extended forward pixel coverage
process.btagana.MinPt                 = options.minJetPt
process.btagana.tracksColl            = cms.InputTag(trackSource)
process.btagana.useTrackHistory       = options.useTrackHistory ## Can only be used with GEN-SIM-RECODEBUG files
process.btagana.produceJetTrackTruthTree = options.useTrackHistory ## can only be used with GEN-SIM-RECODEBUG files and when useTrackHistory is True
process.btagana.produceAllTrackTree   = options.produceAllTrackTree ## True if you want to run info for all tracks : for commissioning studies
#------------------
process.btagana.runTagVariables     = options.runTagVariables  ## True if you want to run TagInfo TaggingVariables
process.btagana.runCSVTagVariables  = options.runCSVTagVariables   ## True if you want to run CSV TaggingVariables
process.btagana.runCSVTagTrackVariables  = options.runCSVTagTrackVariables   ## True if you want to run CSV Tagging Track Variables
process.btagana.runDeepFlavourTagVariables = options.runDeepFlavourTagVariables
process.btagana.primaryVertexColl     = cms.InputTag(pvSource)
process.btagana.Jets                  = cms.InputTag(patJetSource)
# process.btagana.muonCollectionName    = cms.InputTag(muSource)
# process.btagana.patMuonCollectionName = cms.InputTag(patMuons)
process.btagana.use_ttbar_filter      = cms.bool(options.useTTbarFilter)
process.btagana.rho                   = cms.InputTag(rho)
process.btagana.deepFlavourJetTags            = PFDeepFlavourTags
#process.btagana.triggerTable          = cms.InputTag('TriggerResults::HLT') # Data and MC
process.btagana.triggerTable          = cms.InputTag(trigresults) # Data and MC
process.btagana.genParticles          = cms.InputTag(genParticles)
process.btagana.candidates            = cms.InputTag(pfCandidates)
process.btagana.runJetVariables     = options.runJetVariables
process.btagana.runQuarkVariables   = options.runQuarkVariables
process.btagana.runHadronVariables  = options.runHadronVariables
process.btagana.runGenVariables     = options.runGenVariables
# process.btagana.runPFElectronVariables = options.runPFElectronVariables
# process.btagana.runPFMuonVariables = options.runPFMuonVariables
# process.btagana.runPatMuons = options.runPatMuons
process.btagana.runEventInfo = options.runEventInfo
process.btagana.runOnData = options.runOnData

if options.runOnData:
  process.btagana.runHadronVariables  = False
  process.btagana.runQuarkVariables   = False
  process.btagana.runGenVariables     = False

if not process.btagana.useTrackHistory  or not options.produceJetTrackTree:
    process.btagana.produceJetTrackTruthTree = False

if process.btagana.useTrackHistory:
    process.load('SimTracker.TrackAssociatorProducers.quickTrackAssociatorByHits_cfi')
    process.load('SimTracker.TrackerHitAssociation.tpClusterProducer_cfi')

if process.btagana.produceJetTrackTruthTree:
    process.load("SimTracker.TrackerHitAssociation.tpClusterProducer_cfi")
    process.load("SimTracker.TrackHistory.TrackHistory_cff")
    process.load("SimTracker.TrackHistory.TrackClassifier_cff")
    process.load("SimTracker.TrackAssociatorProducers.quickTrackAssociatorByHits_cfi")
    process.load("SimTracker.TrackAssociation.trackingParticleRecoTrackAsssociation_cfi")

#---------------------------------------
process.options.numberOfThreads = cms.untracked.uint32(1)
process.options.numberOfStreams = cms.untracked.uint32(1)
#---------------------------------------
## Trigger selection !
#import HLTrigger.HLTfilters.triggerResultsFilter_cfi as hlt
#process.JetHLTFilter = hlt.triggerResultsFilter.clone(
#    triggerConditions = cms.vstring(
#        "HLT_PFJet80_v*"
#    ),
#    hltResults = cms.InputTag("TriggerResults","","HLT"),
#    l1tResults = cms.InputTag( "" ),
#    throw = cms.bool( False ) #set to false to deal with missing triggers while running over different trigger menus
#)
#---------------------------------------

#---------------------------------------
## Optional MET filters:
## https://twiki.cern.ch/twiki/bin/view/CMS/MissingETOptionalFilters
#process.load("RecoMET.METFilters.metFilters_cff")
#process.trackingFailureFilter.VertexSource = cms.InputTag('goodOfflinePrimaryVertices')
#---------------------------------------

#---------------------------------------
## Event counter
from RecoBTag.PerformanceMeasurements.eventcounter_cfi import eventCounter
process.allEvents = eventCounter.clone()
process.selectedEvents = eventCounter.clone()
#---------------------------------------

#---------------------------------------
## Define event filter sequence
# process.filtSeq = cms.Sequence(
#     #process.JetHLTFilter*
#     #process.noscraping
#     process.primaryVertexFilter
# )


## Define analyzer sequence
process.analyzerSeq = cms.Sequence( )
# if options.processStdAK4Jets:
process.analyzerSeq += process.btagana
# if options.processStdAK4Jets and options.useTTbarFilter:
#     process.analyzerSeq.replace( process.btagana, process.ttbarselectionproducer * process.ttbarselectionfilter * process.btagana )
#---------------------------------------

#Trick to make it work in 9_1_X
# process.tsk = cms.Task()
# for mod in process.producers_().itervalues():
#     process.tsk.add(mod)
# for mod in process.filters_().itervalues():
#     process.tsk.add(mod)



process.p = cms.Path(
    # process.jetMatchingPath
    process.allEvents
    # * process.filtSeq
    * process.selectedEvents
    * process.analyzerSeq
    # process.tsk
)

# Delete predefined output module (needed for running with CRAB)
del process.out

open('pydump.py','w').write(process.dumpPython())
