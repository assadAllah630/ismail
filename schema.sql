CREATE TABLE categories (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE tags (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name_ar VARCHAR(255) NOT NULL,
    name_en VARCHAR(255) NOT NULL,
    item_uid VARCHAR(255) NOT NULL,
    item_code VARCHAR(255) NOT NULL,
    category_id INT NOT NULL,
    short_description TEXT,
    total_cost DECIMAL(10,2) NOT NULL,
    barcode VARCHAR(255),
    quantity INT NOT NULL,
    inventory_location VARCHAR(255) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    cost DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (category_id) REFERENCES categories(id)
);

CREATE TABLE product_tags (
    product_id INT NOT NULL,
    tag_id INT NOT NULL,
    PRIMARY KEY (product_id, tag_id),
    FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE,
    FOREIGN KEY (tag_id) REFERENCES tags(id) ON DELETE CASCADE
);

CREATE TABLE product_photos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT NOT NULL,
    photo_url VARCHAR(512) NOT NULL,
    uploaded_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE
);

CREATE TABLE media (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    media_type ENUM('post', 'reel', 'story') NOT NULL,
    description TEXT,
    file_url VARCHAR(512) NOT NULL,
    upload_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    published BOOLEAN DEFAULT FALSE
);

CREATE TABLE product_media (
    product_id INT NOT NULL,
    media_id INT NOT NULL,
    PRIMARY KEY (product_id, media_id),
    FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE,
    FOREIGN KEY (media_id) REFERENCES media(id) ON DELETE CASCADE
); 