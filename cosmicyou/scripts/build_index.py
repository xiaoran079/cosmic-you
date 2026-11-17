
from pathlib import Path
import json
from xml.etree.ElementTree import Element, SubElement, ElementTree, indent

root = Path(__file__).resolve().parents[1]
folder = root / "blog" / "posts"

# Generate blog index
slugs = sorted(p.stem for p in folder.glob("*.md"))
(folder.parent / "posts.json").write_text(
    json.dumps(slugs, indent=2) + "\n",
    encoding="utf-8"
)

# Generate sitemap
base_url = "https://writteninthe-stars.netlify.app"

urlset = Element(
    "urlset",
    xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
)

urls = [
    base_url + "/",
    base_url + "/blog/"
]

for slug in slugs:
    urls.append(base_url + "/blog/?post=" + slug)

for url in urls:
    entry = SubElement(urlset, "url")
    SubElement(entry, "loc").text = url

indent(urlset, space="  ")

tree = ElementTree(urlset)
tree.write(
    root / "sitemap.xml",
    encoding="utf-8",
    xml_declaration=True
)
# Trigger Netlify rebuild
