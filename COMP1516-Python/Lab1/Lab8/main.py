

countries = ('Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda', 'Argentina', 'Armenia',
             'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium',
             'Belize', 'Benin', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Brunei',
             'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde',
             'Central African Republic', 'Chad', 'Chile', 'China', 'Colombia', 'Comoros',
             'Congo, Democratic Republic of the', 'Congo, Republic of the', 'Costa Rica', "Cote d'Ivoire (Ivory Coast)",
             'Croatia', 'Cuba', 'Cyprus', 'Czech Republic (Czechia)', 'Denmark', 'Djibouti', 'Dominica',
             'Dominican Republic', 'East Timor', 'Ecuador', 'Egypt', 'El Salvador', 'England', 'Equatorial Guinea',
             'Eritrea', 'Estonia', 'Eswatini (Swaziland)', 'Ethiopia', 'Federated States of Micronesia', 'Fiji',
             'Finland', 'France', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Greece', 'Grenada', 'Guatemala',
             'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hungary', 'Iceland', 'India', 'Indonesia',
             'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya',
             'Kiribati', 'Kosovo', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya',
             'Liechtenstein', 'Lithuania', 'Luxembourg', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta',
             'Marshall Islands', 'Mauritania', 'Mauritius', 'Mexico', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro',
             'Morocco', 'Mozambique', 'Myanmar (Burma)', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Zealand',
             'Nicaragua', 'Niger', 'Nigeria', 'North Korea', 'North Macedonia (Macedonia)', 'Northern Ireland', 'Norway',
             'Oman', 'Pakistan', 'Palau', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland',
             'Portugal', 'Qatar', 'Romania', 'Russia', 'Rwanda', 'Saint Kitts and Nevis', 'Saint Lucia',
             'Saint Vincent and the Grenadines', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia',
             'Scotland', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia',
             'Solomon Islands', 'Somalia', 'South Africa', 'South Korea', 'South Sudan', 'Spain', 'Sri Lanka', 'Sudan',
             'Suriname', 'Sweden', 'Switzerland', 'Syria', 'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'Togo',
             'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Tuvalu', 'Uganda', 'Ukraine',
             'United Arab Emirates', 'United Kingdom', 'United States', 'Uruguay', 'Uzbekistan', 'Vanuatu',
             'Vatican City', 'Venezuela', 'Vietnam', 'Wales', 'Yemen', 'Zambia', 'Zimbabwe')

capitals = ('Kabul', 'Tirana (Tirane)', 'Algiers', 'Andorra la Vella', 'Luanda', "Saint John's", 'Buenos Aires',
            'Yerevan', 'Canberra', 'Vienna', 'Baku', 'Nassau', 'Manama', 'Dhaka', 'Bridgetown', 'Minsk', 'Brussels',
            'Belmopan', 'Porto Novo', 'Thimphu', 'Sucre', 'Sarajevo', 'Gaborone', 'Brasilia', 'Bandar Seri Begawan',
            'Sofia', 'Ouagadougou', 'Gitega', 'Phnom Penh', 'Yaounde', 'Ottawa', 'Praia', 'Bangui', "N'Djamena",
            'Santiago', 'Beijing', 'Bogota', 'Moroni', 'Kinshasa', 'Brazzaville', 'San Jose', 'Yamoussoukro', 'Zagreb',
            'Havana', 'Nicosia', 'Prague', 'Copenhagen', 'Djibouti', 'Roseau', 'Santo Domingo', 'Dili', 'Quito', 'Cairo',
            'San Salvador', 'London', 'Malabo', 'Asmara', 'Tallinn', 'Mbabana', 'Addis Ababa', 'Palikir', 'Suva',
            'Helsinki', 'Paris', 'Libreville', 'Banjul', 'Tbilisi', 'Berlin', 'Accra', 'Athens', "Saint George's",
            'Guatemala City', 'Conakry', 'Bissau', 'Georgetown', 'Port au Prince', 'Tegucigalpa', 'Budapest',
            'Reykjavik', 'New Delhi', 'Jakarta', 'Tehran', 'Baghdad', 'Dublin', 'Jerusalem', 'Rome', 'Kingston',
            'Tokyo', 'Amman', 'Nur-Sultan', 'Nairobi', 'Tarawa Atoll', 'Pristina', 'Kuwait City', 'Bishkek',
            'Vientiane', 'Riga', 'Beirut', 'Maseru', 'Monrovia', 'Tripoli', 'Vaduz', 'Vilnius', 'Luxembourg',
            'Antananarivo', 'Lilongwe', 'Kuala Lumpur', 'Male', 'Bamako', 'Valletta', 'Majuro', 'Nouakchott',
            'Port Louis', 'Mexico City', 'Chisinau', 'Monaco', 'Ulaanbaatar', 'Podgorica', 'Rabat', 'Maputo',
            'Nay Pyi Taw', 'Windhoek', 'No official capital', 'Kathmandu', 'Amsterdam', 'Wellington', 'Managua',
            'Niamey', 'Abuja', 'Pyongyang', 'Skopje', 'Belfast', 'Oslo', 'Muscat', 'Islamabad', 'Melekeok',
            'Panama City', 'Port Moresby', 'Asuncion', 'Lima', 'Manila', 'Warsaw', 'Lisbon', 'Doha', 'Bucharest',
            'Moscow', 'Kigali', 'Basseterre', 'Castries', 'Kingstown', 'Apia', 'San Marino', 'Sao Tome', 'Riyadh',
            'Edinburgh', 'Dakar', 'Belgrade', 'Victoria', 'Freetown', 'Singapore', 'Bratislava', 'Ljubljana', 'Honiara',
            'Mogadishu', 'Pretoria, Bloemfontein, Cape Town', 'Seoul', 'Juba', 'Madrid', 'Colombo', 'Khartoum',
            'Paramaribo', 'Stockholm', 'Bern', 'Damascus', 'Taipei', 'Dushanbe', 'Dodoma', 'Bangkok', 'Lome',
            "Nuku'alofa", 'Port of Spain', 'Tunis', 'Ankara', 'Ashgabat', 'Funafuti', 'Kampala', 'Kiev', 'Abu Dhabi',
            'London', 'Washington D.C.', 'Montevideo', 'Tashkent', 'Port Vila', 'Vatican City', 'Caracas', 'Hanoi',
            'Cardiff', "Sana'a", 'Lusaka', 'Harare')


def get_countries(substring):
    """
    Function loop over a tuple of countries and write in a text file the countries with a given string in the name.
    :param substring:
    """
    f = open("lab-week-8.txt", "w")
    f.write(f'countries with {substring} in the name are:\n')
    for country in countries:
        if substring.lower() in country.casefold():
            f.write(country + "\n")
    f.close()


def get_capitals(substring):
    """
    Function loop over a tuple of capitals and append in a text file the capitals with a given string in the name.
    :param substring:
    """
    f = open("lab-week-8.txt", "a")
    f.write(f'capitals with {substring} in the name are:\n')
    for capital in capitals:
        if substring.lower() in capital.casefold():
            f.write(capital + "\n")
    f.close()


def get_file_data():
    """
    Function to open a text file and print the content line by line.
    :return:
    """
    with open("lab-week-8.txt", "r") as file:
        result = file.readlines()
        for lines in result:
            print(lines.strip())


def main():
    get_countries("ne")
    get_capitals("city")
    get_file_data()


if __name__ == '__main__':
    main()

