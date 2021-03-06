from db import db

def get_all_hotels():
    sql = """SELECT id, hotel_name
             FROM hotels"""

    return db.session.execute(sql).fetchall()

def get_hotels_by_owner_id(owner_id):
    sql = """SELECT id, hotel_name
             FROM hotels 
             where owner_id = :owner_id"""
    return db.session.execute(sql, {"owner_id": owner_id}).fetchall()

def get_all_amenities_by_hotel_id(hotel_id):
    sql = """SELECT id, hotel_name
             FROM hotels 
             WHERE id= :hotel_id"""

    return db.session.execute(sql, {"hotel_id": hotel_id}).fetchone()

def get_hotel_information(hotel_id):
    sql = """SELECT id, hotel_name, hotel_address, stars
             FROM hotels WHERE id= :hotel_id"""

    return db.session.execute(sql, {"hotel_id": hotel_id}).fetchone()

def get_amenities(hotel_id):
    sql = """SELECT DISTINCT amenity
             FROM amenities 
             WHERE hotel_id= :hotel_id"""
    return db.session.execute(sql, {"hotel_id": hotel_id}).fetchall()

def get_all_hotel_names():
    sql = """SELECT hotel_name
             FROM hotels"""
    return [name[0] for name in db.session.execute(sql).fetchall()]

def get_all_room_names_by_hotel_id(hotel_id):
    sql = """SELECT rooms
             FROM rooms 
             where hotel_id = :hotel_id"""
    return [name[0] for name in db.session.execute(sql, {"hotel_id": hotel_id}).fetchall()]

def add_hotel(hotel_name, hotel_address, stars, owner_id):
    sql = """INSERT INTO hotels (hotel_name, hotel_address, stars, owner_id)
             VALUES (:hotel_name, :hotel_address, :stars, :owner_id)"""
    db.session.execute(sql, {"hotel_name":hotel_name,
                             "hotel_address": hotel_address,
                             "stars":stars,
                             "owner_id":owner_id})
    db.session.commit()

def add_amenity(amenities, hotel_id):
    for amenity in amenities:
        sql = """INSERT INTO amenities (hotel_id, amenity)
                 VALUES (:hotel_id, :amenity)"""
        db.session.execute(sql, {"hotel_id":hotel_id, "amenity": amenity})
        db.session.commit()

def get_room_guest_number(room_id):
    sql = """SELECT number_of_rooms
             FROM rooms 
             WHERE id= :room_id"""
    return db.session.execute(sql, {"room_id": room_id}).fetchone()

def add_room(hotel_id, room_description, guests, square_meters, number_of_rooms, price):
    sql = """INSERT INTO rooms (hotel_id, room_description,
             guests, square_meters, number_of_rooms, price)
             VALUES (:hotel_id, :room_description, :guests,
             :square_meters, :number_of_rooms, :price)"""
    db.session.execute(sql, {"hotel_id":hotel_id,
                             "room_description": room_description,
                             "guests":guests,
                             "square_meters":square_meters,
                             "number_of_rooms": number_of_rooms,
                             "price":price})
    db.session.commit()


def get_rooms(hotel_id):
    sql = """SELECT id, hotel_id, room_description, guests, square_meters, number_of_rooms, price
             FROM rooms 
             WHERE hotel_id= :hotel_id"""
    return db.session.execute(sql, {"hotel_id": hotel_id}).fetchall()

def delete_hotel(hotel_id):
    sql = """DELETE FROM hotels where id = :hotel_id"""
    db.session.execute(sql, {"hotel_id" : int(hotel_id)})
    db.session.commit()

def count_rooms_by_hotel_id(hotel_id):
    sql = """SELECT COUNT(id) as count_rooms
             FROM rooms
             where hotel_id = :hotel_id"""
    return db.session.execute(sql, {"hotel_id": hotel_id}).fetchone()[0]

def count_hotels_by_owner_id(owner_id):
    sql = """SELECT COUNT(id) as count_rooms
             FROM hotels
             where owner_id = :owner_id"""
    return db.session.execute(sql, {"owner_id": owner_id}).fetchone()[0]


