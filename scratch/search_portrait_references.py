import glob, re, os

print("Searching HTML files for portrait/profile images...")
for f in glob.glob("*.html"):
    with open(f, "r", encoding="utf-8", errors="ignore") as fp:
        lines = fp.readlines()
    for idx, line in enumerate(lines):
        if any(w in line.lower() for w in ["new image", "new%20image", "profile", "portrait", "actual_portrait"]):
            if "<img" in line or "meta" in line or "src=" in line or "content=" in line:
                print(f"{f}:{idx+1} -> {line.strip()}")

