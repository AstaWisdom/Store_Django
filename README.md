# Store_Django — E-Commerce + Blog System (Django)

A basic e-commerce web application built with Django featuring product catalog, guest shopping cart, discount codes, and an integrated blog system with CKEditor for rich text content.

---

## 🛒 Overview

This project shows:
- E-commerce product catalog
- Guest shopping cart
- Promo code (discount) logic
- Blog / article system
- Admin CRUD
- CKEditor rich-text editor for blog posts
- Fully working store flows using Django templates and ORM

---

## ✨ Features

### 🛍 Store
- Product list and detail pages
- Category browsing
- Shopping cart (guest supported)
- Cart total + discount calculation
- Minimal checkout (without login)
- Django admin for product/order management

### 📰 Blog
- Article creation and editing
- Rich-text fields using CKEditor
- Article listing view
- Single article page
- Image upload supported (if configured)
- SEO-friendly fields (title, slug, content)

---

## 🔧 Tech Stack

- Python 3.x
- Django
- SQLite (dev)
- Django CKEditor
- HTML/CSS Templates
- Vanilla JS
- Django Admin

---

## 🚀 Local Setup

```bash
git clone https://github.com/AstaWisdom/Store_Django.git
cd Store_Django

python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt   # or install Django + CKEditor manually

python manage.py migrate
python manage.py runserver

Visit:

http://127.0.0.1:8000/

📦 Admin Panel

Default Django admin available at:

/admin

You can manage:

    Products

    Categories

    Blog Posts

    Discounts (if available)

    Orders

🛠 What You Learn From This Project

    Django ORM

    Model relationships (product/category + blog)

    Template rendering

    Context + view logic

    CKEditor integration

    Handling media uploads

    Guest checkout implementation

    Basic e-commerce business logic

🧪 Future Improvements

    User authentication / login checkout

    Payments and gateways

    Shipping & addresses

    Blog tags & comments

    Pagination & search

    Docker deployment

    PostgreSQL configuration

    Responsive UI redesign

    Tests (unit + integration)

⚠️ Note

This is a demo and not a production-ready e-commerce system. Some security and payments are intentionally simplified for learning purposes.
📌 Author

Portfolio project created to learn practical Django development and combine e-commerce with blog / CMS functionality using CKEditor.


---
