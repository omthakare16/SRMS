
# Gas Utilities Service Request Management System  

This is a Django-based application for managing customers and their service requests. It includes both API endpoints and UI views for seamless interaction. The application allows users to create, view, and manage customer information and their associated service requests, including support for file attachments.

---

## **Features**

### **1. Customer Management**
- Add, view, update, and delete customer records.
- Track customers' associated service requests.

### **2. Service Request Management**
- Create and manage service requests for customers.
- Assign request types (e.g., installation, maintenance, repair).
- Update and track request statuses (e.g., pending, in progress, resolved).

### **3. File Attachments**
- Upload and manage attachments related to service requests.

### **4. API Endpoints**
- RESTful APIs to programmatically interact with the system.
- Endpoints for CRUD operations on customers and service requests.

### **5. UI Views**
- User-friendly interface to manage customers and service requests.

---

## **Installation**

### **1. Clone the Repository**
```bash
git clone <repository_url>
cd <project_directory>
```

### **2. Create a Virtual Environment**
```bash
python3 -m venv env
source env/bin/activate
```

### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4. Apply Migrations**
```bash
python3 manage.py migrate
```

### **5. Run the Server**
```bash
python3 manage.py runserver
```

---

## **Usage**

### **API Endpoints**
The API can be accessed via the following routes:

- **Customer List/Creation**: `/api/customers/`
- **Customer Details**: `/api/customers/<int:pk>/`
- **Customer's Service Requests**: `/api/customers/<int:customer_id>/service-requests/`
- **Service Request List/Creation**: `/api/service-requests/`
- **Service Request Details**: `/api/service-requests/<int:pk>/`

### **UI Views**
Access the web interface to manage customers and service requests:

- **Customer List**: `http://127.0.0.1:8000/customers/list/`
- **Create Service Request**: `http://127.0.0.1:8000/service-requests/new/`
- **Service Request Details**: `http://127.0.0.1:8000/service-requests/<int:pk>/detail/`

---

## **Directory Structure**

```
├── gas_utility/               # Main project directory
│   ├── settings.py            # Django settings
│   ├── urls.py                # Project-level URL configuration
│   └── ...
├── service_requests/          # App for managing service requests
│   ├── models.py              # Models for customers and service requests
│   ├── views.py               # Logic for handling requests
│   ├── urls.py                # App-level URL configuration
│   ├── forms.py               # Form definitions
│   ├── serializers.py         # Serializers for API
│   └── templates/             # HTML templates for UI
│       ├── customers/
│       │   └── customer_list.html
│       └── service_requests/
│           ├── create_request.html
│           └── service_request_detail.html
├── manage.py                  # Django project manager
└── requirements.txt           # Dependencies
```

---

## **Technologies Used**

- **Backend**: Django, Django REST Framework
- **Frontend**: Django Templates
- **Database**: SQLite (default, can be configured to PostgreSQL, MySQL, etc.)
- **File Uploads**: Handled via Django's `FileField`

---

## **Screenshots**
Include screenshots of your application here if applicable:
- **Customer List**
- **Create Service Request**
- **Service Request Details**

---

## **Contributing**

1. Fork the repository.
2. Create a new branch for your feature/fix:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Description of your feature"
   ```
4. Push to your fork and submit a pull request.

---

## **License**

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## **Contact**

For any questions or suggestions, contact us at:  
**Developer:** Om Thakare  
**Email:** omthakare1606@gmail.com  
**LinkedIn:** [Om Thakare](https://linkedin.com/in/om-thakare)  

Happy coding! 🚀
