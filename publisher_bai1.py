import paho.mqtt.client as mqtt
import time

BROKER = "broker.hivemq.com"
PORT = 1883
TOPIC = "iot/lab/message"

def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print("Ket noi thanh cong toi broker!")
    else:
        print(f"Ket noi that bai voi ma loi {rc}")

# Xử lý tương thích cho cả paho-mqtt v1 và v2
try:
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
except AttributeError:
    client = mqtt.Client()

client.on_connect = on_connect

client.connect(BROKER, PORT, 60)
client.loop_start()

hoten = "Lang Viet Thanh" 
masv = "B23DCCN768"    
loichao = "Xin chao tu client Python MQTT"

try:
    while True:
        payload = f"{loichao} - {masv} - {hoten}"
        print(f"Dang gui: {payload}")
        client.publish(TOPIC, payload)
        time.sleep(5) # Gửi lặp lại mỗi 5 giây (gợi ý mở rộng)
except KeyboardInterrupt:
    print("\nKet thuc chuong trinh Publisher")
    client.loop_stop()
    client.disconnect()
