import pandas as pd

df = pd.read_csv('data-pandas\IMDB_OMDB_Kaggle_TestSet_OMDB_Detailed.csv')

# Dosya hakkında bilgiler
result = df
# ilk 5 kaydı göster
result = df.head()
# ilk 10 kaydı göster
result = df.head(10)
# son 5 kaydı göster
result = df.tail()
# son 10 kaydı göster
result = df.tail(10)
# sadece Movie_Title kolonunu al
result = df["Title"]
# sadece Movie_Title kolonunu içeren ilk 5 kayıt
result = df["Title"].head()
# sadece Movie_Title kolonunu ve Rating kolonunu içeren ilk 5
result = df[["Title","Ratings.Value"]].head()
# sadece Movie_Title kolonunu ve Rating kolonunu içeren son 7
result = df[["Title","Ratings.Value"]].tail(7)
# sadece Movie_Title kolonunu ve Rating kolonunu içeren ikinci 5
result = df[5:][["Title","Ratings.Value"]].head()
# sadece Movie_Title kolonunu ve Rating kolonunu içeren ve imdb puanı 8.0 üstünde olan kayıtlardan ilk 50 tanesi
result = df[df["imdbRating"] >= 7.0][["Title","Ratings.Value"]].head(50)
# Yayın tarihi 2014 ve 2015 arasında olan filmlerin isimlerini getirin
result = df[(df["Year"] >= 2014) & (df["Year"] <= 2015)]
# Değerlendirme sayısı (Num_Reviews) 100.000 den büyük yada imdb puanı 8 ile 9 arası olan filmleri listeleyin
result = df[(df["imdbVotes"] >= str(100000)) | ((df["imdbRating"] >= 8.0) & (df["imdbRating"] <= 9.0))]


print(result)
print(df.columns)
