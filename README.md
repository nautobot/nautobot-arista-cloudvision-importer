# nautobot-aristacv-importer

This command line utility is used to onboard user tags from Cloudvision to Nautobot.

## Installation

To use this tool, clone this repository to your local machine using

```shell
git clone https://github.com/networktocode-llc/nautobot-aristacv-importer
```

This command line tool is managed and ran from poetry. To install poetry follow the instructions (here)[https://python-poetry.org/docs/].

## Usage

Before using this tool, you need to configure a few variables in the `pyproject.toml` file under the `[tool.nautobot_aristacv_importer]` section.

For Nautobot, you need to configure the the following:

- `nautobot_url` - The url to your Nautobot instance.
- `nautobot_token` - The created token used to authenticate to your Nautobot instance. Token creation information can be found [here](https://nautobot.readthedocs.io/en/latest/rest-api/authentication/)

For Cloudvision, the variable you set depend on if you are using an onprem instance of Cloudvision or Cloudvision as a service (CVAAS). For onprem, the following must be set:

- `cvp_url` - The url to your Cloudvision instance.
- `cvp_username` - The username used to connect to Cloudvision.
- `cvp_password` - The password used to connect to Cloudvision.
- `insecure` - A boolean telling the tool whether or not to download and automatically trust the Cloudvision certificate. Defaults to False.

The following must be set when connecting to Cloudvision as a service.

- `cvaas_token` - The token for the service account that will be used to connect to CVAAS.

To run the tool use the command `poetry run nautobot_aristacv_importer`. The terminal will display the the expected diff and ask you to verify whether you would like to procedd with the sync or not.