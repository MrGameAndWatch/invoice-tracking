# invoice-tracking
This is a small demo application to show off a little bit.
To run the application, clone the repository and run `docker-compose up --build` from the project root.
A proper deployment to the cloud will follow soon.

### Use case:
You have been on a business trip, accumulating personal expenses for traveling, sleeping at a hotel and having a business dinner. 
Your company covers your expenses but you need to enter the data and they need to process it. This small project solves this problem by providing
an UI to enter your data and an UI for the company to download a summary of the expenses (within a certain time frame) in order to execute the payments.

### Services:
This application consists of different microservices, each having their own individual domain and task.
#### Invoice Service
This is the backend for storing and querying invoices.
#### Employee Frontend
This is the view for employees. Employees can enter new invoices here to be refunded by their employer.
#### Employer Frontend
This is the view for employers. Employers can gather an overview of all invoices and the refund sum for each individual employee during a certain time frame.

### Extensions:
See issue list for upcoming feature plans.
