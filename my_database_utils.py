import pandas as pd
from sqlalchemy import create_engine


def get_aw_data(query: str):
    # 注意：URL 里的 mssql+pyodbc 明确告诉了 SQLAlchemy：
    # “请使用 pyodbc 作为底层驱动去连接 SQL Server”
    conn_url = (
        "mssql+pyodbc://@./AdventureWorksDW2020?"
        "driver=ODBC+Driver+18+for+SQL+Server&"
        "trusted_connection=yes&"
        "Encrypt=yes&"
        "TrustServerCertificate=yes"
    )

    try:
        engine = create_engine(conn_url)
        # 现在 Pandas 会非常开心，因为你传给它的是一个标准的 engine 对象
        return pd.read_sql(query, engine)
    except Exception as e:
        print(f"❌ 提取失败: {e}")
        return None
