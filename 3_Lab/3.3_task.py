def calculate_total_lessons(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            subjects_dict = {}
            for line in lines:
                parts = line.split(':')
                if len(parts) == 2:
                    subject = parts[0].strip()
                    lessons = parts[1].split()
                    total_lessons = sum(int(lesson.split("(")[0]) for lesson in lessons)
                    subjects_dict[subject] = total_lessons

            print("Словарь с количеством занятий по предметам:")
            print(subjects_dict)
    except Exception as e:
        print(f"Произошла ошибка при обработке файла: {e}")

if __name__ == "__main__":
    subjects_file = "subjects.txt"
    calculate_total_lessons(subjects_file)
