---
callout-appearance: simple
editor:
  render-on-save: true
execute:
  freeze: true
title: Climate Analysis with ClimRR
---






## Getting Started

::: {.callout-caution title="Useful links + References" collapse="true" width="100%"}

- Useful links + References:
    - [Geopandas: An Introduction](https://autogis-site.readthedocs.io/en/latest/lessons/lesson-2/geopandas-an-introduction.html)
    - [An Introduction to Earth and Environmental Data Science](https://earth-env-data-science.github.io/intro.html)
        - [Final Projects](https://earth-env-data-science.github.io/projects.html) (good examples)
        - [Hands-On: Aggregating the Data](https://climateestimate.net/content/example-step3.html)
    - [Using Weather Data and Climate Model Output in Economic Analyses of Climate Change](https://www.journals.uchicago.edu/doi/10.1093/reep/ret016)
    - [On the use and misuse of climate change projections in international development](https://wires.onlinelibrary.wiley.com/doi/full/10.1002/wcc.579)

:::

::: {.callout-note title="Learning Goals" collapse="false" style="width:100%;"}

The goal of this project is to teach students to[^goals]:

- Use Unix commands to work with files and navigate directories
- Use JupyterHub + basic familiarity with how to use Jupyter notebooks on HPC systems
- Identify some of the common file types and data formats for geospatial data
    - (+ common python libraries for geospatial data analysis)
- Perform exploratory data analysis on geospatial data
    - (+ understand different operations for manipulating and interacting with this data)
    - tabular vs. gridded data
- Perform simple visualizations in Python to display different types of data (e.g. maps, line charts, interactive visualizations, etc)
    - using figures to illustrate a point or idea
    - know what types of plots to use for which situations / data types
- Understand control flow / basic structure of a Python script
    - using Python in Jupyter[^surprise]
    - `import`-ing libraries, etc

:::

[^surprise]: Getting Python setup correctly can be **surprisingly** difficult

[^goals]: Building on ideas from [Earth and Environmental Science](https://earth-env-data-science.github.io/intro.html)

### Reading and Writing Files

We use [`GeoPandas`](https://geopandas.org/en/stable/index.html), an open
source project to make working with geospatial data in python easier.

GeoPandas extends the datatypes used by [pandas](http://pandas.pydata.org/) to
allow spatial operations on geometric types.

Geometric operations are performed by [`shapely`](https://shapely.readthedocs.io/).

GeoPandas further depends on [`fiona`](https://fiona.readthedocs.io/) and
[`matplotlib`](http://matplotlib.org/) for plotting.

GeoPandas can read almost any vector-based spatial data format including ESRI
shapefile, GeoJSON files and more using the command


::: {.cell execution_count=1}
``` {.python .cell-code}
import geopandas as gpd
import geodatasets
gdf = gpd.read_file(geodatasets.get_path("geoda.chicago_commpop"))
gdf.head(n=2)
```

::: {.cell-output .cell-output-stderr}
```
/Users/samforeman/miniconda3/envs/ClimRR/lib/python3.11/site-packages/pyproj/__init__.py:91: UserWarning: Valid PROJ data directory not found. Either set the path using the environmental variable PROJ_DATA (PROJ 9.1+) | PROJ_LIB (PROJ<9.1) or with `pyproj.datadir.set_data_dir`.
  warnings.warn(str(err))
```
:::

::: {.cell-output .cell-output-display execution_count=1}

```{=html}
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>community</th>
      <th>NID</th>
      <th>POP2010</th>
      <th>POP2000</th>
      <th>POPCH</th>
      <th>POPPERCH</th>
      <th>popplus</th>
      <th>popneg</th>
      <th>geometry</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>DOUGLAS</td>
      <td>35</td>
      <td>18238</td>
      <td>26470</td>
      <td>-8232</td>
      <td>-31.099358</td>
      <td>0</td>
      <td>1</td>
      <td>MULTIPOLYGON (((-87.60914 41.84469, -87.60915 ...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>OAKLAND</td>
      <td>36</td>
      <td>5918</td>
      <td>6110</td>
      <td>-192</td>
      <td>-3.142390</td>
      <td>0</td>
      <td>1</td>
      <td>MULTIPOLYGON (((-87.59215 41.81693, -87.59231 ...</td>
    </tr>
  </tbody>
</table>
</div>
```

:::
:::


which returns a GeoDataFrame object.

A `GeoDataFrame` is a tabular data structure that contains a `GeoSeries`.

The most important property of a `GeoDataFrame` is that it always has one
`GeoSeries` column that holds a special status.

This `GeoSeries` is referred to as the `GeoDataFrame`'s "geometry". When a
spatial method is applied to a `GeoDataFrame` (or a spatial attribute like area
is called), this commands will always act on the "geometry" column[^geometry].

[^geometry]: The “geometry” column – no matter its name – can be accessed
through the geometry attribute (`gdf.geometry`), and the name of the geometry
column can be found by typing `gdf.geometry.name`.

### Imports / setup

We've prepared some useful functions in
[`src/ClimRR/data.py`](https://github.com/saforem2/climate-analysis/blob/main/src/ClimRR/data.py)
to simplify the process of loading and working with our data.

<!-- ::: {.callout-warning title="Warning" collapse="false"} -->
<!---->
<!-- Make sure to follow the instructions from [Setup and -->
<!-- Installation](/qmd/GettingStarted/setup.qmd) for installing the `ClimRR` -->
<!-- package. -->
<!---->
<!-- ::: -->

::: {.cell execution_count=2}
``` {.python .cell-code code-fold="true" code-summary="Imports"}
import matplotlib_inline
import matplotlib.pyplot as plt
import geopandas as gpd
import warnings

import matplotlib.pyplot as plt

from enrich.style import STYLES
from rich.theme import Theme
from rich.console import Console as Console
from ClimRR import get_logger, set_plot_style
from ClimRR.data import DATA_DIR

matplotlib_inline.backend_inline.set_matplotlib_formats('svg')

set_plot_style()
theme = Theme(STYLES)
log = get_logger()
console = Console(
    theme=Theme(STYLES),
    log_path=False,
    markup=True,
    width=512
)
```
:::


# Data Organization

The [ClimRR Data](https://anl.box.com/s/hmkkgkrkzxxocfe9kpgrzk2gfc4gizp8) can
be downloaded as a `*.zip` file, and contains:  

- **Shapefile** (as an additional `*.zip` _inside_ the original)
- Individual `*.csv`'s for each of the climate variables
    - `{AnnualTemperatureMaximum,...,HeatingDegreeDays}.csv`

::: {.callout-tip title="`*.zip` contents:" collapse="true"}

```bash
📂 ClimRR Data Download/
┣━━ 📂 GridCells2Shapefile/
┃   ┣━━ 📄 GridCells2.cpg
┃   ┣━━ 📄 GridCells2.dbf
┃   ┣━━ 📄 GridCells2.prj
┃   ┣━━ 📄 GridCells2.sbn
┃   ┣━━ 📄 GridCells2.sbx
┃   ┣━━ 📄 GridCells2.shp
┃   ┣━━ 📄 GridCells2.shp.xml
┃   ┗━━ 📄 GridCells2.shx
┣━━ 📂 GridCellsShapefile/
┃   ┣━━ 📄 GridCells.cpg
┃   ┣━━ 📄 GridCells.dbf
┃   ┣━━ 📄 GridCells.prj
┃   ┣━━ 📄 GridCells.sbn
┃   ┣━━ 📄 GridCells.sbx
┃   ┣━━ 📄 GridCells.shp
┃   ┣━━ 📄 GridCells.shp.xml
┃   ┗━━ 📄 GridCells.shx
┣━━ 📄 AnnualTemperatureMaximum.csv
┣━━ 📄 AnnualTemperatureMinimum.csv
┣━━ 📄 ClimRR Metadata and Data Dictionary.pdf
┣━━ 📄 ConsecutiveDayswithNoPrecipitation.csv
┣━━ 📄 FireWeatherIndex_Wildfire.csv
┣━━ 📄 GridCells2Shapefile.zip
┣━━ 📄 GridCellsShapefile.zip
┣━━ 📄 HeatingDegreeDays.csv
┣━━ 📄 Precipitation_inches_AnnualTotal.csv
┣━━ 📄 README.txt
┣━━ 📄 SeasonalTemperatureMaximum.csv
┣━━ 📄 SeasonalTemperatureMinimum.csv
┗━━ 📄 WindSpeed.csv
```



:::

## Types of Data

::: {#fig-data-types}

![](../../assets/vector-data.png)

(Image credit: National Ecological Observatory Network (NEON))
:::

One of the most common file formats for vector data is the [ESRI
shapefile](https://en.wikipedia.org/wiki/Shapefile), which is what we will be
working with for this project.

### Metadata

Metadata is "data about the data"[^metadata] and is (by design) meant to give
additional information or provide context about a dataset.

Examples might include:

- When was this data created?
    - By who? For what? Where at? When? **Why**??
- How is this data licensed?
- Is there a reference for this data? (DOI ? URL ? etc.)
- What variables or fields are contained in this data?
    - What do they represent? Are there units?
- If the data is geospatial, what geographical or temporal area is included?
- Additional (often contextual) information about the data
    - e.g. "this data was created to inform a population about upcoming weather events" or similar


Metadata is often expected to be of a certain form, or to follow specific conventions / guidelines.

This is important to keep in mind and will allow others to understand your data
without needing an explanation (e.g. "what does this abbreviation mean?", "how
is this variable defined?", etc.)

Some common metadata conventions for GIS data include:

- [Climate and Forecast (CF) Conventions](https://cfconventions.org/)
- [Attribute Convention for Data Discovery](https://wiki.esipfed.org/Attribute_Convention_for_Data_Discovery_1-3)

[Schema.org](https://schema.org) is another useful reference and provides a
general framework for dealing with metadata.

## FAIR Data

[FAIR](https://www.force11.org/group/fairgroup/fairprinciples) stands for
"Findable, Accessible, Interoperable, Reusable", and provides a set
of guidelines for data sharing.

In the age of "big data", its important that we use (and promote!) tools that
facilitate the effective sharing of data.

Ideally, our data would be completely self-contained and provide, via
metadata, all of the information required to understand and work with it.

<!-- This is important to keep in mind as it allows others to understand and -->
<!-- interpret your data in a well-defined manner. -->
<!---->
<!-- There are oftentimes well-established conventions and formats that metadata is -->
<!-- expected to adhere to, so it is important to make -->



[^metadata]: [Metadata](https://earth-env-data-science.github.io/lectures/data.html#metadata)


## Load Shapefile and inspect

A `shapefile` is provided in the [ClimRR Data Download
(ANL)](https://anl.box.com/s/hmkkgkrkzxxocfe9kpgrzk2gfc4gizp8) and can be loaded using `geopandas.read_file(...)` which will return a `geopandas.GeoDataFrame`:

::: {.cell execution_count=3}
``` {.python .cell-code}
shpfile = DATA_DIR.joinpath(
    "GridCellsShapefile/GridCells.shp"
)
shape = gpd.read_file(shpfile)
```
:::


Each entry in this table defines a single **grid cell** (12km x 12 km) which
collectively tile the United States.

We can get a better understanding of whats going on by looking at the first few
entries:

::: {.cell execution_count=4}
``` {.python .cell-code}
shape.head(n=2)
```

::: {.cell-output .cell-output-display execution_count=4}

```{=html}
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>OBJECTID</th>
      <th>Crossmodel</th>
      <th>Shape_Leng</th>
      <th>Shape_Area</th>
      <th>geometry</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>R161C438</td>
      <td>63614.764866</td>
      <td>2.529273e+08</td>
      <td>POLYGON ((-9530601.177 4726046.614, -9534793.8...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>R125C222</td>
      <td>61384.219597</td>
      <td>2.355013e+08</td>
      <td>POLYGON ((-12959076.287 4395610.472, -12974301...</td>
    </tr>
  </tbody>
</table>
</div>
```

:::
:::


We see that each row has the following columns: `{OBJECTID, Crossmodel,
Shape_Leng, Shape_Area, geometry}`.

In particular, the `Crossmodel`[^crossmodel] column is a text ID that uniquely
identifies an individual cell.

[^crossmodel]: Truncated name for "Crossmodel_CellName".

To be explicit, let's look at the `WindSpeed.csv` file.


## Dealing with Geometry

Our shapefile contains a grid of _cells_ (12km x 12km) which tile the
continental US.

We can inspect a single cell:

::: {.cell execution_count=5}
``` {.python .cell-code}
cell = shape[shape["Crossmodel"] == 'R146C497']
cell.head()
```

::: {.cell-output .cell-output-display execution_count=5}

```{=html}
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>OBJECTID</th>
      <th>Crossmodel</th>
      <th>Shape_Leng</th>
      <th>Shape_Area</th>
      <th>geometry</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>R146C497</td>
      <td>60142.919468</td>
      <td>2.260731e+08</td>
      <td>POLYGON ((-8733007.764 4224658.634, -8738250.3...</td>
    </tr>
  </tbody>
</table>
</div>
```

:::
:::


::: {.cell execution_count=6}
``` {.python .cell-code}
ax = cell.boundary.plot()
ax.set_axis_off()
_ = ax.set_title('Grid from shapefile: 12 x 12 km')
plt.tight_layout()
```

::: {.cell-output .cell-output-display}
![](2-intro_files/figure-html/cell-7-output-1.svg){}
:::
:::


::: {.cell execution_count=7}
``` {.python .cell-code}
cell.explore()
```

::: {.cell-output .cell-output-display execution_count=7}

```{=html}
<div style="width:100%;"><div style="position:relative;width:100%;height:0;padding-bottom:60%;"><span style="color:#565656">Make this Notebook Trusted to load map: File -> Trust Notebook</span><iframe srcdoc="&lt;!DOCTYPE html&gt;
&lt;html&gt;
&lt;head&gt;
    
    &lt;meta http-equiv=&quot;content-type&quot; content=&quot;text/html; charset=UTF-8&quot; /&gt;
    
        &lt;script&gt;
            L_NO_TOUCH = false;
            L_DISABLE_3D = false;
        &lt;/script&gt;
    
    &lt;style&gt;html, body {width: 100%;height: 100%;margin: 0;padding: 0;}&lt;/style&gt;
    &lt;style&gt;#map {position:absolute;top:0;bottom:0;right:0;left:0;}&lt;/style&gt;
    &lt;script src=&quot;https://cdn.jsdelivr.net/npm/leaflet@1.9.3/dist/leaflet.js&quot;&gt;&lt;/script&gt;
    &lt;script src=&quot;https://code.jquery.com/jquery-1.12.4.min.js&quot;&gt;&lt;/script&gt;
    &lt;script src=&quot;https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.bundle.min.js&quot;&gt;&lt;/script&gt;
    &lt;script src=&quot;https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.js&quot;&gt;&lt;/script&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdn.jsdelivr.net/npm/leaflet@1.9.3/dist/leaflet.css&quot;/&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css&quot;/&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://netdna.bootstrapcdn.com/bootstrap/3.0.0/css/bootstrap.min.css&quot;/&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.2.0/css/all.min.css&quot;/&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.css&quot;/&gt;
    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdn.jsdelivr.net/gh/python-visualization/folium/folium/templates/leaflet.awesome.rotate.min.css&quot;/&gt;
    
            &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width,
                initial-scale=1.0, maximum-scale=1.0, user-scalable=no&quot; /&gt;
            &lt;style&gt;
                #map_b70d712a386da276168c48036ba9854e {
                    position: relative;
                    width: 100.0%;
                    height: 100.0%;
                    left: 0.0%;
                    top: 0.0%;
                }
                .leaflet-container { font-size: 1rem; }
            &lt;/style&gt;
        
    
                    &lt;style&gt;
                        .foliumtooltip {
                            
                        }
                       .foliumtooltip table{
                            margin: auto;
                        }
                        .foliumtooltip tr{
                            text-align: left;
                        }
                        .foliumtooltip th{
                            padding: 2px; padding-right: 8px;
                        }
                    &lt;/style&gt;
            
&lt;/head&gt;
&lt;body&gt;
    
    
            &lt;div class=&quot;folium-map&quot; id=&quot;map_b70d712a386da276168c48036ba9854e&quot; &gt;&lt;/div&gt;
        
&lt;/body&gt;
&lt;script&gt;
    
    
            var map_b70d712a386da276168c48036ba9854e = L.map(
                &quot;map_b70d712a386da276168c48036ba9854e&quot;,
                {
                    center: [35.41360412198978, -78.53675982344929],
                    crs: L.CRS.EPSG3857,
                    zoom: 10,
                    zoomControl: true,
                    preferCanvas: false,
                }
            );
            L.control.scale().addTo(map_b70d712a386da276168c48036ba9854e);

            

        
    
            var tile_layer_243fb61238690c7000bf0f8ecece5f9b = L.tileLayer(
                &quot;https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png&quot;,
                {&quot;attribution&quot;: &quot;Data by \u0026copy; \u003ca target=\&quot;_blank\&quot; href=\&quot;http://openstreetmap.org\&quot;\u003eOpenStreetMap\u003c/a\u003e, under \u003ca target=\&quot;_blank\&quot; href=\&quot;http://www.openstreetmap.org/copyright\&quot;\u003eODbL\u003c/a\u003e.&quot;, &quot;detectRetina&quot;: false, &quot;maxNativeZoom&quot;: 18, &quot;maxZoom&quot;: 18, &quot;minZoom&quot;: 0, &quot;noWrap&quot;: false, &quot;opacity&quot;: 1, &quot;subdomains&quot;: &quot;abc&quot;, &quot;tms&quot;: false}
            ).addTo(map_b70d712a386da276168c48036ba9854e);
        
    
            map_b70d712a386da276168c48036ba9854e.fitBounds(
                [[35.34284968968893, -78.62357613774547], [35.484358554290615, -78.4499435091531]],
                {}
            );
        
    
        function geo_json_8c1daed0ff5bf2ee68127e0f2ad491e6_styler(feature) {
            switch(feature.id) {
                default:
                    return {&quot;fillOpacity&quot;: 0.5, &quot;weight&quot;: 2};
            }
        }
        function geo_json_8c1daed0ff5bf2ee68127e0f2ad491e6_highlighter(feature) {
            switch(feature.id) {
                default:
                    return {&quot;fillOpacity&quot;: 0.75};
            }
        }
        function geo_json_8c1daed0ff5bf2ee68127e0f2ad491e6_pointToLayer(feature, latlng) {
            var opts = {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;#3388ff&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;#3388ff&quot;, &quot;fillOpacity&quot;: 0.2, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 2, &quot;stroke&quot;: true, &quot;weight&quot;: 3};
            
            let style = geo_json_8c1daed0ff5bf2ee68127e0f2ad491e6_styler(feature)
            Object.assign(opts, style)
            
            return new L.CircleMarker(latlng, opts)
        }

        function geo_json_8c1daed0ff5bf2ee68127e0f2ad491e6_onEachFeature(feature, layer) {
            layer.on({
                mouseout: function(e) {
                    if(typeof e.target.setStyle === &quot;function&quot;){
                        geo_json_8c1daed0ff5bf2ee68127e0f2ad491e6.resetStyle(e.target);
                    }
                },
                mouseover: function(e) {
                    if(typeof e.target.setStyle === &quot;function&quot;){
                        const highlightStyle = geo_json_8c1daed0ff5bf2ee68127e0f2ad491e6_highlighter(e.target.feature)
                        e.target.setStyle(highlightStyle);
                    }
                },
            });
        };
        var geo_json_8c1daed0ff5bf2ee68127e0f2ad491e6 = L.geoJson(null, {
                onEachFeature: geo_json_8c1daed0ff5bf2ee68127e0f2ad491e6_onEachFeature,
            
                style: geo_json_8c1daed0ff5bf2ee68127e0f2ad491e6_styler,
                pointToLayer: geo_json_8c1daed0ff5bf2ee68127e0f2ad491e6_pointToLayer
        });

        function geo_json_8c1daed0ff5bf2ee68127e0f2ad491e6_add (data) {
            geo_json_8c1daed0ff5bf2ee68127e0f2ad491e6
                .addData(data)
                .addTo(map_b70d712a386da276168c48036ba9854e);
        }
            geo_json_8c1daed0ff5bf2ee68127e0f2ad491e6_add({&quot;bbox&quot;: [-78.62357613774547, 35.34284968968893, -78.4499435091531, 35.484358554290615], &quot;features&quot;: [{&quot;bbox&quot;: [-78.62357613774547, 35.34284968968893, -78.4499435091531, 35.484358554290615], &quot;geometry&quot;: {&quot;coordinates&quot;: [[[-78.4499435091531, 35.44601079149053], [-78.4970385718653, 35.34284968968893], [-78.62357613774547, 35.38112534319517], [-78.57665372045108, 35.484358554290615], [-78.4499435091531, 35.44601079149053]]], &quot;type&quot;: &quot;Polygon&quot;}, &quot;id&quot;: &quot;4&quot;, &quot;properties&quot;: {&quot;Crossmodel&quot;: &quot;R146C497&quot;, &quot;OBJECTID&quot;: 5, &quot;Shape_Area&quot;: 226073092.218, &quot;Shape_Leng&quot;: 60142.9194675}, &quot;type&quot;: &quot;Feature&quot;}], &quot;type&quot;: &quot;FeatureCollection&quot;});

        
    
    geo_json_8c1daed0ff5bf2ee68127e0f2ad491e6.bindTooltip(
    function(layer){
    let div = L.DomUtil.create(&#x27;div&#x27;);
    
    let handleObject = feature=&gt;typeof(feature)==&#x27;object&#x27; ? JSON.stringify(feature) : feature;
    let fields = [&quot;OBJECTID&quot;, &quot;Crossmodel&quot;, &quot;Shape_Leng&quot;, &quot;Shape_Area&quot;];
    let aliases = [&quot;OBJECTID&quot;, &quot;Crossmodel&quot;, &quot;Shape_Leng&quot;, &quot;Shape_Area&quot;];
    let table = &#x27;&lt;table&gt;&#x27; +
        String(
        fields.map(
        (v,i)=&gt;
        `&lt;tr&gt;
            &lt;th&gt;${aliases[i]}&lt;/th&gt;
            
            &lt;td&gt;${handleObject(layer.feature.properties[v])}&lt;/td&gt;
        &lt;/tr&gt;`).join(&#x27;&#x27;))
    +&#x27;&lt;/table&gt;&#x27;;
    div.innerHTML=table;
    
    return div
    }
    ,{&quot;className&quot;: &quot;foliumtooltip&quot;, &quot;sticky&quot;: true});
                     
&lt;/script&gt;
&lt;/html&gt;" style="position:absolute;width:100%;height:100%;left:0;top:0;border:none !important;" allowfullscreen webkitallowfullscreen mozallowfullscreen></iframe></div></div>
```

:::
:::


## Load data from `*.csv` files

Each entry (row) in the `.csv` has a `Crossmodel` column (e.g. `R146C497`)
which corresponds to a row in our `shapefile` that uniquely determines its
location on the Earth.

We can associate with each of the `.csv`s the `geometry` used in our
`shapefile` to position our data on the globe.

::: {.cell execution_count=8}
``` {.python .cell-code}
import pandas as pd
csvs = [i for i in DATA_DIR.rglob('*.csv')]
data = {}
for f in csvs:
    key = f.stem
    tmp = pd.read_csv(f.as_posix())
    gdf = shape.merge(tmp, on='Crossmodel')
    gdf['boundary'] = gdf.boundary
    gdf['centroid'] = gdf.centroid
    data[key] = gdf
    console.log(f"data['{key}'].shape={data[key].shape}")
```

::: {.cell-output .cell-output-display}

```{=html}
<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #696969; text-decoration-color: #696969">[20:42:54] </span>data<span style="font-weight: bold">[</span><span style="color: #008000; text-decoration-color: #008000">'FireWeatherIndex_Wildfire'</span><span style="font-weight: bold">]</span>.<span style="color: #7d8697; text-decoration-color: #7d8697">shape</span>=<span style="font-weight: bold">(</span><span style="color: #2094f3; text-decoration-color: #2094f3">62834</span>, <span style="color: #2094f3; text-decoration-color: #2094f3">35</span><span style="font-weight: bold">)</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
</pre>
```

:::

::: {.cell-output .cell-output-display}

```{=html}
<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #696969; text-decoration-color: #696969">           </span>data<span style="font-weight: bold">[</span><span style="color: #008000; text-decoration-color: #008000">'HeatingDegreeDays'</span><span style="font-weight: bold">]</span>.<span style="color: #7d8697; text-decoration-color: #7d8697">shape</span>=<span style="font-weight: bold">(</span><span style="color: #2094f3; text-decoration-color: #2094f3">62834</span>, <span style="color: #2094f3; text-decoration-color: #2094f3">10</span><span style="font-weight: bold">)</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
</pre>
```

:::

::: {.cell-output .cell-output-display}

```{=html}
<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #696969; text-decoration-color: #696969">[20:42:55] </span>data<span style="font-weight: bold">[</span><span style="color: #008000; text-decoration-color: #008000">'AnnualTemperatureMinimum'</span><span style="font-weight: bold">]</span>.<span style="color: #7d8697; text-decoration-color: #7d8697">shape</span>=<span style="font-weight: bold">(</span><span style="color: #2094f3; text-decoration-color: #2094f3">62834</span>, <span style="color: #2094f3; text-decoration-color: #2094f3">18</span><span style="font-weight: bold">)</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
</pre>
```

:::

::: {.cell-output .cell-output-display}

```{=html}
<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #696969; text-decoration-color: #696969">           </span>data<span style="font-weight: bold">[</span><span style="color: #008000; text-decoration-color: #008000">'SeasonalTemperatureMaximum'</span><span style="font-weight: bold">]</span>.<span style="color: #7d8697; text-decoration-color: #7d8697">shape</span>=<span style="font-weight: bold">(</span><span style="color: #2094f3; text-decoration-color: #2094f3">62834</span>, <span style="color: #2094f3; text-decoration-color: #2094f3">27</span><span style="font-weight: bold">)</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
</pre>
```

:::

::: {.cell-output .cell-output-display}

```{=html}
<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #696969; text-decoration-color: #696969">           </span>data<span style="font-weight: bold">[</span><span style="color: #008000; text-decoration-color: #008000">'ConsecutiveDayswithNoPrecipitation'</span><span style="font-weight: bold">]</span>.<span style="color: #7d8697; text-decoration-color: #7d8697">shape</span>=<span style="font-weight: bold">(</span><span style="color: #2094f3; text-decoration-color: #2094f3">55896</span>, <span style="color: #2094f3; text-decoration-color: #2094f3">19</span><span style="font-weight: bold">)</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                         
</pre>
```

:::

::: {.cell-output .cell-output-display}

```{=html}
<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #696969; text-decoration-color: #696969">           </span>data<span style="font-weight: bold">[</span><span style="color: #008000; text-decoration-color: #008000">'SeasonalTemperatureMinimum'</span><span style="font-weight: bold">]</span>.<span style="color: #7d8697; text-decoration-color: #7d8697">shape</span>=<span style="font-weight: bold">(</span><span style="color: #2094f3; text-decoration-color: #2094f3">62834</span>, <span style="color: #2094f3; text-decoration-color: #2094f3">27</span><span style="font-weight: bold">)</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
</pre>
```

:::

::: {.cell-output .cell-output-display}

```{=html}
<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #696969; text-decoration-color: #696969">           </span>data<span style="font-weight: bold">[</span><span style="color: #008000; text-decoration-color: #008000">'WindSpeed'</span><span style="font-weight: bold">]</span>.<span style="color: #7d8697; text-decoration-color: #7d8697">shape</span>=<span style="font-weight: bold">(</span><span style="color: #2094f3; text-decoration-color: #2094f3">62834</span>, <span style="color: #2094f3; text-decoration-color: #2094f3">18</span><span style="font-weight: bold">)</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
</pre>
```

:::

::: {.cell-output .cell-output-display}

```{=html}
<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #696969; text-decoration-color: #696969">           </span>data<span style="font-weight: bold">[</span><span style="color: #008000; text-decoration-color: #008000">'AnnualTemperatureMaximum'</span><span style="font-weight: bold">]</span>.<span style="color: #7d8697; text-decoration-color: #7d8697">shape</span>=<span style="font-weight: bold">(</span><span style="color: #2094f3; text-decoration-color: #2094f3">62834</span>, <span style="color: #2094f3; text-decoration-color: #2094f3">18</span><span style="font-weight: bold">)</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
</pre>
```

:::

::: {.cell-output .cell-output-display}

```{=html}
<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace"><span style="color: #696969; text-decoration-color: #696969">           </span>data<span style="font-weight: bold">[</span><span style="color: #008000; text-decoration-color: #008000">'Precipitation_inches_AnnualTotal'</span><span style="font-weight: bold">]</span>.<span style="color: #7d8697; text-decoration-color: #7d8697">shape</span>=<span style="font-weight: bold">(</span><span style="color: #2094f3; text-decoration-color: #2094f3">55896</span>, <span style="color: #2094f3; text-decoration-color: #2094f3">18</span><span style="font-weight: bold">)</span>                                                                                                                                                                                                                                                                                                                                                                                                                                                           
</pre>
```

:::
:::


## Look at the WindSpeed data

Lets inspect one of the entries in our `data[(...)]` dictionary, `WindSpeed`, for example:

::: {.cell execution_count=9}
``` {.python .cell-code}
data["WindSpeed"].head()
```

::: {.cell-output .cell-output-display execution_count=9}

```{=html}
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>OBJECTID</th>
      <th>Crossmodel</th>
      <th>Shape_Leng</th>
      <th>Shape_Area</th>
      <th>geometry</th>
      <th>hist</th>
      <th>rcp45_midc</th>
      <th>rcp45_endc</th>
      <th>rcp85_midc</th>
      <th>rcp85_endc</th>
      <th>mid45_hist</th>
      <th>end45_hist</th>
      <th>mid85_hist</th>
      <th>end85_hist</th>
      <th>mid85_45</th>
      <th>end85_45</th>
      <th>boundary</th>
      <th>centroid</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>R161C438</td>
      <td>63614.764866</td>
      <td>2.529273e+08</td>
      <td>POLYGON ((-9530601.177 4726046.614, -9534793.8...</td>
      <td>7.21540</td>
      <td>7.19415</td>
      <td>7.38917</td>
      <td>7.30470</td>
      <td>7.22690</td>
      <td>-0.021256</td>
      <td>0.173764</td>
      <td>0.089297</td>
      <td>0.011499</td>
      <td>0.110553</td>
      <td>-0.162264</td>
      <td>LINESTRING (-9530601.177 4726046.614, -9534793...</td>
      <td>POINT (-9540369.710 4720470.575)</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>R125C222</td>
      <td>61384.219597</td>
      <td>2.355013e+08</td>
      <td>POLYGON ((-12959076.287 4395610.472, -12974301...</td>
      <td>8.32612</td>
      <td>8.11360</td>
      <td>8.26028</td>
      <td>8.17420</td>
      <td>8.02081</td>
      <td>-0.212523</td>
      <td>-0.065843</td>
      <td>-0.151919</td>
      <td>-0.305307</td>
      <td>0.060603</td>
      <td>-0.239465</td>
      <td>LINESTRING (-12959076.287 4395610.472, -129743...</td>
      <td>POINT (-12967596.341 4402326.143)</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>R121C235</td>
      <td>61111.892875</td>
      <td>2.334164e+08</td>
      <td>POLYGON ((-12754805.395 4355815.951, -12770000...</td>
      <td>8.58573</td>
      <td>8.59828</td>
      <td>8.56058</td>
      <td>8.54483</td>
      <td>8.55421</td>
      <td>0.012547</td>
      <td>-0.025149</td>
      <td>-0.040898</td>
      <td>-0.031519</td>
      <td>-0.053446</td>
      <td>-0.006370</td>
      <td>LINESTRING (-12754805.395 4355815.951, -127700...</td>
      <td>POINT (-12763132.114 4362694.465)</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>R169C431</td>
      <td>64716.234995</td>
      <td>2.617618e+08</td>
      <td>POLYGON ((-9605729.481 4879238.815, -9609863.1...</td>
      <td>9.17284</td>
      <td>9.21681</td>
      <td>9.44966</td>
      <td>9.26548</td>
      <td>9.14917</td>
      <td>0.043968</td>
      <td>0.276813</td>
      <td>0.092635</td>
      <td>-0.023674</td>
      <td>0.048667</td>
      <td>-0.300487</td>
      <td>LINESTRING (-9605729.481 4879238.815, -9609863...</td>
      <td>POINT (-9615619.029 4873482.586)</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>R146C497</td>
      <td>60142.919468</td>
      <td>2.260731e+08</td>
      <td>POLYGON ((-8733007.764 4224658.634, -8738250.3...</td>
      <td>8.25430</td>
      <td>8.19130</td>
      <td>8.34417</td>
      <td>8.29698</td>
      <td>8.29411</td>
      <td>-0.062996</td>
      <td>0.089874</td>
      <td>0.042684</td>
      <td>0.039807</td>
      <td>0.105680</td>
      <td>-0.050067</td>
      <td>LINESTRING (-8733007.764 4224658.634, -8738250...</td>
      <td>POINT (-8742676.917 4220233.536)</td>
    </tr>
  </tbody>
</table>
</div>
```

:::
:::


We see that each entry has a `geometry` column, as well as columns for
`{hist,rcp45_midc, rcp45_endc, rcp85_midc, rcp85_endc, ...}` which contains the
numerical value of the `WindSpeed` in each cell under different scenarios at
different points in time.

<!-- We can see this explicitly by plotting this value for a single cell: -->

Let's look at the `WindSpeed` for our individual cell:

::: {.cell execution_count=10}
``` {.python .cell-code}
cell_wind = data["WindSpeed"][data["WindSpeed"]["Crossmodel"] == 'R146C497']
```
:::


::: {.cell execution_count=11}
``` {.python .cell-code}
ax = cell_wind.plot(column='hist', legend=True)
ax.set_axis_off()
_ = ax.set_title("WindSpeed [Hist] for CELL: R146C497")
```

::: {.cell-output .cell-output-display}
![](2-intro_files/figure-html/cell-12-output-1.svg){}
:::
:::


## Visualizing our Data

Lets inspect the first few entries from our Shapefile:

::: {#fig-increasing-cells style="text-align:left!important;"}

::: {.cell execution_count=12}
``` {.python .cell-code code-fold="true"}
fig, ax = plt.subplots(
    figsize=(12, 3.5),
    nrows=1,
    ncols=3,
    sharey='row'
)
ax = ax.flatten()
pairs = {
    '1k': list(range(1000)),
    '5k': list(range(5000)),
    '20k': list(range(20000)),
}
for idx, (key, val) in enumerate(pairs.items()):
    ax[idx] = shape.loc[val, :].plot(ax=ax[idx])
    ax[idx].set_axis_off()
    _ = ax[idx].set_title(f"First {key} cells")
plt.tight_layout()
```

::: {.cell-output .cell-output-display}
![](2-intro_files/figure-html/cell-13-output-1.svg){}
:::
:::


As we include more cells, we see the outline of the US beginning to take shape.
:::


[^venv]:
    Preferably, inside a virtual environment, e.g.
    ```bash
    $ mkdir -p ~/.venvs/ClimRR
    $ python3 -m venv ~/.venvs/ClimRR --system-site-packages
    $ source ~/.venvs/ClimRR/bin/activate
    $ python3 -m pip install git+https://github.com/saforem2/climate-analysis
    ```

