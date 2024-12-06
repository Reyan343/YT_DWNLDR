import sys
import os
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QPushButton, QLineEdit, QWidget, QHBoxLayout
from pytube import YouTube
from pytube.exceptions import VideoUnavailable

class DownloadVideo:
        def download(self, url):
            try:
                yt = YouTube(url)

                stream = yt.streams.get_highest_resolution()
                
                videos_folder = os.path.join(os.environ['USERPROFILE'], "Videos")
                
                stream.download(output_path=videos_folder)
                
                return "Download Complete!"
            
            except VideoUnavailable:
                return "Error: video unavailable"
            
            except Exception as e:
                return f"An error occurred: {str(e)}"

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Youtube downloader")
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        self.url_input = QLineEdit()
        self.url_input.setPlaceholderText("Enter YouTube URL: ")
        
        self.download_button = QPushButton("Download")
        self.download_button.clicked.connect(self.handle_download)
        
        layout = QHBoxLayout()
        layout.addWidget(self.url_input)
        layout.addWidget(self.download_button)
        
        central_widget.setLayout(layout)
        
    def handle_download(self):
        url = self.url_input.text()
        
        if not url:
            error_popup = QMessageBox()
            error_popup.setIcon(QMessageBox.Warning)
            error_popup.setText("invalid URL")
            error_popup.exec()
            
        downloader = DownloadVideo()
        
        output = downloader.download(url)
        
        feedback_popup = QMessageBox()
        feedback_popup.setText(output)
        feedback_popup.exec()


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()