from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # 从 templates 文件夹加载 index.html

if __name__ == '__main__':
    app.run(debug=True)

