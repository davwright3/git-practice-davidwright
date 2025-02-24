# David Wright -- Pip Pip Hooray Assignment

## Purpose
Pip Pip Hooray is designed to show students how to install modules, uninstall modules, and create requirements.txt.


## List of steps

1. Activated virtual environment in root project folder.

2. Imported geopandas, requests and plotly.  Pandas, numpy, and zipfile were already available.

3. Transcribed code from project directory on Blackboard.

4. Used pip freeze > all_requirements.txt to generate requirements file.

5. Uninstalled all requirements using command pip uninstall -y -r all_requirements.txt (see screenshot in file tree)

6. Reinstalled dependencies from the all_requirements.txt file.


## Output from Dependency Tree
   coverage==7.6.12
geopandas==1.0.1
  - numpy [required: >=1.22, installed: 2.2.3]
  - packaging [required: Any, installed: 24.2]
  - pandas [required: >=1.4.0, installed: 2.2.3]
    - numpy [required: >=1.26.0, installed: 2.2.3]
    - python-dateutil [required: >=2.8.2, installed: 2.9.0.post0]
      - six [required: >=1.5, installed: 1.17.0]
    - pytz [required: >=2020.1, installed: 2025.1]
    - tzdata [required: >=2022.7, installed: 2025.1]
  - pyogrio [required: >=0.7.2, installed: 0.10.0]
    - certifi [required: Any, installed: 2025.1.31]
    - numpy [required: Any, installed: 2.2.3]
    - packaging [required: Any, installed: 24.2]
  - pyproj [required: >=3.3.0, installed: 3.7.1]
    - certifi [required: Any, installed: 2025.1.31]
  - shapely [required: >=2.0.0, installed: 2.0.7]
    - numpy [required: >=1.14,<3, installed: 2.2.3]
pipdeptree==2.25.0
  - packaging [required: >=24.1, installed: 24.2]
  - pip [required: >=24.2, installed: 25.0.1]
plotly==6.0.0
  - narwhals [required: >=1.15.1, installed: 1.28.0]
  - packaging [required: Any, installed: 24.2]
requests==2.32.3
  - certifi [required: >=2017.4.17, installed: 2025.1.31]
  - charset-normalizer [required: >=2,<4, installed: 3.4.1]
  - idna [required: >=2.5,<4, installed: 3.10]
  - urllib3 [required: >=1.21.1,<3, installed: 2.3.0]

## Observations
I initially got an error on the file download because I had transcribed the url incorrectly, but it was easily fixed.

The Chroropleth autocompleted to something unusable and I did not catch it at first, so I received an error when I tried to run the file.

The assignment says to reinstall modules from requirements.txt, but had us save as all_requirements.txt, so users need to use the second filename to reinstall required modules.

   



