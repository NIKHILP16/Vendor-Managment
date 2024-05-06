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

# 2. Create a virtual environment:
python -m venv venv  
source venv/bin/activate  # For Linux/Mac  
venv\Scripts\activate     # For Windows  

# 3. Install dependencies:
pip install -r requirements.txt  

# 4. Database setup:
python manage.py makemigrations  
python manage.py migrate  


## Usage

# 1. Start the server:
python manage.py runserver  

# 2. Create User 

● Create User:  
&emsp;- POST /api/account/register   
&emsp;&emsp;eg. { "email":"x@y.xyz","password":"Passport1" ,"name":"XYZ" } 

● Login User to genrate token:   
&emsp;- POST /api/account/login      
&emsp;&emsp;eg. { "email":x@y.xyz","password":"Passport1" } 

● User Logout:   
&emsp;- POST /api/account/logout

● Change Password for User:    
&emsp;- POST /api/account/change-password     
&emsp;&emsp;eg. {"current_password": "string","new_password": "string"}

● Refresh token for User:  
&emsp;- POST /api/account/token-refresh'      
&emsp;&emsp;eg. {"refresh": "string"}


# 3. Access API endpoints:


## Vendor API Endpoints: 

● Create a new vendor:  
&emsp;- POST /api/vendors/

● List all vendors:  
&emsp;- GET /api/vendors/  

● Retrieve a specific vendor's details:  
&emsp;- GET /api/vendors/{vendor_id}/

● Update a vendor's details:  
&emsp;- PUT /api/vendors/{vendor_id}/ 

● Delete a vendor:  
&emsp;- DELETE /api/vendors/{vendor_id}/

● Retrieve a vendor's performance metrics:   
&emsp;- GET /api/vendors/{vendor_id}/performance



## Purchase Order API Endpoints:  

● Create a purchase order:  
&emsp;- POST /api/purchase_orders/  

● List all purchase orders with an option to filter by vendor:  
&emsp;- GET /api/purchase_orders/

● Retrieve details of a specific purchase order:  
&emsp;- GET /api/purchase_orders/{po_id}/ 

● Update a purchase order:    
&emsp;- PUT /api/purchase_orders/{po_id}/

● Delete a purchase order:    
&emsp;- DELETE /api/purchase_orders/{po_id}/  

● Acknowledge POs:  
&emsp;- POST /api/purchase_orders/{po_id}/acknowledge 

