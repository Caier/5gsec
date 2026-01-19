import requests
import time

SERVER = "http://127.0.0.1:5000"

DATA_MAP = {
    "1": "Dane dla numeru 1\n costam1\n costam1",
    "2": "Dane dla numeru 2\n costam2\n costam2",
    "3": "Dane dla numeru 3\n costam3\n costam3"
}

while True:
    try:
        response = requests.get(f"{SERVER}/command")
        command = response.json().get("command")

        if command is None:
            time.sleep(1)
            continue

        if command in DATA_MAP:
            text_payload = DATA_MAP[command]
        else:

            text_payload = f"Brak danych dla numeru {command}"

        requests.post(
            f"{SERVER}/data",
            data=text_payload,
            headers={"Content-Type": "text/plain"}
        )

        print("Obsłużono komendę:", command)

    except Exception as e:
        print("Błąd:", e)

    time.sleep(1)
