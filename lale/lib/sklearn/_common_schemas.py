# Copyright 2021 IBM Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

schema_X_numbers_y_top = {
    "type": "object",
    "required": ["X"],
    "additionalProperties": False,
    "properties": {
        "X": {
            "description": "Features; the outer array is over samples.",
            "type": "array",
            "items": {"type": "array", "items": {"type": "number"}},
        },
        "y": {"description": "Target class labels (unused)."},
    },
}

schema_X_numbers = {
    "type": "object",
    "required": ["X"],
    "additionalProperties": False,
    "properties": {
        "X": {
            "type": "array",
            "items": {"type": "array", "items": {"type": "number"}},
        },
    },
}

schema_1D_cats = {
    "anyOf": [
        {"type": "array", "items": {"type": "string"}},
        {"type": "array", "items": {"type": "number"}},
        {"type": "array", "items": {"type": "boolean"}},
    ],
}

schema_1D_numbers = {"type": "array", "items": {"type": "number"}}

schema_2D_numbers = {
    "type": "array",
    "items": {"type": "array", "items": {"type": "number"}},
}

schema_sample_weight = {
    "anyOf": [
        {"type": "array", "items": {"type": "number"}},
        {"enum": [None], "description": "Uniform weights."},
    ],
    "default": None,
    "description": "Weights applied to individual samples.",
}


def schema_monotonic_cst(desc_add):
    return {
        "anyOf": [
            {
                "type": "array",
                "description": "array-like of int of shape (n_features)",
                "items": {"enum": [-1, 0, 1]},
            },
            {"enum": [None], "description": "No constraints are applied."},
        ],
        "default": None,
        "description": "Indicates the monotonicity constraint to enforce on each feature."
        + desc_add,
    }


schema_monotonic_cst_regressor = schema_monotonic_cst(
    """
Monotonicity constraints are not supported for:
multioutput regressions (i.e. when n_outputs_ > 1),

regressions trained on data with missing values."""
)

schema_monotonic_cst_classifier = schema_monotonic_cst(
    """
Monotonicity constraints are not supported for:
multioutput regressions (i.e. when n_outputs_ > 1),

regressions trained on data with missing values."""
)
