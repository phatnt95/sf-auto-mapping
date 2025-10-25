# 🔄 Salesforce Auto Mapper (CSV Version)

Ứng dụng cá nhân hỗ trợ **Salesforce Developer** tự động **mapping giữa file dữ liệu CSV và các field trong Salesforce Object** — giúp tiết kiệm thời gian khi import dữ liệu bằng Data Loader hoặc các ETL tools.

Ứng dụng sử dụng:
- **Python + Flask** cho backend
- **OpenAI API** để gợi ý mapping thông minh
- **MaterializeCSS** cho giao diện web gọn nhẹ, dễ dùng

---

## 🧩 Cấu trúc thư mục

```
sf-auto-mapper/
│
├── app.py                # Flask backend chính
├── mapping_ai.py         # Gọi OpenAI API để gợi ý mapping
├── salesforce_helper.py  # Lấy metadata từ Salesforce API hoặc CSV
├── requirements.txt       # Danh sách thư viện Python cần cài
├── README.md              # Hướng dẫn dự án (file này)
│
├── templates/             # HTML giao diện web
│   ├── index.html         # Màn hình upload và chọn metadata source
│   └── result.html        # Hiển thị kết quả mapping
│
└── data/
    └── sample.csv         # File mẫu (tùy chọn)
```

---

## ⚙️ Cài đặt môi trường

### 1️⃣ Tạo và kích hoạt môi trường ảo

```bash
python -m venv venv
# Kích hoạt:
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate
```

### 2️⃣ Cài đặt các thư viện cần thiết

```bash
pip install -r requirements.txt
```

---

## 📦 Danh sách thư viện (`requirements.txt`)

| Thư viện | Mục đích |
|-----------|-----------|
| **flask** | Tạo web backend, xử lý request và render giao diện HTML |
| **openai** | Gọi API OpenAI (GPT) để sinh mapping thông minh giữa CSV và Salesforce fields |
| **pandas** | Đọc và xử lý dữ liệu CSV |
| **simple-salesforce** | Kết nối và lấy metadata từ Salesforce API (nếu chọn metadata source là API) |

---

## 🧠 Cách hoạt động

1. Người dùng truy cập vào trang web (Flask app).
2. Upload file **CSV dữ liệu** cần mapping.
3. Chọn **metadata source**:
   - **Salesforce API** → nhập username, password, token, object name → app sẽ tự lấy metadata fields.
   - **CSV File** → upload thêm file metadata chứa `label` và `api_name`.
4. Ứng dụng gửi thông tin lên **OpenAI GPT model** → gợi ý mapping giữa các cột CSV và các field Salesforce tương ứng.
5. Kết quả hiển thị trong bảng HTML.

---

## 🌐 Chạy ứng dụng

```bash
python app.py
```

Mở trình duyệt và truy cập:
```
http://127.0.0.1:5000/
```

---

## 📋 Cách sử dụng

### 🧾 Trên giao diện chính:
1. Upload **Data CSV**
2. Chọn **Metadata Source**:
   - Nếu chọn *Salesforce API*: điền thông tin đăng nhập và Object name
   - Nếu chọn *CSV*: upload file metadata CSV có 2 cột `label`, `api_name`
3. Nhấn **Generate Mapping**
44. Xem kết quả mapping ở trang kết quả

---

## 📄 Định dạng file metadata CSV

Ví dụ file `contact_metadata.csv`:

| label           | api_name       |
|-----------------|----------------|
| First Name      | FirstName      |
| Last Name       | LastName       |
| Email           | Email          |
| Phone Number    | Phone          |

---

## 🧠 Ví dụ sử dụng thực tế

1. File khách hàng gửi: `customer_data.csv`

| full name | mail_address | phone_no |
|------------|---------------|-----------|
| John Doe   | john@email.com | 12345678 |

2. Metadata (Salesforce Contact) từ API hoặc CSV
3. Kết quả AI gợi ý:

| CSV Column   | Salesforce Field |
|---------------|------------------|
| full name     | Name             |
| mail_address  | Email            |
| phone_no      | Phone            |

---

## 🚀 Mở rộng tính năng (tùy chọn)

- [ ] Thêm nút **Export Mapping.csv** để tải kết quả mapping.
- [ ] Cho phép chỉnh sửa mapping thủ công trước khi export.
- [ ] Lưu lại lịch sử mapping (sử dụng SQLite hoặc JSON).
- [ ] Tích hợp OAuth 2.0 để login Salesforce thay vì username/password.

---

## 🧑‍💻 Tác giả

**Phát Nguyễn**  
Salesforce Developer @ FPT Software  
💬 Dự án cá nhân phục vụ công việc xử lý dữ liệu nhanh chóng, chính xác và tự động hóa.

---

## 📜 Giấy phép

MIT License — tự do sử dụng, chỉnh sửa và mở rộng.

---

> 💡 *“Let AI handle the boring part — you focus on building Salesforce solutions.”*
