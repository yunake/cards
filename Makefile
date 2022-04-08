.PHONY: venv install run

ENVFILE := env.zaliznychnyj.yaml

venv:
	@echo create venv:
	@echo python -m venv venv
	@echo activate venv:
	@echo source venv/bin/activate

install:
	@pip install -r requirements.txt

run:
	@ENVFILE=$(ENVFILE) python bot.py
