def display_movies_for_date(file_name, date):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            movies_for_date = []

            for line in lines:
                date_start = line.find(date)
                if date_start != -1:
                    movie_name = line[:date_start].strip()
                    movies_for_date.append(line.strip())

            if movies_for_date:
                print(f"Фильмы на {date}:")
                for movie in movies_for_date:
                    print(movie)
            else:
                print(f"На {date} фильмов не найдено.")

            if lines:
                most_visited_movie = max(lines, key=lambda x: int(x.split()[-1]))
                print(f"Самый посещаемый фильм: {most_visited_movie.split()[0]}")
    except Exception as e:
        print(f"Произошла ошибка при обработке файла: {e}")

if __name__ == "__main__":
    movie_file = "Кинотеатр.txt"
    date = input("Введите дату для поиска фильмов: ")
    display_movies_for_date(movie_file, date)
