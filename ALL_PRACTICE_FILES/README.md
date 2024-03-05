# RentVista

## Description

A housing website designed to facilitate property rentals and sales, providing users with a platform to explore, search for, and inquire about available properties. The website includes functionalities for property listings, detailed property pages, user reviews, and user authentication.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

## Features

- Homepage displaying property listings with summary information.
- Property detail pages showcasing high-quality images, detailed descriptions, pricing, and terms.
- User authentication and registration system.
- User review system for properties.
- Real-time updates for property availability and pricing.

## Technologies Used

- Frontend: HTML, CSS, JavaScript, React.js
- Backend: Node.js, Express.js
- Database: MongoDB
- APIs: Utilizes custom RESTful APIs for property data and user management.

### Install Dependencies:

### Environment Variables:

- Create a `.env` file based on the provided `.env.example`.
- Fill in necessary environment variables (e.g., database credentials, API keys).

### Run the Application:

### Accessing the Application:

Open your web browser and navigate to [http://localhost:3000](http://localhost:3000) to access the housing website.

## Usage

### Homepage:

- Explore property listings displayed on the homepage.
- Click on individual properties to view detailed information.

### Property Detail Pages:

- Access detailed property information including images, descriptions, pricing, and terms.
- Submit inquiries or view user reviews/ratings for properties.

### User Authentication:

- Register or log in to access additional features such as submitting reviews.

## API Endpoints

The website utilizes the following API endpoints:

- `/api/properties`: Fetches property data for listings and details.
- `/api/reviews`: Manages user reviews and ratings for properties.
- `/api/users`: Handles user registration and authentication.

For detailed API documentation, refer to [API Documentation](api-documentation.md).

## Contributing

Contributions to improve the project are welcome. Follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/improvement`).
3. Make modifications and commit changes (`git commit -am 'Add new feature'`).
4. Push the branch (`git push origin feature/improvement`).
5. Create a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
