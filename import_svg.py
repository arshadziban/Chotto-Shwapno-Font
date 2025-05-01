import fontforge
from pathlib import Path

font = fontforge.font()

svgFilePaths = list(Path('SVG').glob('**/*.svg'))

for p in svgFilePaths:
	dec = p.stem.split(" ", 1)[0]
	glyph = font.createChar(int(dec))
	glyph.importOutlines(str(p))

font.save('output01.sfd')

# font.generate('output.otf')
# font.generate('output.ttf')
# font.generate('output.woff')
# font.generate('output.woff2')
