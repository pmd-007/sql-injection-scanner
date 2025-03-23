# 🔥 SQL Injection Scanner  

Tool tự động kiểm tra **SQL Injection** trên website. 🚀  

## 📌 Tính năng:  
✅ Quét nhiều dạng SQL Injection tự động.  
✅ Hỗ trợ **quét 1 URL** hoặc **quét từ danh sách URL**.  
✅ Lưu kết quả vào **output.txt**.  

## 🚀 Cách chạy:  

### 🔹 Cài đặt thư viện cần thiết:
```bash
pip install requests
```
🔹 Chạy tool:
```bash
python3 sql_scanner_v2.py
```
🔹 Chọn chế độ:

Nhập 1 → Quét 1 URL duy nhất.

Nhập 2 → Quét từ danh sách URL trong file targets.txt.

📜 Ví dụ chạy:

```bash
Nhập (1) để quét 1 URL, (2) để quét từ file: 1
Nhập URL mục tiêu (vd: http://example.com/index.php?id=): http://testphp.vulnweb.com/listproducts.php?cat=1
[🔥] Dính SQLi với payload: ' OR '1'='1
[🔥] Dính SQLi với payload: ' UNION SELECT null,null--
[🔥] Dính SQLi với payload: '; DROP TABLE users--
```
💡 Mở rộng:
Thêm nhiều payload SQL Injection mạnh hơn.

Hỗ trợ proxy hoặc User-Agent giả mạo để tránh bị phát hiện.

🔥 Tạo bởi pmd-007 😈
