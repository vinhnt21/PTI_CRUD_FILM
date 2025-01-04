from PyQt6.QtWidgets import *
from PyQt6 import uic
from models.movie_manager import MovieManager
from ui.movie_dialog_window import MovieDialog


class ManageFilmWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/manage_film.ui", self)

        # Khởi tạo MovieManager
        self.movie_manager = MovieManager("data/movies.json")

        # Kết nối các nút với hàm xử lý
        self.btn_search.clicked.connect(self.search_movies)
        self.btn_add.clicked.connect(self.add_movie)
        self.btn_edit.clicked.connect(self.edit_movie)
        self.btn_delete.clicked.connect(self.delete_movie)
        self.lineEdit.returnPressed.connect(self.search_movies)

        # Hiển thị danh sách phim ban đầu
        self.update_movie_list()

    def update_movie_list(self, movies=None):
        # Xóa tất cả items hiện tại
        self.listWidget.clear()

        # Nếu không có danh sách phim được truyền vào, sử dụng tất cả phim
        if movies is None:
            movies = self.movie_manager.movies

        # Thêm từng phim vào listWidget
        for movie in movies:
            item_text = f"{movie.title} ({movie.year}) - Đạo diễn: {movie.director} - Đánh giá: {movie.rating}"
            self.listWidget.addItem(item_text)

    def search_movies(self):
        query = self.lineEdit.text().strip()
        if query:
            # Tìm kiếm phim và cập nhật danh sách
            movies = self.movie_manager.search_movies(query)
            self.update_movie_list(movies)
        else:
            # Nếu ô tìm kiếm trống, hiển thị tất cả phim
            self.update_movie_list()

    def add_movie(self):
        dialog = MovieDialog(self)
        if dialog.exec():
            movie = dialog.get_movie()
            self.movie_manager.add_movie(movie)
            self.update_movie_list()

    def edit_movie(self):
        # Lấy item được chọn hiện tại
        current_item = self.listWidget.currentRow()

        if current_item >= 0:
            movie = self.movie_manager.movies[current_item]
            dialog = MovieDialog(self, movie)

            if dialog.exec():
                updated_movie = dialog.get_movie()
                self.movie_manager.update_movie(current_item, updated_movie)
                self.update_movie_list()
        else:
            QMessageBox.warning(self, "Cảnh báo", "Vui lòng chọn phim để chỉnh sửa.")

    def delete_movie(self):
        # Lấy item được chọn hiện tại
        current_item = self.listWidget.currentRow()

        if current_item >= 0:
            reply = QMessageBox.question(
                self,
                "Xác nhận xóa",
                "Bạn có chắc chắn muốn xóa phim này?",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            )

            if reply == QMessageBox.StandardButton.Yes:
                self.movie_manager.delete_movie(current_item)
                self.update_movie_list()
        else:
            QMessageBox.warning(self, "Cảnh báo", "Vui lòng chọn phim để xóa.")
