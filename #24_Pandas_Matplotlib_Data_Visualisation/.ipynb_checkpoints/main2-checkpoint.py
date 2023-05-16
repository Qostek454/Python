{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "a98a224b",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd, matplotlib as mat"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "51d69162",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "DATE 1992\n",
      "TAG 1992\n",
      "POSTS 1991\n"
     ]
    }
   ],
   "source": [
    "df = pd.read_csv(\"QueryResults.csv\", names = ['DATE', 'TAG', 'POSTS'], header = 0) #### przypisanie własnych nazw kolumn\n",
    "df.shape # sprawdzanie ile kolumn i rzedow ma tabela \n",
    "df # wyswietlenie calej tabeli - pokaze tez ilosc kolumn i rzedow\n",
    "df.count() # pokaze ile recordow Not-Null ma dana kolumna"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "b349bd3d",
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
       "      <th>POSTS</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>TAG</th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>TagName</th>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>assembly</th>\n",
       "      <td>34852.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>c</th>\n",
       "      <td>336042.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>c#</th>\n",
       "      <td>1423530.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>c++</th>\n",
       "      <td>684210.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>delphi</th>\n",
       "      <td>46212.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>go</th>\n",
       "      <td>47499.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>java</th>\n",
       "      <td>1696403.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>javascript</th>\n",
       "      <td>2056510.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>perl</th>\n",
       "      <td>65286.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>php</th>\n",
       "      <td>1361988.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>python</th>\n",
       "      <td>1496210.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>r</th>\n",
       "      <td>356799.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>ruby</th>\n",
       "      <td>214582.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>swift</th>\n",
       "      <td>273055.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                POSTS\n",
       "TAG                  \n",
       "TagName           0.0\n",
       "assembly      34852.0\n",
       "c            336042.0\n",
       "c#          1423530.0\n",
       "c++          684210.0\n",
       "delphi        46212.0\n",
       "go            47499.0\n",
       "java        1696403.0\n",
       "javascript  2056510.0\n",
       "perl          65286.0\n",
       "php         1361988.0\n",
       "python      1496210.0\n",
       "r            356799.0\n",
       "ruby         214582.0\n",
       "swift        273055.0"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "77cf70d0",
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
