# DTNtuples
Ntuples for the analysis of the CMS drift tubes detector performance

## Preliminary instructions
**Note**: 
In the present days this code is evolving fast, hence the installation recipe may change often. Please keep an eye on this page to check for updates.

### Installation:
```
cmsrel CMSSW_10_6_0
cd CMSSW_10_6_0/src/
cmsenv
git cms-merge-topic battibass:phase2UnpackerFromOscar_10_6_X # phase-2 primitives data format and phase-2 unpacker
git cms-merge-topic -u pozzobon:DTHough_NP_20190619_106X_noL1T # MTT-CHT emulator
git cms-merge-topic -u dtp2-tpg-am:AM_106X_dev # AM emulator
git clone https://github.com/jaimeleonh/DTNtuples.git -b MCresolutions DTDPGAnalysis/DTNtuples
scramv1 b -j 5
```

### Analysis:
```
root -b
root [0] .x loadTPGSimAnalysis.C

root [1] DTNtupleTPGSimAnalyzer analysis("DTDPGNtuple_10_6_0_SX5.root","results.root")
// or
root [1] DTNtupleTPGSimAnalyzer analysis("DTDPGNtuple_10_6_0_Phase2_Simulation.root","results.root")

root [2] analysis.Loop()
```
