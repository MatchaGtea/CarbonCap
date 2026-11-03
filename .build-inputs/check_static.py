from pathlib import Path
from html.parser import HTMLParser
import base64,hashlib,json,re,subprocess,tempfile
root=Path(__file__).resolve().parents[1]
html=(root/'index.html').read_text(encoding='utf-8')
class Parser(HTMLParser):
    def __init__(self):
        super().__init__(); self.scripts=[]; self.script=None; self.external=[]; self.lang=None
    def handle_starttag(self,tag,attrs):
        attrs=dict(attrs)
        if tag=='html': self.lang=attrs.get('lang')
        if tag=='script': self.script=''
        for field in ['src','poster']:
            if attrs.get(field) and not attrs[field].startswith(('data:','#')): self.external.append((tag,attrs[field]))
        if tag=='link' and attrs.get('href') and not attrs['href'].startswith('data:'): self.external.append((tag,attrs['href']))
    def handle_data(self,data):
        if self.script is not None: self.script+=data
    def handle_endtag(self,tag):
        if tag=='script' and self.script is not None:
            self.scripts.append(self.script); self.script=None
p=Parser();p.feed(html)
assert p.lang=='th','HTML lang must be th'
assert '<title>' in html and 'CarbonCap' in html,'Missing product identity'
assert not p.external, 'External resources: '+repr(p.external)
assert '/*__CARBONCAP_GEE_ASSETS__*/' not in html,'Unexpanded asset marker'
match=re.search(r'const GEE_ASSETS = (\{[^\n]*\});',html)
assert match,'Embedded GEE_ASSETS missing'
assets=json.loads(match.group(1))
manifest=json.loads((root/'.build-inputs/gee/manifest.json').read_text())
assert len(assets)==3 and len(manifest['projects'])==3,'Expected three projects'
for project in manifest['projects']:
    for layer in ['rgb','ndvi']:
        raw=base64.b64decode(assets[project['id']][layer].split(',',1)[1])
        assert hashlib.sha256(raw).hexdigest()==project['images'][layer]['sha256'],'Image hash mismatch'
for script in p.scripts:
    with tempfile.NamedTemporaryFile('w',suffix='.js',encoding='utf-8') as handle:
        handle.write(script);handle.flush()
        result=subprocess.run(['node','--check',handle.name],capture_output=True,text=True)
        assert result.returncode==0, result.stderr
assert not re.search(r'url\(\s*[\"\x27]?https?://',html,re.I),'CSS loads external resources'
print(json.dumps({'static_checks':'passed','projects':3,'embedded_images':6,'inline_scripts_checked':len(p.scripts),'external_resources':len(p.external)}))
