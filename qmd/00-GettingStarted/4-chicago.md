---
callout-appearance: simple
editor:
  render-on-save: true
execute:
  freeze: true
title: Chicago Analysis
---







::: {.cell execution_count=1}
``` {.python .cell-code code-fold="true" code-summary="Imports"}
%matplotlib inline
import matplotlib_inline
import matplotlib.pyplot as plt
import geopandas as gpd
import warnings

import matplotlib.pyplot as plt

# from enrich.console import Console, get_theme
matplotlib_inline.backend_inline.set_matplotlib_formats('svg')
from ClimRR import get_logger, set_plot_style
from ClimRR.data import DATA_DIR
set_plot_style()
log = get_logger('ClimRR')
from rich.console import Console as rConsole
from enrich.style import STYLES
from rich.theme import Theme

theme = Theme(STYLES)
log = get_logger('ClimRR')
console = rConsole(theme=theme, log_path=False, markup=True)
```

::: {.cell-output .cell-output-display}

```{=html}
<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">Using updated plot style for matplotlib
</pre>
```

:::
:::


::: {.cell execution_count=2}
``` {.python .cell-code}
from ClimRR.data import load_shapefile, load_csvs

shape = load_shapefile()
data = load_csvs(shape)
```

::: {.cell-output .cell-output-display}

```{=html}
<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">data<span style="font-weight: bold">[</span><span style="color: #008000; text-decoration-color: #008000">'FireWeatherIndex_Wildfire'</span><span style="font-weight: bold">]</span>.<span style="color: #7d8697; text-decoration-color: #7d8697">shape</span>=<span style="font-weight: bold">(</span><span style="color: #2094f3; text-decoration-color: #2094f3">62834</span>, <span style="color: #2094f3; text-decoration-color: #2094f3">35</span><span style="font-weight: bold">)</span>
</pre>
```

:::

::: {.cell-output .cell-output-display}

```{=html}
<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">data<span style="font-weight: bold">[</span><span style="color: #008000; text-decoration-color: #008000">'HeatingDegreeDays'</span><span style="font-weight: bold">]</span>.<span style="color: #7d8697; text-decoration-color: #7d8697">shape</span>=<span style="font-weight: bold">(</span><span style="color: #2094f3; text-decoration-color: #2094f3">62834</span>, <span style="color: #2094f3; text-decoration-color: #2094f3">10</span><span style="font-weight: bold">)</span>
</pre>
```

:::

::: {.cell-output .cell-output-display}

```{=html}
<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">data<span style="font-weight: bold">[</span><span style="color: #008000; text-decoration-color: #008000">'AnnualTemperatureMinimum'</span><span style="font-weight: bold">]</span>.<span style="color: #7d8697; text-decoration-color: #7d8697">shape</span>=<span style="font-weight: bold">(</span><span style="color: #2094f3; text-decoration-color: #2094f3">62834</span>, <span style="color: #2094f3; text-decoration-color: #2094f3">18</span><span style="font-weight: bold">)</span>
</pre>
```

:::

::: {.cell-output .cell-output-display}

```{=html}
<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">data<span style="font-weight: bold">[</span><span style="color: #008000; text-decoration-color: #008000">'SeasonalTemperatureMaximum'</span><span style="font-weight: bold">]</span>.<span style="color: #7d8697; text-decoration-color: #7d8697">shape</span>=<span style="font-weight: bold">(</span><span style="color: #2094f3; text-decoration-color: #2094f3">62834</span>, <span style="color: #2094f3; text-decoration-color: #2094f3">27</span><span style="font-weight: bold">)</span>
</pre>
```

:::

::: {.cell-output .cell-output-display}

```{=html}
<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">data<span style="font-weight: bold">[</span><span style="color: #008000; text-decoration-color: #008000">'ConsecutiveDayswithNoPrecipitation'</span><span style="font-weight: bold">]</span>.<span style="color: #7d8697; text-decoration-color: #7d8697">shape</span>=<span style="font-weight: bold">(</span><span style="color: #2094f3; text-decoration-color: #2094f3">55896</span>, <span style="color: #2094f3; text-decoration-color: #2094f3">19</span><span style="font-weight: bold">)</span>
</pre>
```

:::

::: {.cell-output .cell-output-display}

```{=html}
<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">data<span style="font-weight: bold">[</span><span style="color: #008000; text-decoration-color: #008000">'SeasonalTemperatureMinimum'</span><span style="font-weight: bold">]</span>.<span style="color: #7d8697; text-decoration-color: #7d8697">shape</span>=<span style="font-weight: bold">(</span><span style="color: #2094f3; text-decoration-color: #2094f3">62834</span>, <span style="color: #2094f3; text-decoration-color: #2094f3">27</span><span style="font-weight: bold">)</span>
</pre>
```

:::

::: {.cell-output .cell-output-display}

```{=html}
<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">data<span style="font-weight: bold">[</span><span style="color: #008000; text-decoration-color: #008000">'WindSpeed'</span><span style="font-weight: bold">]</span>.<span style="color: #7d8697; text-decoration-color: #7d8697">shape</span>=<span style="font-weight: bold">(</span><span style="color: #2094f3; text-decoration-color: #2094f3">62834</span>, <span style="color: #2094f3; text-decoration-color: #2094f3">18</span><span style="font-weight: bold">)</span>
</pre>
```

:::

::: {.cell-output .cell-output-display}

```{=html}
<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">data<span style="font-weight: bold">[</span><span style="color: #008000; text-decoration-color: #008000">'AnnualTemperatureMaximum'</span><span style="font-weight: bold">]</span>.<span style="color: #7d8697; text-decoration-color: #7d8697">shape</span>=<span style="font-weight: bold">(</span><span style="color: #2094f3; text-decoration-color: #2094f3">62834</span>, <span style="color: #2094f3; text-decoration-color: #2094f3">18</span><span style="font-weight: bold">)</span>
</pre>
```

:::

::: {.cell-output .cell-output-display}

```{=html}
<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">data<span style="font-weight: bold">[</span><span style="color: #008000; text-decoration-color: #008000">'Precipitation_inches_AnnualTotal'</span><span style="font-weight: bold">]</span>.<span style="color: #7d8697; text-decoration-color: #7d8697">shape</span>=<span style="font-weight: bold">(</span><span style="color: #2094f3; text-decoration-color: #2094f3">55896</span>, <span style="color: #2094f3; text-decoration-color: #2094f3">18</span><span style="font-weight: bold">)</span>
</pre>
```

:::
:::


::: {.cell execution_count=3}
``` {.python .cell-code}
square = shape[shape["Crossmodel"] == 'R146C497']
fig, ax = plt.subplots(figsize=(4, 3))
ax = square.boundary.plot(ax=ax)
ax.set_axis_off()
plt.tight_layout()
```

::: {.cell-output .cell-output-display}
![](4-chicago_files/figure-html/cell-4-output-1.svg){}
:::
:::


::: {.cell execution_count=4}
``` {.python .cell-code}
import geopandas as gpd
import geodatasets
chipop = gpd.read_file(
    geodatasets.get_path('geoda.chicago_commpop')
).to_crs(square.crs)
chihealth = gpd.read_file(
    geodatasets.get_path('geoda.chicago_health')
).to_crs(square.crs)
chigroc = gpd.read_file(
    geodatasets.get_path('geoda.groceries')
).to_crs(square.crs)
```
:::


We can inspect this data, looking at the `chipop.boundary` for example

::: {.cell execution_count=5}
``` {.python .cell-code}
chipop['boundary'] = chipop.boundary
```
:::


::: {.cell execution_count=6}
``` {.python .cell-code}
fig, ax = plt.subplots(figsize=(10, 7))
ax = chipop.boundary.plot(linewidth=0.8, color='#838383', ax=ax)
ax.set_axis_off()
_ = ax.set_title('Chicago Neighborhoods')
```

::: {.cell-output .cell-output-display}
![](4-chicago_files/figure-html/cell-7-output-1.svg){}
:::
:::


Which we can use to plot the population (by neighborhood, in  this case):

::: {.cell execution_count=7}
``` {.python .cell-code}
fig, ax = plt.subplots(figsize=(10, 7))
ax = chipop.to_crs(square.crs).plot(column="POP2010", legend=True, ax=ax)
ax.set_axis_off()
_ = ax.set_title(f"Chicago population by Neighborhood [2010]")
```

::: {.cell-output .cell-output-display}
![](4-chicago_files/figure-html/cell-8-output-1.svg){}
:::
:::


::: {.cell execution_count=8}
``` {.python .cell-code}
wtown = chipop[chipop["community"] == 'WEST TOWN']
humboldt = chipop[chipop["community"] == 'HUMBOLDT PARK']
```
:::


::: {.cell execution_count=9}
``` {.python .cell-code}
humboldt.explore()
```

::: {.cell-output .cell-output-display execution_count=9}

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
                #map_a6aeb5e3309153446cc717acf9c5b267 {
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
    
    
            &lt;div class=&quot;folium-map&quot; id=&quot;map_a6aeb5e3309153446cc717acf9c5b267&quot; &gt;&lt;/div&gt;
        
&lt;/body&gt;
&lt;script&gt;
    
    
            var map_a6aeb5e3309153446cc717acf9c5b267 = L.map(
                &quot;map_a6aeb5e3309153446cc717acf9c5b267&quot;,
                {
                    center: [41.90087280603366, -87.71649034808647],
                    crs: L.CRS.EPSG3857,
                    zoom: 10,
                    zoomControl: true,
                    preferCanvas: false,
                }
            );
            L.control.scale().addTo(map_a6aeb5e3309153446cc717acf9c5b267);

            

        
    
            var tile_layer_92da1b2fedfb5c443aff8cc5e70fb25e = L.tileLayer(
                &quot;https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png&quot;,
                {&quot;attribution&quot;: &quot;Data by \u0026copy; \u003ca target=\&quot;_blank\&quot; href=\&quot;http://openstreetmap.org\&quot;\u003eOpenStreetMap\u003c/a\u003e, under \u003ca target=\&quot;_blank\&quot; href=\&quot;http://www.openstreetmap.org/copyright\&quot;\u003eODbL\u003c/a\u003e.&quot;, &quot;detectRetina&quot;: false, &quot;maxNativeZoom&quot;: 18, &quot;maxZoom&quot;: 18, &quot;minZoom&quot;: 0, &quot;noWrap&quot;: false, &quot;opacity&quot;: 1, &quot;subdomains&quot;: &quot;abc&quot;, &quot;tms&quot;: false}
            ).addTo(map_a6aeb5e3309153446cc717acf9c5b267);
        
    
            map_a6aeb5e3309153446cc717acf9c5b267.fitBounds(
                [[41.88782316811692, -87.74141068668523], [41.9139224439504, -87.69157000948772]],
                {}
            );
        
    
        function geo_json_28838c2b84b3b08dbfb756448f58bfed_styler(feature) {
            switch(feature.id) {
                default:
                    return {&quot;fillOpacity&quot;: 0.5, &quot;weight&quot;: 2};
            }
        }
        function geo_json_28838c2b84b3b08dbfb756448f58bfed_highlighter(feature) {
            switch(feature.id) {
                default:
                    return {&quot;fillOpacity&quot;: 0.75};
            }
        }
        function geo_json_28838c2b84b3b08dbfb756448f58bfed_pointToLayer(feature, latlng) {
            var opts = {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;#3388ff&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;#3388ff&quot;, &quot;fillOpacity&quot;: 0.2, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 2, &quot;stroke&quot;: true, &quot;weight&quot;: 3};
            
            let style = geo_json_28838c2b84b3b08dbfb756448f58bfed_styler(feature)
            Object.assign(opts, style)
            
            return new L.CircleMarker(latlng, opts)
        }

        function geo_json_28838c2b84b3b08dbfb756448f58bfed_onEachFeature(feature, layer) {
            layer.on({
                mouseout: function(e) {
                    if(typeof e.target.setStyle === &quot;function&quot;){
                        geo_json_28838c2b84b3b08dbfb756448f58bfed.resetStyle(e.target);
                    }
                },
                mouseover: function(e) {
                    if(typeof e.target.setStyle === &quot;function&quot;){
                        const highlightStyle = geo_json_28838c2b84b3b08dbfb756448f58bfed_highlighter(e.target.feature)
                        e.target.setStyle(highlightStyle);
                    }
                },
            });
        };
        var geo_json_28838c2b84b3b08dbfb756448f58bfed = L.geoJson(null, {
                onEachFeature: geo_json_28838c2b84b3b08dbfb756448f58bfed_onEachFeature,
            
                style: geo_json_28838c2b84b3b08dbfb756448f58bfed_styler,
                pointToLayer: geo_json_28838c2b84b3b08dbfb756448f58bfed_pointToLayer
        });

        function geo_json_28838c2b84b3b08dbfb756448f58bfed_add (data) {
            geo_json_28838c2b84b3b08dbfb756448f58bfed
                .addData(data)
                .addTo(map_a6aeb5e3309153446cc717acf9c5b267);
        }
            geo_json_28838c2b84b3b08dbfb756448f58bfed_add({&quot;bbox&quot;: [-87.74141068668523, 41.88782316811692, -87.69157000948772, 41.9139224439504], &quot;features&quot;: [{&quot;bbox&quot;: [-87.74141068668523, 41.88782316811692, -87.69157000948772, 41.9139224439504], &quot;geometry&quot;: {&quot;coordinates&quot;: [[[[-87.69157000948772, 41.88819563418098], [-87.6950063048167, 41.8881563696754], [-87.69520212162912, 41.888154128922224], [-87.69540013131694, 41.88818507270278], [-87.69560781293417, 41.88821298285437], [-87.69579902942102, 41.88823462667609], [-87.69594580432188, 41.88824744748701], [-87.6961669203025, 41.888263081549255], [-87.69638854046876, 41.88827425886155], [-87.69652530140336, 41.888278447080154], [-87.69666712656904, 41.88828129191418], [-87.69705919482163, 41.88827900578061], [-87.69713815772664, 41.88827875692503], [-87.69760877366438, 41.88827175885854], [-87.69859405096075, 41.88826040023992], [-87.6989457404786, 41.888256169320144], [-87.70012660748259, 41.88824210453234], [-87.70035341632193, 41.88823923855547], [-87.7005788476445, 41.888236364540454], [-87.7012014238564, 41.88822847324952], [-87.70141195323203, 41.88822620574601], [-87.70141034635363, 41.88816395032566], [-87.70141047232082, 41.888163950469995], [-87.70177773218956, 41.888164067146135], [-87.70386833267622, 41.88816422578379], [-87.7038710669997, 41.88830659813613], [-87.70422918926009, 41.888301699958696], [-87.70484717281452, 41.88829410677201], [-87.70508132683977, 41.888291271655206], [-87.70546515290167, 41.88828685354515], [-87.7060202365489, 41.88827993921636], [-87.70624061802887, 41.888277026225886], [-87.70633798743931, 41.88827549888407], [-87.70645641013847, 41.888274087759946], [-87.70653354286333, 41.88827313694062], [-87.70685860495789, 41.888269079201194], [-87.70723417732744, 41.888263581059235], [-87.70748167663655, 41.888257383226495], [-87.70756158108388, 41.88825473139528], [-87.70770853260103, 41.888249700551285], [-87.70788030565363, 41.88824137440564], [-87.70805069891749, 41.888233383520564], [-87.70821604524805, 41.88822502215365], [-87.70841719448023, 41.88821719814058], [-87.70863439281456, 41.88821117623348], [-87.70883686935291, 41.88820850416283], [-87.70937588222975, 41.88820182897162], [-87.70957376753715, 41.888199130381], [-87.7096747734814, 41.888197964364444], [-87.7108271746199, 41.88818397768832], [-87.71109071332077, 41.88818060408757], [-87.71122066413054, 41.888178299358685], [-87.71135149773646, 41.888177214140946], [-87.71170224478738, 41.888172792501656], [-87.71180832815772, 41.8881714550562], [-87.71198487311716, 41.88816913955515], [-87.71288222814896, 41.88815736644174], [-87.71355346870156, 41.88814898503168], [-87.713563900467, 41.888148922231395], [-87.71365789030195, 41.888148355626335], [-87.71373847170321, 41.88814671797067], [-87.71375823907132, 41.888146316387925], [-87.71399226042635, 41.888143512602504], [-87.71411360025446, 41.88814205881936], [-87.71488079688211, 41.88813247159094], [-87.71510576957819, 41.88812956658486], [-87.71542348486564, 41.88812544504564], [-87.71599785350395, 41.888117899910796], [-87.71609105586617, 41.88811668629969], [-87.71657147878615, 41.88811114648552], [-87.71688304820371, 41.88810653290384], [-87.71723288472923, 41.888101892994115], [-87.71723290309369, 41.88810189281822], [-87.71736696706282, 41.888100210501165], [-87.71854049163676, 41.88808523171561], [-87.71902461513716, 41.888078983828535], [-87.71976176564958, 41.8880694661537], [-87.71986001851316, 41.88806827591884], [-87.71987249723587, 41.8880682624487], [-87.72098330194046, 41.8880670559419], [-87.72117495368113, 41.88805128075567], [-87.72220659595077, 41.88803928087666], [-87.7225697625982, 41.88803469536955], [-87.72306653500955, 41.88802841758079], [-87.72343061965701, 41.88802383422926], [-87.72421342574972, 41.88801392478733], [-87.72464970768694, 41.88804470961779], [-87.72464525430091, 41.887836809456566], [-87.72587007906353, 41.887834032629556], [-87.72587189698224, 41.887897257852146], [-87.72587356206537, 41.887993556455434], [-87.72587356201858, 41.88799356139482], [-87.7263212544715, 41.887988038437655], [-87.72680653325332, 41.88798339886705], [-87.72697457667581, 41.8879808562499], [-87.72722004961398, 41.88799450094603], [-87.72732511231783, 41.88800122997002], [-87.72749260274192, 41.88800863156508], [-87.72766013459656, 41.888011573461654], [-87.7278269003386, 41.88800230741632], [-87.7281560807384, 41.887984016763404], [-87.72832114432795, 41.887974844762425], [-87.72839602309755, 41.887970684057315], [-87.72845982736696, 41.88796713868449], [-87.72861871261809, 41.88795830967445], [-87.72993041566589, 41.88794291237627], [-87.73078944115838, 41.887931300378746], [-87.73122882453214, 41.88792537248203], [-87.73246063629962, 41.88791124225324], [-87.73345830676472, 41.88789896379675], [-87.73378841381397, 41.88789485617033], [-87.7349095887857, 41.88788080806522], [-87.7357098519779, 41.88786919605946], [-87.73678511464576, 41.88785557703692], [-87.73796272570338, 41.88784453706838], [-87.73816949684401, 41.88787450852697], [-87.73851549234323, 41.887839168511846], [-87.73931983240804, 41.88783338398475], [-87.74029588319573, 41.88782539341012], [-87.74059567510004, 41.88782316811692], [-87.74060043106633, 41.88795423040556], [-87.7406173871776, 41.888454113402155], [-87.74062672562039, 41.88873510373841], [-87.74065720045614, 41.88960998947832], [-87.74066329227372, 41.88979525718269], [-87.74068470773084, 41.890408706425504], [-87.74069045475291, 41.89058162349734], [-87.74069219241026, 41.890642006120395], [-87.74069436023834, 41.89070547768903], [-87.74070578982442, 41.8909092968274], [-87.74073534184615, 41.891337894754045], [-87.74074886855868, 41.891463856759636], [-87.74058130991014, 41.891462648414155], [-87.74065397799592, 41.89199472131806], [-87.74071510826478, 41.892483854956524], [-87.74072931580996, 41.89258580859565], [-87.74076206223289, 41.89281786588707], [-87.74081902166498, 41.89326169813981], [-87.74086994307278, 41.89366330616705], [-87.74091670321185, 41.89401858412602], [-87.74096118740525, 41.8943717918479], [-87.74102804835346, 41.89488702499056], [-87.74104225444812, 41.894989321847206], [-87.74107090755813, 41.895092200073464], [-87.74106517234318, 41.8951921709637], [-87.74108330092866, 41.895317127491296], [-87.74111219724043, 41.895518978329356], [-87.74113485681197, 41.89565047550979], [-87.74115200407275, 41.89578228756174], [-87.7411631763521, 41.89591475485757], [-87.74116838105263, 41.8960471913766], [-87.74116503387579, 41.89611132077357], [-87.74115527189295, 41.89617404496907], [-87.74114046326375, 41.89623640010768], [-87.7410977644056, 41.89643513771701], [-87.74102097049624, 41.896509549674256], [-87.74102746609044, 41.896589824808224], [-87.74103646327099, 41.89665473136858], [-87.74107438361501, 41.89692829458453], [-87.74108373307617, 41.89735747329672], [-87.74109153543235, 41.89765594950832], [-87.74109610622305, 41.89785698930016], [-87.7410977042027, 41.89793246389895], [-87.74110478027788, 41.89801139732467], [-87.74110809255843, 41.89834861329731], [-87.74111698723057, 41.89867796779867], [-87.74111928180275, 41.89877744079679], [-87.7412124964966, 41.898776086682595], [-87.74122124802568, 41.89887300350576], [-87.74123230437833, 41.89896842232959], [-87.74124887342973, 41.89906352791668], [-87.74126963731156, 41.89915179370318], [-87.741294028213, 41.89924522336092], [-87.7413124438145, 41.899339308541194], [-87.74132534601975, 41.899433708598], [-87.74133073771277, 41.89949616758938], [-87.74134167935509, 41.899852632209324], [-87.7413447972121, 41.900061896323], [-87.74133957276867, 41.90062752613632], [-87.7411636785007, 41.90063142163794], [-87.74117695781975, 41.9011820532129], [-87.74120127198078, 41.90217833748226], [-87.74120719742605, 41.90243152409123], [-87.74120720062707, 41.902431654733505], [-87.74123055316109, 41.903432262585866], [-87.74127187807176, 41.90512224029641], [-87.74129396484425, 41.90602792483947], [-87.74134015013347, 41.90792171410454], [-87.74135437728108, 41.90856874142377], [-87.74141068668523, 41.908657265203736], [-87.74136701600074, 41.909039785808154], [-87.74137265223678, 41.90922505078332], [-87.74137991260315, 41.909433307373305], [-87.74138036112579, 41.909683509058304], [-87.7413769865425, 41.90984938646337], [-87.74137006582518, 41.91000199915824], [-87.74134734480039, 41.91032398637491], [-87.74132384663316, 41.910630533514095], [-87.7413255527848, 41.9107440853121], [-87.74133056179738, 41.9108977882986], [-87.7413395428229, 41.91101926672356], [-87.74134272134717, 41.91107279596593], [-87.741331056852, 41.91124184930413], [-87.74130814459195, 41.91153467796367], [-87.74129119839128, 41.911827880942354], [-87.74128885788656, 41.91188241081093], [-87.74128477194121, 41.91205250648676], [-87.74128698855169, 41.912161622638976], [-87.74130062030306, 41.91283275534097], [-87.74132408768921, 41.9134869400661], [-87.74133439799202, 41.91376278870974], [-87.74133544805804, 41.9138976045996], [-87.74102707259183, 41.91382157727509], [-87.74061374953972, 41.91377142042107], [-87.74025777068191, 41.91372807555386], [-87.7399582130393, 41.91369188174077], [-87.73995632962985, 41.913691655213704], [-87.73940726572734, 41.913625572967575], [-87.73909484499953, 41.913589996976725], [-87.73878192720014, 41.91355853363821], [-87.73872047161176, 41.913553347970165], [-87.73871263446682, 41.91355268664093], [-87.7387083910273, 41.913552325479365], [-87.73846804666769, 41.91353186686843], [-87.73831200707426, 41.91352042421522], [-87.7380127528761, 41.913501378909], [-87.73771299352092, 41.913487132336996], [-87.73734983948655, 41.91347495716914], [-87.7370371525085, 41.913468188651144], [-87.73672396804699, 41.91346553277274], [-87.73641119810972, 41.91346768005481], [-87.73633449448249, 41.9134686539555], [-87.7362234082331, 41.91347007744726], [-87.73609933062234, 41.913471547147864], [-87.73550820081219, 41.91347944800073], [-87.73499975203121, 41.91348689851398], [-87.7349900946789, 41.91348704001359], [-87.73498933224892, 41.91348704784089], [-87.73491808059241, 41.91348776956705], [-87.73425200823137, 41.91349451211823], [-87.73388547949598, 41.91349945929679], [-87.73376756532362, 41.91350135821349], [-87.73364663915896, 41.91350267185049], [-87.7335488066342, 41.9135038762968], [-87.73338437455594, 41.91350610455167], [-87.73254799125766, 41.91351551283188], [-87.73184341752227, 41.91352411295448], [-87.73132787799194, 41.91353194365209], [-87.73048984744173, 41.91354068340804], [-87.73010904801242, 41.91354683339777], [-87.72981281860037, 41.91355050541192], [-87.72889172763362, 41.9135611654622], [-87.72833801094168, 41.9135664137671], [-87.7279600012049, 41.913571281811926], [-87.72766549575113, 41.91357522932789], [-87.72708501824718, 41.91358278816875], [-87.72685169068588, 41.9135856723888], [-87.72644799289698, 41.91359126283712], [-87.7262353052789, 41.91359304879885], [-87.72575263305846, 41.913592897340884], [-87.72557353673365, 41.91359160625006], [-87.72523968722182, 41.91358880966758], [-87.72502661488586, 41.9135866520067], [-87.7247033277006, 41.91358390981922], [-87.72436302626993, 41.91358347796791], [-87.72419264631779, 41.913583260036326], [-87.7240029114293, 41.91362088255512], [-87.72395641663157, 41.91362108889329], [-87.723903055915, 41.91362132518321], [-87.72371695272734, 41.9136218990544], [-87.723604591621, 41.91362287931005], [-87.72349773538441, 41.91362381102992], [-87.72317912433599, 41.91362658910186], [-87.72234754851767, 41.913635112450514], [-87.72234744379519, 41.91363511381425], [-87.72223159440097, 41.913636300838796], [-87.72215029782127, 41.91363723999638], [-87.72155260514938, 41.913662896273166], [-87.72153508465645, 41.91366364842324], [-87.72144920674963, 41.91366733434981], [-87.72133984442489, 41.91367202869193], [-87.721227904726, 41.913659769317434], [-87.72111480642704, 41.91365418449077], [-87.72100205921514, 41.91364861734153], [-87.72079629813177, 41.91365026413802], [-87.72034801577729, 41.9136557613211], [-87.72023962137945, 41.91365689776851], [-87.7196843580028, 41.91365976320781], [-87.71919060786888, 41.91366535618071], [-87.71910860628525, 41.9136666280521], [-87.71887689873436, 41.913669509395916], [-87.71856277276527, 41.913669200144525], [-87.71824914995419, 41.913664433351315], [-87.71788239410195, 41.91364232305604], [-87.7175512935771, 41.91364285556454], [-87.7175141920595, 41.91364207317031], [-87.71742043326654, 41.91364009555065], [-87.71715134560318, 41.91363659371709], [-87.71693549435034, 41.91363680760668], [-87.71665846434864, 41.913638409064916], [-87.71665595986535, 41.913549165252945], [-87.71625167995063, 41.91355360668172], [-87.71592120479998, 41.91355715403661], [-87.71584837605587, 41.91355825034348], [-87.71514712526161, 41.913568823500164], [-87.71503940612635, 41.913569245722144], [-87.71489346185535, 41.91356981762705], [-87.71433284330514, 41.91357752679889], [-87.71423591108918, 41.91357870564626], [-87.71408731692377, 41.91358051141379], [-87.71375484615055, 41.91358527667523], [-87.71354870282796, 41.913588500075655], [-87.71341692303793, 41.91358940231886], [-87.71333577965038, 41.9135899576326], [-87.71275205445357, 41.913597369666704], [-87.71260746421471, 41.91359916853899], [-87.71242759955055, 41.91360140602111], [-87.71212114777455, 41.913605429087575], [-87.71195910324045, 41.91360754352588], [-87.71179831119738, 41.91360954129895], [-87.71161601952728, 41.91361180608499], [-87.71111684765937, 41.91361763684749], [-87.7109824795282, 41.9136186432915], [-87.71080648104285, 41.91361996120969], [-87.71028178136865, 41.91362891557708], [-87.7101798270557, 41.91362974843758], [-87.70999724299428, 41.91363124068162], [-87.70954615185182, 41.91363455393665], [-87.70935962513207, 41.91363805008929], [-87.7091693127318, 41.913641617018435], [-87.70869611562844, 41.91364749584286], [-87.70854809520073, 41.91364917269963], [-87.70837533855676, 41.913651129391766], [-87.7080603634218, 41.91365506778699], [-87.70772726959291, 41.913659633002226], [-87.70753880366885, 41.91366221552323], [-87.70702498262709, 41.91366471650121], [-87.70685459550175, 41.9137160163347], [-87.706856599437, 41.91377310948323], [-87.70668041249407, 41.9137761401322], [-87.70599100955275, 41.91378266631917], [-87.70583301146505, 41.913784203933545], [-87.70516699774251, 41.91378996303247], [-87.705027859671, 41.913792493489844], [-87.70383849939944, 41.913804866861405], [-87.7033353402989, 41.91380997618081], [-87.70246499189689, 41.91381651737836], [-87.70232540321805, 41.913818862886565], [-87.70232710867805, 41.91388182739715], [-87.70232820871246, 41.9139224439504], [-87.70198050822421, 41.913921219588666], [-87.7019778760598, 41.91383887872346], [-87.70197787128551, 41.91383872941105], [-87.7019620793674, 41.91331629292841], [-87.70194877106901, 41.91286608341743], [-87.70193567483044, 41.91242792221503], [-87.70192731886576, 41.91214222228423], [-87.70192237471205, 41.911973184694155], [-87.70190984970992, 41.911588923288726], [-87.70189365934046, 41.91106216113999], [-87.70188094201418, 41.91065643871255], [-87.70187196180713, 41.91037104398445], [-87.70186767558026, 41.910228872982266], [-87.70186599251481, 41.91017304355525], [-87.70194444681948, 41.91017293654928], [-87.70221558767244, 41.91017256707241], [-87.70266192344378, 41.91017195733992], [-87.70279847357212, 41.91017017787492], [-87.70337751590729, 41.9101626304463], [-87.70401321563695, 41.91015434122971], [-87.70451463251341, 41.91014919383564], [-87.7053293640158, 41.91012972970373], [-87.70566225110943, 41.91012607121965], [-87.70654090080615, 41.91011641052617], [-87.70696046604995, 41.910115328402796], [-87.70698624423117, 41.910063266286635], [-87.70699232043573, 41.91001053166186], [-87.70700030993852, 41.90985467533349], [-87.70700477564093, 41.90957072639377], [-87.70699507197959, 41.90930064086113], [-87.7069909745907, 41.90919109586352], [-87.70698356741723, 41.90899305953021], [-87.70697856082377, 41.908857357016515], [-87.70697068808684, 41.908645733623686], [-87.70696386717411, 41.908373907460344], [-87.70696128690616, 41.90828783419781], [-87.70695683056547, 41.908139182156454], [-87.70694535169103, 41.90777259958337], [-87.70693670764544, 41.907514457163686], [-87.70693208623352, 41.90738130940197], [-87.70692710559095, 41.90723778619536], [-87.70691857903911, 41.906914989941704], [-87.70690871683577, 41.906623608149665], [-87.70690351434753, 41.906477384483466], [-87.70689744901411, 41.90630691682514], [-87.70688874793252, 41.90596817583229], [-87.7068812920434, 41.905697471211724], [-87.70687733075184, 41.905571297366066], [-87.70687512928082, 41.90550116986141], [-87.70686337032915, 41.90517462398679], [-87.70685464656952, 41.90486453262508], [-87.70684833638417, 41.904665513372905], [-87.70684378046963, 41.90452182803337], [-87.70683303494201, 41.90421189025918], [-87.70682227505479, 41.90389591506914], [-87.70681841668369, 41.90375953318441], [-87.70681403035094, 41.903604487058544], [-87.70680658699546, 41.903381394897686], [-87.70679354619469, 41.90301694399331], [-87.7067898133444, 41.90285029822992], [-87.70678940164522, 41.90283191563375], [-87.70678880775722, 41.90280541596281], [-87.70678607893205, 41.902683588237956], [-87.70677555934883, 41.902376889793416], [-87.7067663748847, 41.90215911190315], [-87.7067626688907, 41.901995590026196], [-87.70675898330583, 41.901871612441816], [-87.70675703917645, 41.90180174782043], [-87.7067564207128, 41.90177952956973], [-87.70674318789379, 41.90137465489243], [-87.70673572082765, 41.90115027272064], [-87.70673108831417, 41.90100601003334], [-87.70672552720063, 41.90083281855725], [-87.70671621314203, 41.9005418785143], [-87.70670822035274, 41.9002548150418], [-87.70670402489601, 41.90013615434204], [-87.70669760215763, 41.899954509999525], [-87.70668376913277, 41.89950964835921], [-87.70667857197742, 41.89931236413369], [-87.70667445662721, 41.89919540061361], [-87.70653791299962, 41.899197189149454], [-87.70613375496661, 41.89920065639598], [-87.70596150308606, 41.899202301622495], [-87.70524718616556, 41.8992089895945], [-87.70464532013952, 41.89921417576206], [-87.70440707695158, 41.8992164779295], [-87.70398000587086, 41.89922060271532], [-87.70386469429555, 41.89922163917634], [-87.70324218073888, 41.89922723169877], [-87.70302206291503, 41.89922929921588], [-87.7027774426477, 41.899231596203414], [-87.70246754478192, 41.89923387929246], [-87.70219060808789, 41.8992359190005], [-87.7019511288497, 41.899238356643856], [-87.70195431712196, 41.89891469674352], [-87.7019458311871, 41.89860902423871], [-87.70193899707091, 41.89836313031952], [-87.70193177366978, 41.89810455586558], [-87.701929111958, 41.89802224095762], [-87.7019234400612, 41.89784682600936], [-87.70191201323377, 41.89746311855684], [-87.70190068983788, 41.89709129447749], [-87.70189539708862, 41.8969201343325], [-87.70188855042026, 41.89668348643633], [-87.70188087482323, 41.8964181992034], [-87.70223367989679, 41.8965590254703], [-87.70222631266056, 41.89631849518527], [-87.70221651074952, 41.89600087788641], [-87.70221005850097, 41.895801912473814], [-87.7022040470765, 41.89559488552747], [-87.7020354474349, 41.89559647936358], [-87.70189872918802, 41.89559748399079], [-87.70176607804808, 41.895599493261564], [-87.70172514097163, 41.89560011333363], [-87.70160896119707, 41.89560187273138], [-87.70098089838011, 41.89561504601612], [-87.7005574019897, 41.89562264733381], [-87.69991108718366, 41.895628737508886], [-87.69929701086741, 41.89563452070981], [-87.69916127873472, 41.895636115887086], [-87.69894432676371, 41.895638665097565], [-87.69860721811813, 41.89564256518494], [-87.69824638346103, 41.89564638795372], [-87.69794554235253, 41.895648822013435], [-87.69729151477691, 41.89565411080363], [-87.6969860038775, 41.89565331505409], [-87.69670263372936, 41.89565351829936], [-87.6966961806667, 41.89545240329528], [-87.69668875635993, 41.89519775156015], [-87.69668528310115, 41.895079565331834], [-87.69666968390904, 41.89472226084416], [-87.69666554981028, 41.894627534469976], [-87.69667111677165, 41.894333273557145], [-87.69646185830554, 41.894249538736474], [-87.69595803445056, 41.89404753847273], [-87.69559169166158, 41.893900718699], [-87.69507997068001, 41.893695625162295], [-87.69416547439194, 41.89332976221414], [-87.6940280699637, 41.89327478980869], [-87.69367797849786, 41.893134475643265], [-87.693212437497, 41.89294774298534], [-87.6927960824946, 41.892781794630004], [-87.692485945023, 41.89265818021582], [-87.692264374395, 41.892569018031416], [-87.69166778193147, 41.892332378868346], [-87.69170143236082, 41.89200379418852], [-87.69164800124331, 41.89191212694888], [-87.69164529079515, 41.891761856363665], [-87.69162352773706, 41.89055529564389], [-87.6916208111525, 41.89040469156341], [-87.69160649260216, 41.889610842819565], [-87.69158683545206, 41.88852098438254], [-87.69158412810916, 41.8884361773643], [-87.69157000948772, 41.88819563418098]]]], &quot;type&quot;: &quot;MultiPolygon&quot;}, &quot;id&quot;: &quot;23&quot;, &quot;properties&quot;: {&quot;NID&quot;: 23, &quot;POP2000&quot;: 65836, &quot;POP2010&quot;: 56323, &quot;POPCH&quot;: -9513, &quot;POPPERCH&quot;: -14.449541, &quot;community&quot;: &quot;HUMBOLDT PARK&quot;, &quot;popneg&quot;: 1, &quot;popplus&quot;: 0}, &quot;type&quot;: &quot;Feature&quot;}], &quot;type&quot;: &quot;FeatureCollection&quot;});

        
    
    geo_json_28838c2b84b3b08dbfb756448f58bfed.bindTooltip(
    function(layer){
    let div = L.DomUtil.create(&#x27;div&#x27;);
    
    let handleObject = feature=&gt;typeof(feature)==&#x27;object&#x27; ? JSON.stringify(feature) : feature;
    let fields = [&quot;community&quot;, &quot;NID&quot;, &quot;POP2010&quot;, &quot;POP2000&quot;, &quot;POPCH&quot;, &quot;POPPERCH&quot;, &quot;popplus&quot;, &quot;popneg&quot;];
    let aliases = [&quot;community&quot;, &quot;NID&quot;, &quot;POP2010&quot;, &quot;POP2000&quot;, &quot;POPCH&quot;, &quot;POPPERCH&quot;, &quot;popplus&quot;, &quot;popneg&quot;];
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


::: {.cell execution_count=10}
``` {.python .cell-code}
fig, ax = plt.subplots(figsize=(10, 7))
ax = humboldt.overlay(shape, how='intersection').plot(ax=ax, legend=True)
ax = (
    hp := chipop[chipop['community'] == 'HUMBOLDT PARK'].overlay(
        shape,
        how='intersection'
    )
).plot(ax=ax, legend=True)
ax = (
    lp := chipop[chipop['community'] == 'LINCOLN PARK'].overlay(
        shape,
        how='intersection'
    )
).plot(ax=ax, legend=True)
ax = chipop.boundary.plot(ax=ax, color='#666666', linewidth=0.8)
ax = lp.boundary.plot(color='red', ax=ax)
ax = hp.boundary.plot(color='red', ax=ax)
ax.set_axis_off()
_ = ax.set_title('Intersection of Humboldt Park & ClimRR data')
```

::: {.cell-output .cell-output-display}
![](4-chicago_files/figure-html/cell-11-output-1.svg){}
:::
:::


::: {.cell execution_count=11}
``` {.python .cell-code}
fig, ax = plt.subplots(figsize=(10, 7))
chiwind = data['WindSpeed'].overlay(
    chipop,
    how='intersection'
).overlay(chipop, how='union')
ax = chiwind.boundary.plot(ax=ax, color='#666666', linewidth=0.8)
ax.set_axis_off()
```

::: {.cell-output .cell-output-display}
![](4-chicago_files/figure-html/cell-12-output-1.svg){}
:::
:::


::: {.cell execution_count=12}
``` {.python .cell-code}
_, ax = plt.subplots(figsize=(10, 7))
ax = chipop.boundary.plot(color='#666666', linewidth=0.8, ax=ax, alpha=0.2)
ax = chiwind.plot(column='hist', ax=ax, legend=True)
ax.set_axis_off()
ax.set_title('Historical Wind Data across Chicago Neighborhoods')
plt.tight_layout()
```

::: {.cell-output .cell-output-display}
![](4-chicago_files/figure-html/cell-13-output-1.svg){}
:::
:::


::: {.cell execution_count=13}
``` {.python .cell-code}
chiwind.explore(column='hist')
```

::: {.cell-output .cell-output-display execution_count=13}

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
                #map_736d2ae11394dc339f10e975182924c2 {
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
            
    &lt;script src=&quot;https://cdnjs.cloudflare.com/ajax/libs/d3/3.5.5/d3.min.js&quot;&gt;&lt;/script&gt;
&lt;/head&gt;
&lt;body&gt;
    
    
            &lt;div class=&quot;folium-map&quot; id=&quot;map_736d2ae11394dc339f10e975182924c2&quot; &gt;&lt;/div&gt;
        
&lt;/body&gt;
&lt;script&gt;
    
    
            var map_736d2ae11394dc339f10e975182924c2 = L.map(
                &quot;map_736d2ae11394dc339f10e975182924c2&quot;,
                {
                    center: [41.83379085382681, -87.73212559320933],
                    crs: L.CRS.EPSG3857,
                    zoom: 10,
                    zoomControl: true,
                    preferCanvas: false,
                }
            );
            L.control.scale().addTo(map_736d2ae11394dc339f10e975182924c2);

            

        
    
            var tile_layer_61874093661f6c5deeb886c4f6565069 = L.tileLayer(
                &quot;https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png&quot;,
                {&quot;attribution&quot;: &quot;Data by \u0026copy; \u003ca target=\&quot;_blank\&quot; href=\&quot;http://openstreetmap.org\&quot;\u003eOpenStreetMap\u003c/a\u003e, under \u003ca target=\&quot;_blank\&quot; href=\&quot;http://www.openstreetmap.org/copyright\&quot;\u003eODbL\u003c/a\u003e.&quot;, &quot;detectRetina&quot;: false, &quot;maxNativeZoom&quot;: 18, &quot;maxZoom&quot;: 18, &quot;minZoom&quot;: 0, &quot;noWrap&quot;: false, &quot;opacity&quot;: 1, &quot;subdomains&quot;: &quot;abc&quot;, &quot;tms&quot;: false}
            ).addTo(map_736d2ae11394dc339f10e975182924c2);
        
    
            map_736d2ae11394dc339f10e975182924c2.fitBounds(
                [[41.64454312150605, -87.94011408252345], [42.02303858614757, -87.52413710389521]],
                {}
            );
        
    
        function geo_json_dba2a81e93d48ddc1483ca2a5c2af934_styler(feature) {
            switch(feature.id) {
                case &quot;0&quot;: case &quot;4&quot;: case &quot;6&quot;: case &quot;14&quot;: 
                    return {&quot;color&quot;: &quot;#404588&quot;, &quot;fillColor&quot;: &quot;#404588&quot;, &quot;fillOpacity&quot;: 0.5, &quot;weight&quot;: 2};
                case &quot;2&quot;: case &quot;7&quot;: case &quot;9&quot;: case &quot;13&quot;: case &quot;15&quot;: case &quot;21&quot;: case &quot;22&quot;: case &quot;74&quot;: case &quot;76&quot;: case &quot;77&quot;: case &quot;79&quot;: case &quot;80&quot;: case &quot;139&quot;: case &quot;140&quot;: 
                    return {&quot;color&quot;: &quot;#482071&quot;, &quot;fillColor&quot;: &quot;#482071&quot;, &quot;fillOpacity&quot;: 0.5, &quot;weight&quot;: 2};
                case &quot;3&quot;: case &quot;5&quot;: case &quot;11&quot;: case &quot;17&quot;: case &quot;19&quot;: case &quot;136&quot;: 
                    return {&quot;color&quot;: &quot;#ece51b&quot;, &quot;fillColor&quot;: &quot;#ece51b&quot;, &quot;fillOpacity&quot;: 0.5, &quot;weight&quot;: 2};
                case &quot;23&quot;: case &quot;34&quot;: case &quot;36&quot;: case &quot;41&quot;: case &quot;45&quot;: case &quot;46&quot;: case &quot;47&quot;: case &quot;49&quot;: case &quot;57&quot;: case &quot;58&quot;: case &quot;59&quot;: case &quot;60&quot;: case &quot;62&quot;: case &quot;64&quot;: case &quot;69&quot;: case &quot;71&quot;: 
                    return {&quot;color&quot;: &quot;#440154&quot;, &quot;fillColor&quot;: &quot;#440154&quot;, &quot;fillOpacity&quot;: 0.5, &quot;weight&quot;: 2};
                case &quot;24&quot;: case &quot;26&quot;: case &quot;28&quot;: case &quot;100&quot;: case &quot;101&quot;: case &quot;104&quot;: case &quot;107&quot;: case &quot;108&quot;: case &quot;111&quot;: case &quot;113&quot;: case &quot;128&quot;: case &quot;142&quot;: case &quot;144&quot;: case &quot;147&quot;: 
                    return {&quot;color&quot;: &quot;#46075a&quot;, &quot;fillColor&quot;: &quot;#46075a&quot;, &quot;fillOpacity&quot;: 0.5, &quot;weight&quot;: 2};
                case &quot;25&quot;: case &quot;27&quot;: case &quot;29&quot;: case &quot;30&quot;: case &quot;31&quot;: case &quot;32&quot;: case &quot;33&quot;: case &quot;35&quot;: case &quot;37&quot;: case &quot;38&quot;: case &quot;40&quot;: case &quot;44&quot;: case &quot;82&quot;: case &quot;84&quot;: case &quot;86&quot;: case &quot;88&quot;: case &quot;91&quot;: case &quot;94&quot;: case &quot;95&quot;: case &quot;97&quot;: case &quot;102&quot;: case &quot;105&quot;: case &quot;109&quot;: case &quot;110&quot;: case &quot;119&quot;: case &quot;121&quot;: case &quot;123&quot;: case &quot;124&quot;: case &quot;126&quot;: case &quot;129&quot;: case &quot;141&quot;: case &quot;143&quot;: 
                    return {&quot;color&quot;: &quot;#48186a&quot;, &quot;fillColor&quot;: &quot;#48186a&quot;, &quot;fillOpacity&quot;: 0.5, &quot;weight&quot;: 2};
                case &quot;39&quot;: case &quot;42&quot;: case &quot;51&quot;: case &quot;52&quot;: case &quot;53&quot;: case &quot;55&quot;: case &quot;96&quot;: case &quot;114&quot;: case &quot;118&quot;: case &quot;120&quot;: case &quot;122&quot;: case &quot;125&quot;: case &quot;127&quot;: case &quot;146&quot;: 
                    return {&quot;color&quot;: &quot;#fde725&quot;, &quot;fillColor&quot;: &quot;#fde725&quot;, &quot;fillOpacity&quot;: 0.5, &quot;weight&quot;: 2};
                case &quot;72&quot;: case &quot;78&quot;: 
                    return {&quot;color&quot;: &quot;#482374&quot;, &quot;fillColor&quot;: &quot;#482374&quot;, &quot;fillOpacity&quot;: 0.5, &quot;weight&quot;: 2};
                case &quot;81&quot;: case &quot;83&quot;: case &quot;85&quot;: case &quot;87&quot;: case &quot;89&quot;: case &quot;90&quot;: case &quot;92&quot;: case &quot;93&quot;: case &quot;98&quot;: case &quot;99&quot;: case &quot;103&quot;: case &quot;106&quot;: case &quot;145&quot;: 
                    return {&quot;color&quot;: &quot;#404688&quot;, &quot;fillColor&quot;: &quot;#404688&quot;, &quot;fillOpacity&quot;: 0.5, &quot;weight&quot;: 2};
                case &quot;112&quot;: case &quot;148&quot;: 
                    return {&quot;color&quot;: &quot;#482878&quot;, &quot;fillColor&quot;: &quot;#482878&quot;, &quot;fillOpacity&quot;: 0.5, &quot;weight&quot;: 2};
                case &quot;153&quot;: case &quot;154&quot;: case &quot;155&quot;: case &quot;156&quot;: case &quot;157&quot;: case &quot;158&quot;: case &quot;159&quot;: case &quot;160&quot;: case &quot;161&quot;: case &quot;162&quot;: case &quot;163&quot;: case &quot;164&quot;: case &quot;165&quot;: case &quot;166&quot;: case &quot;167&quot;: case &quot;168&quot;: case &quot;169&quot;: case &quot;170&quot;: case &quot;171&quot;: case &quot;172&quot;: case &quot;173&quot;: 
                    return {&quot;color&quot;: null, &quot;fillColor&quot;: null, &quot;fillOpacity&quot;: 0.5, &quot;weight&quot;: 2};
                default:
                    return {&quot;color&quot;: &quot;#424086&quot;, &quot;fillColor&quot;: &quot;#424086&quot;, &quot;fillOpacity&quot;: 0.5, &quot;weight&quot;: 2};
            }
        }
        function geo_json_dba2a81e93d48ddc1483ca2a5c2af934_highlighter(feature) {
            switch(feature.id) {
                default:
                    return {&quot;fillOpacity&quot;: 0.75};
            }
        }
        function geo_json_dba2a81e93d48ddc1483ca2a5c2af934_pointToLayer(feature, latlng) {
            var opts = {&quot;bubblingMouseEvents&quot;: true, &quot;color&quot;: &quot;#3388ff&quot;, &quot;dashArray&quot;: null, &quot;dashOffset&quot;: null, &quot;fill&quot;: true, &quot;fillColor&quot;: &quot;#3388ff&quot;, &quot;fillOpacity&quot;: 0.2, &quot;fillRule&quot;: &quot;evenodd&quot;, &quot;lineCap&quot;: &quot;round&quot;, &quot;lineJoin&quot;: &quot;round&quot;, &quot;opacity&quot;: 1.0, &quot;radius&quot;: 2, &quot;stroke&quot;: true, &quot;weight&quot;: 3};
            
            let style = geo_json_dba2a81e93d48ddc1483ca2a5c2af934_styler(feature)
            Object.assign(opts, style)
            
            return new L.CircleMarker(latlng, opts)
        }

        function geo_json_dba2a81e93d48ddc1483ca2a5c2af934_onEachFeature(feature, layer) {
            layer.on({
                mouseout: function(e) {
                    if(typeof e.target.setStyle === &quot;function&quot;){
                        geo_json_dba2a81e93d48ddc1483ca2a5c2af934.resetStyle(e.target);
                    }
                },
                mouseover: function(e) {
                    if(typeof e.target.setStyle === &quot;function&quot;){
                        const highlightStyle = geo_json_dba2a81e93d48ddc1483ca2a5c2af934_highlighter(e.target.feature)
                        e.target.setStyle(highlightStyle);
                    }
                },
            });
        };
        var geo_json_dba2a81e93d48ddc1483ca2a5c2af934 = L.geoJson(null, {
                onEachFeature: geo_json_dba2a81e93d48ddc1483ca2a5c2af934_onEachFeature,
            
                style: geo_json_dba2a81e93d48ddc1483ca2a5c2af934_styler,
                pointToLayer: geo_json_dba2a81e93d48ddc1483ca2a5c2af934_pointToLayer
        });

        function geo_json_dba2a81e93d48ddc1483ca2a5c2af934_add (data) {
            geo_json_dba2a81e93d48ddc1483ca2a5c2af934
                .addData(data)
                .addTo(map_736d2ae11394dc339f10e975182924c2);
        }

        
    
    geo_json_dba2a81e93d48ddc1483ca2a5c2af934.bindTooltip(
    function(layer){
    let div = L.DomUtil.create(&#x27;div&#x27;);
    
    let handleObject = feature=&gt;typeof(feature)==&#x27;object&#x27; ? JSON.stringify(feature) : feature;
    let fields = [&quot;OBJECTID&quot;, &quot;Crossmodel&quot;, &quot;Shape_Leng&quot;, &quot;Shape_Area&quot;, &quot;hist&quot;, &quot;rcp45_midc&quot;, &quot;rcp45_endc&quot;, &quot;rcp85_midc&quot;, &quot;rcp85_endc&quot;, &quot;mid45_hist&quot;, &quot;end45_hist&quot;, &quot;mid85_hist&quot;, &quot;end85_hist&quot;, &quot;mid85_45&quot;, &quot;end85_45&quot;, &quot;community_1&quot;, &quot;NID_1&quot;, &quot;POP2010_1&quot;, &quot;POP2000_1&quot;, &quot;POPCH_1&quot;, &quot;POPPERCH_1&quot;, &quot;popplus_1&quot;, &quot;popneg_1&quot;, &quot;community_2&quot;, &quot;NID_2&quot;, &quot;POP2010_2&quot;, &quot;POP2000_2&quot;, &quot;POPCH_2&quot;, &quot;POPPERCH_2&quot;, &quot;popplus_2&quot;, &quot;popneg_2&quot;];
    let aliases = [&quot;OBJECTID&quot;, &quot;Crossmodel&quot;, &quot;Shape_Leng&quot;, &quot;Shape_Area&quot;, &quot;hist&quot;, &quot;rcp45_midc&quot;, &quot;rcp45_endc&quot;, &quot;rcp85_midc&quot;, &quot;rcp85_endc&quot;, &quot;mid45_hist&quot;, &quot;end45_hist&quot;, &quot;mid85_hist&quot;, &quot;end85_hist&quot;, &quot;mid85_45&quot;, &quot;end85_45&quot;, &quot;community_1&quot;, &quot;NID_1&quot;, &quot;POP2010_1&quot;, &quot;POP2000_1&quot;, &quot;POPCH_1&quot;, &quot;POPPERCH_1&quot;, &quot;popplus_1&quot;, &quot;popneg_1&quot;, &quot;community_2&quot;, &quot;NID_2&quot;, &quot;POP2010_2&quot;, &quot;POP2000_2&quot;, &quot;POPCH_2&quot;, &quot;POPPERCH_2&quot;, &quot;popplus_2&quot;, &quot;popneg_2&quot;];
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
                     
    
    var color_map_cee3d49f5f5c95e414f81a6aa3e98a93 = {};

    
    color_map_cee3d49f5f5c95e414f81a6aa3e98a93.color = d3.scale.threshold()
              .domain([7.19385004, 7.200137313767535, 7.2064245875350705, 7.212711861302605, 7.21899913507014, 7.225286408837675, 7.231573682605211, 7.237860956372746, 7.24414823014028, 7.250435503907815, 7.256722777675351, 7.263010051442886, 7.269297325210421, 7.275584598977956, 7.281871872745491, 7.288159146513026, 7.294446420280561, 7.3007336940480965, 7.307020967815632, 7.313308241583166, 7.319595515350701, 7.3258827891182365, 7.332170062885772, 7.338457336653307, 7.344744610420841, 7.351031884188377, 7.357319157955912, 7.363606431723447, 7.369893705490982, 7.376180979258517, 7.382468253026052, 7.388755526793587, 7.395042800561122, 7.401330074328658, 7.407617348096193, 7.413904621863727, 7.4201918956312625, 7.426479169398798, 7.432766443166333, 7.439053716933868, 7.4453409907014025, 7.451628264468938, 7.457915538236473, 7.464202812004008, 7.4704900857715435, 7.476777359539078, 7.483064633306613, 7.489351907074148, 7.495639180841684, 7.501926454609219, 7.508213728376753, 7.514501002144288, 7.520788275911824, 7.527075549679359, 7.533362823446894, 7.5396500972144285, 7.545937370981964, 7.552224644749499, 7.558511918517034, 7.564799192284569, 7.571086466052105, 7.577373739819639, 7.583661013587174, 7.5899482873547095, 7.596235561122245, 7.60252283488978, 7.608810108657314, 7.61509738242485, 7.621384656192385, 7.62767192995992, 7.633959203727455, 7.6402464774949905, 7.646533751262525, 7.65282102503006, 7.659108298797595, 7.665395572565131, 7.671682846332666, 7.6779701201002, 7.684257393867735, 7.690544667635271, 7.696831941402806, 7.703119215170341, 7.7094064889378755, 7.715693762705411, 7.721981036472946, 7.728268310240481, 7.7345555840080165, 7.740842857775551, 7.747130131543086, 7.753417405310621, 7.7597046790781565, 7.765991952845692, 7.772279226613227, 7.778566500380761, 7.784853774148297, 7.791141047915832, 7.797428321683367, 7.803715595450901, 7.810002869218437, 7.816290142985972, 7.822577416753507, 7.828864690521042, 7.835151964288578, 7.841439238056112, 7.847726511823647, 7.8540137855911825, 7.860301059358718, 7.866588333126253, 7.872875606893787, 7.8791628806613225, 7.885450154428858, 7.891737428196393, 7.898024701963928, 7.9043119757314635, 7.910599249498998, 7.916886523266533, 7.923173797034068, 7.929461070801604, 7.935748344569138, 7.942035618336673, 7.948322892104208, 7.954610165871744, 7.960897439639279, 7.967184713406814, 7.9734719871743485, 7.979759260941884, 7.986046534709419, 7.992333808476954, 7.998621082244489, 8.004908356012024, 8.011195629779559, 8.017482903547094, 8.02377017731463, 8.030057451082165, 8.0363447248497, 8.042631998617235, 8.04891927238477, 8.055206546152304, 8.06149381991984, 8.067781093687374, 8.07406836745491, 8.080355641222445, 8.08664291498998, 8.092930188757515, 8.09921746252505, 8.105504736292586, 8.111792010060121, 8.118079283827655, 8.12436655759519, 8.130653831362725, 8.13694110513026, 8.143228378897795, 8.14951565266533, 8.155802926432866, 8.162090200200401, 8.168377473967936, 8.174664747735472, 8.180952021503007, 8.18723929527054, 8.193526569038076, 8.19981384280561, 8.206101116573146, 8.212388390340681, 8.218675664108217, 8.224962937875752, 8.231250211643287, 8.237537485410822, 8.243824759178358, 8.250112032945893, 8.256399306713426, 8.262686580480961, 8.268973854248497, 8.275261128016032, 8.281548401783567, 8.287835675551102, 8.294122949318638, 8.300410223086173, 8.306697496853708, 8.312984770621243, 8.319272044388779, 8.325559318156312, 8.331846591923847, 8.338133865691383, 8.344421139458918, 8.350708413226453, 8.356995686993988, 8.363282960761524, 8.369570234529059, 8.375857508296594, 8.38214478206413, 8.388432055831665, 8.394719329599198, 8.401006603366733, 8.407293877134268, 8.413581150901804, 8.419868424669339, 8.426155698436874, 8.43244297220441, 8.438730245971945, 8.44501751973948, 8.451304793507013, 8.457592067274549, 8.463879341042084, 8.470166614809619, 8.476453888577154, 8.48274116234469, 8.489028436112225, 8.49531570987976, 8.501602983647295, 8.507890257414829, 8.514177531182366, 8.5204648049499, 8.526752078717434, 8.53303935248497, 8.539326626252505, 8.54561390002004, 8.551901173787575, 8.55818844755511, 8.564475721322646, 8.570762995090181, 8.577050268857715, 8.58333754262525, 8.589624816392785, 8.59591209016032, 8.602199363927856, 8.60848663769539, 8.614773911462926, 8.621061185230461, 8.627348458997997, 8.633635732765532, 8.639923006533067, 8.6462102803006, 8.652497554068136, 8.658784827835671, 8.665072101603206, 8.671359375370741, 8.677646649138277, 8.683933922905812, 8.690221196673347, 8.696508470440882, 8.702795744208418, 8.709083017975953, 8.715370291743486, 8.721657565511022, 8.727944839278557, 8.734232113046092, 8.740519386813627, 8.746806660581163, 8.753093934348698, 8.759381208116233, 8.765668481883768, 8.771955755651303, 8.778243029418839, 8.784530303186372, 8.790817576953907, 8.797104850721443, 8.803392124488978, 8.809679398256513, 8.815966672024048, 8.822253945791584, 8.828541219559119, 8.834828493326654, 8.84111576709419, 8.847403040861725, 8.853690314629258, 8.859977588396793, 8.866264862164329, 8.872552135931864, 8.878839409699399, 8.885126683466934, 8.89141395723447, 8.897701231002005, 8.90398850476954, 8.910275778537073, 8.916563052304609, 8.922850326072144, 8.92913759983968, 8.935424873607214, 8.94171214737475, 8.947999421142285, 8.95428669490982, 8.960573968677355, 8.96686124244489, 8.973148516212426, 8.97943578997996, 8.985723063747495, 8.99201033751503, 8.998297611282565, 9.0045848850501, 9.010872158817635, 9.01715943258517, 9.023446706352706, 9.029733980120241, 9.036021253887776, 9.042308527655312, 9.048595801422845, 9.05488307519038, 9.061170348957916, 9.06745762272545, 9.073744896492986, 9.080032170260521, 9.086319444028057, 9.092606717795592, 9.098893991563127, 9.105181265330662, 9.111468539098198, 9.117755812865731, 9.124043086633266, 9.130330360400801, 9.136617634168337, 9.142904907935872, 9.149192181703407, 9.155479455470942, 9.161766729238478, 9.168054003006013, 9.174341276773548, 9.180628550541083, 9.186915824308617, 9.193203098076152, 9.199490371843687, 9.205777645611223, 9.212064919378758, 9.218352193146293, 9.224639466913828, 9.230926740681362, 9.237214014448899, 9.243501288216432, 9.24978856198397, 9.256075835751503, 9.262363109519038, 9.268650383286573, 9.274937657054108, 9.281224930821644, 9.287512204589179, 9.293799478356714, 9.30008675212425, 9.306374025891785, 9.312661299659318, 9.318948573426855, 9.325235847194389, 9.331523120961924, 9.337810394729459, 9.344097668496994, 9.35038494226453, 9.356672216032065, 9.3629594897996, 9.369246763567135, 9.37553403733467, 9.381821311102204, 9.38810858486974, 9.394395858637274, 9.40068313240481, 9.406970406172345, 9.41325767993988, 9.419544953707415, 9.42583222747495, 9.432119501242486, 9.43840677501002, 9.444694048777556, 9.45098132254509, 9.457268596312625, 9.46355587008016, 9.469843143847696, 9.47613041761523, 9.482417691382766, 9.488704965150301, 9.494992238917837, 9.501279512685372, 9.507566786452905, 9.513854060220442, 9.520141333987976, 9.526428607755511, 9.532715881523046, 9.539003155290581, 9.545290429058117, 9.551577702825652, 9.557864976593187, 9.564152250360722, 9.570439524128258, 9.576726797895791, 9.583014071663328, 9.589301345430862, 9.595588619198397, 9.601875892965932, 9.608163166733467, 9.614450440501003, 9.620737714268538, 9.627024988036073, 9.633312261803606, 9.639599535571142, 9.645886809338677, 9.652174083106212, 9.658461356873747, 9.664748630641283, 9.671035904408818, 9.677323178176353, 9.683610451943888, 9.689897725711422, 9.696184999478959, 9.702472273246492, 9.708759547014028, 9.715046820781563, 9.721334094549098, 9.727621368316633, 9.733908642084169, 9.740195915851704, 9.746483189619239, 9.752770463386774, 9.759057737154308, 9.765345010921845, 9.771632284689378, 9.777919558456913, 9.784206832224449, 9.790494105991984, 9.79678137975952, 9.803068653527054, 9.80935592729459, 9.815643201062125, 9.82193047482966, 9.828217748597194, 9.83450502236473, 9.840792296132264, 9.8470795698998, 9.853366843667335, 9.85965411743487, 9.865941391202405, 9.87222866496994, 9.878515938737475, 9.88480321250501, 9.891090486272546, 9.89737776004008, 9.903665033807616, 9.90995230757515, 9.916239581342685, 9.92252685511022, 9.928814128877756, 9.93510140264529, 9.941388676412826, 9.947675950180361, 9.953963223947897, 9.960250497715432, 9.966537771482965, 9.9728250452505, 9.979112319018036, 9.985399592785571, 9.991686866553106, 9.997974140320641, 10.004261414088177, 10.010548687855712, 10.016835961623247, 10.02312323539078, 10.029410509158318, 10.035697782925851, 10.041985056693386, 10.048272330460922, 10.054559604228457, 10.060846877995992, 10.067134151763527, 10.073421425531063, 10.079708699298598, 10.085995973066133, 10.092283246833667, 10.098570520601204, 10.104857794368737, 10.111145068136272, 10.117432341903807, 10.123719615671343, 10.130006889438878, 10.136294163206413, 10.142581436973948, 10.148868710741484, 10.155155984509019, 10.161443258276552, 10.16773053204409, 10.174017805811623, 10.180305079579158, 10.186592353346693, 10.192879627114229, 10.199166900881764, 10.205454174649299, 10.211741448416834, 10.21802872218437, 10.224315995951905, 10.230603269719438, 10.236890543486975, 10.243177817254509, 10.249465091022044, 10.25575236478958, 10.262039638557114, 10.26832691232465, 10.274614186092185, 10.28090145985972, 10.287188733627255, 10.29347600739479, 10.299763281162324, 10.30605055492986, 10.312337828697395, 10.31862510246493, 10.324912376232465, 10.33119965])
              .range([&#x27;#440154ff&#x27;, &#x27;#440155ff&#x27;, &#x27;#440256ff&#x27;, &#x27;#440356ff&#x27;, &#x27;#450457ff&#x27;, &#x27;#450458ff&#x27;, &#x27;#450559ff&#x27;, &#x27;#450659ff&#x27;, &#x27;#46075aff&#x27;, &#x27;#46075bff&#x27;, &#x27;#46085cff&#x27;, &#x27;#46095cff&#x27;, &#x27;#460a5dff&#x27;, &#x27;#460a5eff&#x27;, &#x27;#460b5eff&#x27;, &#x27;#460c5fff&#x27;, &#x27;#470d60ff&#x27;, &#x27;#470d61ff&#x27;, &#x27;#470e61ff&#x27;, &#x27;#470f62ff&#x27;, &#x27;#471063ff&#x27;, &#x27;#471064ff&#x27;, &#x27;#471164ff&#x27;, &#x27;#471265ff&#x27;, &#x27;#471365ff&#x27;, &#x27;#481366ff&#x27;, &#x27;#481467ff&#x27;, &#x27;#481568ff&#x27;, &#x27;#481668ff&#x27;, &#x27;#481669ff&#x27;, &#x27;#481769ff&#x27;, &#x27;#48176aff&#x27;, &#x27;#48186bff&#x27;, &#x27;#48196cff&#x27;, &#x27;#481a6cff&#x27;, &#x27;#481a6dff&#x27;, &#x27;#481b6dff&#x27;, &#x27;#481c6eff&#x27;, &#x27;#481c6eff&#x27;, &#x27;#481d6fff&#x27;, &#x27;#481d6fff&#x27;, &#x27;#481f70ff&#x27;, &#x27;#481f70ff&#x27;, &#x27;#482071ff&#x27;, &#x27;#482072ff&#x27;, &#x27;#482173ff&#x27;, &#x27;#482273ff&#x27;, &#x27;#482374ff&#x27;, &#x27;#482374ff&#x27;, &#x27;#482475ff&#x27;, &#x27;#482476ff&#x27;, &#x27;#482576ff&#x27;, &#x27;#482577ff&#x27;, &#x27;#482677ff&#x27;, &#x27;#482778ff&#x27;, &#x27;#482878ff&#x27;, &#x27;#482879ff&#x27;, &#x27;#482979ff&#x27;, &#x27;#47297aff&#x27;, &#x27;#472a7aff&#x27;, &#x27;#472b7aff&#x27;, &#x27;#472c7aff&#x27;, &#x27;#472c7bff&#x27;, &#x27;#472d7bff&#x27;, &#x27;#472d7cff&#x27;, &#x27;#472e7cff&#x27;, &#x27;#472e7dff&#x27;, &#x27;#472f7dff&#x27;, &#x27;#462f7eff&#x27;, &#x27;#46307eff&#x27;, &#x27;#46317eff&#x27;, &#x27;#46327eff&#x27;, &#x27;#46327fff&#x27;, &#x27;#46337fff&#x27;, &#x27;#463480ff&#x27;, &#x27;#453480ff&#x27;, &#x27;#453581ff&#x27;, &#x27;#453581ff&#x27;, &#x27;#453681ff&#x27;, &#x27;#453781ff&#x27;, &#x27;#453882ff&#x27;, &#x27;#443882ff&#x27;, &#x27;#443983ff&#x27;, &#x27;#443983ff&#x27;, &#x27;#443a83ff&#x27;, &#x27;#443a83ff&#x27;, &#x27;#443b84ff&#x27;, &#x27;#433c84ff&#x27;, &#x27;#433d84ff&#x27;, &#x27;#433d85ff&#x27;, &#x27;#433e85ff&#x27;, &#x27;#423e85ff&#x27;, &#x27;#423f85ff&#x27;, &#x27;#423f86ff&#x27;, &#x27;#424086ff&#x27;, &#x27;#424086ff&#x27;, &#x27;#424186ff&#x27;, &#x27;#414187ff&#x27;, &#x27;#414287ff&#x27;, &#x27;#414387ff&#x27;, &#x27;#414487ff&#x27;, &#x27;#404488ff&#x27;, &#x27;#404588ff&#x27;, &#x27;#404588ff&#x27;, &#x27;#404688ff&#x27;, &#x27;#3f4688ff&#x27;, &#x27;#3f4788ff&#x27;, &#x27;#3f4789ff&#x27;, &#x27;#3f4889ff&#x27;, &#x27;#3e4889ff&#x27;, &#x27;#3e4989ff&#x27;, &#x27;#3e4a89ff&#x27;, &#x27;#3e4a89ff&#x27;, &#x27;#3e4b8aff&#x27;, &#x27;#3d4c8aff&#x27;, &#x27;#3d4d8aff&#x27;, &#x27;#3d4d8aff&#x27;, &#x27;#3d4e8aff&#x27;, &#x27;#3c4e8aff&#x27;, &#x27;#3c4f8aff&#x27;, &#x27;#3c4f8aff&#x27;, &#x27;#3c508bff&#x27;, &#x27;#3b508bff&#x27;, &#x27;#3b518bff&#x27;, &#x27;#3b518bff&#x27;, &#x27;#3b528bff&#x27;, &#x27;#3a528bff&#x27;, &#x27;#3a538bff&#x27;, &#x27;#3a538bff&#x27;, &#x27;#3a548cff&#x27;, &#x27;#39548cff&#x27;, &#x27;#39558cff&#x27;, &#x27;#39558cff&#x27;, &#x27;#39568cff&#x27;, &#x27;#38578cff&#x27;, &#x27;#38588cff&#x27;, &#x27;#38588cff&#x27;, &#x27;#38598cff&#x27;, &#x27;#37598cff&#x27;, &#x27;#375a8cff&#x27;, &#x27;#375a8dff&#x27;, &#x27;#375b8dff&#x27;, &#x27;#365b8dff&#x27;, &#x27;#365c8dff&#x27;, &#x27;#365c8dff&#x27;, &#x27;#365d8dff&#x27;, &#x27;#355d8dff&#x27;, &#x27;#355e8dff&#x27;, &#x27;#355f8dff&#x27;, &#x27;#355f8dff&#x27;, &#x27;#34608dff&#x27;, &#x27;#34608dff&#x27;, &#x27;#34618dff&#x27;, &#x27;#34618dff&#x27;, &#x27;#33628dff&#x27;, &#x27;#33628dff&#x27;, &#x27;#33638dff&#x27;, &#x27;#32638dff&#x27;, &#x27;#32648eff&#x27;, &#x27;#32648eff&#x27;, &#x27;#32658eff&#x27;, &#x27;#31658eff&#x27;, &#x27;#31668eff&#x27;, &#x27;#31668eff&#x27;, &#x27;#31678eff&#x27;, &#x27;#31678eff&#x27;, &#x27;#31688eff&#x27;, &#x27;#30688eff&#x27;, &#x27;#30698eff&#x27;, &#x27;#30698eff&#x27;, &#x27;#306a8eff&#x27;, &#x27;#2f6a8eff&#x27;, &#x27;#2f6b8eff&#x27;, &#x27;#2f6b8eff&#x27;, &#x27;#2f6c8eff&#x27;, &#x27;#2e6c8eff&#x27;, &#x27;#2e6d8eff&#x27;, &#x27;#2e6d8eff&#x27;, &#x27;#2e6e8eff&#x27;, &#x27;#2e6e8eff&#x27;, &#x27;#2e6f8eff&#x27;, &#x27;#2d6f8eff&#x27;, &#x27;#2d708eff&#x27;, &#x27;#2d708eff&#x27;, &#x27;#2d718eff&#x27;, &#x27;#2c718eff&#x27;, &#x27;#2c718eff&#x27;, &#x27;#2c728eff&#x27;, &#x27;#2c728eff&#x27;, &#x27;#2c738eff&#x27;, &#x27;#2c738eff&#x27;, &#x27;#2b748eff&#x27;, &#x27;#2b748eff&#x27;, &#x27;#2b758eff&#x27;, &#x27;#2b758eff&#x27;, &#x27;#2a768eff&#x27;, &#x27;#2a768eff&#x27;, &#x27;#2a778eff&#x27;, &#x27;#2a778eff&#x27;, &#x27;#2a788eff&#x27;, &#x27;#29788eff&#x27;, &#x27;#29798eff&#x27;, &#x27;#29798eff&#x27;, &#x27;#297a8eff&#x27;, &#x27;#297a8eff&#x27;, &#x27;#297b8eff&#x27;, &#x27;#287b8eff&#x27;, &#x27;#287c8eff&#x27;, &#x27;#287c8eff&#x27;, &#x27;#287d8eff&#x27;, &#x27;#277d8eff&#x27;, &#x27;#277e8eff&#x27;, &#x27;#277e8eff&#x27;, &#x27;#277f8eff&#x27;, &#x27;#277f8eff&#x27;, &#x27;#27808eff&#x27;, &#x27;#26808eff&#x27;, &#x27;#26818eff&#x27;, &#x27;#26818eff&#x27;, &#x27;#26828eff&#x27;, &#x27;#26828eff&#x27;, &#x27;#26828eff&#x27;, &#x27;#25828eff&#x27;, &#x27;#25838eff&#x27;, &#x27;#25838eff&#x27;, &#x27;#25848eff&#x27;, &#x27;#25858eff&#x27;, &#x27;#25858eff&#x27;, &#x27;#24868eff&#x27;, &#x27;#24868eff&#x27;, &#x27;#24878eff&#x27;, &#x27;#24878eff&#x27;, &#x27;#23888eff&#x27;, &#x27;#23888eff&#x27;, &#x27;#23898eff&#x27;, &#x27;#23898eff&#x27;, &#x27;#238a8dff&#x27;, &#x27;#238a8dff&#x27;, &#x27;#228b8dff&#x27;, &#x27;#228b8dff&#x27;, &#x27;#228c8dff&#x27;, &#x27;#228c8dff&#x27;, &#x27;#228d8dff&#x27;, &#x27;#218d8dff&#x27;, &#x27;#218e8dff&#x27;, &#x27;#218e8dff&#x27;, &#x27;#218f8dff&#x27;, &#x27;#218f8dff&#x27;, &#x27;#21908dff&#x27;, &#x27;#21908dff&#x27;, &#x27;#21918cff&#x27;, &#x27;#20918cff&#x27;, &#x27;#20928cff&#x27;, &#x27;#20928cff&#x27;, &#x27;#20928cff&#x27;, &#x27;#20928cff&#x27;, &#x27;#20938cff&#x27;, &#x27;#1f938cff&#x27;, &#x27;#1f948cff&#x27;, &#x27;#1f948cff&#x27;, &#x27;#1f958bff&#x27;, &#x27;#1f958bff&#x27;, &#x27;#1f968bff&#x27;, &#x27;#1f968bff&#x27;, &#x27;#1f978bff&#x27;, &#x27;#1f988bff&#x27;, &#x27;#1f988bff&#x27;, &#x27;#1f998bff&#x27;, &#x27;#1f998aff&#x27;, &#x27;#1f9a8aff&#x27;, &#x27;#1f9a8aff&#x27;, &#x27;#1e9b8aff&#x27;, &#x27;#1e9b8aff&#x27;, &#x27;#1e9c8aff&#x27;, &#x27;#1e9c89ff&#x27;, &#x27;#1e9d89ff&#x27;, &#x27;#1e9d89ff&#x27;, &#x27;#1e9e89ff&#x27;, &#x27;#1f9e89ff&#x27;, &#x27;#1f9f88ff&#x27;, &#x27;#1f9f88ff&#x27;, &#x27;#1fa088ff&#x27;, &#x27;#1fa088ff&#x27;, &#x27;#1fa188ff&#x27;, &#x27;#1fa188ff&#x27;, &#x27;#1fa187ff&#x27;, &#x27;#1fa187ff&#x27;, &#x27;#1fa287ff&#x27;, &#x27;#1fa287ff&#x27;, &#x27;#1fa386ff&#x27;, &#x27;#20a386ff&#x27;, &#x27;#20a486ff&#x27;, &#x27;#20a486ff&#x27;, &#x27;#20a585ff&#x27;, &#x27;#21a585ff&#x27;, &#x27;#21a685ff&#x27;, &#x27;#21a685ff&#x27;, &#x27;#21a785ff&#x27;, &#x27;#22a785ff&#x27;, &#x27;#22a884ff&#x27;, &#x27;#22a884ff&#x27;, &#x27;#22a983ff&#x27;, &#x27;#23a983ff&#x27;, &#x27;#23aa83ff&#x27;, &#x27;#24ab83ff&#x27;, &#x27;#25ab82ff&#x27;, &#x27;#25ac82ff&#x27;, &#x27;#25ac82ff&#x27;, &#x27;#25ad82ff&#x27;, &#x27;#26ad81ff&#x27;, &#x27;#26ad81ff&#x27;, &#x27;#27ad81ff&#x27;, &#x27;#27ae81ff&#x27;, &#x27;#28ae80ff&#x27;, &#x27;#28af80ff&#x27;, &#x27;#29af7fff&#x27;, &#x27;#29b07fff&#x27;, &#x27;#2ab07fff&#x27;, &#x27;#2bb17eff&#x27;, &#x27;#2cb17eff&#x27;, &#x27;#2cb27dff&#x27;, &#x27;#2db27dff&#x27;, &#x27;#2db37cff&#x27;, &#x27;#2eb37cff&#x27;, &#x27;#2eb47cff&#x27;, &#x27;#2fb47cff&#x27;, &#x27;#30b57bff&#x27;, &#x27;#31b57bff&#x27;, &#x27;#31b67aff&#x27;, &#x27;#32b67aff&#x27;, &#x27;#33b679ff&#x27;, &#x27;#34b679ff&#x27;, &#x27;#34b779ff&#x27;, &#x27;#35b779ff&#x27;, &#x27;#36b878ff&#x27;, &#x27;#37b878ff&#x27;, &#x27;#37b977ff&#x27;, &#x27;#38b977ff&#x27;, &#x27;#39ba76ff&#x27;, &#x27;#3aba76ff&#x27;, &#x27;#3abb75ff&#x27;, &#x27;#3bbb75ff&#x27;, &#x27;#3cbc74ff&#x27;, &#x27;#3dbc74ff&#x27;, &#x27;#3ebc73ff&#x27;, &#x27;#3fbd73ff&#x27;, &#x27;#40bd72ff&#x27;, &#x27;#40be72ff&#x27;, &#x27;#41be71ff&#x27;, &#x27;#42bf71ff&#x27;, &#x27;#43bf70ff&#x27;, &#x27;#45c070ff&#x27;, &#x27;#46c06fff&#x27;, &#x27;#47c16fff&#x27;, &#x27;#48c16eff&#x27;, &#x27;#49c16eff&#x27;, &#x27;#4ac16dff&#x27;, &#x27;#4bc26cff&#x27;, &#x27;#4cc26cff&#x27;, &#x27;#4dc36bff&#x27;, &#x27;#4ec36bff&#x27;, &#x27;#4fc46aff&#x27;, &#x27;#50c46aff&#x27;, &#x27;#51c569ff&#x27;, &#x27;#52c569ff&#x27;, &#x27;#53c568ff&#x27;, &#x27;#54c568ff&#x27;, &#x27;#55c667ff&#x27;, &#x27;#56c667ff&#x27;, &#x27;#57c766ff&#x27;, &#x27;#58c765ff&#x27;, &#x27;#59c864ff&#x27;, &#x27;#5ac864ff&#x27;, &#x27;#5bc863ff&#x27;, &#x27;#5cc863ff&#x27;, &#x27;#5dc962ff&#x27;, &#x27;#5ec962ff&#x27;, &#x27;#5fca61ff&#x27;, &#x27;#60ca60ff&#x27;, &#x27;#62cb5fff&#x27;, &#x27;#63cb5fff&#x27;, &#x27;#64cb5eff&#x27;, &#x27;#65cc5dff&#x27;, &#x27;#66cc5cff&#x27;, &#x27;#67cd5cff&#x27;, &#x27;#68cd5bff&#x27;, &#x27;#6acd5bff&#x27;, &#x27;#6bcd5aff&#x27;, &#x27;#6cce59ff&#x27;, &#x27;#6ece58ff&#x27;, &#x27;#6fcf58ff&#x27;, &#x27;#70cf57ff&#x27;, &#x27;#71d057ff&#x27;, &#x27;#72d056ff&#x27;, &#x27;#74d055ff&#x27;, &#x27;#75d054ff&#x27;, &#x27;#76d153ff&#x27;, &#x27;#77d153ff&#x27;, &#x27;#78d152ff&#x27;, &#x27;#7ad151ff&#x27;, &#x27;#7bd250ff&#x27;, &#x27;#7cd250ff&#x27;, &#x27;#7dd34fff&#x27;, &#x27;#7fd34eff&#x27;, &#x27;#80d34dff&#x27;, &#x27;#81d34dff&#x27;, &#x27;#82d44cff&#x27;, &#x27;#84d44bff&#x27;, &#x27;#85d54aff&#x27;, &#x27;#86d549ff&#x27;, &#x27;#88d548ff&#x27;, &#x27;#89d548ff&#x27;, &#x27;#8ad647ff&#x27;, &#x27;#8bd646ff&#x27;, &#x27;#8dd645ff&#x27;, &#x27;#8ed645ff&#x27;, &#x27;#8fd744ff&#x27;, &#x27;#90d743ff&#x27;, &#x27;#92d742ff&#x27;, &#x27;#93d741ff&#x27;, &#x27;#94d840ff&#x27;, &#x27;#96d83fff&#x27;, &#x27;#97d83eff&#x27;, &#x27;#99d93dff&#x27;, &#x27;#9ad93cff&#x27;, &#x27;#9bd93cff&#x27;, &#x27;#9dd93bff&#x27;, &#x27;#9eda3aff&#x27;, &#x27;#9fda39ff&#x27;, &#x27;#a1da38ff&#x27;, &#x27;#a2da37ff&#x27;, &#x27;#a3db36ff&#x27;, &#x27;#a4db36ff&#x27;, &#x27;#a6db35ff&#x27;, &#x27;#a8db34ff&#x27;, &#x27;#a9dc33ff&#x27;, &#x27;#aadc32ff&#x27;, &#x27;#abdc31ff&#x27;, &#x27;#addc30ff&#x27;, &#x27;#aedd2fff&#x27;, &#x27;#b0dd2fff&#x27;, &#x27;#b1dd2eff&#x27;, &#x27;#b2dd2dff&#x27;, &#x27;#b3de2cff&#x27;, &#x27;#b5de2bff&#x27;, &#x27;#b6de2aff&#x27;, &#x27;#b8de29ff&#x27;, &#x27;#b9de28ff&#x27;, &#x27;#bade28ff&#x27;, &#x27;#bcdf27ff&#x27;, &#x27;#bddf26ff&#x27;, &#x27;#bfdf25ff&#x27;, &#x27;#c0df25ff&#x27;, &#x27;#c1df24ff&#x27;, &#x27;#c2df23ff&#x27;, &#x27;#c4e022ff&#x27;, &#x27;#c5e021ff&#x27;, &#x27;#c7e020ff&#x27;, &#x27;#c8e020ff&#x27;, &#x27;#c9e11fff&#x27;, &#x27;#cbe11eff&#x27;, &#x27;#cce11dff&#x27;, &#x27;#cee11dff&#x27;, &#x27;#cfe11cff&#x27;, &#x27;#d1e11bff&#x27;, &#x27;#d2e21bff&#x27;, &#x27;#d3e21aff&#x27;, &#x27;#d4e21aff&#x27;, &#x27;#d6e219ff&#x27;, &#x27;#d7e219ff&#x27;, &#x27;#d9e319ff&#x27;, &#x27;#dae319ff&#x27;, &#x27;#dbe318ff&#x27;, &#x27;#dde318ff&#x27;, &#x27;#dee318ff&#x27;, &#x27;#dfe318ff&#x27;, &#x27;#e0e418ff&#x27;, &#x27;#e2e418ff&#x27;, &#x27;#e3e418ff&#x27;, &#x27;#e5e418ff&#x27;, &#x27;#e6e419ff&#x27;, &#x27;#e7e419ff&#x27;, &#x27;#e8e519ff&#x27;, &#x27;#eae519ff&#x27;, &#x27;#ebe51aff&#x27;, &#x27;#ece51aff&#x27;, &#x27;#ede51bff&#x27;, &#x27;#efe51bff&#x27;, &#x27;#f0e51cff&#x27;, &#x27;#f1e51dff&#x27;, &#x27;#f3e61dff&#x27;, &#x27;#f4e61eff&#x27;, &#x27;#f5e61eff&#x27;, &#x27;#f6e61fff&#x27;, &#x27;#f7e620ff&#x27;, &#x27;#f8e621ff&#x27;, &#x27;#fae722ff&#x27;, &#x27;#fbe723ff&#x27;, &#x27;#fce724ff&#x27;, &#x27;#fde725ff&#x27;]);
    

    color_map_cee3d49f5f5c95e414f81a6aa3e98a93.x = d3.scale.linear()
              .domain([7.19385004, 10.33119965])
              .range([0, 450 - 50]);

    color_map_cee3d49f5f5c95e414f81a6aa3e98a93.legend = L.control({position: &#x27;topright&#x27;});
    color_map_cee3d49f5f5c95e414f81a6aa3e98a93.legend.onAdd = function (map) {var div = L.DomUtil.create(&#x27;div&#x27;, &#x27;legend&#x27;); return div};
    color_map_cee3d49f5f5c95e414f81a6aa3e98a93.legend.addTo(map_736d2ae11394dc339f10e975182924c2);

    color_map_cee3d49f5f5c95e414f81a6aa3e98a93.xAxis = d3.svg.axis()
        .scale(color_map_cee3d49f5f5c95e414f81a6aa3e98a93.x)
        .orient(&quot;top&quot;)
        .tickSize(1)
        .tickValues([7.19385004, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, 7.513736666901961, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, 7.833623293803922, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, 8.153509920705883, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, 8.473396547607843, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, 8.793283174509805, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, 9.113169801411765, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, 9.433056428313726, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, 9.752943055215686, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, 10.072829682117646, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;, &#x27;&#x27;]);

    color_map_cee3d49f5f5c95e414f81a6aa3e98a93.svg = d3.select(&quot;.legend.leaflet-control&quot;).append(&quot;svg&quot;)
        .attr(&quot;id&quot;, &#x27;legend&#x27;)
        .attr(&quot;width&quot;, 450)
        .attr(&quot;height&quot;, 40);

    color_map_cee3d49f5f5c95e414f81a6aa3e98a93.g = color_map_cee3d49f5f5c95e414f81a6aa3e98a93.svg.append(&quot;g&quot;)
        .attr(&quot;class&quot;, &quot;key&quot;)
        .attr(&quot;transform&quot;, &quot;translate(25,16)&quot;);

    color_map_cee3d49f5f5c95e414f81a6aa3e98a93.g.selectAll(&quot;rect&quot;)
        .data(color_map_cee3d49f5f5c95e414f81a6aa3e98a93.color.range().map(function(d, i) {
          return {
            x0: i ? color_map_cee3d49f5f5c95e414f81a6aa3e98a93.x(color_map_cee3d49f5f5c95e414f81a6aa3e98a93.color.domain()[i - 1]) : color_map_cee3d49f5f5c95e414f81a6aa3e98a93.x.range()[0],
            x1: i &lt; color_map_cee3d49f5f5c95e414f81a6aa3e98a93.color.domain().length ? color_map_cee3d49f5f5c95e414f81a6aa3e98a93.x(color_map_cee3d49f5f5c95e414f81a6aa3e98a93.color.domain()[i]) : color_map_cee3d49f5f5c95e414f81a6aa3e98a93.x.range()[1],
            z: d
          };
        }))
      .enter().append(&quot;rect&quot;)
        .attr(&quot;height&quot;, 40 - 30)
        .attr(&quot;x&quot;, function(d) { return d.x0; })
        .attr(&quot;width&quot;, function(d) { return d.x1 - d.x0; })
        .style(&quot;fill&quot;, function(d) { return d.z; });

    color_map_cee3d49f5f5c95e414f81a6aa3e98a93.g.call(color_map_cee3d49f5f5c95e414f81a6aa3e98a93.xAxis).append(&quot;text&quot;)
        .attr(&quot;class&quot;, &quot;caption&quot;)
        .attr(&quot;y&quot;, 21)
        .text(&quot;hist&quot;);
&lt;/script&gt;
&lt;/html&gt;" style="position:absolute;width:100%;height:100%;left:0;top:0;border:none !important;" allowfullscreen webkitallowfullscreen mozallowfullscreen></iframe></div></div>
```

:::
:::


::: {.cell execution_count=14}
``` {.python .cell-code}
_, ax = plt.subplots()
ax = chiwind.plot(column='hist', scheme='quantiles', k=8, ax=ax)
_ = ax.set_title('WindSpeed, historical')
ax.set_axis_off()
plt.tight_layout()
```

::: {.cell-output .cell-output-display}
![](4-chicago_files/figure-html/cell-15-output-1.svg){}
:::
:::


::: {.cell execution_count=15}
``` {.python .cell-code}
fig, ax = plt.subplots()
ax = chiwind.plot(column='rcp45_midc', scheme='quantiles', k=3, ax=ax)
ax.set_axis_off()
_ = ax.set_title('WindSpeed, Mid-Century [RCP45]')
plt.tight_layout()
```

::: {.cell-output .cell-output-display}
![](4-chicago_files/figure-html/cell-16-output-1.svg){}
:::
:::


::: {.cell execution_count=16}
``` {.python .cell-code}
fig, ax = plt.subplots()
ax = chiwind.plot(column='rcp45_endc', scheme='quantiles', k=3, ax=ax)
_ = ax.set_title('WindSpeed, End-Century [RCP45]')
plt.tight_layout()
```

::: {.cell-output .cell-output-display}
![](4-chicago_files/figure-html/cell-17-output-1.svg){}
:::
:::


::: {.cell execution_count=17}
``` {.python .cell-code}
fig, ax = plt.subplots(ncols=3, figsize=(16, 7))
ax0 = chiwind.plot('hist', ax=ax[0])
ax1 = chiwind.plot('rcp45_midc', ax=ax[1])
ax2 = chiwind.plot('rcp45_midc', ax=ax[2])
ax0.set_axis_off()
ax1.set_axis_off()
ax2.set_axis_off()
```

::: {.cell-output .cell-output-display}
![](4-chicago_files/figure-html/cell-18-output-1.svg){}
:::
:::


::: {.cell execution_count=18}
``` {.python .cell-code}
data['WindSpeed'].shape
```

::: {.cell-output .cell-output-display execution_count=18}
```
(62834, 18)
```
:::
:::


::: {.cell execution_count=19}
``` {.python .cell-code}
selection = shape[0:5]

for index, row in selection.iterrows():
    # get the area of the polygon
    poly_area = row['geometry'].area
    console.print(f"Polygon area at {index} is {poly_area:.3f}")
```

::: {.cell-output .cell-output-display}

```{=html}
<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">Polygon area at <span style="color: #2094f3; text-decoration-color: #2094f3">0</span> is <span style="color: #2094f3; text-decoration-color: #2094f3">252927293.657</span>
</pre>
```

:::

::: {.cell-output .cell-output-display}

```{=html}
<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">Polygon area at <span style="color: #2094f3; text-decoration-color: #2094f3">1</span> is <span style="color: #2094f3; text-decoration-color: #2094f3">235501313.715</span>
</pre>
```

:::

::: {.cell-output .cell-output-display}

```{=html}
<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">Polygon area at <span style="color: #2094f3; text-decoration-color: #2094f3">2</span> is <span style="color: #2094f3; text-decoration-color: #2094f3">233416379.950</span>
</pre>
```

:::

::: {.cell-output .cell-output-display}

```{=html}
<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">Polygon area at <span style="color: #2094f3; text-decoration-color: #2094f3">3</span> is <span style="color: #2094f3; text-decoration-color: #2094f3">261761834.191</span>
</pre>
```

:::

::: {.cell-output .cell-output-display}

```{=html}
<pre style="white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">Polygon area at <span style="color: #2094f3; text-decoration-color: #2094f3">4</span> is <span style="color: #2094f3; text-decoration-color: #2094f3">226073092.218</span>
</pre>
```

:::
:::

