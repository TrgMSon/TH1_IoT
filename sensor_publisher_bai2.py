import time
import json
import random
import paho.mqtt.client as mqtt

BROKER = "broker.hivemq.com"
PORT = 1883

# Danh sách nhiều thiết bị cần mô phỏng
DEVICES = ["sensor01", "sensor02"]

def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print("Ket noi Broker thanh cong!")
    else:
        print(f"Ket noi that bai voi ma loi: {rc}")

def main():
    try:
        client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id="MultiSensorPublisher")
    except AttributeError:
        client = mqtt.Client(client_id="MultiSensorPublisher")

    client.on_connect = on_connect
    client.connect(BROKER, PORT, keepalive=60)
    client.loop_start()

    try:
        while True:
            # Lần lượt gửi dữ liệu cho từng sensor trong danh sách
            for dev_id in DEVICES:
                topic = f"iot/lab/{dev_id}/data"
                temperature = round(random.uniform(20.0, 42.0), 1)
                humidity = round(random.uniform(30.0, 85.0), 1)

                payload = {
                    "device_id": dev_id,
                    "temperature": temperature,
                    "humidity": humidity
                }
                payload_json = json.dumps(payload)

                client.publish(topic, payload_json)
                print(f"-> Da gui toi [{topic}]: {payload_json}")

            # Đợi 3 giây trước chu kỳ gửi tiếp theo
            time.sleep(3)

    except KeyboardInterrupt:
        print("\nDung Multi Sensor Publisher...")
    finally:
        client.loop_stop()
        client.disconnect()

if __name__ == "__main__":
    main()