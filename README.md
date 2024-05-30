# News-Aggregator-Website

Functional & Non Functional Requirements

User Registration
1) The system allows new users to register using a username, email, and password.
2) The username should be required, unique, and consist of 150 characters or fewer, containing letters, digits, and characters (@/./+/-/_).
3) The email should be required and unique.
4) The system should require users to confirm their password by entering it twice.
5) The system provides feedback on password requirements and any issues with the input.

User Login
1) The system allows registered users to log in using their username or email and password.
2) The system  displays an error message for incorrect username/email or password.
   
Profile Management
1) Users should be able to view and edit their profile information
2) The profile page displays the user's saved articles.
   
Update Profile
1) Users should be able to update their profile information, including username, email address, full name and profile picture.

News Scraping
1) The system scrapes news articles from The Onion website.
2) The system should scrape the following details from each article:
  a) Title
  b) URL
  C) Image URL (if available)
  d) Source name

Dashboard
1) The system displays a list of news articles on the dashboard, including title, image, source.
   
Saving Articles
1) Logged-in users should be able to save articles to their profile for later reading by clicking a "Save" button.
2) Users should be able to remove articles from their profile by clicking a "Remove" button.
   
Sharing Articles
1) Users should be able to share articles via social media platforms (e.g., Facebook, WhatsApp).
2) Users should be able to copy the article link to the clipboard using a "Copy to Clipboard" button.
   
Dark Mode
1) Users should be able to toggle between light mode and dark mode for the website interface.

#Installation

    pip install bs4
    pip install requests
    pip install django-social-share
    
#Run Using Command Prompt

   python manage.py runserver
