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

::: {.callout-important title="Finding the data" collapse="true" style="width:100%; place-self: end;"}

The data needed for this project has already been copied to the NERSC systems and can be found at:

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

