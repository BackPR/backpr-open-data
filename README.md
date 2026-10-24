# BackPR open data for US youth programs

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23577823.svg)](https://doi.org/10.5281/zenodo.23577823)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

Reference data on camps, after-school programs, childcare and youth sports in the United States, compiled by [BackPR](https://backpr.com), a company that makes registration and payments software for youth programs. Each dataset names its sources, and the data is free to use under CC BY 4.0.

- **State rules** for all 50 states and DC: childcare licensing, staff ratios, camp licensing, background checks, medication and mandated child abuse reporting, with links to the official sources
- **A registration software pricing index:** what 56 platforms publish about price, fees and nonprofit terms
- **Youth and community nonprofits by state**, counted from IRS records
- **An index of free templates for youth program forms**, written by BackPR
- **Counts of the licensed programs listed in BackPR's program finder**, by state, from state and local licensing data

BackPR competes with the companies in the pricing index, so we left BackPR out of it.

The latest versions are listed at **[backpr.com/ai](https://backpr.com/ai)**. This repository is updated from backpr.com every Monday, and each dataset below shows its version and the date we last checked it.

## Use the data

CSV and JSON files are in [`data/`](data/). [`data/datapackage.json`](data/datapackage.json) is a machine-readable index of the files, with each one's version, date, sources, license and citation (in the Frictionless Data Package format).

Load a file straight from this repository, for example with pandas:

```python
import pandas as pd

base = "https://raw.githubusercontent.com/BackPR/backpr-open-data/main/data"
rules = pd.read_csv(f"{base}/state-rules.csv")
nonprofits = pd.read_csv(f"{base}/youth-nonprofits-by-state.csv")
```

Each dataset below also has a live copy on backpr.com, which is updated first.

The same files are also on:

- [Zenodo](https://doi.org/10.5281/zenodo.23577823): a permanent, citable copy with a DOI, for research and reports
- [Hugging Face](https://huggingface.co/datasets/backpr/us-youth-program-data): load it with the datasets library or browse it in the dataset viewer
- [Kaggle](https://www.kaggle.com/datasets/backpr/us-youth-program-data-rules-nonprofits-pricing): explore it in a notebook

## Datasets

Each dataset lists its sources, with notes on how it was made and what it doesn't cover.

<!-- datasets:start -->
### Youth program rules by state: childcare licensing, staff ratios, camps, background checks, medication and mandated reporting

Rules for childcare centers, camps and after-school programs in all 50 states and DC, summarized from official state sources and published copies of state law, with links to each source.

- Files: [`data/state-rules.csv`](data/state-rules.csv), [`data/state-rules.json`](data/state-rules.json) (51 records)
- Version 2026.10 · Last checked October 2026
- Sources: State licensing rules, statutes and agency pages, and published copies of state law such as Cornell's Legal Information Institute, listed per record
- Notes: General information, not legal advice. Rules change; confirm with the state agency. A blank (null) value means the rules don't set a single value for it or we couldn't confirm it from the sources.
- Live copy: https://backpr.com/data/state-rules.json · Page on backpr.com: https://backpr.com/resources/states
- Cite as: BackPR (2026). Youth program rules by state: childcare licensing, staff ratios, camps, background checks, medication and mandated reporting (version 2026.10, checked October 2026). https://backpr.com/data/state-rules.json. CC BY 4.0.

### Registration software pricing index: what 56 platforms publish about price, fees and nonprofit terms

What registration, camp, childcare, class and sports software publishes about plan prices, nonprofit offers, fees passed on to families, card processing rates, contracts, onboarding fees and Spanish-language support. Each record has a short summary of what the platform publishes, a link to the source and the date we checked.

- Files: [`data/registration-software-pricing-index.csv`](data/registration-software-pricing-index.csv), [`data/registration-software-pricing-index.json`](data/registration-software-pricing-index.json) (56 records)
- Version 1.0 · Last checked October 2026
- Sources: Each company's public pricing pages and terms, linked from its BackPR comparison page
- Notes: BackPR competes with the companies in this index, so we left BackPR out. A value of "not published" means we found nothing, not that the company doesn't offer it. CC BY 4.0 covers BackPR's compilation; quoted company text remains the company's. Companies in the index can send corrections to support@backpr.com. BackPR's State of Youth Programs 2026 report uses only the 48 registration and management platforms in this index and leaves out the form, fundraising, event and membership tools (categories "forms" and "membership").
- Live copy: https://backpr.com/data/registration-software-pricing-index.json · Page on backpr.com: https://backpr.com/resources/registration-software-pricing
- Cite as: BackPR (2026). Registration software pricing index: what 56 platforms publish about price, fees and nonprofit terms (version 1.0, checked October 2026). https://backpr.com/data/registration-software-pricing-index.json. CC BY 4.0.

### Youth and community nonprofits by state: active 501(c)(3) organizations from IRS data

Counts of active 501(c)(3) youth development, amateur sports, PTA and PTO, recreation, camp and club, children's and youth services, arts education and childcare nonprofits in each state and DC, by group, including how many report under $50,000 in annual revenue. There are 171,592 nationally. The state rows total 171,286; the other 306 have no state on file or are in US territories, at military addresses or abroad.

- Files: [`data/youth-nonprofits-by-state.csv`](data/youth-nonprofits-by-state.csv), [`data/youth-nonprofits-by-state.json`](data/youth-nonprofits-by-state.json) (51 records)
- Version 1.0 · Last checked September 8, 2026
- Sources: IRS Exempt Organizations Business Master File, posted September 8, 2026
- Notes: Filter: Active 501(c)(3) organizations in the NTEE codes listed for each group. Group codes (NTEE, the IRS's activity codes for nonprofits): Amateur sports: N40, N6x, N7x; Youth development: all O codes; PTAs and PTOs: B94; Recreation, camps and clubs: N20, N30, N31, N50; Children's and youth services: P30; Arts education: A25; Childcare: P33. Each organization is counted once, by its main NTEE code. Some groups, such as amateur sports and arts education, include organizations that also serve adults. The "under_50k" column counts organizations that report annual revenue under $50,000 on their latest IRS filing or have no revenue amount on file.
- Live copy: https://backpr.com/data/youth-nonprofits-by-state.json · Page on backpr.com: https://backpr.com/resources/nonprofits-by-state
- Cite as: BackPR (2026). Youth and community nonprofits by state: active 501(c)(3) organizations from IRS data (version 1.0, checked September 2026). https://backpr.com/data/youth-nonprofits-by-state.json. CC BY 4.0.

### Free youth program form templates: registration, medical, pickup, waivers, policies and staff forms

BackPR's free printable PDF and editable Word templates for camps, after-school programs, childcare and other youth programs, with Spanish versions of the forms families fill out.

- Files: [`data/templates.csv`](data/templates.csv), [`data/templates.json`](data/templates.json) (28 records)
- Version 1.0 · Last checked October 2026
- Sources: Written by BackPR
- Notes: A list of BackPR's free templates, with links to each PDF and Word file. CC BY 4.0 covers this list; the templates themselves are free to use and change without credit. They're starting points to adapt, not legal advice. Have a lawyer review waivers and agreements.
- Live copy: https://backpr.com/data/templates.json · Page on backpr.com: https://backpr.com/resources/templates
- Cite as: BackPR (2026). Free youth program form templates: registration, medical, pickup, waivers, policies and staff forms (version 1.0, checked October 2026). https://backpr.com/data/templates.json. CC BY 4.0.

### Licensed youth program directory statistics: centers, after-school programs and camps by state

Live counts of the childcare centers, school-age (after-school) programs, camps and other youth programs listed in BackPR's program finder, by state and program type, from official state and local licensing data. One record per state with listings. Updated daily on backpr.com; each file shows its update date.

- Files: [`data/finder-directory-stats.csv`](data/finder-directory-stats.csv), [`data/finder-directory-stats.json`](data/finder-directory-stats.json) (one record per state with listings: 20 states)
- Version: live · Updated daily on backpr.com and weekly here
- Sources: Each state's official licensing or program data, as listed on each state's finder page
- Notes: Home-based family childcare isn't listed. Counts cover the states that publish program data.
- Live copy: https://backpr.com/data/finder-directory-stats.json · Page on backpr.com: https://backpr.com/find
- Cite as: BackPR (2026). Licensed youth program directory statistics (live data, updated <the date shown in the file>). https://backpr.com/data/finder-directory-stats.json. CC BY 4.0.
<!-- datasets:end -->

## Ask an AI assistant about this data

MCP (Model Context Protocol) is the standard way AI assistants such as Claude and ChatGPT connect to outside data. The BackPR data MCP server lets an assistant answer questions using these datasets. It's public and read-only and needs no sign-in. Every result links to its source on backpr.com.

Server address: `https://backpr.com/ai/mcp` (listed in the [official MCP Registry](https://registry.modelcontextprotocol.io/v0.1/servers?search=com.backpr) as `com.backpr/data`)

- **Claude:** open **Customize**, then **Connectors**. Select **+** and choose **Add custom connector**. Name it "BackPR data" and paste the server address.
- **ChatGPT:** open **Plugins**, select **+** and choose **Add custom MCP server**. Name it "BackPR data", paste the server address and choose **No authentication**.
- **Claude Code:**

  ```bash
  claude mcp add --transport http --scope user backpr-data https://backpr.com/ai/mcp
  ```

- **Cursor** (`~/.cursor/mcp.json`):

  ```json
  { "mcpServers": { "backpr-data": { "url": "https://backpr.com/ai/mcp" } } }
  ```

- **VS Code** (`.vscode/mcp.json`):

  ```json
  { "servers": { "backpr-data": { "type": "http", "url": "https://backpr.com/ai/mcp" } } }
  ```

The registration software tool answers only from the pricing index, which doesn't include BackPR.

Try asking: "What are the staff ratios for childcare centers in Texas?", "Which states require everyone to report child abuse?" or "Does a day camp in Texas need a license?"

The server has 10 tools: `get_state_rules`, `list_states_by_rule`, `calculate_staff_needed`, `find_registration_software`, `find_programs`, `get_directory_stats`, `find_template`, `search_backpr`, `list_datasets` and `about_backpr`. Details: [backpr.com/ai](https://backpr.com/ai).

## License and citation

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/): free to use, share and adapt, including commercially, as long as you credit BackPR and link to the source. The license covers BackPR's compilation and summaries. Text quoted from companies' websites stays theirs, and the linked state sources have their own terms.

Each dataset above has its own citation line. To cite the whole collection:

> BackPR (2026). BackPR open data for US youth programs [Data set]. Zenodo. https://doi.org/10.5281/zenodo.23577823. Current version: https://backpr.com/ai. CC BY 4.0.

That DOI always points to the newest version. To cite a fixed snapshot, use the version DOI shown on the Zenodo page or a release of this repository. GitHub's "Cite this repository" button uses [`CITATION.cff`](CITATION.cff).

## Notes

- The state rules are general information, not legal advice. They summarize state law and state agency rules; cities and counties can add their own. Each record links to the state's official sources and to the exact section on backpr.com (for example https://backpr.com/resources/states/texas#ratios). Confirm requirements with your state licensing agency.
- Found an error? Email support@backpr.com. We'll check it, and if we got it wrong, we'll fix it and note the change on [backpr.com/changes](https://backpr.com/changes).
- Please don't send corrections as pull requests: the files here are copied from backpr.com, so changes made here would be overwritten.
