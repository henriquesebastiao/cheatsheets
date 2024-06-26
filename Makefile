lint:
	ruff check . && blue --check . --diff
format:
	blue .

.PHONY: lint
.PHONY: format