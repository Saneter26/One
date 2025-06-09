import os
from PySide6.QtWidgets import QApplication, QVBoxLayout, QPushButton, QWidget
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import QUrl, QDir, QFileInfo

os.environ["QT_ENABLE_HIGHDPI_SCALING"] = "1"

app = QApplication([])

# Создаем главное окно с кнопкой и WebView
window = QWidget()
layout = QVBoxLayout()
web_view = QWebEngineView()
window.setWindowTitle("Калькулятор")
window.resize(400, 500)

# Кнопка "Назад"
back_button = QPushButton("← Назад")
back_button.clicked.connect(web_view.back)  # Корректно: метод без скобок

layout.addWidget(back_button)
layout.addWidget(web_view)
window.setLayout(layout)

# Загружаем начальную страницу
base_dir = QDir.currentPath()  # Получаем текущую рабочую папку
html_path = os.path.join(base_dir, "info", "cal.html")  # Путь к HTML-файлу

# Проверяем существование файла
if QFileInfo(html_path).exists():
    web_view.load(QUrl.fromLocalFile(html_path))
else:
    web_view.setHtml(f"<h1>Ошибка: файл не найден</h1><p>{html_path}</p>")

window.show()
app.exec()