# project-aig
## Algorithmic Micro Crawler (DSA + OOP)

Text-based micro-dungeon to revise graphs, BFS, basic OOP Strategy. Implement the stubs in src/ to make tests pass.

## Quickstart
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
PYTHONPATH=src pytest -q
PYTHONPATH=src python -m game.game
docker build -t alg-adventure .
docker run --rm -it alg-adventure