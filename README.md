# Arista CloudVision Importer

This tool acts as your initial sync of user tags from CloudVision to tags in Nautobot. After running this tool once, you can use the "Sync To" feature in the SSoT plugin found [here](https://github.com/nautobot/nautobot-plugin-ssot-arista-cloudvision) to keep CloudVision up to date with any new tags created in Nautobot.

If devices in CloudVision already have tags assigned to them, this tool will assign the tags to the device in Nautobot as long as the device exists. If the deivce does not exist in Nautobot, only the tag is created. Below is a small gif showing the CLI tool in action.

![arista_importer](https://user-images.githubusercontent.com/38091261/126538807-e0b2b451-2297-4b28-b5c0-781c7b6a9e9f.gif)

> This tool only syncs tags from CloudVision to Nautobot and will NOT delete tags from Nautobot even if the tag is deleted in CloudVision.

## Installation
This command line tool is ran from poetry. To install poetry follow the instructions [here](https://python-poetry.org/docs/).

To use this tool, clone this repository to your local machine using

```shell
git clone git@github.com:nautobot/nautobot-arista-cloudvision-importer.git
```

Once the repo is cloned, you will need to change your working directory to the root of the project to run the commands in the section below.

## Usage
Before using this tool, you need to configure a few variables in the `pyproject.toml` file under the `[tool.nautobot_aristacv_importer]` section.

For Nautobot, you need to configure the the following:

- `nautobot_url` - The url to your Nautobot instance.
- `nautobot_token` - The created token used to authenticate to your Nautobot instance. Token creation information can be found [here](https://nautobot.readthedocs.io/en/latest/rest-api/authentication/)

For CloudVision, the variables you set depend on whether you are using an onprem instance of CloudVision or CloudVision as a service (CVAAS). For onprem, the following must be set:

- `cvp_host` - The ip to your CloudVision instance.
- `cvp_user` - The username used to connect to CloudVision.
- `cvp_password` - The password used to connect to CloudVision.
- `insecure` - A boolean telling the tool whether or not to download and automatically trust the CloudVision certificate. Defaults to False.

The following must be set when connecting to CloudVision as a service.

- `cvaas_token` - The token for the service account that will be used to connect to CVAAS.

Once configured you need to run `poetry install` to install dependencies for the tool. After that you can run the tool using the command `poetry run nautobot_aristacv_importer`. The terminal will display the the expected diff and ask you to verify whether you would like to proceed with the sync or not.

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
