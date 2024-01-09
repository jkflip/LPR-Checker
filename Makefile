install:
	.scripts/setup_venv.sh

start-server:
	.scripts/run_dev_server_locally.sh

write-format:
	black .

show-migrations:
	python3 lpr_checker_project/manage.py showmigrations

makemigrations:
	python3 lpr_checker_project/manage.py makemigrations

migrate:
	python3 lpr_checker_project/manage.py migrate

shell:
	python3 lpr_checker_project/manage.py shell

