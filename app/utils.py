def generate_sample_data():
    import pandas as pd
    import numpy as np
    np.random.seed(42)
    countries = ["USA", "China", "India", "Brazil"]
    years = list(range(2018, 2023))
    data = {
        "country": [c for c in countries for _ in years],
        "year": years * len(countries),
        "sales": np.random.randint(1000, 10000, len(countries) * len(years)),
        "gdp": np.random.randint(1000000, 20000000, len(countries) * len(years)),
        "population": np.random.randint(50000000, 1500000000, len(countries) * len(years))
    }
    df = pd.DataFrame(data)
    df.to_csv("data/sample_sales_data.csv", index=False)