# CQAsk
This tool utilizes Language Models (LLMs) to generate Computer-Aided Design (CAD) models effortlessly.

<p align="center">
    <a href="https://discord.gg/H7qRauGkQ6">
        <img src="https://img.shields.io/discord/913193916885524552?logo=discord"
            alt="chat on Discord">
    </a>
    <a href="https://www.patreon.com/openorion">
        <img src="https://img.shields.io/badge/dynamic/json?color=%23e85b46&label=Patreon&query=data.attributes.patron_count&suffix=%20patrons&url=https%3A%2F%2Fwww.patreon.com%2Fapi%2Fcampaigns%2F9860430"
            alt="donate to Patreon">
    </a>
</p>

![assets/gear.png](assets/gear.png)


## Installation

### Frontend
1. Clone this repository.
2. Navigate to the UI library directory.
3. Run `yarn install` to install dependencies.
4. Execute `yarn dev` to start the UI library.

### Backend
1. Ensure you have Python installed.
2. Navigate to the backend directory.
3. Run `pip install -r requirements.txt` to install backend dependencies.
4. Add a `.env` file with `OPENAI={OPENAI KEY}`
5. Start the server by running `python api.py`.

## Usage

1. Access the UI via the specified URL after starting the UI library.
2. Input your CAD requirements or specifications.
3. Interact with the tool to generate CAD models using Language Models.
4. All CQ generated files are in the generated directory of `backend`, you can generate STEP/STL files of your choice 
by taking the `obj`` and using CQ functions as needed: https://cadquery.readthedocs.io/en/latest/importexport.html

## Features

- Seamless integration of Language Models for CAD generation.
- User-friendly UI for easy interaction.
- Customizable input for CAD specifications.


## License

This project is licensed under the [MIT License](LICENSE.md) - see the LICENSE.md file for details.

