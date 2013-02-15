

SHELL=/bin/bash

.PHONY: install

install:
	virtualenv env
	env/bin/pip install -r requirements.txt

run:
	env/bin/python cityconf/manage.py runserver

manage:
ifdef CMD
	env/bin/python cityconf/manage.py $(CMD)
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

