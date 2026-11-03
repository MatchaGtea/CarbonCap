from pathlib import Path
import runpy,shutil
root=Path(__file__).resolve().parents[1]
source=root/'.build-inputs/index-source.html'
assert source.exists() and source.stat().st_size<1000000, 'Expected compact HTML source fixture'
assert '/*__CARBONCAP_GEE_ASSETS__*/' in source.read_text(), 'Asset marker missing in source'
shutil.copyfile(source,root/'index.html')
runpy.run_path(str(root/'.build-inputs/embed_assets.py'),run_name='__main__')
runpy.run_path(str(root/'.build-inputs/check_static.py'),run_name='__main__')
