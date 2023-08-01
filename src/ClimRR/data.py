"""
src/ClimRR/data.py

Contains helper functions for loading + working with our data.
"""
from __future__ import absolute_import, annotations, division, print_function

import geodatasets
import geopandas as gpd
import pandas as pd
from ClimRR import console

from ClimRR import DATA_DIR, DEFAULT_CRS


def save_counties_data(counties):
    outfile = DATA_DIR.joinpath("us-counties.shp")
    console.log(
        f"Saving US Counties to: {outfile.resolve().absolute().as_posix()}"
    )
    counties.to_file(outfile)


def download_counties_data(
        crs: str = DEFAULT_CRS,
        save: bool = True,
) -> gpd.GeoDataFrame:
    counties = gpd.read_file(
        "https://public.opendatasoft.com/api/explore/v2.1/"
        "catalog/datasets/georef-united-states-of-america-county/exports/shp"
    ).to_crs(crs)
    if save:
        save_counties_data(counties)
    return counties


def load_counties(crs: str = DEFAULT_CRS):
    counties_fpath = DATA_DIR.joinpath("us-counties.shp")
    if not counties_fpath.is_file():
        return download_counties_data(crs=crs, save=True)
    return gpd.read_file(counties_fpath).to_crs(crs)


def load_chicago_data(crs: str = DEFAULT_CRS) -> dict[str, gpd.GeoDataFrame]:
    chipop = gpd.read_file(
        geodatasets.get_path('geoda.chicago_commpop')
    ).to_crs(crs)
    chihealth = gpd.read_file(
        geodatasets.get_path('geoda.chicago_health')
    ).to_crs(crs)
    chigroc = gpd.read_file(
        geodatasets.get_path('geoda.groceries')
    ).to_crs(crs)
    return {
        'population': chipop,
        'health': chihealth,
        'groceries': chigroc,
    }


def load_csvs(gdf: gpd.GeoDataFrame) -> dict[str, gpd.GeoDataFrame]:
    csvs = [i for i in DATA_DIR.rglob('*.csv')]
    data = {}
    for f in csvs:
        key = f.stem
        tmp = pd.read_csv(f.as_posix())
        merged = gdf.merge(tmp, on='Crossmodel')
        # merged = tmp.merge(gdf, on='Crossmodel')
        merged['boundary'] = merged.boundary
        merged['centroid'] = merged.centroid
        data[key] = merged
        console.print(f"data['{key}'].shape={data[key].shape}")

    return data


def load_shapefile() -> gpd.GeoDataFrame:
    shpfile = DATA_DIR.joinpath(
        "GridCells2Shapefile/GridCellsShapefile/GridCells.shp"
    )
    return gpd.read_file(shpfile)
