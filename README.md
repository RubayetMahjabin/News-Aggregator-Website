# News-Aggregator-Website

# Home Page

![image](https://github.com/RubayetMahjabin/News-Aggregator-Website/assets/159466698/a5fa514a-28ee-4dd5-9850-08c9a9a61535)

# User Login Page

![image](https://github.com/RubayetMahjabin/News-Aggregator-Website/assets/159466698/6b3ce895-025b-49d6-86a0-846338e7d112)

# User Registration Page

![image](https://github.com/RubayetMahjabin/News-Aggregator-Website/assets/159466698/a85cbbcf-21b1-4e83-b5d4-b09e081fffdd)

# Dashboard Page 1

![image](https://github.com/RubayetMahjabin/News-Aggregator-Website/assets/159466698/66b1648d-fb1a-4af9-9caa-a0c5901f516e)

# Dark mode

![image](https://github.com/RubayetMahjabin/News-Aggregator-Website/assets/159466698/e0845ebe-b6c3-4830-a39c-d84d3163c50c)

# Copy to Clipboard

![image](https://github.com/RubayetMahjabin/News-Aggregator-Website/assets/159466698/b53daac6-9095-4312-a388-6509f2cf4d4c)

# Profile Page

![image](https://github.com/RubayetMahjabin/News-Aggregator-Website/assets/159466698/87eb692a-873a-4018-b0f3-b17d445925ea)

# Update Profile Page

![image](https://github.com/RubayetMahjabin/News-Aggregator-Website/assets/159466698/38537aa3-baa7-4c1f-a08b-2ecdeda82e30)

# Article Saved in Profile Using save button

![image](https://github.com/RubayetMahjabin/News-Aggregator-Website/assets/159466698/1ca06d26-6e10-4d47-b092-73c1aa77759e)

# Article Removed from Profile Using remove button

![image](https://github.com/RubayetMahjabin/News-Aggregator-Website/assets/159466698/ed50ac65-6f1a-49c0-b6c7-b21270799538)

# Facebook Share Page

![image](https://github.com/RubayetMahjabin/News-Aggregator-Website/assets/159466698/65527d92-9210-4f2a-bbb9-ab35c24bd15b)

# Whatsapp Share Page

![image](https://github.com/RubayetMahjabin/News-Aggregator-Website/assets/159466698/b3fd5a26-86d6-4530-beac-2dc900a0418d)


------------------------------------------------------------------------------------------------------------------------------------------

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
