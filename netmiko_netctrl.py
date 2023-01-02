from netmiko import ConnectHandler

def send_config(device_ip, config_str, username, password):
    """
    Send configuration to a device using Netmiko.
    """
    device = {
        "device_type": "cisco_ios",
        "ip": device_ip,
        "username": username,
        "password": password
    }

    net_connect = ConnectHandler(**device)
    output = net_connect.send_config_set(config_str)
    net_connect.disconnect()

    return output

def check_status(device_ip, username, password):
    """
    Check the status of a device using Netmiko.
    """
    device = {
        "device_type": "cisco_ios",
        "ip": device_ip,
        "username": username,
        "password": password
    }

    net_connect = ConnectHandler(**device)
    output = net_connect.send_command("show version")
    net_connect.disconnect()

    if "Cisco IOS Software" in output:
        return "OK"
    else:
        return "Error"

