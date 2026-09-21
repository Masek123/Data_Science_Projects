# Movie Recommender System

Content-based movie recommendation system with exploratory analysis of 
what drives movie revenue and ratings.

## Dataset
[The Movies Dataset](https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset) 
(Kaggle) — ~45,000 movies with metadata, budgets, revenue, genres, cast, 
crew, keywords, and user ratings.

## Project Structure
- `notebooks/01_cleaning.ipynb` — data loading, merging, and cleaning
- `notebooks/02_eda.ipynb` — exploratory data analysis
- `notebooks/03_plots.ipynb` — visualizations
- `notebooks/04_model.ipynb` — content-based recommender (TF-IDF + cosine similarity)
- `utils.py` — shared helper functions

## Key Findings
- We observe a high correlation (0.73) between budget and revenue, suggesting 
  that budget is a strong predictor of a film's box office performance.
- The highest correlation (0.77) is between revenue and vote count. This 
  likely reflects a shared underlying factor — audience size — rather than 
  profitability directly driving engagement, since both metrics grow with 
  how many people actually watched the film.
- The two highest-grossing periods are from May to July and from November 
  to December. The former likely relates to summer release strategies 
  (blockbuster season, more free time for audiences), while the latter 
  aligns with the holiday season.
  
## How the Recommender Works
Movies are represented as text combining their genres and keywords, 
converted to numerical vectors using TF-IDF, then compared using 
cosine similarity to find the most similar titles.

Example:
```python
get_recommendations('Toy Story')
#
2008                 Small Soldiers
19                      Toy Story 3
324                          Trolls
4123    The Transformers: The Movie
2232                   Child's Play
```
**Note:** the recommender matches on shared keywords and genres, not tone. 
"Toy Story 3" and "Trolls" are close matches (family animation), but "Child's 
Play" appears due to the shared keyword "toy" despite being a horror film — 
a known limitation of pure keyword-based similarity, which doesn't capture 
genre weight or tone.

## Setup
1. Download the dataset from the link above and place the CSV files
2. Install dependencies: `pip install -r requirements.txt`
3. Run notebooks in order (01 → 04)
