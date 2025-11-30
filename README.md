# Job Board Platform Backend

A modern, scalable, passwordless/SSO-ready **Job Board Platform Backend** built with a modular architecture and production-grade standards.

---

## 🚀 Project Overview
This backend powers a job board system that supports:
- User authentication via **SSO/passwordless providers** (Google, GitHub, Email Magic Link, Phone OTP).
- Role-based access for admins and users.
- Company management.
- Job postings with advanced filtering.
- Job applications.
- Following companies and saving jobs.
- Swagger/OpenAPI documentation.

This project follows real-world backend development workflows including modular apps, optimized database queries, and clean API design.

---

## 🧩 Key Features

### **1. Authentication (SSO / Passwordless)**
- No password storage.
- Supports Google, GitHub, Apple, email link, phone OTP, etc.
- Users can link multiple auth providers.

### **2. Users & Profiles**
- Skill tagging system.
- Editable professional profile.

### **3. Companies**
- Create, update, and manage company profiles.
- Users can follow companies.

### **4. Job Postings**
- Admin/company accounts can create jobs.
- Filtering by location, employment type, remote, salary, etc.

### **5. Applications**
- Users can apply for jobs.
- Each user can only apply once per job.

### **6. Saved Jobs / Bookmarks**
- Users save jobs for quick access.

### **7. Swagger Documentation**
- Complete API docs at `/api/docs`.

---

## 🛠 Tech Stack

| Technology | Purpose |
|------------|----------|
| **Django** | Backend framework |
| **PostgreSQL** | Relational database |
| **JWT** | Authentication tokens |
| **Swagger / drf-yasg** | API documentation |
<<<<<<< HEAD
| **Render| Deployment |
=======
| **Render** | Deployment |
>>>>>>> 704aa0c (feat: Update README with project setup instructions and usage details)

---

## 🗂 Django Apps

| App | Responsibility |
|-----|----------------|
| `accounts` | Users, skills, SSO authentication |
| `companies` | Company profiles |
| `jobs` | Job postings, filtering |
| `applications` | Job applications |
| `documentation` | Swagger/OpenAPI setup |

---

## 🗄 Database Schema Summary

### **Users (passwordless)**
- Stores only profile info and email.

### **Auth Providers**
- Stores provider type and external provider user ID.

### **Skills**
- Many-to-Many with users.

### **Companies**
- Companies posting jobs.

### **Jobs**
- Posted by companies.

### **Applications**
- One user → many applications.  
- One job → many applications.

### **Saved Jobs**
- Many-to-Many between users and jobs.

### **Company Followers**
- Many-to-Many between users and companies.

---

## API Endpoints:
```bash
/api-auth/login
/api/users/ 
/api/applications/ 
/api/jobs/ 
/api/skills/
/api/company/ 
/api/silk/ 
```


