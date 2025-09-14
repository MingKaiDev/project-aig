.PHONY: venv install test run docker-build docker-test
venv: ; python -m venv .venv
install: ; . .venv/bin/activate && pip install -r requirements.txt
test: ; PYTHONPATH=src pytest -q
run: ; PYTHONPATH=src python -m game.game
docker-build: ; docker build -t alg-adventure .
docker-test: ; docker run --rm alg-adventure
