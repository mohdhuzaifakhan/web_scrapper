{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 81,
   "id": "d8b73317",
   "metadata": {},
   "outputs": [],
   "source": [
    "import requests\n",
    "from bs4 import BeautifulSoup\n",
    "url = \"https://github.com/topics\"\n",
    "\n",
    "page_content = requests.get(url)\n",
    "page = BeautifulSoup(page_content.content,\"html.parser\")\n",
    "# print(page.prettify())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "274142c0",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "id": "afae5be2",
   "metadata": {},
   "outputs": [],
   "source": [
    "All_featured = []\n",
    "list_of_all_features = page.find_all('div',attrs={'class':'py-4 border-bottom d-flex flex-justify-between'})\n",
    "# print(list_of_all_features)\n",
    "# print(list_of_all_features[0].find_all('a',attrs={'class':'no-underline flex-grow-0'})[0][\"href\"])\n",
    "# print(list_of_all_features[0].find_all('p',attrs={'class':'f3 lh-condensed mb-0 mt-1 Link--primary'})[0].text)\n",
    "# print(list_of_all_features[0].find_all('p',attrs={'class':'f5 color-fg-muted mb-0 mt-1'})[0].text)\n",
    "for i in range(len(list_of_all_features)):\n",
    "    dic={}\n",
    "    dic[\"topic_name\"] = list_of_all_features[i].find_all('p',attrs={'class':'f3 lh-condensed mb-0 mt-1 Link--primary'})[0].text\n",
    "    dic[\"topic_description\"] = list_of_all_features[i].find_all('p',attrs={'class':'f5 color-fg-muted mb-0 mt-1'})[0].text\n",
    "    topic_url = \"https://github.com\" + list_of_all_features[0].find_all('a',attrs={'class':'no-underline flex-grow-0'})[0][\"href\"]\n",
    "    dic[\"topic_url\"] = topic_url\n",
    "    All_featured.append(dic)\n",
    "\n",
    "# print((All_featured))\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "id": "0fb349f3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "CSV file created successfully!\n"
     ]
    }
   ],
   "source": [
    "import csv\n",
    "filename = \"github_topics.csv\"\n",
    "\n",
    "# Define the fieldnames for the CSV header\n",
    "fieldnames = ['topic_name', 'topic_description', 'topic_url']\n",
    "\n",
    "# Write data to the CSV file\n",
    "with open(filename, 'w', newline='',encoding='utf-8') as csvfile:\n",
    "    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)\n",
    "\n",
    "    # Write the header\n",
    "    writer.writeheader()\n",
    "\n",
    "    # Write data rows\n",
    "    for item in All_featured:\n",
    "        writer.writerow(item)\n",
    "\n",
    "print(\"CSV file created successfully!\")\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "23c4b771",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "id": "e76689f7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[]\n"
     ]
    }
   ],
   "source": [
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "83c7099e",
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
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
