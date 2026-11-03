import glob
import xml.etree.ElementTree as ET

replacements = {
    "&bull;": "&#8226;",
    "&times;": "&#215;",
    "&rarr;": "&#8594;",
    "&larr;": "&#8592;",
    "&uarr;": "&#8593;",
    "&darr;": "&#8595;",
    "&hellip;": "&#8230;",
    "&copy;": "&#169;"
}

svg_files = glob.glob(r"c:\Users\siddi\Desktop\New folder\assets\*.svg")
for svg_path in svg_files:
    with open(svg_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    modified = False
    for entity, num in replacements.items():
        if entity in content:
            content = content.replace(entity, num)
            modified = True
            
    if modified:
        with open(svg_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Fixed entities in {svg_path}")

# Now verify XML validity
all_valid = True
for svg_path in svg_files:
    try:
        ET.parse(svg_path)
    except Exception as e:
        all_valid = False
        print(f"STILL INVALID: {svg_path} -> {e}")

if all_valid:
    print(f"ALL {len(svg_files)} SVGs ARE NOW 100% VALID XML!")
