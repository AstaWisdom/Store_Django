# Store_Django — E-Commerce + Blog + User Auth + Referral & Rewards (Django)

A full Django e-commerce application featuring product catalog, guest shopping cart, discount logic, user authentication, referral codes with reward points, blog system with CKEditor, comments, tags, shipping & addresses, search, pagination, and responsive UI.

---

## 🛒 Overview

This project demonstrates:
- Real e-commerce flows with Django
- Guest shopping cart and checkout logic
- User authentication and extended profile data
- Invite / referral system + reward points
- Blog system (CKEditor, tags, comments)
- Responsive UI design
- Search & pagination
- Shipping & addresses
- Django ORM and admin integrations

---

## ✨ Features

### 🛍 Store
- Product list & detail pages
- Category browsing
- Add to cart (guest supported)
- Discount / promo code
- Shipping & address handling
- Responsive UI design
- Checkout flow (without payment gateway yet)
- Admin management for products, orders and categories

### 🔐 User Authentication
- Register / login
- Extended user info
- Authentication forms
- Login required for specific actions
- User dashboard (profile, orders, invites, reward points)

### 🧑‍🤝‍🧑 Invite & Referral Rewards
- Register using invite code
- Validate referral code on registration
- Earn reward points for referred users
- Extendable to more complex reward systems

### 🔎 Search & Pagination
- Product search
- Blog search
- Pagination for product lists & blog lists

### 📰 Blog (CKEditor)
- Create / edit articles
- Rich-text editor (CKEditor)
- Blog tags and categories
- Comments system
- Image upload (if configured)
- SEO fields (title, slug, content)

---

## 🔧 Tech Stack

- Python 3.x
- Django
- SQLite (development)
- CKEditor
- HTML / CSS (responsive)
- Vanilla JS

---

## 🚀 Local Setup

```bash
git clone https://github.com/AstaWisdom/Store_Django.git
cd Store_Django

python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

Visit:

http://127.0.0.1:8000/

📦 Admin Panel

/admin

Manage:

    Products

    Categories

    Orders

    Blog posts

    Tags

    Comments

    Users

    Invite codes

🧠 What You Learn From This Project

    Django ORM & models

    Template rendering and context data

    User authentication flows

    Referral & reward logic

    Blog CMS integration

    Handling media uploads

    Search & pagination

    Responsive UI development

    Basic e-commerce architecture

🧪 Future Improvements

    Payment gateway integration

    Better shipping methods & tracking

    Docker deployment

    PostgreSQL for production

    Additional security hardening

    Automated tests (unit & integration)

⚠️ Note

This is a demo / portfolio project and not fully production hardened. Payments and certain security features are intentionally simplified.
📌 Author

Portfolio project created to practice Django development by combining e-commerce, authentication, referral logic, search, pagination, responsive UI and blog CMS functionality.


---
