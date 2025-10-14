#!/usr/bin/env python3
import argparse
import os

# Hardcoded constants to match AMF
K_HEX = "fec86ba6eb707ed08905757b1bb44b8f"
OPC_HEX = "C42449363BBAD02B66D16BC975D77CC1"

UE_TEMPLATE = """[rf]
freq_offset = 0
tx_gain = 80
rx_gain = 40
srate = 23.04e6
nof_antennas = 1

device_name = zmq
device_args = tx_port={tx_port},rx_port={rx_port},base_srate=23.04e6

[rat.eutra]
dl_earfcn = 2850
nof_carriers = 0

[rat.nr]
bands = 3
nof_carriers = 1
max_nof_prb = 106
nof_prb = 106

[log]
all_level = warning
phy_lib_level = none
all_hex_limit = 32
filename = {log_file}
file_max_size = 1000

[usim]
mode = soft
algo = milenage
opc  = {opc}
k    = {k}
imsi = {imsi}
imei = 356938035643803

[rrc]
release = 15
ue_category = 4

[nas]
apn = {apn}
apn_protocol = ipv4

[gw]
netns = {netns}
ip_devname = tun_srsue
ip_netmask = 255.255.255.0

[gui]
enable = false
"""

def imsi_for(ue_number: int) -> str:
    # Matches your AMF format: 0010100000000NN
    return f"0010100000000{ue_number:02d}"

def apn_for(ue_number: int) -> str:
    # Hardcoded slice mapping:
    # odd-numbered UE -> "internet" (slice_1)
    # even-numbered UE -> "streaming" (slice_2)
    return "internet" if ue_number % 2 == 1 else "streaming"

def generate_ue_config(ue_number: int, output_directory: str) -> str:
    os.makedirs(output_directory, exist_ok=True)

    cfg = UE_TEMPLATE.format(
        tx_port=f"tcp://10.10.3.232:{2100 + ue_number}",
        rx_port=f"tcp://10.10.3.232:{2200 + ue_number}",
        log_file=os.path.join(output_directory, f"ue{ue_number}.log"),
        opc=OPC_HEX,
        k=K_HEX,
        imsi=imsi_for(ue_number),
        apn=apn_for(ue_number),
        netns=f"ue{ue_number}",
    )

    path = os.path.join(output_directory, f"ue_{ue_number}.conf")
    with open(path, "w") as f:
        f.write(cfg)
    print(f"Wrote {path}")
    return path

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate hardcoded UE configuration files.')
    parser.add_argument('ue_number', type=int, help='UE number (e.g., 6 -> IMSI ...000006)')
    parser.add_argument('output_directory', type=str, help='Directory to save the UE configuration')
    args = parser.parse_args()
    generate_ue_config(args.ue_number, args.output_directory)
