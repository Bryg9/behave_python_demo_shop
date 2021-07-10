deps:
	pip install -r requirements.txt
	pip install -r test_requirements.txt
test:
	behave
lint:
	flake8 features
