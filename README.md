# Semla Showcase Project

A web application built with Django to showcase different semlas (Swedish cream buns) and featuring their locations, prices, and other data. The application uses SQLite for data storage and includes features for displaying and managing semla information.

Also uses Pylint for analysing and optimizing the code

## Prerequisites

- Python 3
- Visual Studio Code or PyCharm
- Git (for version control)

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd Semla
   ```

2. **Create and Activate Virtual Environment**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install django
   pip install Pillow
   ```

4. **Database Setup**
   ```bash
   cd semla_web
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Import Initial Data**
   - Ensure images are placed in the `media/` directory
   - Place `semlor.csv` in the `semla_web/` directory
   - Run the import command:
   ```bash
   python manage.py import_semlor
   ```

6. **Run Development Server**
   ```bash
   python manage.py runserver
   ```
   Visit `http://127.0.0.1:8000` in your browser

## Project Structure

```
Semla/
├── semla_web/
│   ├── manage.py
│   ├── media/          # Stores semla images
│   ├── semlor.csv      # Data source for semla information
│   ├── semla_django/   # Main application
│   │   ├── models.py   # Database models
│   │   ├── views.py    # View logic
│   │   └── templates/  # HTML templates
│   └── semla_web/      # Project settings
```

## Features

- Display semlas in a responsive grid layout
- Show details including:
  - Bakery name
  - Location
  - Price
  - Type of semla
  - Vegan options
- Image for each semla
- Responsive design for various screen sizes (not phone adapted yet)

## Technology Stack

- **Backend**: Django 5.x
- **Database**: SQLite
- **Frontend**: HTML5, CSS3
- **Image Handling**: Pillow

## Future Enhancements

- Rating system implementation and ip-adress limit
- Phone size adaption
- The page will show the top 3 in ranking before all are shown
- Comment functionality
- Search and filter options

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.