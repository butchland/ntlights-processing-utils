# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/05_build_itemdb.ipynb.

# %% auto 0
__all__ = ['DATA_DB_DIR', 'DB']

# %% ../nbs/05_build_itemdb.ipynb 4
import sqlite3 as sql
import ntlights_processing_utils.explore_ntlights_stac as ntls

# %% ../nbs/05_build_itemdb.ipynb 5
DATA_DB_DIR = '../data/sqlite'
DB = f'{DATA_DB_DIR}/db.db'