# Arista Cloudvision Importer

The tool acts as your initial sync of user tags from Cloudvision to tags in Nautobot. Once you run this tool once, you can use the "Sync To" feature in the SSoT plugin found [here](https://github.com/networktocode-llc/nautobot-plugin-ssot-arista-cloudvision) to keep Cloudvision up to date with any new tags created in Nautobot.

If devices in Cloudvision already have tags assigned to them, this tool will assign the tags to the device in Nautobot as long as the device exists. If the deivce does not exist in Nautobot, only the tag is created.

> This tool only syncs tags from Cloudvision to Nautobot.

## Installation

To use this tool, clone this repository to your local machine using

```shell
git clone git@github.com:networktocode-llc/nautobot-arista-cloudvision-importer.git
```

This command line tool is managed and ran from poetry. To install poetry follow the instructions [here](https://python-poetry.org/docs/).

## Usage

Before using this tool, you need to configure a few variables in the `pyproject.toml` file under the `[tool.nautobot_aristacv_importer]` section.

For Nautobot, you need to configure the the following:

- `nautobot_url` - The url to your Nautobot instance.
- `nautobot_token` - The created token used to authenticate to your Nautobot instance. Token creation information can be found [here](https://nautobot.readthedocs.io/en/latest/rest-api/authentication/)

For Cloudvision, the variables you set depend on whether you are using an onprem instance of Cloudvision or Cloudvision as a service (CVAAS). For onprem, the following must be set:

- `cvp_url` - The url to your Cloudvision instance.
- `cvp_username` - The username used to connect to Cloudvision.
- `cvp_password` - The password used to connect to Cloudvision.
- `insecure` - A boolean telling the tool whether or not to download and automatically trust the Cloudvision certificate. Defaults to False.

The following must be set when connecting to Cloudvision as a service.

- `cvaas_token` - The token for the service account that will be used to connect to CVAAS.

To run the tool use the command `poetry run nautobot_aristacv_importer`. The terminal will display the the expected diff and ask you to verify whether you would like to proceed with the sync or not. Below is a short video showing an example.

![arista_importer](https://user-images.githubusercontent.com/38091261/126538807-e0b2b451-2297-4b28-b5c0-781c7b6a9e9f.gif)

### CLI Helper Commands

The project is coming with a CLI helper based on [invoke](http://www.pyinvoke.org/) to help facilitate testing and docker container management. Testing is performed in a docker container to ensure environment uniformity. In order to run the tests you must first build the docker container using `invoke build`. From there, you can run any of the commands below to test your code. Each command also has its own help `invoke <command> --help`

#### Testing

```no-highlight
  bandit           Run bandit to validate basic static code security analysis.
  black            Run black to check that Python files adhere to its style standards.
  flake8           This will run flake8 for the specified name and Python version.
  pydocstyle       Run pydocstyle to validate docstring formatting adheres to NTC defined standards.
  pylint           Run pylint code analysis.
  pytest           Run pytest.
  tests            Run all tests for this plugin.
```

#### Docker Management
```no-highlight
  build            Build all docker images.
  rebuild          Clean the docker image and then rebuild without using cache.
  clean            Remove the project specific image.
```

## Questions

For any questions or comments, please check the [FAQ](FAQ.md) first and feel free to swing by the [Network to Code slack channel](https://networktocode.slack.com/) (channel #networktocode).
Sign up [here](http://slack.networktocode.com/)
