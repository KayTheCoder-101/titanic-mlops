.PHONY: setup download-data preprocess features clean all

setup:
	pip install -r requirements.txt

download-data:
	python src/download_data.py

preprocess:
	python src/preprocess.py

features:
	python src/features.py

all: setup download-data preprocess features

clean:
	rm -rf data/raw/*.csv
	rm -rf data/processed/*.csv
	rm -rf features/*.csv
