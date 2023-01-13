all: shell run mig makmig

.PHONY: shell run mig makmig

shell:
	venv/Scripts/python.exe manage.py shell
run:
	venv/Scripts/python.exe manage.py runserver

mig:
	venv/Scripts/python.exe manage.py migrate

makmig:
	venv/Scripts/python.exe manage.py makemigrations