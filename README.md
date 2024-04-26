# random-colors-visuals

### paste logo randomly

Each SPACE adds python logo to a random place. ESCAPE to quit.

### install libraries
```bash
pip install -r requirements.txt
```

### run game locally
```bash
python game/main.py
```

### build html file
```bash
pygbag --build game
```
Move files from game/build/web to game/web-source if you want to change the repository files. Build folder is ignored by git.

### build zip for itch.io
```bash
pygbag --build --archive game
```

### useful links
- game hosted on https://rioran.itch.io/random-shifting-colors
- also due to ios conflict with itch-io on https://rioran.github.io/random-colors-visuals/game/web-source/index.html
- source code can be found here https://github.com/Rioran/random-colors-visuals
