import json
import paho.mqtt.client as mqtt

BROKER = "broker.hivemq.com"
PORT = 1883
# Dùng '+' để nhận dữ liệu từ mọi thiết bị: sensor01, sensor02, ...
TOPIC_PATTERN = "iot/lab/+/data"

def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print(f"[Monitoring] Ket noi thanh cong! Dang lang nghe: {TOPIC_PATTERN}")
        client.subscribe(TOPIC_PATTERN)
    else:
        print(f"[Monitoring] Ket noi that bai, ma loi: {rc}")

def on_message(client, userdata, msg):
    try:
        raw_payload = msg.payload.decode("utf-8")
        data = json.loads(raw_payload)

        device_id = data.get("device_id", "Unknown")
        temperature = data.get("temperature", 0.0)
        humidity = data.get("humidity", 0.0)

        print("------------------------------")
        print(f"Topic: {msg.topic}")
        print(f"Device: {device_id}")
        print(f"Temperature: {temperature} C")
        print(f"Humidity: {humidity} %")

        if temperature > 35:
            print("CANH BAO: Nhiet do cao")
        if humidity < 40:
            print("CANH BAO: Do am thap")

    except json.JSONDecodeError:
        print(f"[Loi] Khong the parse JSON: {msg.payload.decode('utf-8')}")
    except Exception as e:
        print(f"[Loi] {e}")

def main():
    try:
        client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id="MultiMonitorSubscriber")
    except AttributeError:
        client = mqtt.Client(client_id="MultiMonitorSubscriber")

    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(BROKER, PORT, keepalive=60)

    try:
        client.loop_forever()
    except KeyboardInterrupt:
        print("\nDung Monitoring Subscriber...")
    finally:
        client.disconnect()

if __name__ == "__main__":
    main()