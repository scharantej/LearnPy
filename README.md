## Flask Application Design for a Website That Teaches Python

### HTML Files

- **index.html:**
    - Main landing page of the website.
    - Contains an introduction to Python and links to various lessons.
- **lessons.html:**
    - Page that displays a list of all Python lessons available on the website.
    - Each lesson is linked to its corresponding page.
- **lesson_detail.html:**
    - Page that displays the content of a specific Python lesson.
    - Includes code examples, explanations, and exercises.
- **exercises.html:**
    - Page that provides interactive exercises for users to practice their Python skills.
    - Includes code editor and submission form.
- **solutions.html:**
    - Page that displays solutions to the exercises.

### Routes

- **@app.route('/')**: Displays the index.html page.
- **@app.route('/lessons')**: Displays the lessons.html page.
- **@app.route('/lessons/<lesson_id>')**: Displays the lesson_detail.html page for a specific lesson.
- **@app.route('/exercises')**: Displays the exercises.html page.
- **@app.route('/solutions')**: Displays the solutions.html page.
- **@app.route('/submit_exercise')**: Handles the submission of exercise code and returns feedback.