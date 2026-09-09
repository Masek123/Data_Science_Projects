import ast

def parse_names(text):
    try:
        items = ast.literal_eval(text)
        return [item['name'] for item in items]
    except (ValueError, SyntaxError, TypeError):
        return []

def load_clean_data(path='movies_clean.csv'):
    import pandas as pd
    df = pd.read_csv(path)
    for col in ['genres_list', 'keywords_list', 'cast_list']:
        df[col] = df[col].apply(ast.literal_eval)
    return df