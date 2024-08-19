# Spotify-Playlist-Recommendation-System
This project utilizes the Spotify API to recommend songs based on a user's playlist. It involves authenticating with the API, managing paginated data retrieval, and generating song recommendations. Through this project, I gained experience in API authentication, handling large datasets with pagination, and applying recommendation algorithms to provide personalized music suggestions.

# Dependencies
```bash
pip install spotipy
```
# Spotify API setup:

**1. Create a Spotify Developer Account:**
Go to the Spotify Developer Dashboard.
Sign in with your Spotify account or create one if you don’t have it.

**2. Create a New Application:**
Click on "Create an App."
Fill in the application name and description. You can use something descriptive like "Playlist Recommendation System."
Accept the terms and conditions and click "Create."

**3. Get Your API Credentials:**
After creating the app, you will see the Client ID and Client Secret on the app details page.
Copy these credentials and keep them secure. You will need them for your code.

**4. Set Up Redirect URI:**
In the app settings, find the "Edit Settings" button.
Add a Redirect URI, which is the URL where Spotify will redirect after authentication. For local development, you can use http://localhost:3000/callback.
Save the changes.

**5. Set Environment Variables:**
