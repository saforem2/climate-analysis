# Climate Analysis

Climate Analysis project using data from the [Climate Risk \& Resilience Portal](https://disgeoportal.egs.anl.gov/ClimRR/)

## Instructions / Setup

<!--Download the `ClimRR Data Download.zip` file from:

[ClimRR Data Download](https://anl.app.box.com/s/hmkkgkrkzxxocfe9kpgrzk2gfc4gizp8)

and unzip it into the [`data/`](./data/) directory.-->

On Perlmutter at NERSC, everything you need is already in

```bash
/global/cfs/cdirs/m4388/Project3-Climrr
```

```bash
foremans@login23:~> ls /global/cfs/cdirs/m4388/Project3-Climrr/
foremans
foremans@login23:~> # you can make your own directory here, e.g. YOUR username
foremans@login23:~> mkdir /global/cfs/cdirs/m4388/Project3-Climrr/$USER
foremans@login23:~> cd /global/cfs/cdirs/m4388/Project3-Climrr/$USER
foremans@login23:~> git clone https://github.com/saforem2/climate-analysis
foremans@login23:~> cd climate-analysis
foremans@login23:~> # copy into `./data/`
foremans@login23:~> cp -r /global/cfs/cdirs/m4388/Project3-Climrr/data ./data/
```

🚀 and good to go!

<!-- you should unzip `ClimRR Data Download.zip` and place the contents into

You can also conveniently download a map of all the US counties using

```bash
curl -X GET --verbose --output us-counties.zip \
    "https://public.opendatasoft.com/api/explore/v2.1/catalog/datasets/georef-united-states-of-america-county/exports/shp?" 
``` -->
