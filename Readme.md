# Task

Write a library that supports validating and formatting post codes for UK. The details of which postI l codes are valid and which are the
parts they consist of can be found at https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom#Formatting.
The API that this library provides is your choice.

# Building
```sh
python setup.py sdist
```
# Installing
```sh
pip install . --upgrade
```
# How to use
```python
from postcodeworker import EnglandPostCodeWorker
worker = EnglandPostCodeWorker(False)
validated_post_code = worker.validate("le12 9SL")
```
Parameters of EnglandPostCodeWorker:
  - use_special_case: bool.

Available methods:
  - validate(post_code: str). Method return formatted post code if post_code is valid. If isn't the method raises exception ValidationError.

# Run tests
Install pytest:
```sh
pip install pytest
```
Run tests:
```sh
python -m pytest .
```
# Another similar libraries
  - postcode_validator_uk. Library doesn't work with special cases.
  - uk_postcode_validator. Library requires Internet connection.

# What can improve
  - Add more detailed checking of areas and districts. For example: 'EC63' - available outward part, but there isn't this post code in the real world.
  - Add checking non-geographic post codes
