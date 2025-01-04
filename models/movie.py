class Movie:
    # Lớp Movie đại diện cho một bộ phim với các thuộc tính như tiêu đề, đạo diễn, năm sản xuất và đánh giá.

    def __init__(self, title: str, director: str, year: int, rating: float = 0.0):
        # Hàm khởi tạo của lớp Movie.
        # title: Tiêu đề của bộ phim (chuỗi).
        # director: Tên đạo diễn của bộ phim (chuỗi).
        # year: Năm sản xuất của bộ phim (số nguyên).
        # rating: Đánh giá của bộ phim (số thực, giá trị mặc định là 0.0).
        self.title = title
        self.director = director
        self.year = year
        self.rating = rating

    def to_dict(self):
        # Phương thức chuyển đổi đối tượng Movie thành một dictionary.
        # Kết quả trả về là dictionary chứa các thông tin của bộ phim với các cặp key-value.
        return {
            "title": self.title,  # Tiêu đề của bộ phim.
            "director": self.director,  # Đạo diễn của bộ phim.
            "year": self.year,  # Năm sản xuất.
            "rating": self.rating,  # Đánh giá.
        }
