# 🛒 Django E-Commerce

A simple e-commerce platform built using **Django** and **Django REST Framework** with a responsive frontend using **HTML, CSS, and JavaScript**.

## 📌 Features
- 🛍️ **Product Listing** – View available products
- 🛒 **Shopping Cart** – Add and manage items in the cart
- 📦 **Checkout Process** – Simulated checkout flow
- 🔍 **Search Functionality** – Search for products
- 🎨 **Responsive UI** – Built with HTML, CSS, and JavaScript

---

## 🚀 Installation & Setup

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/arbaz5656/django-ecommerce.git
cd django-ecommerce
```

### 2️⃣ Create a Virtual Environment
```sh
python -m venv ven
source ven/bin/activate  # On Mac/Linux
ven\Scripts\activate  # On Windows
```

### 3️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 4️⃣ Run Database Migrations
```sh
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Create a Superuser (Admin)
```sh
python manage.py createsuperuser
```

### 6️⃣ Start the Development Server
```sh
python manage.py runserver
```

Now visit **`http://127.0.0.1:8000/admin/`** to access the admin panel.

---

## 📜 API Endpoints
| Method | Endpoint | Description |
|--------|---------|-------------|
| GET | `/api/products/` | List all products |
| POST | `/api/cart/` | Add item to cart |
| GET | `/api/cart/` | View cart items |
| DELETE | `/api/cart/<id>/` | Remove item from cart |

---

## 🎨 Frontend Setup
The frontend uses **HTML, CSS, and JavaScript** and fetches data from the Django API.

To test it, open the `index.html` file in your browser.

---

## 🛠️ Technologies Used
- **Backend:** Django, Django REST Framework, SQLite/MySQL
- **Frontend:** HTML, CSS, JavaScript
- **Version Control:** Git & GitHub

---

## 📌 Future Enhancements
✅ User Authentication (Login/Signup)
✅ Payment Gateway Integration
✅ Order Management
✅ Product Categories & Filters

---

## 📄 License
This project is licensed under the **MIT License**.

---

## 🙌 Contribution
Feel free to fork this repository and contribute!

```sh
git clone https://github.com/arbaz5656/django-ecommerce.git
git checkout -b feature-branch
git commit -m "Add new feature"
git push origin feature-branch
```

Create a **pull request**, and I'll review it. 🚀

---

## 📞 Contact
For any queries, reach out at **your-email@example.com** or connect on GitHub!

Happy coding! 😊
