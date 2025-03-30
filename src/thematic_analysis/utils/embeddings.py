from typing import Union

import polars as pl

from thematic_analysis.llm import get_embeddings


async def embed_column(
    df: pl.DataFrame, column_name: str, embedding_col_name: Union[str, None] = None
) -> pl.DataFrame:
    """
    Add an embedding column to a DataFrame for a given column.
    """
    embedding_col_name = embedding_col_name or f"{column_name}_embedding"
    data = df[column_name].to_list()
    embeddings = await get_embeddings(data)
    return df.with_columns(pl.Series(name=embedding_col_name, values=embeddings))
