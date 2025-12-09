# config_cardiac.py
import glob
import os
from math import floor

config = {}

# ---------------- Model config ----------------
model_config = dict()
model_config["name"] = "DynUNet"
model_config["in_channels"] = 1          # 1-channel cardiac MRI
model_config["out_channels"] = 7         # 7 anatomical labels (no background)
model_config["spatial_dims"] = 3
model_config["deep_supervision"] = False

# Downsampling structure (can adjust later if you hit OOM)
model_config["strides"] = [
    [1, 1, 1],
    [2, 2, 2],
    [2, 2, 2],
    [2, 2, 2],
]
model_config["filters"] = [32, 64, 96, 128][:len(model_config["strides"])]
model_config["kernel_size"] = [[3, 3, 3]] * len(model_config["strides"])
model_config["upsample_kernel_size"] = model_config["strides"][1:]

config["model"] = model_config

# ---------------- Optimizer & loss ----------------
config["optimizer"] = {"name": "Adam", "lr": 1e-3}

config["loss"] = {
    "name": "GeneralizedDiceLoss",
    "include_background": False,   # background=0, ignore in loss
    "sigmoid": True
}

# ---------------- Scheduler ----------------
config["scheduler"] = {
    "name": "ReduceLROnPlateau",
    "patience": 10,
    "factor": 0.5,
    "min_lr": 1e-8
}

# ---------------- Dataset config ----------------
config["dataset"] = {
    "name": "SegmentationDatasetPersistent",
    "desired_shape": [256, 256, 256],   # adjust based on GPU memory
    # IMPORTANT: use your *actual* label values here:
    "labels": [205, 420, 500, 550, 600, 820, 850],
    "setup_label_hierarchy": False,
    "normalization": "NormalizeIntensityD",
    "normalization_kwargs": {"channel_wise": True, "nonzero": False},
    "resample": True,
    "crop_foreground": True,
}

# ---------------- Training setup ----------------
config["training"] = {
    "batch_size": 1,
    "validation_batch_size": 1,
    "amp": False,
    "early_stopping_patience": None,
    "n_epochs": 200,
    "save_every_n_epochs": None,
    "save_last_n_models": 3,
    "save_best": True,
}

config["cross_validation"] = {
    "folds": 5,
    "seed": 42,
}
