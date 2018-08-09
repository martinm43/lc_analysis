CREATE VIRTUAL TABLE IF NOT EXISTS ftsproducts using fts3(entry_id,name);
INSERT INTO ftsproducts SELECT id, name FROM products;
