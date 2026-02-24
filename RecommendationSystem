import pandas as pd
import tkinter as tk
from tkinter import messagebox

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# -------------------------------
# Load Dataset
# -------------------------------
df = pd.read_csv("Rotten Tomatoes Movies 2.csv")

df['movie_info'] = df['movie_info'].fillna("")


# -------------------------------
# Create Recommendation System
# -------------------------------
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['movie_info'])

cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

indices = pd.Series(df.index, index=df['movie_title'])


# -------------------------------
# Recommendation Function
# -------------------------------
def recommend_movie(title):

    if title not in indices:
        return None

    idx = indices[title]

    sim_scores = list(enumerate(cosine_sim[idx]))

    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    sim_scores = sim_scores[1:6]

    movie_indices = [i[0] for i in sim_scores]

    return df['movie_title'].iloc[movie_indices]


# -------------------------------
# GUI Function
# -------------------------------
def get_recommendation():

    movie_name = entry.get().strip()

    if movie_name == "":
        messagebox.showerror("Error", "Please enter movie name")
        return

    result = recommend_movie(movie_name)

    if result is None:
        messagebox.showerror("Error", "Movie not found in dataset")
        return

    # Clear old result
    listbox.delete(0, tk.END)

    # Show new result
    for movie in result:
        listbox.insert(tk.END, movie)


# -------------------------------
# Create GUI Window
# -------------------------------
root = tk.Tk()
root.title("Movie Recommendation System")
root.geometry("500x400")


# -------------------------------
# GUI Widgets
# -------------------------------

# Heading
title_label = tk.Label(
    root,
    text="Movie Recommendation System",
    font=("Arial", 18, "bold")
)
title_label.pack(pady=10)


# Input Label
input_label = tk.Label(root, text="Enter Movie Name:")
input_label.pack()


# Input Box
entry = tk.Entry(root, width=40)
entry.pack(pady=5)


# Button
btn = tk.Button(
    root,
    text="Recommend",
    command=get_recommendation,
    bg="blue",
    fg="white",
    width=15
)
btn.pack(pady=10)


# Result Label
result_label = tk.Label(root, text="Recommended Movies:")
result_label.pack()


# List Box
listbox = tk.Listbox(root, width=50, height=10)
listbox.pack(pady=5)


# -------------------------------
# Run App
# -------------------------------
root.mainloop()