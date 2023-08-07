---
callout-appearance: simple
editor:
  render-on-save: true
execute:
  freeze: true
title: Getting Started
---






We provide below a brief introduction to the project and how to get started using Jupyter @ NERSC

::: {.callout-caution title="Intro to Unix" collapse="true" style="width:100%;"}

- The [Intro to Unix](https://earth-env-data-science.github.io/lectures/environment/intro_to_unix.html) page from the Earth and Environmental Data Science book is an excellent resource for those just getting started or who are unfamiliar with the basics of Linux.

- Similarly for their reference on [Intro to Git for Version Control](https://earth-env-data-science.github.io/lectures/environment/intro_to_git.html)

:::

Our project directory can be found at:

```bash
/global/cfs/cdirs/m4388/Project2-ClimRR/
```

All of the data needed for this project has already been copied to the filesystem on NERSC.

In addition, we provide a pre-built (`hpc-bootcamp`) python kernel which we will use for running our code in Jupyter @ NERSC.

This `hpc-bootcamp` kernel has everything we will need for this project,
including the [`ClimRR` Python
package](https://github.com/saforem2/climate-analysis/tree/main/src/ClimRR).

## Overview of Python

::: {.callout-caution title="Reference" collapse="true" style="width:100%;"}

**Material below modified from[^modified]**: [Python
Fundamentals](https://earth-env-data-science.github.io/lectures/core_python/python_fundamentals.html)

:::

[^modified]: Which _itself_ is modified from the [official python
tutorial](https://docs.python.org/3/tutorial/)

### Invoking Python

There are three main ways to use Python:

1. Running / executing a Python file, e.g. `python filename.py`
    - this will launch python, execute (line by line) the contents of `filename.py`, and return
2. Interactively, either through:
    1. a **console** (e.g. the Python interpreter `python` or an [IPython](https://ipython.org/) shell `ipython`)
    2. a **notebook** (e.g. Jupyter notebook)*

*we will (mostly) focus on using Jupyter notebooks for this project.

## Modules and Packages in Python

As an illustrative example for how to use and work with Python, we've included
a simple Python package (`ClimRR`) in our [{{< fa brands github >}}
`climate-analysis/`](https://github.com/saforem2/climate-analysis) repo.

This Python package, `CLimRR`, is located in [`src/ClimRR/`](../../src/ClimRR) and contains the following[^modules]:

<!-- package, `ClimRR`, located in  -->
<!-- This python package, `ClimRR` is located in [`src/ClimRR`](../../src/ClimRR/), -->
<!-- and contains only a few (relatively) simple Python -->
<!-- `modules`[^modules] as we can see by looking in the  -->

   - {{< fa brands github >}} [__climate\-analysis__/](../../)
      - 📂 [__src__/](../../src/)
         - 📂 [__ClimRR__/](../../src/ClimRR/)
            - 🐍 [\_\_about\_\_.py](src/ClimRR/__about__.py)
            - 🐍 [\_\_init\_\_.py](src/ClimRR/__init__.py)
            - 🐍 [data.py](src/ClimRR/__init__.py)

In particular, the _Python package[^package]_ that we will use for this
project, `ClimRR` is located inside our `src/ClimRR` directory.

This is a simple example just to 

- [`__init__.py`](../../src/ClimRR/__init__.py): Any folder containing an `__init__.py` file is considered a
  Python library.  

  Oftentimes they are empty[^init_files], but ours contains some (not terribly
  important) functions for [specifying where our data
  lives](https://github.com/saforem2/climate-analysis/src/ClimRR/__init__.py#L29),
  [setting up
  logging](https://github.com/saforem2/climate-analysis/src/ClimRR/__init__.py#L107),
  etc.

- [`__about__.py`](../../src/ClimRR/__about__.py): A **strictly informational**
(`metadata`!) file that can be used to (dynamically!) specify a package
version. Again, this isn't important for our purposes but incase you're
wondering what it does[^about_files].

- [`data.py`](../src/ClimRR/data.py): Contains some simple (but useful!)
functions for [loading our
Shapefile](https://github.com/saforem2/climate-analysis/src/ClimRR/data.py#L77),
[loading US County
data](https://github.com/saforem2/climate-analysis/blob/8d6a62896112963d2fd95ef86f14cdf0df4834eb/src/ClimRR/data.py#L37),
and loading [`ClimRR` climate data from
`*.CSV`s](https://github.com/saforem2/climate-analysis/blob/8d6a62896112963d2fd95ef86f14cdf0df4834eb/src/ClimRR/data.py#L61)


[^package]: Roughly, `package` $\simeq$ `library` for our purposes

[^about_files]:  
   Additional information
   [here](https://hatch.pypa.io/latest/version/). Again, understanding the details
   of python packaging is **well beyond** the scope of this project, but I've
   included some details here for those curious.

[^init_files]:  
   More information on `__init__.py` and Python packages can be found
   [here](https://docs.python.org/3/tutorial/modules.html#packages)

[^modules]: Recall, a Python _module_ is an individual file `.py` containing
some Python code. A Python _library_ is then a collection of these _modules_,
organized around some central idea or purpose.

::: {.callout-important title="Finding the data" collapse="true" style="width:100%; place-self: end;"}

The data needed for this project has already been copied to the NERSC systems and can be found at:

For those curious, the ClimRR data we will be working with looks something like:

```bash
$ tree /global/cfs/cdirs/m4388/Project2-ClimRR/data/ClimRR/
/global/cfs/cdirs/m4388/Project2-ClimRR/data/ClimRR/
├── AnnualTemperatureMaximum.csv
├── AnnualTemperatureMinimum.csv
├── ClimRR Metadata and Data Dictionary.pdf
├── ConsecutiveDayswithNoPrecipitation.csv
├── FireWeatherIndex_Wildfire.csv
├── GridCells2Shapefile.zip
├── GridCellsShapefile.zip
├── HeatingDegreeDays.csv
├── Precipitation_inches_AnnualTotal.csv
├── README.txt
├── SeasonalTemperatureMaximum.csv
├── SeasonalTemperatureMinimum.csv
└── WindSpeed.csv
```

the data is also available online and can be downloaded from [ClimRR Data Download
(ANL)](https://anl.box.com/s/hmkkgkrkzxxocfe9kpgrzk2gfc4gizp8)

:::

## Setup

To get started, we will need to:

1. Create a symlink from the project directory,
   `/global/cfs/cdirs/m4388/Project2-ClimRR/` into your `$HOME` directory

   ```bash
   ln -s /global/cfs/cdirs/m4388/Project2-ClimRR/ $HOME/Project2-ClimRR
   ```

2. Navigate into here and create your personal directory (where you will store
   and work on **your** project):

   ```bash
   cd $HOME/Project2-ClimRR/
   mkdir $USER
   cd $USER
   ```

3. Clone the [{{< fa brands github >}} GitHub repo](https://github.com/saforem2/climate-analysis)
   ```bash
   git clone https://github.com/saforem2/climate-analysis
   ```

4. Navigate to [`jupyter.nersc.gov`](https://jupyter.nersc.gov/hub/) and login.
      - [Jupyter for the New User to NERSC](https://www.nersc.gov/assets/Uploads/13-Using-Jupyter-20200616.pdf)
      - [Using Jupyter at NERSC](https://www.nersc.gov/assets/Uploads/13-Using-Jupyter-20200616.pdf)

5. Navigate into your personal directory in our `/global/cfs/cdirs/m4388/Project2-ClimRR/` project space:

   ::: {#fig-jupyter-nersc}

   ![](https://github.com/saforem2/climate-analysis/blob/main/assets/jupyter1-dark.png?raw=true)
   ![](https://github.com/saforem2/climate-analysis/blob/main/assets/jupyter2-dark.png?raw=true)
   Screenshots of the Jupyter interface at NERSC
   :::


