# # Makefile

# .PHONY: test
# test:
# 	pytest --cov=app --cov-report=term-missing

# .PHONY: test-base
# test-base:
# 	pytest --cov=app.models.Base --cov-report=term-missing tests/test_base.py

# .PHONY: test-fund
# test-fund:
# 	pytest --cov=app.models.Fund --cov-report=term-missing tests/test_fund.py

# .PHONY: test-transaction
# test-transaction:
# 	pytest --cov=app.models.Transaction --cov-report=term-missing tests/test_transaction.py

# .PHONY: coverage
# coverage:
# 	pytest --cov=app --cov-report=html


MODULE = models

t:
	@echo "Executing..."
	PYTHONPATH=/app pytest --cov=app/$(MODULE)/ \
	app/tests/test_$(MODULE)/ --cov-config=.coveragerc --cov-report=term-missing -x -s -W \
	ignore::DeprecationWarning

# t:
# 	@echo "Executing..."
# 	pytest --cov=app/$(MODULE)/ \
# 	app/tests/test_$(MODULE)/ --cov-config=.coveragerc --cov-report term-missing -x -s -W \
# 	ignore::DeprecationWarning -o cache_dir=/tmp/application/cache

# m:
# 	@echo "Executing..."
# 	export DJANGO_SETTINGS_MODULE=project.settings;\
# 	pytest --cov=$(MODULE)/ \
# 	tests/test_$(MODULE)/ --cov-config=.coveragerc --cov-report term-missing -x -s -W \
# 	ignore::DeprecationWarning --nomigrations -o cache_dir=/tmp/application/cache




# a:
# 	@echo "Executing..."
# 	export DJANGO_SETTINGS_MODULE=project.settings;\
# 	pytest --cov=./ \
# 	tests/ --cov-config=.coveragerc --cov-report term-missing -x -s -W \
# 	ignore::DeprecationWarning --nomigrations