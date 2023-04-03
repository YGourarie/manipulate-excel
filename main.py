import pandas as pd
import numpy as np
import openai
from io import StringIO
import os
from dotenv import load_dotenv

def configure():
    load_dotenv()


def generate_prompt(og_data):
    print(og_data)
    commands = input('Commands: ')
    return """ 
        I will give you a DataFrame and some manipulation commands.
        You will return the manipulated data in csv format with absolutely nothing
        else, no explanations - nothing. For example - 
        DataFrame:    Name  Age  Gender
                    0   John   24    Male
                    1   Emma   27  Female
                    2  James   22    Male
                    3  Emily   31  Female
        Commands: Delete column "Age"
        Output: Name,Gender
                John,Male
                Emma,Female
                James,Male
                Emily,Female
        DataFrame: {og_data}
        Commands: {commands}
        Output:
        
    """.format(og_data=og_data,commands= commands)


def write_to_excel(df):
    print(df)

    choice = input('Write this DataFrame to file? (y/n)')

    if choice.lower().startswith('y'):
        writer = pd.ExcelWriter('data.xlsx', engine='openpyxl', mode='w')
        df.to_excel(writer, sheet_name='Sheet1', index=False, header=True)
        writer.save()


def main():
    configure()
    openai.api_key = os.getenv('API_KEY')

    og_data = pd.read_excel('data.xlsx',sheet_name="Sheet1")

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=generate_prompt(og_data),
        temperature=0,
        max_tokens=3000,
        top_p=1.0,
        frequency_penalty=0.2,
        presence_penalty=0.0,
    )

    df = pd.read_csv(StringIO(response.choices[0].text))
    write_to_excel(df)

main()