from pathlib import Path
import base64,json
root=Path(__file__).resolve().parents[1]
source=root/'.build-inputs/gee'
manifest=json.loads((source/'manifest.json').read_text())
assets={}
for project in manifest['projects']:
    item={k:project[k] for k in ['name','province','bounds','center','observed_start','observed_end','scene_count','mean_ndvi','valid_fraction']}
    for layer in ['rgb','ndvi']:
        item[layer]='data:image/png;base64,'+base64.b64encode((source/project['images'][layer]['file']).read_bytes()).decode('ascii')
    assets[project['id']]=item
html_path=root/'index.html'
html=html_path.read_text(encoding='utf-8')

# 1) GEE satellite image assets (unchanged behaviour/bytes)
marker='/*__CARBONCAP_GEE_ASSETS__*/'
if marker in html:
    assert html.count(marker)==1, 'Use exactly one GEE asset marker'
    html=html.replace(marker,'const GEE_ASSETS = '+json.dumps(assets,ensure_ascii=False,separators=(',',':'))+';')
else:
    assert 'const GEE_ASSETS = ' in html, 'Missing GEE asset marker or embedded data'

# 2) Standalone UI illustrations (farmer/farm/globe) - only when marker present
ui_root=root/'design/assets'
ui_marker='/*__CARBONCAP_UI_ASSETS__*/'
ui_embedded=False
if ui_marker in html:
    assert html.count(ui_marker)==1, 'Use exactly one UI asset marker'
    ui_assets={}
    for key in ['farmer','farm','globe']:
        ui_assets[key]='data:image/png;base64,'+base64.b64encode((ui_root/(key+'.png')).read_bytes()).decode('ascii')
    html=html.replace(ui_marker,'const UI_ASSETS = '+json.dumps(ui_assets,ensure_ascii=False,separators=(',',':'))+';')
    ui_embedded=True

# 3) Embedded Thai font (data URI used by @font-face) - only when marker present
font_marker='__CARBONCAP_THAI_FONT__'
font_embedded=False
if font_marker in html:
    assert html.count(font_marker)==1, 'Use exactly one font marker'
    font_data='data:font/ttf;base64,'+base64.b64encode((root/'design/assets/fonts/NotoSansThai.ttf').read_bytes()).decode('ascii')
    html=html.replace(font_marker,font_data)
    font_embedded=True

html_path.write_text(html,encoding='utf-8')
print(json.dumps({'embedded_projects':len(assets),'ui_assets_embedded':ui_embedded,'font_embedded':font_embedded,'html_bytes':html_path.stat().st_size}))
