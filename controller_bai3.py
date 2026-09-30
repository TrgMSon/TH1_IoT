import paho.mqtt.client as mqtt
import time
import sys

# Cấu hình MQTT
BROKER = "broker.hivemq.com"
PORT = 1883
TOPIC_CMD = "iot/lab/light01/cmd"
TOPIC_STATUS = "iot/lab/light01/status"

def on_connect(client, userdata, flags, rc):
    # Đăng ký topic lắng nghe trạng thái phản hồi
    client.subscribe(TOPIC_STATUS)

def on_message(client, userdata, msg):
    # In ra phản hồi và in lại dòng nhắc lệnh (prompt)
    print("\n\nTrạng thái nhận được:")
    print(msg.payload.decode("utf-8"))
    print("\nNhập lệnh (ON / OFF / EXIT): ", end="", flush=True)

# Khởi tạo MQTT Client
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

print("Đang kết nối tới Server điều khiển...")
client.connect(BROKER, PORT, 60)

# Khởi chạy một luồng (thread) chạy ngầm để lắng nghe message
client.loop_start()
time.sleep(1) # Chờ 1 giây để đảm bảo kết nối thành công

print("\n=== CONTROLLER APP ===")

# Vòng lặp chính xử lý nhập liệu từ bàn phím
while True:
    try:
        command = input().strip()
        
        if command in ["ON", "OFF"]:
            # Gửi lệnh đi
            client.publish(TOPIC_CMD, command)
            print(f"Đã gửi lệnh {command} tới light01")
            # Chờ một chút để dòng nhắc lệnh không bị in đè bởi phản hồi
            time.sleep(0.5) 
            
        elif command == "EXIT":
            print("Đã ngắt kết nối. Kết thúc chương trình Controller.")
            client.loop_stop()
            client.disconnect()
            sys.exit(0)
            
        elif len(command) > 0:
            # Xử lý mở rộng: Bắt lỗi nhập sai
            print("Lỗi: Lệnh không hợp lệ. Vui lòng chỉ nhập ON, OFF hoặc EXIT.")
            print("\nNhập lệnh (ON / OFF / EXIT): ", end="", flush=True)
            
    except KeyboardInterrupt:
        print("\nĐã ép buộc dừng chương trình.")
        client.loop_stop()
        sys.exit(0)