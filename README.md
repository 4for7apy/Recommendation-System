# Movie Recommender System 🎬

This Movie Recommender System is a web application built with Streamlit that recommends movies based on the similarity to a selected movie. The app uses machine learning to find the closest movies based on a precomputed similarity matrix, and displays the movie posters using data from The Movie Database (TMDB) API.

![Screenshot (1597)](https://github.com/user-attachments/assets/b1694c0e-a52f-4864-a07f-f4dcf0582893)

## Features
- Recommends 5 similar movies based on a selected movie title.
- Displays movie posters and titles for each recommendation.
- Sleek and responsive UI built with Streamlit, including column-based layout for recommendations.
- Integration with TMDB API to fetch movie posters.

## Installation and Setup
1. **Clone the repository**
    ```bash
    git clone https://github.com/your-username/movie-recommender-system.git
    cd movie-recommender-system
    ```

2. **Install dependencies**
    This project uses `requirements.txt` for managing dependencies. Install them using:
    ```bash
    pip install -r requirements.txt
    ```

3. **Obtain a TMDB API Key**
    - Create an account on [TMDB](https://www.themoviedb.org/) and get an API key.
    - Replace the API key in the `fetch_poster` function within the code:
      ```python
      f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=YOUR_API_KEY&language=en-US"
      ```

4. **Run the app**
    Launch the Streamlit app by running:
    ```bash
    streamlit run app.py
    ```

## Usage
1. Select a movie title from the dropdown menu.
2. Click the **Recommend** button to get movie recommendations.
3. The app will display the top 5 recommended movies along with their posters.

## Project Structure
- **app.py**: Main file for the Streamlit app containing the UI and recommendation logic.
- **movie_dict.pkl**: A precomputed dictionary of movie titles and IDs used for movie selection.
- **similarity.pkl**: A precomputed similarity matrix used to find similar movies.

## Acknowledgments
- **The Movie Database (TMDB)** for the API that allows fetching movie posters and details.
- **Streamlit** for the easy-to-use framework that made this web application possible.

## Built With ❤️ by Arpit
Enjoy the app and find your next favorite movie! 😊
