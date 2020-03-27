import os
from os import path
from pathlib import Path


def relative_to_abs_path(relative_path):
    dirname = Path(__file__).parent
    return str((dirname / relative_path).resolve())

prefix              = relative_to_abs_path('../resources/')+"/"
device_cmd_fpath    = relative_to_abs_path('../depthai.cmd')
custom_calib_fpath  = relative_to_abs_path('../resources/depthai.calib')
blob_labels_fpath   = relative_to_abs_path('../labels_fruits.txt')
blob_fpath          = relative_to_abs_path('../fruits_19R3_IRv6/frozen_inference_graph.blob')
blob_config_fpath   = relative_to_abs_path('../resources/nn/object_detection_4shave/object_detection.json')
pipeline_config_fpath = relative_to_abs_path('../resources/config.json')

if Path(custom_calib_fpath).exists():
    calib_fpath = custom_calib_fpath
    print("Using Custom Calibration File: depthai.calib")
else:
    calib_fpath = ''
    print("No calibration file. Using Calibration Defaults.")
