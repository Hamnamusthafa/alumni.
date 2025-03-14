# College Alumni Portal

## Description
The **College Alumni Portal** is a web-based platform designed to connect students and alumni of a college. It provides various features such as profile management, job and internship postings, event updates, mentorship opportunities, and networking options.
link :https://drive.google.com/drive/folders/11vGsEDmaOomlrqexNJYqPJFlVHqqTuE5?usp=sharing
## Features
### 1. Authentication
- **Login Page (`index.html`)**: Users can log in using their username and password.
- **Signup Page (`reg31.html`)**: New users can register with details like name, email, phone number, role (student/alumni), and academic year.
- **JavaScript Files**: `index.js` for login and `reg31.js` for signup functionalities.

### 2. Home Page (`home.html`)
- **Navbar with Sections**:
  - **Profile (`pro.html`)**: Users can update their profiles and manage information.
  - **Events**: Displays upcoming alumni events with an option to apply.
  - **Jobs**: Job listings with application links.
  - **Internships**: Internship opportunities for students.
  - **About Us (`aboutus.html`)**: Information about the portal.
  - **Contact Us (`contactus.html`)**: Contact information and support.

### 3. Additional Features
- **Messaging System** (Future Enhancement): Allows users to connect and chat.
- **Public Chat Feature**: Similar to Quora for discussion and Q&A.
- **Admin Verification**: New users are verified against the admin database before approval.

## File Structure
```
College-Alumni-Portal/
│── index.html         # Login Page
│── reg31.html         # Signup Page
│── home.html          # Main Home Page
│── pro.html           # Profile Page
│── aboutus.html       # About Us Page
│── contactus.html     # Contact Page
│── apply.html         # Apply for jobs/events
│── styles/            # Contains all CSS files
│   ├── style1.css     # Login Page Styles
│   ├── styles.css     # Signup Page Styles
│   ├── homestyle.css  # Home Page Styles
│── scripts/           # JavaScript Files
│   ├── index.js       # Login Functionality
│   ├── reg31.js       # Signup Functionality
│── assets/            # Images and logos
│── README.md          # Project Documentation
```

## Technologies Used
- **HTML**: Structure of the website
- **CSS**: Styling and UI design
- **JavaScript**: Functionalities (Login, Signup, Navigation, etc.)
- **Firebase**: User authentication and data storage (if implemented)

## How to Run the Project
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/College-Alumni-Portal.git
   ```
2. Navigate to the project directory:
   ```bash
   cd College-Alumni-Portal
   ```
3. Open `index.html` in a browser to start the application.

## Contribution Guidelines
- Fork the repository and create a new branch for features or bug fixes.
- Make changes and commit with a meaningful message.
- Push the branch and create a pull request.

## License
This project is licensed under the MIT License.

## Contact
For any queries, reach out via the Contact Us page (`contactus.html`).



