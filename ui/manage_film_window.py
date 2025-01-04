from PyQt6.QtWidgets import *
from PyQt6.QtCore import QStringListModel
from PyQt6 import uic
from models.movie_manager import MovieManager
from ui.movie_dialog_window import MovieDialog


class ManageFilmWindow(QMainWindow):
    # Lớp ManageFilmWindow kế thừa từ QMainWindow để tạo giao diện quản lý phim.
    def __init__(self):
        # Hàm khởi tạo cho cửa sổ quản lý phim.
        super().__init__()
        uic.loadUi("ui/manage_film.ui", self)  # Tải giao diện từ file .ui.

        self.movie_manager = MovieManager(
            "data/movies.json"
        )  # Tạo đối tượng quản lý phim, nạp dữ liệu từ file JSON.
        self.model = QStringListModel()  # Khởi tạo model cho danh sách phim.
        self.listView.setModel(
            self.model
        )  # Gắn model vào listView để hiển thị danh sách phim.

        # Kết nối các nút bấm với các chức năng tương ứng.
        self.btn_search.clicked.connect(self.search_movies)  # Nút tìm kiếm.
        self.btn_add.clicked.connect(self.add_movie)  # Nút thêm phim.
        self.btn_edit.clicked.connect(self.edit_movie)  # Nút chỉnh sửa phim.
        self.btn_delete.clicked.connect(self.delete_movie)  # Nút xóa phim.
        self.lineEdit.returnPressed.connect(
            self.search_movies
        )  # Nhấn Enter trong ô tìm kiếm sẽ kích hoạt tìm kiếm.

        self.update_movie_list()  # Cập nhật danh sách phim hiển thị.

    def update_movie_list(self, movies=None):
        # Cập nhật danh sách phim trong listView.
        # movies: Danh sách phim để hiển thị, nếu không có thì hiển thị tất cả phim.
        if movies is None:
            movies = (
                self.movie_manager.movies
            )  # Lấy danh sách tất cả phim từ MovieManager.
        movie_strings = [
            f"{movie.title} ({movie.year}) - Đạo diễn: {movie.director} - Đánh giá: {movie.rating}"
            for movie in movies
        ]  # Tạo danh sách chuỗi mô tả phim.
        self.model.setStringList(movie_strings)  # Gắn danh sách chuỗi này vào model.

    def search_movies(self):
        # Xử lý chức năng tìm kiếm phim.
        query = self.lineEdit.text()  # Lấy chuỗi tìm kiếm từ ô nhập liệu.
        if query:
            movies = self.movie_manager.search_movies(
                query
            )  # Tìm kiếm phim theo tiêu đề.
            self.update_movie_list(
                movies
            )  # Cập nhật danh sách hiển thị với kết quả tìm kiếm.
        else:
            self.update_movie_list()  # Nếu không có chuỗi tìm kiếm, hiển thị tất cả phim.

    def add_movie(self):
        # Xử lý chức năng thêm phim.
        dialog = MovieDialog(self)  # Hiển thị hộp thoại thêm phim mới.
        if dialog.exec():  # Nếu người dùng nhấn OK trong hộp thoại.
            movie = dialog.get_movie()  # Lấy đối tượng phim mới từ hộp thoại.
            self.movie_manager.add_movie(movie)  # Thêm phim mới vào danh sách quản lý.
            self.update_movie_list()  # Cập nhật danh sách hiển thị.

    def edit_movie(self):
        # Xử lý chức năng chỉnh sửa phim.
        current_index = (
            self.listView.currentIndex().row()
        )  # Lấy chỉ số phim được chọn trong listView.
        if current_index >= 0:  # Kiểm tra nếu có phim được chọn.
            movie = self.movie_manager.movies[
                current_index
            ]  # Lấy phim từ danh sách quản lý.
            dialog = MovieDialog(
                self, movie
            )  # Hiển thị hộp thoại chỉnh sửa phim với dữ liệu hiện tại.
            if dialog.exec():  # Nếu người dùng nhấn OK trong hộp thoại.
                updated_movie = (
                    dialog.get_movie()
                )  # Lấy đối tượng phim đã chỉnh sửa từ hộp thoại.
                self.movie_manager.update_movie(
                    current_index, updated_movie
                )  # Cập nhật phim trong danh sách quản lý.
                self.update_movie_list()  # Cập nhật danh sách hiển thị.
        else:
            QMessageBox.warning(
                self, "Cảnh báo", "Vui lòng chọn phim để chỉnh sửa."
            )  # Hiển thị cảnh báo nếu không có phim nào được chọn.

    def delete_movie(self):
        # Xử lý chức năng xóa phim.
        current_index = (
            self.listView.currentIndex().row()
        )  # Lấy chỉ số phim được chọn trong listView.
        if current_index >= 0:  # Kiểm tra nếu có phim được chọn.
            reply = QMessageBox.question(
                self,
                "Xác nhận xóa",
                "Bạn có chắc chắn muốn xóa phim này?",  # Hiển thị hộp thoại xác nhận xóa.
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            )
            if reply == QMessageBox.StandardButton.Yes:  # Nếu người dùng chọn Yes.
                self.movie_manager.delete_movie(
                    current_index
                )  # Xóa phim khỏi danh sách quản lý.
                self.update_movie_list()  # Cập nhật danh sách hiển thị.
        else:
            QMessageBox.warning(
                self, "Cảnh báo", "Vui lòng chọn phim để xóa."
            )  # Hiển thị cảnh báo nếu không có phim nào được chọn.
