# Forex Structuring Detection System

A modular Python system for detecting structural patterns in Forex datasets.

**Coded in Python, developed by Sahantech Solutions.**

## Features

- Modular data loading and preprocessing
- Detection models for Forex structuring
- Extensible utility functions
- Unit tests for reliability

## Project Structure

```
forex_structuring_detection/
    main.py                # Entry point
    config.py              # Configuration settings
    data/                  # Data loaders, preprocessors
    models/                # Detection models
    utils/                 # Helpers, logging
    tests/                 # Unit tests
```

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
python -m forex_structuring_detection.main
```

## Testing

Run all tests:

```bash
python -m unittest discover forex_structuring_detection/tests
```