#################################################
# İŞ PROBLEMİ:
#################################################
# ID'si verilen bir kullanıcı için item-based ve user-based recommender yöntemlerini kullanarak tahmin yapalım.
import pandas as pd


movie = pd.read_csv("datasets/movie_lens_dataset/movie.csv")
rating = pd.read_csv("datasets/movie_lens_dataset/rating.csv")
df = movie.merge(rating, how="left", on="movieId")


#################################################
# # BİRİNCİ YÖNTEM: USER_BASED COLLABORATIVE FILTERING
#################################################

# Adım 1: Veri Hazırlama işlemleri

# Yorum sayılarına erişim:
comment_counts = pd.DataFrame(df["title"].value_counts())
# Az yorum yapılan filmler:
rare_movies = comment_counts[comment_counts["title"] <= 1000].index
# Popüler filmler:
common_movies = df[~df["title"].isin(rare_movies)]
# verisetini daha çok yorum yapılan filmlere göre daraltalım:
user_movie_df = common_movies.pivot_table(values="rating", index="userId", columns="title")

# Veri inceleme:
df.head()
df.shape
df["title"].value_counts()
df["title"].nunique()


# Adım 2: Öneri yapılacak kullanıcının izlediği filmleri belirlelim:

random_user = int(pd.Series(user_movie_df.index).sample(1).values)
# Daha sonraki fonksiyonların daha rahat çalışması için max 50-60 film izleyen bir kullanıcı seçilebilir.

random_user_df = user_movie_df[user_movie_df.index == random_user]
movies_watched = random_user_df.columns[random_user_df.notna().any()].tolist()
len(movies_watched) # random_user kaç film izlemiş?

# Adım 3: Aynı filmleri izleyen diğer kullanıcıların verisine ve Id'lerine erişelim:

movies_watched_df = user_movie_df[movies_watched]
movies_watched_df.shape

user_movie_count = movies_watched_df.T.notnull().sum()
user_movie_count = user_movie_count.reset_index()
user_movie_count.columns = ["userId", "movie_count"]

# Diğer kullanıcılar ortak filmlerden en az 20'sini izlemiş olacak şekilde verisetini daraltalım:
user_Id_same_movies = user_movie_count[user_movie_count["movie_count"] > 20]["userId"]

# Adım 4: Öneri yapılacak kullanıcı ile en benzer kullanıcıları belirleyelim:

final_df = pd.concat((movies_watched_df[movies_watched_df.index.isin(user_Id_same_movies)],
                      random_user_df[movies_watched]))

final_df.shape
final_df.corr()

# Filmler arası korelasyon tablosu için:
corr_df = final_df.T.corr()
# Pivot tablosu için:
corr_df = corr_df.unstack()
# Sıralayalım:
corr_df = corr_df.sort_values()
# Yinelemeleri silelim:
corr_df = corr_df.drop_duplicates()
corr_df = pd.DataFrame(corr_df, columns=["corr"])
corr_df.index.names = ["user_id_1", "user_id_2"]
corr_df = corr_df.reset_index()
corr_df.sort_values("corr", ascending=False).head(50)

# Random user'a benzer kullanıcıları tespit etmek için
# random user = user_id_1 ve diğer kullanıcılar = user_id_2 olacak şekilde
# korelasyon değeri örnek olarak min 0.65 olan kullanıcıları seçelim.
similar_users = corr_df[(corr_df["user_id_1"] != random_user) & (corr_df["corr"] > 0.65)][
    ["user_id_2", "corr"]].reset_index(drop=True)
similar_users.sort_values("corr", ascending=False)
similar_users.rename(columns={"user_id_2": "userId"}, inplace=True)
similar_users.head()
similar_users_ratings = similar_users.merge(rating[["userId", "movieId", "rating"]], how="inner")
similar_users_ratings.head()

# Adım 5: Weighted Average Recommendation Score'u hesaplayalım ve ilk 5 filmi öneri için tutalım:

similar_users_ratings["weighted_rating"] = similar_users_ratings["corr"] * similar_users_ratings["rating"]

# filmlerin weighted_rating ortalaması:
recommendation_df = similar_users_ratings.groupby("movieId").agg({"weighted_rating": "mean"})
recommendation_df.reset_index()

# ağırlıklı ortalama sıralamasında ilk 5'teki filmler:
five_recommend_user = recommendation_df.sort_values("weighted_rating", ascending=False).head(5)
five_recommend_user = five_recommend_user.reset_index()
five_recommend_user = five_recommend_user.merge(movie[["movieId", "title"]], how="inner")
five_recommend_user = five_recommend_user.rename({"title": "user_based"})
five_recommend_user.head(5)

#################################################
# İKİNCİ YÖNTEM: ITEM_BASED COLLABORATIVE FILTERING
#################################################

# Item based yöntemine göre 5 film önerelim:

user = 29087
len(user_movie_df.columns)

# user'ın en son 5 puan verdiği filme ulaşalım:
# önce 5 puan verdiği filmleri zaman göre sıralayalım:
movie_id = rating[(rating["userId"] == user) & (rating["rating"] == 5.0)]. \
    sort_values("timestamp", ascending=False)["movieId"].values[0]


movie_name = movie[movie["movieId"] == movie_id]["title"].values[0]
# Natural Born Killers (1994)'
movie_name = user_movie_df[movie_name]

# Seçilen filmin diğer filmlerle olan korelasyonu:
five_recommend_item = user_movie_df.corrwith(movie_name).sort_values(ascending=False).head(6)[1:6]
five_recommend_item = five_recommend_item.reset_index()
five_recommend_item.columns = ["item_based", "rating"]

#                         item_based    rating
# 0             Wild at Heart (1990)  0.419080
# 1                Doors, The (1991)  0.390892
# 2                    U Turn (1997)  0.386838
# 3            Bad Lieutenant (1992)  0.366558
# 4              Pulp Fiction (1994)  0.355001