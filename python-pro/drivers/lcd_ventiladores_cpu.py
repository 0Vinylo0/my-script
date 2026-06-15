#!/usr/bin/env python3
import json
import subprocess
import time
import hid

DEVICE_PATH = b"/dev/hidraw0"
UPDATE_INTERVAL = 1.0

BASE_PACKET = bytes.fromhex(
    "20 01 00 00 00 00 32 00 00 2c 00 05 3d "
    + "00 " * 52
)

TEMP_BYTE_INDEX = 6


def read_sensors_json() -> dict:
    out = subprocess.check_output(["sensors", "-j"], text=True)
    return json.loads(out)


def extract_cpu_temp(data: dict) -> int:
    preferred = [
        "k10temp-pci-00c3",
        "k10temp-pci-00cb",
        "zenpower-pci-00c3",
        "zenpower-pci-00cb",
    ]

    for chip in preferred:
        if chip in data:
            for label in ("Tctl", "Tdie", "temp1"):
                if label in data[chip]:
                    block = data[chip][label]
                    for key, value in block.items():
                        if key.endswith("_input") and isinstance(value, (int, float)):
                            return int(round(value))

    for chip_name, chip_data in data.items():
        if not isinstance(chip_data, dict):
            continue
        if "gpu" in chip_name.lower() or "amdgpu" in chip_name.lower():
            continue

        for _, block in chip_data.items():
            if not isinstance(block, dict):
                continue
            for key, value in block.items():
                if key.endswith("_input") and isinstance(value, (int, float)):
                    return int(round(value))

    raise RuntimeError("No se encontró temperatura CPU")


def clamp_temp(value: int) -> int:
    return max(0, min(255, value))


def build_packet(cpu_temp: int) -> bytes:
    pkt = bytearray(BASE_PACKET)
    pkt[TEMP_BYTE_INDEX] = clamp_temp(cpu_temp)
    return bytes(pkt)


def main() -> None:
    h = hid.device()
    h.open_path(DEVICE_PATH)

    try:
        while True:
            sensors_data = read_sensors_json()
            cpu_temp = extract_cpu_temp(sensors_data)
            pkt = build_packet(cpu_temp)
            h.write(pkt)
            print(f"CPU {cpu_temp}°C")
            time.sleep(UPDATE_INTERVAL)
    finally:
        h.close()


if __name__ == "__main__":
    main()
