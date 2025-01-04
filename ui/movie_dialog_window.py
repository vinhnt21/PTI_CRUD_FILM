from PyQt6.QtWidgets import *
from PyQt6 import uic
from models.movie import Movie


class MovieDialog(QDialog):
    # Lớp MovieDialog đại diện cho hộp thoại để thêm hoặc chỉnh sửa thông tin một bộ phim.
    def __init__(self, parent=None, movie=None):
        # Hàm khởi tạo của hộp thoại.
        # parent: Cửa sổ cha (nếu có).
        # movie: Đối tượng Movie (nếu có) dùng để điền sẵn thông tin vào các ô nhập liệu.
        super().__init__(parent)
        uic.loadUi("ui/movie_dialog.ui", self)  # Tải giao diện từ file .ui.

        if movie:
            # Nếu có đối tượng movie được truyền vào, điền các giá trị của nó vào các ô nhập liệu.
            self.title_edit.setText(movie.title)  # Tiêu đề phim.
            self.director_edit.setText(movie.director)  # Tên đạo diễn.
            self.year_spin.setValue(movie.year)  # Năm sản xuất.
            self.rating_spin.setValue(movie.rating)  # Đánh giá.

        # Kết nối nút OK với hàm accept để đóng hộp thoại và trả về trạng thái OK.
        self.ok_button.clicked.connect(self.accept)

        # Kết nối nút Cancel với hàm reject để đóng hộp thoại và trả về trạng thái Cancel.
        self.cancel_button.clicked.connect(self.reject)

    def get_movie(self):
        # Phương thức lấy dữ liệu từ các ô nhập liệu và trả về một đối tượng Movie.
        return Movie(
            title=self.title_edit.text(),  # Lấy tiêu đề từ ô nhập liệu.
            director=self.director_edit.text(),  # Lấy tên đạo diễn từ ô nhập liệu.
            year=self.year_spin.value(),  # Lấy năm sản xuất từ spin box.
            rating=self.rating_spin.value(),  # Lấy đánh giá từ spin box.
        )
