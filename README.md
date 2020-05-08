# Poll Checker
A simple Python project that collects US election polling data for quick
viewing. It is limited to RealClearPolitics (RCP) averages by design,
not comprehensive data analysis with margins of error, pollster ratings, etc.

The `core.py` file contains the general logic for collecting and printing RCP
averages. Individual scripts exist for various elections with self-evident
names. The `all.sh` Bash script simply runs each script for convenience.
