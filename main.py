import sys
from PyQt6.QtWidgets import QApplication
from ui.manage_film_window import ManageFilmWindow


def main():
    # Hàm chính để chạy ứng dụng.
    app = QApplication(sys.argv)  # Tạo một ứng dụng PyQt6 với tham số từ dòng lệnh.
    window = ManageFilmWindow()  # Khởi tạo cửa sổ chính của ứng dụng (quản lý phim).
    window.show()  # Hiển thị cửa sổ chính.
    sys.exit(
        app.exec()
    )  # Bắt đầu vòng lặp sự kiện của ứng dụng và thoát khi ứng dụng kết thúc.


if __name__ == "__main__":
    # Điểm bắt đầu của chương trình.
    main()  # Gọi hàm main để khởi chạy ứng dụng.
