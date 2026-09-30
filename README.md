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

## Bài 3. Ứng dụng điều khiển và phản hồi trạng thái thiết bị đèn qua MQTT

### 1. Giới thiệu
Chương trình minh họa cơ chế **điều khiển và giao tiếp hai chiều** trong MQTT giữa thiết bị đèn thông minh và ứng dụng điều khiển.
- **Device (`device_bai3.py`)**: Lắng nghe lệnh điều khiển trên topic `iot/lab/light01/cmd`, cập nhật trạng thái đèn và gửi (publish) phản hồi trạng thái mới nhất dưới dạng JSON lên topic `iot/lab/light01/status`.
- **Controller (`controller_bai3.py`)**: Cho phép người dùng nhập lệnh từ bàn phím (`ON`, `OFF`, `EXIT`), gửi lệnh tới thiết bị và đồng thời lắng nghe topic `iot/lab/light01/status` để in phản hồi trạng thái nhận được.

### 2. Cách chạy chương trình
Cần mở 2 cửa sổ terminal (cmd/powershell) khác nhau:

**Terminal 1 (Chạy Thiết bị trước để chờ nhận lệnh):**
```bash
python device_bai3.py
```

*Bạn sẽ thấy thông báo: "=== SMART LIGHT DEVICE STARTED ===\nĐã kết nối tới MQTT Broker. Đang chờ lệnh..."

**Terminal 2 (Chạy Controller để bắt đầu gửi lệnh điều khiển):

```bash
python controller_bai3.py
```
*Nhập lệnh ON hoặc OFF để điều khiển thiết bị, hoặc nhập EXIT để kết thúc chương trình Controller.

### 3. Kết quả đạt được
**Bên cửa sổ của Controller:
```
=== CONTROLLER APP ===


Trạng thái nhận được:
{"device_id": "light01", "status": "OFF"}

Nhập lệnh (ON / OFF / EXIT): ON
Đã gửi lệnh ON tới light01


Trạng thái nhận được:
{"device_id": "light01", "status": "ON"}

Nhập lệnh (ON / OFF / EXIT): OFF
Đã gửi lệnh OFF tới light01


Trạng thái nhận được:
{"device_id": "light01", "status": "OFF"}

Nhập lệnh (ON / OFF / EXIT): HELLO
Lỗi: Lệnh không hợp lệ. Vui lòng chỉ nhập ON, OFF hoặc EXIT.

Nhập lệnh (ON / OFF / EXIT): EXIT
Đã ngắt kết nối. Kết thúc chương trình Controller.
```

** Bên cửa sổ của Device:
```
=== SMART LIGHT DEVICE STARTED ===
Đã kết nối tới MQTT Broker. Đang chờ lệnh...

[Device] Đã gửi: {"device_id": "light01", "status": "OFF"}
[Device] Đã nhận lệnh: ON
[Device] Đã gửi: {"device_id": "light01", "status": "ON"}
[Device] Đã nhận lệnh: OFF
[Device] Đã gửi: {"device_id": "light01", "status": "OFF"}
```