# Movie-Recommendation-System

This is a Content-Based Recommender System that recommends movies similar to the movie user likes.

# Files Descryption:
1. I have the preprocessing in 4 stages in 4 separate files:
    1. The file "preprocessing movie data upto 2016 (1).ipynd" is jupyter source file where all the prepocessing of movie
          data upto the year 2016 is done and then saved in the csv file "movie_data.csv".
    2. Similarly, the file "preprocessing movie data upto 2017 (2).ipynd" is another file where the prepocessing of movie
          data for the year 2017 is done and then that data is appended to the already prepocessed data of movies upto 2016, and then saved in new csv file 
            "movie_data_upto_2017.csv".
    3. Similarly, "movie_data_upto_2021.csv", "movie_data_upto_2022_march.csv" contain prepocessed data upto 2021 and 2022 to respecively.
2. After this in the "main.ipynb" file I have used the final preprocessed data "movie_data_upto_2022_march.csv" to recommend movies using cosine similarity.
3. Then in the file "Sentiment Analysis.ipynb", I have performed the sentimental analysis using the data from "reviews.txt" file. The model that I have used "Multinomial Naive Bayes".
   
# Similarity Score
It is a numerical value ranging between zero to one which helps to determine how much two items are similar on a scale of zero to one. This similarity score is obtained by measuring the similarity between the text details of both items. So, similarity score is the measure of similarity between given text details of two items. This can be done by cosine-similarity.

# How Cosine Similarity Works?
Cosine similarity is a metric used to measure how similar the documents are irrespective of their size.
Mathematically, it measures the cosine of the angle between two vectors projected in a multi-dimensional space.
The cosine similarity is advantageous because even if the two similar documents are far apart by the Euclidean distance
(due to the size of the document), chances are they may still be oriented closer together. The smaller the angle, higher the cosine similarity.

![image](https://github.com/Pranjal1004/Movie-Recommendation-System/assets/103432960/a3140414-caca-4991-9f68-653160360b6d)
![6218c43769249759cece5473_Engati-Cosine-Similarity (1)](https://github.com/Pranjal1004/Movie-Recommendation-System/assets/103432960/9e6b0e5f-ebf8-4810-8b17-9a23bc26ab0e)



# Sources of Datasets:
1. <a href="https://en.wikipedia.org/wiki/List_of_American_films_of_2022">
      Movies Data Set (movie_metadata.csv upto 2016) </a>
2. <a href="https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset?resource=download&select=movies_metadata.csv)https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset?resource=download&select=movies_metadata.csv">
      Movies Data Set (credits.csv & movies_metadata.csv for year 2017) </a>
3. <a href="https://en.wikipedia.org/wiki/List_of_American_films_of_2018">
      Movies List of 2018</a>
4.  <a href="https://en.wikipedia.org/wiki/List_of_American_films_of_2019">
      Movies List of 2019</a>
5. <a href="https://en.wikipedia.org/wiki/List_of_American_films_of_2020">
      Movies List of 2020</a>
6. <a href="https://en.wikipedia.org/wiki/List_of_American_films_of_2021">
      Movies List of 2021</a>
7. <a href="https://en.wikipedia.org/wiki/List_of_American_films_of_2022">
      Movies List of 2022</a>
