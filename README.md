#NetCTRL_Script

This script retrieves the hostname from a file and matches it against Netbox to retrieve the IP, then sends configuration to multiple types of switches based on the device type from Netbox. The configuration is from a Jinja2 template.

## Setup

Follow these steps to set up and run the script:

1. Clone the GitHub repository: `git clone https://github.com/user/repo.git`
2. Go into the folder: `cd repo`
3. Create a virtual environment: `python -m venv env`
4. Activate the virtual environment: `source env/bin/activate`
5. Install the dependencies: `python setup.py install`

## Usage

To run the script, use the following command:

```bash
python main.py -h
```

This will display a list of available command line parameters.

## Examples

Here are some examples of how to use the script:

- Retrieve device information from Netbox and generate configuration:

```bash
python main.py -y config.yml
```

- Retrieve device information from Netbox, generate configuration, and send to devices:

```bash
python main.py -y config.yml -s
```

- Retrieve device information from Netbox and generate configuration for a specific device:

```bash
python main.py -y config.yml -i 192.168.0.1
```

- Retrieve device information from Netbox and generate configuration for a specific device type:

```bash
ppython main.py -y config.yml -d cisco_ios
```

- Test that the script is working as expected without actually sending the configuration to devices:

```bash
python main.py -y config.yml -t
```
