# Introduction to Computer Programming Project

This repository contains the group project developed for the course **Introduction to Computer Programming (2024/2025)** at **Luiss University**.  
The project focuses on the analysis of a dataset containing information on 5,000 movies sourced from *The Movie Database (TMDB)*.  
All tasks are implemented using only Python’s Standard Library.

---

## Project Overview

The objective of this project is to practice fundamental programming concepts by performing data analysis on structured CSV datasets.  
The dataset includes details on movies, genres, keywords, production companies, and countries of production.

### Dataset Structure

| File | Description |
|------|--------------|
| `movies_table.csv` | Contains key information for each movie (title, budget, revenue, release date, etc.) |
| `genres_table.csv` | Contains ⟨movie–genre⟩ pairs |
| `keywords_table.csv` | Contains ⟨movie–keyword⟩ pairs |
| `production_companies.csv` | Contains ⟨movie–production company⟩ pairs |
| `production_countries_table.csv` | Contains ⟨movie–production country⟩ pairs |

---

## Implemented Queries

### Query 1 – Budget Distribution by Country
Analyzes the distribution of movie budgets across production countries.  
Movies are grouped into budget ranges (e.g., 0–10M, 10–20M, …).  
**Output:** `query1.pkl` → `{country: {budget_range: count}}`

### Query 2 – Average Revenue by Company Size
Computes the average revenue for movies produced by companies of different sizes:  
- Small: 1–10 movies  
- Medium: 11–50 movies  
- Large: 51+ movies  
**Output:** `query2.pkl` → `{company_size: average_revenue}`

### Query 3 – Genre Distribution by Production Company
Counts the number of movies per genre for each production company and identifies dominant genres.  
**Output:** `query3.pkl` → `{company: {genre: count}}`

---

## Technical Details

- **Language:** Python 3.12+  
- **Libraries used:** `csv`, `json`, `pickle`  
- **Restrictions:** Only modules from the Python Standard Library were permitted  
- **Output format:** Serialized `.pkl` files using the `pickle` module

---
