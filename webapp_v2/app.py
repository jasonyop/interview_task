from flask import Flask
import psutil
import platform

app = Flask(__name__)

@app.route('/')
def main():

    os_information = platform.platform()
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent

    return (
        f'<h1>My System Information</h1>'
        f'<h3>OS Information: {os_information}</h3>'
        f'<h3>CPU Usage: {cpu}</h3>'
        f'<h3>Memory Usage: {memory}</h3>'
    )

    

app.run(host='0.0.0.0', port=5000)