tests-watch:
	ptw -- --cov-report term:skip-covered --cov=src tests

tests-report-html:
	pytest --cov=src --cov-report html:cov_html tests