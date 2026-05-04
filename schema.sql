CREATE TABLE IF NOT EXISTS listings (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    price NUMERIC NOT NULL,
    location TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT NOW()
);
