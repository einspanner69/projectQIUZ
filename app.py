from flask import Flask, render_template, request

app = Flask(__name__)

quiz_data = {
    'title': 'Тест на студента',
    'questions': [
        {
            'id': 1,
            'question_text': 'Где вы сейчас находитесь?',
            'options': ['В школе', 'В университете', 'Хз, я дома', 'В колледже'],
            'correct_answer': 'В колледже'
        },
        {
            'id': 2,
            'question_text': 'Как зовут преподавателя?',
            'options': ['Пушкин', 'Хз я тут впервые', 'Александр Сергеевич', 'Кого?'],
            'correct_answer': 'Александр Сергеевич'
        },
        {
            'id': 3,
            'question_text': 'Какой предмет вы сдаете?',
            'options': ['У меня практика, какой предмет', 'Предмет?', 'Я дома', 'Я болею хз'],
            'correct_answer': 'У меня практика, какой предмет'
        }
    ]
}

@app.route('/')
def home():
    return render_template('quiz.html', title=quiz_data['title'], quiz_title=quiz_data['title'], questions=quiz_data['questions'])

@app.route('/quiz', methods=['POST'])
def quiz():
    user_answers = {}
    for question in quiz_data['questions']:
        answer_key = f'q{question["id"]}'
        user_answers[answer_key] = request.form.get(answer_key)
    
    score, total_questions = calculate_score(user_answers)
    return render_template('result.html', title='Результат страданий человечества', score=score, total_questions=total_questions)

def calculate_score(user_answers):
    score = 0
    total_questions = len(quiz_data['questions'])

    for question in quiz_data['questions']:
        question_id = str(question['id'])  # Обязательно преобразуем ID вопроса в строку
        correct_answer = question['correct_answer']
        
        # Проверяем, соответствует ли ответ пользователя правильному ответу
        if user_answers.get(f'q{question_id}') == correct_answer:
            score += 1

    return score, total_questions

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=3000)