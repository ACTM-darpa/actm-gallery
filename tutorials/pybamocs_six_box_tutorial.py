# -*- coding: utf-8 -*-
"""
Six-Box Model Tutorial
=============

* **ACTM Performer:** JHU-APL;
* **Author:** Chace Ashcraft (chace.ashcraft@jhuapl.edu)

PyBAMOCS Six-Box Model Tutorial


This is a tutorial for using the six-box model of the PyBAMOCS Python package. The six-box model extends the four-box
model by dividing the northern and low portions of the four-box model into Pacific and Atlantic(/Indian) portions.

The API for the six-box model is very similar to the four-box model, for which a separate tutorial may be found in
pybamocs_tutorial.py, but includes various additional parameters that may be set, as well as an
additional result variable, `M_ex`. This tutorial will follow the same format as the pybamocs_tutorial.py but updated
with the new parameters. If something seems unfamiliar or unexplained, please refer to pybamocs_tutorial.py or the
source code for additional information.

This tutorial is meant to be a tool for getting started using the PyBAMOCS package and the included `six_box_model`
functionality, and is not meant to be a comprehensive overview of all functions or capabilities of the included code.
For a more thorough understanding, please consider viewing the code itself, and the examples in the `scripts` folder of
the PyBAMOCS module. There is also a similar, but more, extensive tutorial in the form of a Jupyter Notebook in the
module's `notebooks` directory.

# PyBAMOCS Installation

We recommend installing PyBAMOCS in its own environment using `venv`
(https://docs.python.org/3/library/venv.html) or `conda`
(https://conda.io/projects/conda/en/latest/user-guide/install/index.html). Once in your new environment (if desired),
perform the following steps to install the module.

* Clone the PACMANS repository (https://github.com/JHUAPL/PACMANs)
    * `git clone https://github.com/JHUAPL/PACMANs.git`
* Change directories to `box_model/python/`
    * `cd box_model/python/`
* Install locally using `pip`
    * `pip install -e .`

To execute the snippet:

**Step 1:** Follow the instructions above to install the PyBAMOCS module.

**Step 2:** The snippet itself may be run from the command line as follows:

```
% python pybamocs_tutorial.py
```

We encourage the interested user to examine the code below to identify the relevant objects and methods required to
implement their specific use case.

"""

# .............................................
# IMPORT STATEMENTS
# .............................................

import time
from matplotlib import pyplot as plt
from typing import Union

# Import the `six_box_model` function and its arguments
from pybamocs.six_box_model.six_box_model import six_box_model
from pybamocs.six_box_model.six_box_model import NORTH_A_IDX, NORTH_P_IDX, SOUTH_IDX, LOW_A_IDX, LOW_PI_IDX, DEEP_IDX
from pybamocs.six_box_model.six_box_model_args import (
    SixBoxModelBoxDimensions,
    SixBoxModelInitConditions,
    SixBoxModelTimeStep,
    SixBoxModelParameters,
    SixBoxModelRandomization
)


# Convenience function
def print_six_box_model_argument_settings(argument: Union[SixBoxModelBoxDimensions,
                                                          SixBoxModelInitConditions,
                                                          SixBoxModelTimeStep,
                                                          SixBoxModelParameters,
                                                          SixBoxModelRandomization]
                                          ) -> None:
    """
    Print six-box model settings to console for a given six_box_model argument.
    :param argument: One of the six_box_model argument objects.
    """
    settings_dict = argument.to_dict()  # Get the settings as a python dictionary

    print("vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv")
    # Print each key, value pair in the dictionary
    for key, value in settings_dict.items():
        print(f"{key}={value}")
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print()


def main():
    print("Box model settings are divided into five groups:")
    # Each object represents a set of parameters to the model
    six_box_model_dimensions = SixBoxModelBoxDimensions()
    six_box_model_initial_conditions = SixBoxModelInitConditions()
    six_box_model_time_settings = SixBoxModelTimeStep()
    six_box_model_parameters = SixBoxModelParameters()
    six_box_model_randomization = SixBoxModelRandomization()

    # And there is one object for each group as shown above.
    print("------------------------------------------------------------")
    print("Box Dimensions:")
    print_six_box_model_argument_settings(six_box_model_dimensions)

    print("------------------------------------------------------------")
    print("Initial Conditions")
    print_six_box_model_argument_settings(six_box_model_initial_conditions)

    print("------------------------------------------------------------")
    print("Model Time Step Parameters:")
    print_six_box_model_argument_settings(six_box_model_time_settings)

    print("------------------------------------------------------------")
    print("Model Parameters")
    print_six_box_model_argument_settings(six_box_model_parameters)

    print("------------------------------------------------------------")
    print("Model Randomization Parameters")
    print_six_box_model_argument_settings(six_box_model_randomization)

    # To run the box model, simply call the `six_box_model` function with your argument objects
    print("Running the box model...")
    start = time.time()
    results = six_box_model(six_box_model_dimensions,
                            six_box_model_initial_conditions,
                            six_box_model_parameters,
                            six_box_model_time_settings,
                            six_box_model_randomization)
    print(f"Run complete. Time: {time.time() - start} seconds.")

    # Note that the results are contained in a SixBoxModelResult object
    print("Box model output object:")
    print(results)
    print()

    # You can access specific results directly from the object
    print("Result details:")
    print("------------------------------------------------------")
    print("Shape of M_n_A for run:", results.M_n_A.shape)
    print()

    # or you can "unpack" them all at once
    M_n_A, M_n_P, M_upw_A, M_upw_PI, M_eddy_A, M_eddy_PI, M_ex, D_low_A, D_low_PI, T, S, sigma_0 = results.unpack()

    print("------------------------------------------------------")
    print("First 3 values of each output:")
    print("M_n_A:", M_n_A[:3])
    print("M_n_P:", M_n_P[:3])
    print("M_upw_A:", M_upw_A[:3])
    print("M_upw_PI:", M_upw_PI[:3])
    print("M_eddy_A:", M_eddy_A[:3])
    print("M_eddy_PI:", M_eddy_PI[:3])
    print("M_ex:", M_ex[:3])
    print("D_low_A:", D_low_A[:3])
    print("D_low_PI:", D_low_PI[:3])
    print("T_north_A:", T[NORTH_A_IDX, :3])
    print("T_north_P:", T[NORTH_P_IDX, :3])
    print("T_south:", T[SOUTH_IDX, :3])
    print("T_low_A:", T[LOW_A_IDX, :3])
    print("T_low_PI:", T[LOW_PI_IDX, :3])
    print("T_deep:", T[DEEP_IDX, :3])
    print("S_north_A:", S[NORTH_A_IDX, :3])
    print("S_north_P:", S[NORTH_P_IDX, :3])
    print("S_south:", S[SOUTH_IDX, :3])
    print("S_low_A:", S[LOW_A_IDX, :3])
    print("S_low_PI:", S[LOW_PI_IDX, :3])
    print("S_deep:", S[DEEP_IDX, :3])
    print("sigma_0_north_A:", sigma_0[NORTH_A_IDX, :3])
    print("sigma_0_north_P:", sigma_0[NORTH_P_IDX, :3])
    print("sigma_0_south:", sigma_0[SOUTH_IDX, :3])
    print("sigma_0_low_A:", sigma_0[LOW_A_IDX, :3])
    print("sigma_0_low_PI:", sigma_0[LOW_PI_IDX, :3])
    print("sigma_0_deep:", sigma_0[DEEP_IDX, :3])

    print("Plotting results...")
    plt.plot(M_n_A, label='M_n_A')
    plt.plot(M_n_P, label='M_n_P')
    plt.plot(M_upw_A, label='M_upw_A')
    plt.plot(M_upw_PI, label='M_upw_PI')
    plt.plot(M_eddy_A, label='M_eddy_A')
    plt.plot(M_eddy_PI, label='M_eddy_PI')
    plt.plot(D_low_A, label='Dlow_A')
    plt.plot(D_low_PI, label='D_low_PI')
    plt.legend()
    plt.title("1D Box Model Outputs")

    fig, ax = plt.subplots(nrows=2, ncols=3)
    ax[0, 0].plot(T[NORTH_A_IDX], label='North_A')
    ax[0, 1].plot(T[NORTH_P_IDX], label='North_P')
    ax[0, 2].plot(T[SOUTH_IDX], label='South')
    ax[1, 0].plot(T[LOW_A_IDX], label='Low_A')
    ax[1, 1].plot(T[LOW_PI_IDX], label='Low_PI')
    ax[1, 2].plot(T[DEEP_IDX], label='Deep')
    ax[0, 0].legend(), ax[0, 1].legend(), ax[0, 2].legend()
    ax[1, 0].legend(), ax[1, 1].legend(), ax[1, 2].legend()
    plt.suptitle("Temperature in the 6 different boxes")
    plt.tight_layout()

    fig1, ax1 = plt.subplots(nrows=2, ncols=3)
    ax1[0, 0].plot(S[NORTH_A_IDX], label='North_A')
    ax1[0, 1].plot(S[NORTH_P_IDX], label='North_P')
    ax1[0, 2].plot(S[SOUTH_IDX], label='South')
    ax1[1, 0].plot(S[LOW_A_IDX], label='Low_A')
    ax1[1, 1].plot(S[LOW_PI_IDX], label='Low_PI')
    ax1[1, 2].plot(S[DEEP_IDX], label='Deep')
    ax1[0, 0].legend(), ax1[0, 1].legend(), ax1[0, 2].legend()
    ax1[1, 0].legend(), ax1[1, 1].legend(), ax1[1, 2].legend()
    plt.suptitle("Salinity in the 6 different boxes")
    plt.tight_layout()

    fig2, ax2 = plt.subplots(nrows=2, ncols=3)
    ax2[0, 0].plot(sigma_0[NORTH_A_IDX], label='North_A')
    ax2[0, 1].plot(sigma_0[NORTH_P_IDX], label='North_P')
    ax2[0, 2].plot(sigma_0[SOUTH_IDX], label='South')
    ax2[1, 0].plot(sigma_0[LOW_A_IDX], label='Low_A')
    ax2[1, 1].plot(sigma_0[LOW_PI_IDX], label='Low_PI')
    ax2[1, 2].plot(sigma_0[DEEP_IDX], label='Deep')
    ax2[0, 0].legend(), ax2[0, 1].legend(), ax2[0, 2].legend()
    ax2[1, 0].legend(), ax2[1, 1].legend(), ax2[1, 2].legend()
    plt.suptitle("Density in the 6 different boxes")
    plt.tight_layout()
    plt.show(block=False)

    # Consider an example of some data collection
    Fwn_A_values_to_test = [10000, 50000, 100000, 500000, 1000000]
    alternate_north_atl_starting_temp = 4.0

    box_dims = SixBoxModelBoxDimensions()
    params = SixBoxModelParameters()
    time_step = SixBoxModelTimeStep()
    init = SixBoxModelInitConditions(T_north_A0=alternate_north_atl_starting_temp)
    rand = SixBoxModelRandomization()

    # Collect the data... (should take a few seconds)
    print(f"Generating data for alternate parameter settings: T_north={alternate_north_atl_starting_temp}")
    start_time = time.time()
    results = []
    for fwn in Fwn_A_values_to_test:
        print(f"Fwn_A={fwn}")
        params.Fwn_A = fwn
        results.append(six_box_model(box_dims, init, params, time_step, rand))
    time_to_collect_data = time.time() - start_time
    print(f"Total time to collect data: {time_to_collect_data} seconds")

    # Let's look at the difference in M_n_A for each run
    print("Plotting results...")
    plt.figure()
    for i in range(len(Fwn_A_values_to_test)):
        plt.plot(results[i].M_n_A, label=f"Fwn_A={Fwn_A_values_to_test[i]}")
    plt.title(f"M_n_A for different Northern Fluxes and T_north_A0={alternate_north_atl_starting_temp}")
    plt.legend()
    plt.show()  # suspends script until plot windows are closed
    print("Done")


if __name__ == "__main__":
    main()
