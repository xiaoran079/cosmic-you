from pathlib import Path
import json
folder=Path(__file__).resolve().parents[1]/'blog'/'posts'
slugs=sorted(p.stem for p in folder.glob('*.md'))
(folder.parent/'posts.json').write_text(json.dumps(slugs,indent=2)+'\n')
