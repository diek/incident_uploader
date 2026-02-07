# Incident Reports Django Project

This Django project provides a comprehensive system for managing incident reports within an organization. It allows users to log incidents associated with specific shifts and locations, attach images, and track relevant details such as theft, merchandise costs, and involved personnel.

## Features

- Manage locations where incidents occur
- Record shifts assigned to employees at specific locations
- Create detailed incident reports linked to shifts
- Attach multiple images to incident reports with ordering
- Track incident specifics: date/time, summary, merchandise details, theft, and involved persons

## Models Overview

### Location
Represents a physical or designated area where incidents can occur.

### Shift
Associates employees (users) with specific locations and shifts. Ensures unique shift-location pairs.

### IncidentReport
Stores detailed reports about incidents, including date/time, summary, merchandise info, theft status, and involved persons.

### IncidentImage
Allows attaching multiple images to an incident report, with support for ordering and captions.

## Setup Instructions

### Prerequisites, see pyproject.toml for complete requirements

- Python 3.x
- Django 5.2 or later
- Pillow (for image handling)
- UV (the modern dependency manager)

### Installation using UV


```bash
gh repo clone diek/incident_uploader
cd incident_uploader
uv venv
source .venv/bin/activate.fish
uv sync
```

