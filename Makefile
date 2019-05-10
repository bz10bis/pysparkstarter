help:
	@echo "clean - remove all build, test, coverage and Python artifacts"
	@echo "build - package"

all: default

default: clean build

clean:
	rm -rf ./dist/

build:
	mkdir ./dist
	cp ./src/main.py ./dist
	cd ./src && zip -x main.py -r ../dist/jobs.zip .
