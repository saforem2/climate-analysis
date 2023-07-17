# Climate Analysis

Climate Analysis project using data from the [Climate Risk \& Resilience Portal](https://disgeoportal.egs.anl.gov/ClimRR/)

## Instructions / Setup

Download the `ClimRR Data Download.zip` file from:

[ClimRR Data Download](https://anl.app.box.com/s/hmkkgkrkzxxocfe9kpgrzk2gfc4gizp8)

and unzip it into the [`data/`](./data/) directory.

On Perlmutter at NERSC, for example,

```bash
foremans@login23:~> git clone https://github.com/saforem2/climate-analysis
foremans@login23:~> cd climate-analysis
foremans@login23:~> pwd
/global/homes/f/foremans/climate-analysis
```

Y


Using _my_ (`/home/foremans/`)

```bash
cd ~
git clone https://github.com/saforem2/climate-analysis
cd ./climate-analysis/
pwd
/home/foremans/
```

you should unzip `ClimRR Data Download.zip` and place the contents into

You can also conveniently download a map of all the US counties using

```bash
curl -X GET --verbose --output us-counties.zip \
    "https://public.opendatasoft.com/api/explore/v2.1/catalog/datasets/georef-united-states-of-america-county/exports/shp?" 
```
