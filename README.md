# Craftkalpana

**CraftKalpana** is an eCommerce platform that connects Indian small-scale handmade craftsmen with potential buyers. The platform showcases unique, handcrafted products, enabling artisans to reach a broader market and customers to access high-quality, handmade crafts.

## Table of Contents
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
  
## Features
- Display of various handcrafted items with categories and detailed descriptions.
- User authentication and profile management.
- Shopping cart and order management system.
- Secure payment gateway integration (Google Pay, etc.).
- Rating and review system for products.
- Mobile-friendly, responsive design using Bootstrap 5.
- Database management using SQLite (or Postgres, MySQL as needed).

## Tech Stack
- **Backend:** Python, Django
- **Frontend:** HTML, CSS, Bootstrap 5, Vanilla JS, SASS
- **Database:** SQLite (can be swapped with Postgres or MySQL)
- **Payment Integration:** Google Pay (testing)
- **Icons:** FontAwesome 
- **Version Control:** Git, GitHub

## Getting Started

### Prerequisites
Make sure you have the following installed on your system:
- Python 3.x
- Django
- SQLite (or another database like Postgres, MySQL)
- Node.js (for managing SASS and JavaScript dependencies)
- Git

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Krishnakant-Pal/Craftkalpana.git
   cd craftkalpana
   ```

2. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv\Scripts\activate 
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Migrate the database:
   ```bash
   python manage.py migrate
   ```

5. Create a superuser to access the admin panel:
   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

7. Access the site by visiting `http://127.0.0.1:8000/` in your browser.

## Usage
- **Admin Panel:** To manage the products, orders, and user accounts, go to `http://127.0.0.1:8000/admin/` and log in with the superuser account.
- **Shopping Cart:** Users can browse crafts, add items to their cart, and proceed to checkout.
- **Payment:** Users can complete their purchase using integrated payment gateways with strip.
  
### Customization
- Update the SASS variables to change theme colors or other styling aspects (`static/css/_variable_custom.scss`).
- Modify product categories or add new crafts using the Django admin panel.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

