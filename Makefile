

SHELL=/bin/bash

.PHONY: install

install:
	virtualenv env
	env/bin/pip install -r requirements.txt

run:
	$(MAKE) manage -e CMD=runserver

manage:
ifdef CMD
	cd cityconf && ../env/bin/python manage.py $(CMD)
else
	@echo Usage: $(MAKE) manage -e CMD
endif

migrate:
ifdef APP
	$(MAKE) manage -e CMD="schemamigration $(APP) --auto"
	$(MAKE) manage -e CMD="migrate $(APP)"
else
	@echo Usage: $(MAKE) migrate -e APP="app"
endif

dump:
	$(MAKE) manage -e CMD="dumpdata --indent=4 sites auth core > core/fixtures/initial_data.json"
