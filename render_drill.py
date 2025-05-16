import gerber
from gerber.render import GerberCairoContext

files = [
    gerber.read('LM675T_test-PTH-drl.gbr'),
    gerber.read('LM675T_test-NPTH-drl.gbr'),
    ]

filename = "output.svg"

# Thanks, ChatGPT
def generate_svg_with_circles(circles, width=200, height=200):
    """
    Generate an SVG file with a single layer containing multiple circle paths.
    
    :param filename: Output SVG file name.
    :param circles: List of tuples (cx, cy, r) for each circle.
    :param width: Width of the SVG canvas.
    :param height: Height of the SVG canvas.
    """
    svg_header = f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}mm" height="{height}mm" viewBox="0 0 {width} {height}">\n'
    svg_footer = '</svg>'
    
    # Group to act as a layer
    layer_start = '<g id="layer1" style="fill:#000000; fill-opacity:1.0000;stroke:#000000; stroke-opacity:1.0000; stroke-width:0.1; stroke-linecap:round; stroke-linejoin:round;" transform="translate(0 0) scale(1 1)">\n'
    layer_end = '</g>\n'
    
    circles_svg = ""
    for cx, cy, r in circles:
        circles_svg += f'  <circle cx="{cx}" cy="{cy}" r="{r}" stroke="black" fill="none" />\n'
    
    svg_content = svg_header + layer_start + circles_svg + layer_end + svg_footer
    return svg_content

circles = []
for f in files:
    f.to_metric()
    for p in f.primitives:
        circles.append((p.position[0], -p.position[1], p.radius))

svg_content = generate_svg_with_circles(circles)
with open(filename, 'w') as f:
    f.write(svg_content)
