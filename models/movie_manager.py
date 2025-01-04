# models/movie_manager.py
import json
from typing import List
from .movie import Movie


class MovieManager:
    """
    Quản lý danh sách phim, bao gồm các chức năng tải, lưu, thêm, xóa, cập nhật và tìm kiếm phim.
    Attributes:
        file_path (str): Đường dẫn tới file chứa dữ liệu phim.
        movies (List[Movie]): Danh sách các phim.
    Methods:
        __init__(file_path: str): Khởi tạo MovieManager với đường dẫn file.
        load_movies(): Tải danh sách phim từ file.
        save_movies(): Lưu danh sách phim vào file.
        add_movie(movie: Movie): Thêm một phim vào danh sách và lưu lại.
        delete_movie(index: int): Xóa một phim khỏi danh sách theo chỉ số và lưu lại.
        update_movie(index: int, movie: Movie): Cập nhật thông tin một phim theo chỉ số và lưu lại.
        search_movies(query: str) -> List[Movie]: Tìm kiếm phim theo tiêu đề.
    """

    def __init__(self, file_path: str):
        # Hàm khởi tạo cho lớp MovieManager.
        # file_path: Đường dẫn tới file JSON chứa dữ liệu phim.
        # movies: Danh sách phim sẽ được khởi tạo từ file.
        self.file_path = file_path
        self.movies: List[Movie] = []  # Khởi tạo danh sách rỗng cho các bộ phim.
        self.load_movies()  # Gọi phương thức load_movies để tải dữ liệu từ file.

    def load_movies(self):
        # Phương thức tải danh sách phim từ file JSON.
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                data = json.load(file)  # Đọc dữ liệu từ file JSON.
                self.movies = []  # Làm rỗng danh sách phim trước khi thêm mới.
                for movie_data in data:
                    # Duyệt qua từng phần tử trong dữ liệu và chuyển thành đối tượng Movie.
                    movie = Movie(
                        title=movie_data["title"],  # Tiêu đề phim.
                        director=movie_data["director"],  # Đạo diễn.
                        year=movie_data["year"],  # Năm sản xuất.
                        rating=movie_data["rating"],  # Đánh giá.
                    )
                    self.movies.append(movie)  # Thêm đối tượng Movie vào danh sách.
        except FileNotFoundError:
            # Nếu file không tồn tại, khởi tạo danh sách phim rỗng.
            self.movies = []

    def save_movies(self):
        # Phương thức lưu danh sách phim vào file JSON.
        with open(self.file_path, "w", encoding="utf-8") as file:
            data = [
                movie.to_dict() for movie in self.movies
            ]  # Chuyển danh sách phim thành danh sách dictionary.
            json.dump(
                data, file, ensure_ascii=False, indent=2
            )  # Lưu dữ liệu vào file JSON.

    def add_movie(self, movie: Movie):
        # Phương thức thêm một bộ phim mới vào danh sách.
        # movie: Đối tượng Movie cần thêm.
        self.movies.append(movie)  # Thêm phim vào danh sách.
        self.save_movies()  # Lưu danh sách phim sau khi thêm.

    def delete_movie(self, index: int):
        # Phương thức xóa một bộ phim khỏi danh sách.
        # index: Chỉ số của bộ phim cần xóa.
        if 0 <= index < len(self.movies):  # Kiểm tra chỉ số có hợp lệ không.
            del self.movies[index]  # Xóa phim tại chỉ số được chỉ định.
            self.save_movies()  # Lưu lại danh sách phim sau khi xóa.

    def update_movie(self, index: int, movie: Movie):
        # Phương thức cập nhật thông tin một bộ phim.
        # index: Chỉ số của bộ phim cần cập nhật.
        # movie: Đối tượng Movie mới thay thế.
        if 0 <= index < len(self.movies):  # Kiểm tra chỉ số có hợp lệ không.
            self.movies[index] = movie  # Cập nhật phim tại chỉ số được chỉ định.
            self.save_movies()  # Lưu lại danh sách phim sau khi cập nhật.

    def search_movies(self, query: str) -> List[Movie]:
        # Phương thức tìm kiếm các bộ phim theo tiêu đề.
        # query: Chuỗi tìm kiếm (tiêu đề phim).
        # Kết quả trả về là danh sách các bộ phim có tiêu đề chứa chuỗi tìm kiếm.
        query = query.lower()
        # Chuyển chuỗi tìm kiếm sang chữ thường để tìm kiếm không phân biệt hoa/thường.
        return [
            movie for movie in self.movies if query in movie.title.lower()
        ]  # Tìm kiếm và trả về kết quả.
