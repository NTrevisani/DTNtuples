# DTNtuples
Ntuples for the analysis of the CMS DT Detector Performance

## Preliminary instructions
**Note**: 
In the present days this code is evolving fast, hence the installation recipe may change often. Please keep an eye on this page to check for updates.

### Installation:

For simulation: 
```
cmsrel CMSSW_10_6_5_patch1
cd CMSSW_10_6_5_patch1/src/
cmsenv
git cms-merge-topic battibass:Phase2_DTRecoAndCalib
git cms-merge-topic -u pozzobon:DTHough_NP_20191004_106X_noL1T # MTT-CHT emulator
git cms-merge-topic -u dtp2-tpg-am:AM_106X_dev # AM emulator
git clone https://github.com/battibass/DTNtuples.git DTDPGAnalysis/DTNtuples -b newBranchPhi 
scramv1 b -j 5
```

### Ntuple prduction:
```
cd DTDPGAnalysis/DTNtuples/test/
cmsRun dtDpgNtuples_phase2_cfg.py nEvents=10000
```
