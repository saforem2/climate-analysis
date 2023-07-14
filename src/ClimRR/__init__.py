"""
src/climrr/__init__.py
"""
from __future__ import absolute_import, annotations, division, print_function

import logging
import warnings
from pathlib import Path
from typing import Optional

import cartopy.io.shapereader as shpreader
import geodatasets
import geopandas as gpd
import pandas as pd
import shapely.geometry as sgeom
from enrich.style import STYLES
from rich.console import Console
from rich.theme import Theme

theme = Theme(STYLES)
console = Console(theme=Theme(STYLES), log_path=False, markup=True)

warnings.filterwarnings('ignore')


HERE = Path(__file__).parent
ROOT = HERE.parent.parent
DATA_DIR = ROOT / "data"
DEFAULT_CRS: str = 'EPSG:3857'


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
    return gpd.read_file(
        DATA_DIR.joinpath(
            'us-counties',
            'georef-united-states-of-america-county-millesime.shp',
        )
    ).to_crs(crs)


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


def get_console() -> Console:
    console = Console(theme=Theme(STYLES), log_path=False, markup=True)
    console.is_jupyter = False
    return console


def set_plot_style(params: Optional[dict] = None):
    import matplotlib.pyplot as plt
    defaults = {
        'axes.facecolor': 'none',
        'figure.facecolor': 'none',
        'savefig.facecolor': 'none',
        'savefig.format': 'svg',
        'axes.edgecolor': 'none',
        'axes.grid': True,
        'axes.labelcolor': '#838383',
        'axes.titlecolor': '#838383',
        'grid.color': '#838383',
        'text.color': '#838383',
        'grid.linestyle': '--',
        'grid.linewidth': 0.5,
        'grid.alpha': 0.4,
        'xtick.color': 'none',
        'ytick.color': 'none',
        'xtick.labelcolor': '#838383',
        'legend.edgecolor': 'none',
        'ytick.labelcolor': '#838383',
        'savefig.transparent': True,
    }
    plt.rcParams |= defaults
    if params is not None:
        plt.rcParams |= params
    console.print("Using updated plot style for matplotlib")


import matplotlib.pyplot as plt


def plot_gdf(
        gdf: gpd.GeoDataFrame,
        kwargs: Optional[dict] = None,
        plt_kwargs: Optional[dict] = None
) -> tuple[plt.Figure, plt.Axes]:
    fig, ax = plt.subplots(**plt_kwargs)
    gdf.plot(ax=ax, **kwargs)
    ax.set_axis_off()
    return fig, ax


def get_logger(
        name: Optional[str] = None,
        level: str = 'INFO',
        rank: int = 0,
        world_size: int = 1,
        rank_zero_only: bool = True,
        **kwargs,
) -> logging.Logger:
    # logging.basicConfig(stream=DummyTqdmFile(sys.stderr))
    log = logging.getLogger(name)
    from enrich.console import Console, get_theme
    from enrich.logging import RichHandler
    # log.handlers = []
    # from rich.logging import RichHandler
    # from l2hmc.utils.rich import get_console, is_interactive
    theme = get_theme()
    console = Console(theme=theme, log_path=False, markup=True)
    import os

    from rich.console import Console as rConsole
    os.environ['COLORTERM'] = 'truecolor'
    from rich.console import Console as rConsole
    rconsole = rConsole(theme=theme, log_path=False, markup=True)
    # format = "[%(asctime)s][%(name)s][%(levelname)s] - %(message)s"
    if rank_zero_only:
        if rank != 0:
            log.setLevel('CRITICAL')
        else:
            log.setLevel(level)
    if rank == 0:
        # console = get_console(
        #     markup=True,  # (WORLD_SIZE == 1),
        #     redirect=(world_size > 1),
        #     # file=outfile,
        #     **kwargs
        # )
        if console.is_jupyter:
            console.is_jupyter = False
        # log.propagate = True
        # log.handlers = []
        # use_markup = (
        #     WORLD_SIZE == 1
        #     and not is_interactive()
        # )
        log.addHandler(
            RichHandler(
                omit_repeated_times=False,
                level=level,
                console=console,
                show_time=True,
                show_level=True,
                show_path=False,
                # tracebacks_width=120,
                markup=True,
                enable_link_path=True,
                # keywords=['loss=', 'dt=', 'Saving']
            )
        )
        log.setLevel(level)
    if (
            len(log.handlers) > 1 
            and all([i == log.handlers[0] for i in log.handlers])
    ):
        log.handlers = [log.handlers[0]]
    return log


log = get_logger('ClimRR')
