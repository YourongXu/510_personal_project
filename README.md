# Personal Portfolio Web

This is a personal portfolio website built with HTML, CSS, and JavaScript, served using Flask. It showcases my background, education, experiences, skills, and passion. The site is intended for job searching and professional presentation.

To run this project locally:

```bash
1. Clone the repository

git clone https://github.com/yourusername/portfolio-web.git
cd portfolio-web

2. Set up a virtual environment

python -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate

3. Install Flask

pip install Flask

4. Ensure the following file structure

.
├── app.py              # Flask entry point
├── templates/
│   └── index.html      # Your portfolio HTML file
├── static/
│   ├── css/            # Custom styles (optional)
│   ├── js/             # Optional JavaScript (if used)
├── README.md

5. Run the application

python app.py

6. Open in browser


The portfolio includes a hero section, a timeline of education and experiences, categorized skill cards, and a responsive contact form layout. Animations and transitions enhance the user experience. The site is fully responsive and optimized for both desktop and mobile viewports.

Currently, the contact form is non-functional, but it can be extended using Flask routes and connected to a database or email service. Future improvements include adding a portfolio projects section and enabling dynamic form handling.
