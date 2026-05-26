# 🛠️ FixBoard – Mini Campus Issue Reporting System

FixBoard is a small full-stack campus issue reporting web application.  
It allows students to report campus problems such as network issues, classroom problems, lab issues, lost items, and other campus-related concerns.

The project is built using **HTML, CSS, JavaScript, Python Flask, and MySQL**.  
It is deployed using **Render** for both frontend and backend, with **Aiven MySQL** as the online database.

> **🌐 Live Website:**  
> [https://pronway.diu.my.id](https://pronway.diu.my.id)

> **🔗 Backend API:**  
> [https://fixboard-lrqx.onrender.com](https://fixboard-lrqx.onrender.com)

---

## Our Team

> **Project Name:** FixBoard

- Pronway Prosoon Mitra – Developer

---

## 📸 Demo Images

![FixBoard Dark Theme Demo](resources/main_page_dark.png)

---

## ✨ Technical Stack

- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Python Flask
- **Database:** MySQL
- **Database Hosting:** Aiven MySQL
- **Backend Hosting:** Render Web Service
- **Frontend Hosting:** Render Static Site
- **Version Control:** Git + GitHub
- **Custom Domain:** pronway.diu.my.id

---

## 📚 Core Capabilities

| Feature                    | Description                                                                              |
| -------------------------- | ---------------------------------------------------------------------------------------- |
| **Issue Reporting**        | Students can submit campus-related problems through a simple form                        |
| **Issue Listing**          | All submitted issues are displayed dynamically from the database                         |
| **Category Selection**     | Issues can be categorized as Network, Classroom, Lab, Lost and Found, or Other           |
| **Status Tracking**        | Each issue has a default status such as Pending                                          |
| **MySQL Database Storage** | Submitted issues are stored permanently in an online MySQL database                      |
| **REST API**               | Flask backend provides API routes for creating and fetching issues                       |
| **Responsive Layout**      | Form and issue list are displayed side-by-side on desktop and stacked on smaller screens |
| **Light/Dark Mode**        | Users can switch between light and dark themes                                           |
| **Custom Domain**          | The deployed frontend can be accessed using a custom subdomain                           |

---

## 📂 Project Structure

```text
Fixboard/
│
├── backend/
│   ├── app.py              # Flask backend entry point
│   ├── requirements.txt    # Python dependencies
│   ├── .gitignore          # Ignores venv, .env, cache files
│   └── .env                # Local environment variables, not uploaded to GitHub
│
├── frontend/
│   ├── index.html          # Main frontend page
│   ├── style2.css          # Website styling, gradient theme, responsive layout
│   ├── script.js           # Frontend logic and API calls
│   ├── favicon.ico         # Browser favicon
│   ├── favicon.png         # PNG favicon
│   └── icon-192.png        # App icon
│
└── README.md
```
