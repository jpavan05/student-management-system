
🎓 Student Management System (Django)

A beginner-friendly Django project that provides full CRUD (Create, Read, Update, Delete) functionality to manage student records.
This project is ideal for learning Django Models, Views, Templates, Forms, and basic web development.
----------------------------------------------------------------------------------
🔥   Project Features

  ➕ Add New Students
  📄 View Student List
  ✏️ Update Student Details
  ❌ Delete Students
  🧱 Django MVT Architecture
  ✔️ Form Validation
  🗄 SQLite Database (default)

----------------------------------------------------------------------------------
## 🛠 Tech Stack
- Python  
- Django  
- HTML, CSS, Bootstrap  
- SQLite  

----------------------------------------------------------------------------------

## 🚀 How to Run the Project

⭐ 1️⃣ Clone the Repository
git clone https://github.com/jpavan05/student-management-system.git
cd student-management-system

⭐ 2️⃣ Create Virtual Environment
python -m venv env

⭐ 3️⃣ Activate Virtual Environment
Windows:
env\Scripts\activate

Mac / Linux:
source env/bin/activate

⭐ 4️⃣ Install Dependencies
pip install -r requirements.txt

⭐ 5️⃣ Apply Migrations
python manage.py makemigrations
python manage.py migrate

⭐ 6️⃣ Run the Server
python manage.py runserver

----------------------------------------------------------------------------------
📂 Project Structure

student-management-system/
│── studentmgmt/        # Project settings & URLs
│── students/           # App: models, views, forms, app URLs
│── templates/          # HTML templates
│── db.sqlite3          # SQLite database
│── manage.py           # Django project manager
│── requirements.txt    # Project dependencies
