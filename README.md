# ShopKart
Introducing our Django-based eCommerce platform, where your online shopping experience reaches new heights of convenience and security. Whether you're a discerning shopper looking for the latest trends or a merchant seeking to expand your online business, our website offers an all-encompassing solution.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

Provide a brief overview of your Django eCommerce website. Mention its purpose, key functionalities, and any unique selling points. You can also include a screenshot or link to a live demo here.

## Features

List the main features of your eCommerce website. For example:

- User authentication and registration
- Product catalog
- Shopping cart and checkout
- Payment integration with Paytm
- Order management
- User profiles and order history
- Admin dashboard for managing products and orders

## Requirements

List the prerequisites that are necessary to run your project, such as:

- Python 3.x
- Django 3.x
- PostgreSQL or SQLite
- Other dependencies (mention any additional packages or libraries)


## Installation

Provide instructions on how to set up and install your project. Include any specific steps, commands, or configurations needed. For example:

1. Clone the repository:

   ```bash
   git clone https://github.com/Aayush3014/ShopKart.git
   ```

2.Create a virtual environment and activate it:
  ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'

  ```
3. Install project dependencies:
   ```bash
      pip install -r requirements.txt
   ```
4.Apply database migrations:
```bash
  python manage.py migrate
```
5. Create a Super User for accessing Admin Panel and adding Products:
   ```bash
     python manage.py createsuperuser
   ```

6. After all the setup configure these values
   -In Shoppy/settings.py
     - EMAIL_HOST_USER = 'your email'
     - EMAIL_HOST_PASSWORD = 'your app password'
     - Your email password won't work because google has prohibited unauthorized apps from using it's main credentials
        i.e. .You have to generate an app password for your ecommerce app from google manage accounts section.
       [Refer This video for generating App Password](https://www.youtube.com/watch?v=hXiPshHn9Pw&ab_channel=TweakLibrary)

   -In ShopApp/keys.py
     - MID = "your paytm merchant id"
     - MK = "Your merchant Key"
       

8. Start the development server:
   ```bash
      python manage.py runserver
   ```
## Usage
Provide instructions on how to use your eCommerce website. Explain how users can navigate the site, make purchases, and manage their accounts. Include any important usage tips or considerations.

## Contributing
If you'd like to contribute to this project, please follow these guidelines:

- Fork the repository.

- Create a new branch for your feature or bug fix.

- Make your changes and test thoroughly.

- Create a pull request with a clear description of your changes.

## License
This project is licensed under the MIT License. You are free to use, modify, and distribute it as per the terms of the license.
