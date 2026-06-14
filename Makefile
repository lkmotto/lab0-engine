.PHONY: install test demo-mech demo-elec demo-bio-mol demo-bio-pathway all-demos

install:
	apt-get update -qq && apt-get install -y -qq ngspice libngspice0 python3-venv python3-dev
	python3 -m venv .venv
	.venv/bin/python -m pip install cadquery trimesh numpy scipy numpy-stl shapely manifold3d rtree skidl PySpice biopython rdkit cobra requests pytest

test:
	.venv/bin/pytest tests/

demo-mech:
	PYTHONPATH=src .venv/bin/python src/main.py examples/bracket.yaml

demo-elec:
	PYTHONPATH=src .venv/bin/python src/main.py examples/rc_filter.yaml

demo-bio-mol:
	PYTHONPATH=src .venv/bin/python src/main.py examples/aspirin.yaml

demo-bio-pathway:
	PYTHONPATH=src .venv/bin/python src/main.py examples/ecoli_core.yaml

all-demos: demo-mech demo-elec demo-bio-mol demo-bio-pathway
