# VendorManagement
Build a vendor management app using Django and Django REST Framework. The app will manage vendor profiles and monitor purchase orders and calculate vendor performance metrics.

## Prerequisites
- Python (version 3.11)
- Django (version 5.0.4)

## Installation

# 1. Clone the repository:
   bash:  
   git clone https://github.com/NIKHILP16/VendorManagement.git
   cd project-directory (VendorManagement) 

# 2.Create a virtual environment:
python -m venv venv  
source venv/bin/activate  # For Linux/Mac  
venv\Scripts\activate     # For Windows  

# 3.Install dependencies:
pip install -r requirements.txt  

# 4.Database setup:
python manage.py makemigrations  
python manage.py migrate  


## Usage

# 1.Start the server:
python manage.py runserver  

# 2.Create User 

● Create User:
    - POST /api/account/register 
        eg. { "email":"x@y.xyz","password":"Passport1" ,"name":"XYZ" } 

● Login User to genrate token: 
    - POST /api/account/login   
        eg. { "email":"n@p.com","password":"Passport1" } 

● User Logout 
    - POST /api/account/logout

● Change Password for User :
    - POST /api/account/change-password  
        eg. {"current_password": "string","new_password": "string"}

● Refresh token for User:
    - POST /api/account/token-refresh'   
        eg. {"refresh": "string"}


# 3.Access API endpoints:


## Vendor API Endpoints: 

● Create a new vendor:
    - POST /api/vendors/

● List all vendors:
    - GET /api/vendors/  

● Retrieve a specific vendor's details:
    - GET /api/vendors/{vendor_id}/

● Update a vendor's details:
    - PUT /api/vendors/{vendor_id}/ 

● Delete a vendor:  
    - DELETE /api/vendors/{vendor_id}/

● Retrieve a vendor's performance metrics: 
    - GET /api/vendors/{vendor_id}/performance



## Purchase Order API Endpoints:  

● Create a purchase order:
    - POST /api/purchase_orders/  

● List all purchase orders with an option to filter by vendor:
    - GET /api/purchase_orders/

● Retrieve details of a specific purchase order:
    - GET /api/purchase_orders/{po_id}/: 

● Update a purchase order:  
    - PUT /api/purchase_orders/{po_id}/: 

● Delete a purchase order:  
    - DELETE /api/purchase_orders/{po_id}/: 

● Acknowledge POs:
    - POST /api/purchase_orders/{po_id}/acknowledge 

