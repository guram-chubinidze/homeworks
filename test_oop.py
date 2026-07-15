import pytest
# დაიმპორტეთ თქვენი ფაილიდან (მაგალითად, თუ კლასები წერია "hotel.py"-ში)
from oop import Customer, Hotel, Room, RoomType 

# Fixture გამოიყენება სატესტო გარემოს მოსამზადებლად (setup-ის ნაცვლად)
@pytest.fixture
def hotel_setup():
    room1 = Room(101, RoomType.SINGLE, 100.0, True, 1)
    room2 = Room(102, RoomType.DOUBLE, 150.0, False, 2)  # დაკავებული
    hotel = Hotel("Sheraton", [room1, room2])
    customer = Customer("გიორგი", 500.0)
    
    # ვაბრუნებთ მომზადებულ ობიექტებს
    return hotel, room1, room2, customer

# 1. ტესტი: წარმატებული გადახდა
def test_pay_for_booking_success(hotel_setup):
    _, _, _, customer = hotel_setup # ვიღებთ მხოლოდ კლიენტს
    
    initial_budget = customer.budget
    total_price = 200.0
    
    success = customer.pay_for_booking(total_price)
    
    assert success is True
    assert customer.budget == initial_budget - total_price
    assert customer.reward_points == 20  # 200 / 10 = 20 ქულა

# 2. ტესტი: არასაკმარისი ბიუჯეტით გადახდა
def test_pay_for_booking_insufficient_budget(hotel_setup):
    _, _, _, customer = hotel_setup
    
    success = customer.pay_for_booking(1000.0)
    
    assert success is False
    assert customer.budget == 500.0
    assert customer.reward_points == 0

# 3. ტესტი: თავისუფალი ოთახის წარმატებული დაჯავშნა
def test_book_free_room_success(hotel_setup):
    hotel, room1, _, customer = hotel_setup
    
    success = hotel.book_room_for_customer(customer, 101, nights=2) # 200₾
    
    assert success is True
    assert room1.is_available is False  # ოთახი უნდა დაიკავოს
    assert room1 in customer.booked_rooms
    assert customer.budget == 300.0  # 500 - 200 = 300

# 4. ტესტი: დაკავებული ოთახის დაჯავშნის მცდელობა
def test_book_already_occupied_room(hotel_setup):
    hotel, _, room2, customer = hotel_setup
    
    success = hotel.book_room_for_customer(customer, 102, nights=1)
    
    assert success is False
    assert room2.is_available is False  # სტატუსი არ უნდა შეიცვალოს
    assert customer.budget == 500.0  # თანხა არ უნდა ჩამოიჭრას