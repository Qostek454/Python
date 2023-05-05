{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "7446f6d1",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Wgranie bilbioteki\n",
    "import pandas as pd\n",
    "pd.options.display.float_format = '{:,.2f}'.format # Lepsza wizualizacja danych numerycznych"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "e61d3169",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Wczytanie pliku CSV\n",
    "df = pd.read_csv(\"salaries_by_college_major.csv\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b76ee5e4",
   "metadata": {},
   "source": [
    "# Wielkość danych (rzędy, kolumn)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7c9bbf2b",
   "metadata": {},
   "outputs": [],
   "source": [
    "df.shape"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "43779daa",
   "metadata": {},
   "source": [
    "# nazwy kolumn"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b1ea2ec8",
   "metadata": {},
   "outputs": [],
   "source": [
    "df.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "01e720e8",
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "# Szukanie Missing Data >> Pokazuje cała tabele jezeli jest TRUE znaczy ze jest NaN\n",
    "df.isna()\n",
    "# usunanie rzedów z Missing data lub Junk Data\n",
    "df.dropna()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7a1c1873",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Pokazanie danych wybranej kolumn\n",
    "df[\"Starting Median Salary\"]\n",
    "# Wyszukanie największej wartości w tej kolumnie\n",
    "df[\"Starting Median Salary\"].max()\n",
    "# Wyszukanie numeru rzędu z największą wartością\n",
    "df[\"Starting Median Salary\"].idxmax()\n",
    "# Zlokalizawnie danych z rzedu 43 >> wyniki ukazane w tabeli nazwa kolumny wartosc\n",
    "df.loc[43]\n",
    "# Wyswietlenie poszcegolnej wartosci\n",
    "df[\"Starting Median Salary\"].loc[43]\n",
    "df[\"Starting Median Salary\"][43]\n",
    "# Wynik ukazany jako czesc pierwotnej tabeli\n",
    "df[43:44]\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5ed0a6a7",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Dodawanie kolumny na podstawie wyliczenia danych z innych kolumn\n",
    "\n",
    "spread_col = df['Mid-Career 90th Percentile Salary'] - df['Mid-Career 10th Percentile Salary']\n",
    "df.insert(6, 'Spread', spread_col)\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "234bd152",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Sortowanie\n",
    "## po kolumnie spread\n",
    "low_risk = df.sort_values('Spread')\n",
    "## pokaznie całej tabeli posortowanej\n",
    "low_risk\n",
    "\n",
    "### wybranie kolumn ktore chce sie zobaczyc\n",
    "low_risk[['Undergraduate Major', 'Spread']]\n",
    "\n",
    "\n",
    "## szybszy sposob sortowania z wybraniem kolumn\n",
    "test = df\n",
    "\n",
    "# Sortowanie od największej do najmniejszej\n",
    "test[['Undergraduate Major', 'Spread']].sort_values('Spread',ascending=False)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "37fad1b7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Starting Median Salary</th>\n",
       "      <th>Mid-Career Median Salary</th>\n",
       "      <th>Mid-Career 10th Percentile Salary</th>\n",
       "      <th>Mid-Career 90th Percentile Salary</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Group</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Business</th>\n",
       "      <td>44,633.33</td>\n",
       "      <td>75,083.33</td>\n",
       "      <td>43,566.67</td>\n",
       "      <td>147,525.00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>HASS</th>\n",
       "      <td>37,186.36</td>\n",
       "      <td>62,968.18</td>\n",
       "      <td>34,145.45</td>\n",
       "      <td>129,363.64</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>STEM</th>\n",
       "      <td>53,862.50</td>\n",
       "      <td>90,812.50</td>\n",
       "      <td>56,025.00</td>\n",
       "      <td>157,625.00</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "          Starting Median Salary  Mid-Career Median Salary  \\\n",
       "Group                                                        \n",
       "Business               44,633.33                 75,083.33   \n",
       "HASS                   37,186.36                 62,968.18   \n",
       "STEM                   53,862.50                 90,812.50   \n",
       "\n",
       "          Mid-Career 10th Percentile Salary  Mid-Career 90th Percentile Salary  \n",
       "Group                                                                           \n",
       "Business                          43,566.67                         147,525.00  \n",
       "HASS                              34,145.45                         129,363.64  \n",
       "STEM                              56,025.00                         157,625.00  "
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Grupowanie (podobne do Pivot Table w excelu)\n",
    "df.groupby(\"Group\").count() # pokazuje ile mamy rzędow w danej grupie\n",
    "df.groupby(\"Group\").sum() # sumuje wszystkie wartosci per grupa\n",
    "df.groupby(\"Group\").mean() # pokazuje srednia wartosc dla grupy\n",
    "df.groupby(['Group','Starting Median Salary']).mean() # grupowanie po większej ilości kolumn"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "adb070ce",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "3df51a8a",
   "metadata": {},
   "source": [
    "# Challenges:\n",
    "\n",
    "1. What college major has the highest mid-career salary? How much do graduates with this major earn? (Mid-career is defined as having 10+ years of experience).\n",
    "\n",
    "2. Which college major has the lowest starting salary and how much do graduates earn after university?\n",
    "\n",
    "3. Which college major has the lowest mid-career salary and how much can people expect to earn with this degree? "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "204d6396",
   "metadata": {},
   "outputs": [],
   "source": [
    "#1\n",
    "df.loc[df[\"Mid-Career Median Salary\"].idxmax()]\n",
    "\n",
    "#2\n",
    "df.loc[df[\"Starting Median Salary\"].idxmin()]\n",
    "\n",
    "#3\n",
    "df.loc[df[\"Mid-Career Median Salary\"].idxmin()]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9291e35c",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
