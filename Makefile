.PHONY: setup download-data clean all

setup:
	pip install -r requirements.txt

download-data:
	python src/download_data.py

all: setup download-data

clean:
	rm -rf data/raw/*.csv
preprocess:
	python src/preprocess.py
