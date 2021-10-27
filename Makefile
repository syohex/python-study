all:
	echo "Support only make clean"

.PHONY: clean
clean:
	-find . -name 'venv' -type d | xargs rm -rf
	-find . -name '.venv' -type d | xargs rm -rf

