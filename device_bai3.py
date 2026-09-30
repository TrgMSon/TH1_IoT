import paho.mqtt.client as mqtt
import json

# Cấu hình MQTT
BROKER = "broker.hivemq.com"
PORT = 1883
TOPIC_CMD = "iot/lab/light01/cmd"
TOPIC_STATUS = "iot/lab/light01/status"
DEVICE_ID = "light01"

current_status = "OFF"

def publish_status(client):
    """Hàm đóng gói JSON và gửi trạng thái hiện tại"""
    payload = json.dumps({
        "device_id": DEVICE_ID,
        "status": current_status
    })
    client.publish(TOPIC_STATUS, payload, retain=True)
    print(f"[Device] Đã gửi: {payload}")

def on_connect(client, userdata, flags, rc):
    print("=== SMART LIGHT DEVICE STARTED ===")
    print("Đã kết nối tới MQTT Broker. Đang chờ lệnh...\n")
    # Đăng ký topic nhận lệnh
    client.subscribe(TOPIC_CMD)
    # Gửi trạng thái ban đầu khi vừa khởi động
    publish_status(client)

def on_message(client, userdata, msg):
    global current_status
    command = msg.payload.decode("utf-8").strip()
    
    if command in ["ON", "OFF"]:
        current_status = command
        # Tương đương với lệnh GPIO bật/tắt đèn thực tế ở đây
        print(f"[Device] Đã nhận lệnh: {command}")
        publish_status(client)
    else:
        print(f"[Device] Bỏ qua lệnh không hợp lệ: {command}")

# Khởi tạo MQTT Client
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# Kết nối và duy trì vòng lặp vĩnh viễn
client.connect(BROKER, PORT, 60)
client.loop_forever()