start-setup:
	.scripts/setup_venv.sh

start-server:
	.scripts/run_dev_server_locally.sh

write-format:
	black .

show-migrations:
	python3 demoproject/manage.py showmigrations

makemigrations:
	python3 demoproject/manage.py makemigrations

migrate:
	python3 demoproject/manage.py migrate

shell:
	python3 demoproject/manage.py shell