# THỰC HÀNH: LẬP TRÌNH PYTHON VỚI GIAO THỨC MQTT

## Cấu hình MQTT Broker
- Các bài tập trong lab này sử dụng broker miễn phí có sẵn trên mạng.
- **Broker sử dụng**: `broker.hivemq.com`
- **Port**: `1883`

---

## Bài 1. Ứng dụng gửi và nhận thông điệp MQTT cơ bản

### 1. Giới thiệu
Chương trình minh họa cơ chế **publisher/subscriber** cơ bản trong MQTT qua topic `iot/lab/message`.
- **Publisher**: Gửi thông tin sinh viên định kỳ 5 giây/lần.
- **Subscriber**: Lắng nghe và in ra thông điệp nhận được kèm thời gian.

### 2. Cách chạy chương trình
Cần mở 2 cửa sổ terminal (cmd/powershell) khác nhau:

**Terminal 1 (Chạy Subscriber trước để đứng chờ nhận thông điệp):**
```bash
python subscriber_bai1.py
```
*Bạn sẽ thấy thông báo: "Ket noi thanh cong! Dang lang nghe topic: iot/lab/message"*

**Terminal 2 (Chạy Publisher để bắt đầu gửi thông điệp):**
```bash
python publisher_bai1.py
```

*Nhấn `Ctrl+C` ở mỗi terminal để dừng chương trình tương ứng.*

### 3. Kết quả đạt được
**Bên cửa sổ của Publisher:**
```
Ket noi thanh cong toi broker!
Dang gui: Xin chao tu client Python MQTT - B23DCCN001 - Nguyen Van A
Dang gui: Xin chao tu client Python MQTT - B23DCCN001 - Nguyen Van A
```

**Bên cửa sổ của Subscriber:**
```
Nhan duoc message:
Topic: iot/lab/message
Payload: Xin chao tu client Python MQTT - B23DCCN001 - Nguyen Van A
Time: 10:15:20
```

