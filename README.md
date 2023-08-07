# Climate Analysis

Climate Analysis project using data from the [Climate Risk \& Resilience Portal](https://disgeoportal.egs.anl.gov/ClimRR/)

## Links / References

> **Note**<br>
> For additional information on using resources @ NERSC,
> check out their [Getting Started](https://docs.nersc.gov/getting-started/) page

- [`ClimRR`: Project Website](https://github.com/saforem2/climate-analysis)
- [NERSC/intro-HPC-bootcamp-2023](https://github.com/NERSC/intro-HPC-bootcamp-2023)

## Instructions / Setup

<!--Download the `ClimRR Data Download.zip` file from:

[ClimRR Data Download](https://anl.app.box.com/s/hmkkgkrkzxxocfe9kpgrzk2gfc4gizp8)

and unzip it into the [`data/`](./data/) directory.-->

On Perlmutter at NERSC, everything you need is already in

```bash
/global/cfs/cdirs/m4388/Project2-Climrr
```


```bash
foremans@login23:~> ls /global/cfs/cdirs/m4388/Project2-ClimRR/
adebroy  adebroy1  climate-analysis  data  foremans  venvs
foremans@login23:~> # you can make your own directory here, e.g. YOUR username
foremans@login23:~> mkdir /global/cfs/cdirs/m4388/Project2-ClimR/$USER
foremans@login23:~> # make a symlink from project dir into your $HOME directory
foremans@login23:~> ln -s /global/cfs/cdirs/m4388/Project2-ClimRR/ $HOME/Project2-ClimRR
foremans@login23:~> cd /global/cfs/cdirs/m4388/Project2-ClimRR/$USER
foremans@login23:~> git clone https://github.com/saforem2/climate-analysis
foremans@login23:~> cd climate-analysis
```

🚀 and good to go!



<!-- you should unzip `ClimRR Data Download.zip` and place the contents into

You can also conveniently download a map of all the US counties using

```bash
curl -X GET --verbose --output us-counties.zip \
    "https://public.opendatasoft.com/api/explore/v2.1/catalog/datasets/georef-united-states-of-america-county/exports/shp?" 
``` -->
