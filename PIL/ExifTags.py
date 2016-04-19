#
# The Python Imaging Library.
# $Id$
#
# EXIF tags
#
# Copyright (c) 2003 by Secret Labs AB
#
# See the README file for information on usage and redistribution.
#

##
# This module provides constants and clear-text names for various
# well-known EXIF tags.
##

##
# Maps EXIF tags to tag names.

TAGS = {

    # possibly incomplete
    0x000b: "ProcessingSoftware",
    0x00fe: "NewSubfileType",
    0x00ff: "SubfileType",
    0x0100: "ImageWidth",
    0x0101: "ImageLength",
    0x0102: "BitsPerSample",
    0x0103: "Compression",
    0x0106: "PhotometricInterpretation",
    0x0107: "Thresholding",
    0x0108: "CellWidth",
    0x0109: "CellLength",
    0x010a: "FillOrder",
    0x010d: "DocumentName",
    0x011d: "PageName",
    0x010e: "ImageDescription",
    0x010f: "Make",
    0x0110: "Model",
    0x0111: "StripOffsets",
    0x0112: "Orientation",
    0x0115: "SamplesPerPixel",
    0x0116: "RowsPerStrip",
    0x0117: "StripByteCounts",
    0x0118: "MinSampleValue",
    0x0119: "MaxSampleValue",
    0x011a: "XResolution",
    0x011b: "YResolution",
    0x011c: "PlanarConfiguration",
    0x0120: "FreeOffsets",
    0x0121: "FreeByteCounts",
    0x0122: "GrayResponseUnit",
    0x0123: "GrayResponseCurve",
    0x0124: "T4Options",
    0x0125: "T6Options",
    0x0128: "ResolutionUnit",
    0x0129: "PageNumber",
    0x012d: "TransferFunction",
    0x0131: "Software",
    0x0132: "DateTime",
    0x013b: "Artist",
    0x013c: "HostComputer",
    0x013d: "Predictor",
    0x013e: "WhitePoint",
    0x013f: "PrimaryChromaticities",
    0x0140: "ColorMap",
    0x0141: "HalftoneHints",
    0x0142: "TileWidth",
    0x0143: "TileLength",
    0x0144: "TileOffsets",
    0x0145: "TileByteCounts",
    0x014a: "SubIFDs",
    0x014c: "InkSet",
    0x014d: "InkNames",
    0x014e: "NumberOfInks",
    0x0150: "DotRange",
    0x0151: "TargetPrinter",
    0x0152: "ExtraSamples",
    0x0153: "SampleFormat",
    0x0154: "SMinSampleValue",
    0x0155: "SMaxSampleValue",
    0x0156: "TransferRange",
    0x0157: "ClipPath",
    0x0158: "XClipPathUnits",
    0x0159: "YClipPathUnits",
    0x015a: "Indexed",
    0x015b: "JPEGTables",
    0x015f: "OPIProxy",
    0x0200: "JPEGProc",
    0x0201: "JpegIFOffset",
    0x0202: "JpegIFByteCount",
    0x0203: "JpegRestartInterval",
    0x0205: "JpegLosslessPredictors",
    0x0206: "JpegPointTransforms",
    0x0207: "JpegQTables",
    0x0208: "JpegDCTables",
    0x0209: "JpegACTables",
    0x0211: "YCbCrCoefficients",
    0x0212: "YCbCrSubSampling",
    0x0213: "YCbCrPositioning",
    0x0214: "ReferenceBlackWhite",
    0x02bc: "XMLPacket",
    0x1000: "RelatedImageFileFormat",
    0x1001: "RelatedImageWidth",
    0x1002: "RelatedImageLength",
    0x4746: "Rating",
    0x4749: "RatingPercent",
    0x800d: "ImageID",
    0x828d: "CFARepeatPatternDim",
    0x828e: "CFAPattern",
    0x828f: "BatteryLevel",
    0x8298: "Copyright",
    0x829a: "ExposureTime",
    0x829d: "FNumber",
    0x83bb: "IPTCNAA",
    0x8649: "ImageResources",
    0x8769: "ExifOffset",
    0x8773: "InterColorProfile",
    0x8822: "ExposureProgram",
    0x8824: "SpectralSensitivity",
    0x8825: "GPSInfo",
    0x8827: "ISOSpeedRatings",
    0x8828: "OECF",
    0x8829: "Interlace",
    0x882a: "TimeZoneOffset",
    0x882b: "SelfTimerMode",
    0x9000: "ExifVersion",
    0x9003: "DateTimeOriginal",
    0x9004: "DateTimeDigitized",
    0x9101: "ComponentsConfiguration",
    0x9102: "CompressedBitsPerPixel",
    0x9201: "ShutterSpeedValue",
    0x9202: "ApertureValue",
    0x9203: "BrightnessValue",
    0x9204: "ExposureBiasValue",
    0x9205: "MaxApertureValue",
    0x9206: "SubjectDistance",
    0x9207: "MeteringMode",
    0x9208: "LightSource",
    0x9209: "Flash",
    0x920a: "FocalLength",
    0x920b: "FlashEnergy",
    0x920c: "SpatialFrequencyResponse",
    0x920d: "Noise",
    0x9211: "ImageNumber",
    0x9212: "SecurityClassification",
    0x9213: "ImageHistory",
    0x9214: "SubjectLocation",
    0x9215: "ExposureIndex",
    0x9216: "TIFF/EPStandardID",
    0x927c: "MakerNote",
    0x9286: "UserComment",
    0x9290: "SubsecTime",
    0x9291: "SubsecTimeOriginal",
    0x9292: "SubsecTimeDigitized",
    0x9c9b: "XPTitle",
    0x9c9c: "XPComment",
    0x9c9d: "XPAuthor",
    0x9c9e: "XPKeywords",
    0x9c9f: "XPSubject",
    0xa000: "FlashPixVersion",
    0xa001: "ColorSpace",
    0xa002: "ExifImageWidth",
    0xa003: "ExifImageHeight",
    0xa004: "RelatedSoundFile",
    0xa005: "ExifInteroperabilityOffset",
    0xa20b: "FlashEnergy",
    0xa20c: "SpatialFrequencyResponse",
    0xa20e: "FocalPlaneXResolution",
    0xa20f: "FocalPlaneYResolution",
    0xa210: "FocalPlaneResolutionUnit",
    0xa214: "SubjectLocation",
    0xa215: "ExposureIndex",
    0xa217: "SensingMethod",
    0xa300: "FileSource",
    0xa301: "SceneType",
    0xa302: "CFAPattern",
    0xa401: "CustomRendered",
    0xa402: "ExposureMode",
    0xa403: "WhiteBalance",
    0xa404: "DigitalZoomRatio",
    0xa405: "FocalLengthIn35mmFilm",
    0xa406: "SceneCaptureType",
    0xa407: "GainControl",
    0xa408: "Contrast",
    0xa409: "Saturation",
    0xa40a: "Sharpness",
    0xa40b: "DeviceSettingDescription",
    0xa40c: "SubjectDistanceRange",
    0xa420: "ImageUniqueID",
    0xa430: "CameraOwnerName",
    0xa431: "BodySerialNumber",
    0xa432: "LensSpecification",
    0xa433: "LensMake",
    0xa434: "LensModel",
    0xa435: "LensSerialNumber",
    0xa500: "Gamma",
    0xc4a5: "PrintImageMatching",
    0xc612: "DNGVersion",
    0xc613: "DNGBackwardVersion",
    0xc614: "UniqueCameraModel",
    0xc615: "LocalizedCameraModel",
    0xc616: "CFAPlaneColor",
    0xc617: "CFALayout",
    0xc618: "LinearizationTable",
    0xc619: "BlackLevelRepeatDim",
    0xc61a: "BlackLevel",
    0xc61b: "BlackLevelDeltaH",
    0xc61c: "BlackLevelDeltaV",
    0xc61d: "WhiteLevel",
    0xc61e: "DefaultScale",
    0xc61f: "DefaultCropOrigin",
    0xc620: "DefaultCropSize",
    0xc621: "ColorMatrix1",
    0xc622: "ColorMatrix2",
    0xc623: "CameraCalibration1",
    0xc624: "CameraCalibration2",
    0xc625: "ReductionMatrix1",
    0xc626: "ReductionMatrix2",
    0xc627: "AnalogBalance",
    0xc628: "AsShotNeutral",
    0xc629: "AsShotWhiteXY",
    0xc62a: "BaselineExposure",
    0xc62b: "BaselineNoise",
    0xc62c: "BaselineSharpness",
    0xc62d: "BayerGreenSplit",
    0xc62e: "LinearResponseLimit",
    0xc62f: "CameraSerialNumber",
    0xc630: "LensInfo",
    0xc631: "ChromaBlurRadius",
    0xc632: "AntiAliasStrength",
    0xc633: "ShadowScale",
    0xc634: "DNGPrivateData",
    0xc635: "MakerNoteSafety",
    0xc65a: "CalibrationIlluminant1",
    0xc65b: "CalibrationIlluminant2",
    0xc65c: "BestQualityScale",
    0xc65d: "RawDataUniqueID",
    0xc68b: "OriginalRawFileName",
    0xc68c: "OriginalRawFileData",
    0xc68d: "ActiveArea",
    0xc68e: "MaskedAreas",
    0xc68f: "AsShotICCProfile",
    0xc690: "AsShotPreProfileMatrix",
    0xc691: "CurrentICCProfile",
    0xc692: "CurrentPreProfileMatrix",
    0xc6bf: "ColorimetricReference",
    0xc6f3: "CameraCalibrationSignature",
    0xc6f4: "ProfileCalibrationSignature",
    0xc6f6: "AsShotProfileName",
    0xc6f7: "NoiseReductionApplied",
    0xc6f8: "ProfileName",
    0xc6f9: "ProfileHueSatMapDims",
    0xc6fa: "ProfileHueSatMapData1",
    0xc6fb: "ProfileHueSatMapData2",
    0xc6fc: "ProfileToneCurve",
    0xc6fd: "ProfileEmbedPolicy",
    0xc6fe: "ProfileCopyright",
    0xc714: "ForwardMatrix1",
    0xc715: "ForwardMatrix2",
    0xc716: "PreviewApplicationName",
    0xc717: "PreviewApplicationVersion",
    0xc718: "PreviewSettingsName",
    0xc719: "PreviewSettingsDigest",
    0xc71a: "PreviewColorSpace",
    0xc71b: "PreviewDateTime",
    0xc71c: "RawImageDigest",
    0xc71d: "OriginalRawFileDigest",
    0xc71e: "SubTileBlockSize",
    0xc71f: "RowInterleaveFactor",
    0xc725: "ProfileLookTableDims",
    0xc726: "ProfileLookTableData",
    0xc740: "OpcodeList1",
    0xc741: "OpcodeList2",
    0xc74e: "OpcodeList3",
    0xc761: "NoiseProfile"
}

##
# Maps EXIF GPS tags to tag names.

GPSTAGS = {
    0: "GPSVersionID",
    1: "GPSLatitudeRef",
    2: "GPSLatitude",
    3: "GPSLongitudeRef",
    4: "GPSLongitude",
    5: "GPSAltitudeRef",
    6: "GPSAltitude",
    7: "GPSTimeStamp",
    8: "GPSSatellites",
    9: "GPSStatus",
    10: "GPSMeasureMode",
    11: "GPSDOP",
    12: "GPSSpeedRef",
    13: "GPSSpeed",
    14: "GPSTrackRef",
    15: "GPSTrack",
    16: "GPSImgDirectionRef",
    17: "GPSImgDirection",
    18: "GPSMapDatum",
    19: "GPSDestLatitudeRef",
    20: "GPSDestLatitude",
    21: "GPSDestLongitudeRef",
    22: "GPSDestLongitude",
    23: "GPSDestBearingRef",
    24: "GPSDestBearing",
    25: "GPSDestDistanceRef",
    26: "GPSDestDistance",
    27: "GPSProcessingMethod",
    28: "GPSAreaInformation",
    29: "GPSDateStamp",
    30: "GPSDifferential",
    31: "GPSHPositioningError",
}
