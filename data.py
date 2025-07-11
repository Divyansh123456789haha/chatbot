
import cloudinary
import cloudinary.uploader
import psycopg2

# 1. Configure Cloudinary
cloudinary.config(
  cloud_name='dao25x730',
  api_key='664614224452613',
  api_secret='rtWKNfYgFwdn3ooBTafTTbTqumQ'
)

# 2. Upload the image
result = cloudinary.uploader.upload("D:\coding\chatbot\frontend\1.png",)
image_url = result['IMAGE1']  # This is what you will store in PostgreSQL

# 3. Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="dcfinal",
    user="postgres",
    password="qwerty123456789",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

# 4. Insert into your table
cur.execute("""
    INSERT INTO tshirts (name, fit, available, cost, image_url)
    VALUES (%s, %s, %s, %s, %s)
""", (
    'Skull Tee', 'STREET STYLE', True, 1599.00, image_url
))

conn.commit()
cur.close()
conn.close()

print("Image uploaded and saved to DB:", image_url)
