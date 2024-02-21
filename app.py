from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task = request.form['task']
    tasks.append(task)
    return redirect(url_for('index'))

@app.route('/delete/<int:index>')
def delete_task(index):
    del tasks[index - 1]
    return redirect(url_for('index'))

@app.route('/update/<int:index>', methods=['GET', 'POST'])
def update_task(index):
    if request.method == 'POST':
        updated_task = request.form['task']
        tasks[index - 1] = updated_task
        return redirect(url_for('index'))
    return render_template('update.html', index=index, task=tasks[index - 1])

if __name__ == '__main__':
    app.run(debug=True)
