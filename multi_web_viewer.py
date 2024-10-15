import sys
from math import ceil, sqrt
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl, Qt

class MultiWebViewer(QWidget):
    def __init__(self, urls):
        super().__init__()

        self.setWindowFlags(Qt.FramelessWindowHint)

        total_sites = len(urls)

        if total_sites == 3:
            rows, cols = 1, 3
        else:
            cols = ceil(sqrt(total_sites))
            rows = ceil(total_sites / cols)

        grid_layout = QGridLayout()
        self.setLayout(grid_layout)

        for i, url in enumerate(urls):
            web_view = QWebEngineView()
            web_view.load(QUrl(url))
            row, col = divmod(i, cols)
            grid_layout.addWidget(web_view, row, col)

if __name__ == "__main__":
    # URLs
    urls = [
        "https://www.bbc.com",
        "https://www.github.com",
        "https://www.wikipedia.org"
    ]

    app = QApplication(sys.argv)
    viewer = MultiWebViewer(urls)

    viewer.showFullScreen()

    sys.exit(app.exec_())

#By: D Palacios ® - 2024