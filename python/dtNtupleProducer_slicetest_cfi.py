import FWCore.ParameterSet.Config as cms

dtNtupleProducer = cms.EDAnalyzer("DTNtupleProducer",
                                  ph1DtDigiTag = cms.untracked.InputTag("muonDTDigis"),
                                  ph2DtDigiTag = cms.untracked.InputTag("dtAB7unpacker"),

                                  ph1TwinMuxInTag  = cms.untracked.InputTag("none"),
                                  ph1TwinMuxOutTag = cms.untracked.InputTag("none"),
                                  ph1BmtfInTag  = cms.untracked.InputTag("none"),

                                  ph1TwinMuxInThTag = cms.untracked.InputTag("none"),
                                  ph1BmtfInThTag  = cms.untracked.InputTag("none"),

                                  ph2TPGPhiHwTag  = cms.untracked.InputTag("dtAB7unpacker"),
                                  ph2TPGPhiHbTag  = cms.untracked.InputTag("none"),
                                  ph2TPGPhiAmTag  = cms.untracked.InputTag("none"),

                                  ph1DtSegmentTag = cms.untracked.InputTag("none"),        
                                  ph2DtSegmentTag = cms.untracked.InputTag("none"),

                                  tTrigMode = cms.untracked.string('DTTTrigSyncFromDB'),
                                  tTrigModeConfig = cms.untracked.PSet(vPropWire = cms.double(24.4),
                                                                       doTOFCorrection = cms.bool(False),
                                                                       tofCorrType = cms.int32(2),
                                                                       wirePropCorrType = cms.int32(0),
                                                                       doWirePropCorrection = cms.bool(False),
                                                                       doT0Correction = cms.bool(True),
                                                                       tTrigLabel = cms.string(''),
                                                                       debug = cms.untracked.bool(False)
                                                                       ),
)

