"""
src/climrr/__init__.py
"""
from __future__ import absolute_import, annotations, division, print_function

import logging
import warnings

from pathlib import Path
from typing import Optional
import cartopy.io.shapereader as shpreader
import pandas as pd
import shapely.geometry as sgeom
from rich.theme import Theme
from rich.console import Console
from enrich.style import STYLES
import geopandas as gpd

theme = Theme(STYLES)
console = Console(theme=Theme(STYLES), log_path=False, markup=True)

warnings.filterwarnings('ignore')


HERE = Path(__file__).parent
ROOT = HERE.parent.parent
DATA_DIR = ROOT / "data"



def load_csvs(gdf: gpd.GeoDataFrame) -> dict[str, gpd.GeoDataFrame]:
    csvs = [i for i in DATA_DIR.rglob('*.csv')]
    data = {}
    for f in csvs:
        key = f.stem
        tmp = pd.read_csv(f.as_posix())
        merged = gdf.merge(tmp, on='Crossmodel')
        merged['boundary'] = merged.boundary
        merged['centroid'] = merged.centroid
        data[key] = merged
        console.print(f"data['{key}'].shape={data[key].shape}")

    return data


def load_shapefile():
    shpfile = DATA_DIR.joinpath(
        "GridCells2Shapefile/GridCellsShapefile/GridCells.shp"
    )
    return gpd.read_file(shpfile)


def get_console():
    from enrich.console import Console, get_theme
    from ClimRR import get_logger, DATA_DIR
    theme = get_theme()
    console = Console(theme=theme, log_path=False)
    console.is_jupyter = False
    return console


def set_plot_style(params: Optional[dict] = None, **kwargs):
    import matplotlib.pyplot as plt
    plt.rcParams.update({
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
    })


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
    from enrich.logging import RichHandler
    from enrich.console import get_theme, Console
    # log.handlers = []
    # from rich.logging import RichHandler
    # from l2hmc.utils.rich import get_console, is_interactive
    theme = get_theme()
    console = Console(theme=theme, log_path=False, markup=True)
    from rich.console import Console as rConsole
    import os
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
    return log


log = get_logger('ClimRR')
