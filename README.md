# library-management
# 📚 Library Management System — Python + MySQL

A simple console-based Library Management System built with **Python** and **MySQL** Connector.  
This project helps in performing basic CRUD operations on a library database like adding, viewing, searching, updating, and deleting books.

---

## 💻 Tech Stack:
- Python 3.x
- MySQL Database
- MySQL Connector (Python Library)
- VS Code / Any Python IDE

---

## 🎯 Features:
- ✅ Add New Books
- ✅ View All Books in the Library
- ✅ Search Books by Author
- ✅ Update Book Availability
- ✅ Delete Book by ID
- ✅ Menu-Driven Console Interface

---

## 🗃️ Database Structure:
**Database Name:** `library_db`  
**Table Name:** `books`

| Column     | Type         |
|------------|--------------|
| id        | INT PRIMARY KEY AUTO_INCREMENT |
| title     | VARCHAR(255) |
| author    | VARCHAR(255) |
| year      | INT          |
| available | BOOLEAN / TINYINT(1) |

---

## ⚙️ How to Run:
1. Install MySQL and create the `library_db` database.
2. Create the `books` table using:
   ```sql
   CREATE TABLE books (
       id INT AUTO_INCREMENT PRIMARY KEY,
       title VARCHAR(255),
       author VARCHAR(255),
       year INT,
       available BOOLEAN
   );
