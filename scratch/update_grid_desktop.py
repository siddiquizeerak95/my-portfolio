with open("style.css", "r", encoding="utf-8") as f:
    content = f.read()

target = """.hero-cinematic-grid {
  display: grid;
  grid-template-columns: minmax(0, 1.22fr) minmax(0, 1fr);
  align-items: center;
  gap: clamp(28px, 4vw, 56px);
  width: 100%;
  min-height: calc(100vh - 84px);
  padding: clamp(40px, 6vh, 70px) 0 20px 0;
  box-sizing: border-box;
}

.hero-content-col {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  z-index: 3;
  width: 100%;
  max-width: 100%;
  box-sizing: border-box;
}"""

replacement = """.hero-cinematic-grid {
  display: grid;
  grid-template-columns: minmax(0, 1.15fr) minmax(0, 1.05fr);
  align-items: flex-end;
  gap: clamp(28px, 3.5vw, 52px);
  width: 100%;
  min-height: calc(100vh - 84px);
  padding: clamp(30px, 4vh, 60px) 0 0 0;
  box-sizing: border-box;
}

.hero-content-col {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  z-index: 3;
  width: 100%;
  max-width: 100%;
  padding-bottom: clamp(60px, 10vh, 120px);
  box-sizing: border-box;
}"""

if target in content:
    content = content.replace(target, replacement, 1)
    with open("style.css", "w", encoding="utf-8") as f:
        f.write(content)
    print("Updated hero-cinematic-grid desktop rules!")
else:
    print("target not found!")

