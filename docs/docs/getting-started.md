---
sidebar_position: 2
---

# Getting Started

:::info Prerequisites

To use flute effectively, it is helpful to have a familiarity with Python and Selenium concepts.

:::

This section will guide you through the steps to create a new flute project using starter template, which is recommended for most Greenfield automation projects.

---

Clone Starter Template

```bash
git clone https://github.com/cryptodinh/flute-starter my-flute-project
```

Then change into `my-flute-project` directory, install dependencies, open vscode, and start the project:

```bash
cd my-flute-project
python -m pip install -r requirements.txt
code . # Optionally, open the project in VSCode
python main.py
```

<!-- Once started it will scrape google search for "flute web scraping framework" keyword and store the results in `output/finished.json` -->
Once started it will scrape data and store the results in `output/finished.json`. 
<!-- ![Result](./img/google-scraping.png) -->

You can edit the `task.py` file based on your Project Needs. 

## Next Steps

If you are new to flute, we encourage you to learn about flute [here](sign-up-tutorial.md).