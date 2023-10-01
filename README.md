## Running

### Setup
This project uses poetry as its package manager. Make sure both poetry and a suitable version of python (^3.11) are installed.

In arch linux this can be done with:

```
sudo pacman -S python
sudo pacman -S poetry
```

Then, execute poetry install in order to install all project dependencies:

```
poetry install
```

Place the game's original rom file under `rom/goemon.gbc`.

Also place any additional data under `data/`. This includes:

- `data/edited_font.bmp`: new font to be injected into the hacked rom

### Execution
To execute any of the scripts, use `poetry run` followed by the command name, as such:

```
poetry run <command-name>
```

The commands are as follows:

- `extract_font`: extracts the original rom's font into a bitmap file at out/image/font.bmp
- `inject_font`: creates rom with new font from data/edited_font.bmp
