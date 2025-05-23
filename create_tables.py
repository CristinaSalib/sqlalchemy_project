from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

class Supplier(Base):
    __tablename__ = 'suppliers'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    phone = Column(String(20))
    email = Column(String(50))
    address = Column(String(100))

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    description = Column(String(200))
    price = Column(Integer)
    supplier_id = Column(Integer, ForeignKey('suppliers.id'))
    
    # Product and Supplier relationship

    supplier = relationship("Supplier")

# Create db and tables

engine = create_engine('sqlite:///inventory.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# insert data to Supplier

suppliers = [
    Supplier(name="Supplier A", phone="12345678", email="contact@a.com", address="Address A"),
    Supplier(name="Supplier B", phone="87654321", email="contact@b.com", address="Address B"),
    Supplier(name="Supplier C", phone="12348765", email="contact@c.com", address="Address C"),
    Supplier(name="Supplier D", phone="56781234", email="contact@d.com", address="Address D"),
    Supplier(name="Supplier E", phone="43217865", email="contact@e.com", address="Address E"),
    Supplier(name="Supplier F", phone="55512345", email="contact@f.com", address="Address F"),
    Supplier(name="Supplier G", phone="66623456", email="contact@g.com", address="Address G"),
    Supplier(name="Supplier H", phone="77734567", email="contact@h.com", address="Address H"),
    Supplier(name="Supplier I", phone="88845678", email="contact@i.com", address="Address I"),
    Supplier(name="Supplier J", phone="99956789", email="contact@j.com", address="Address J")
]

session.add_all(suppliers)
session.commit()

# insert data to products

products = [
    Product(name="Product 1",  description="Description of Product 1",  price=100,  supplier_id=1),
    Product(name="Product 2",  description="Description of Product 2",  price=200,  supplier_id=2),
    Product(name="Product 3",  description="Description of Product 3",  price=300,  supplier_id=3),
    Product(name="Product 4",  description="Description of Product 4",  price=400,  supplier_id=4),
    Product(name="Product 5",  description="Description of Product 5",  price=500,  supplier_id=5),
    Product(name="Product 6",  description="Description of Product 6",  price=600,  supplier_id=6),
    Product(name="Product 7",  description="Description of Product 7",  price=700,  supplier_id=7),
    Product(name="Product 8",  description="Description of Product 8",  price=800,  supplier_id=8),
    Product(name="Product 9",  description="Description of Product 9",  price=900,  supplier_id=9),
    Product(name="Product 10", description="Description of Product 10", price=1000, supplier_id=10),
    Product(name="Product 11", description="Description of Product 11", price=1100, supplier_id=1),
    Product(name="Product 12", description="Description of Product 12", price=1200, supplier_id=2),
    Product(name="Product 13", description="Description of Product 13", price=1300, supplier_id=3),
    Product(name="Product 14", description="Description of Product 14", price=1400, supplier_id=4),
    Product(name="Product 15", description="Description of Product 15", price=1500, supplier_id=5),
    Product(name="Product 16", description="Description of Product 16", price=1600, supplier_id=6),
    Product(name="Product 17", description="Description of Product 17", price=1700, supplier_id=7),
    Product(name="Product 18", description="Description of Product 18", price=1800, supplier_id=8),
    Product(name="Product 19", description="Description of Product 19", price=1900, supplier_id=9),
    Product(name="Product 20", description="Description of Product 20", price=2000, supplier_id=10),
]

session.add_all(products)
session.commit()

