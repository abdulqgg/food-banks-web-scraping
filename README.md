# Foodbank Data Scraper

This project involved web scraping data on all independent foodbanks in the UK from the Independent Food Aid Network. To get a comprehensive view of the network, I also used data from the [Google Maps website](https://www.google.com/maps/d/viewer?mid=15mnlXFpd8-x0j4O6Ck6U90chPn4bkbWz&ll=51.64010438452066%2C1.3356308175781262&z=9) to supplement the Independent Food Aid Network data.

I used Python and Selenium to extract the foodbank names, addresses, contact numbers, and social media handles. The collected data was saved in a CSV file named foodbanks.csv.

The goal of this project was to obtain a detailed overview of the UK foodbank network, which can be used to understand the scale and distribution of foodbanks across the country. This data can also be used by policymakers to identify areas of need and to develop strategies to combat food poverty.

## Installation

- Clone the repository
- Run the scripts in the following order: `main.py` or `main-data.py`, and then `txt-to-csv.py`.

## Demo
![demo video](https://user-images.githubusercontent.com/43912641/223794580-cc10d75d-6f6d-444b-a3f7-f1ca4df08b3f.gif)


## Usage

- Run `main.py` to extract the foodbank names to `foodbank_names.txt`
- Run `main-data.py` to extract the foodbank names, addresses, numbers, and social media handles to `foodbank_data.txt`
- Run `txt-to-csv.py` to convert the extracted data from a txt file to a csv file to `data.csv`.

## Tools Used

- Python
- Selenium

## Contributing

Feel free to submit pull requests or suggest improvements.

## License

This project is licensed under the [MIT License](LICENSE).
