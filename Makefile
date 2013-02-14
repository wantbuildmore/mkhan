

SHELL=/bin/bash

.PHONY: install

install:
	virtualenv env
	env/bin/pip install -r requirements.txt

