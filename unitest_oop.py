import unittest

from oop import Customer, Hotel, Room, RoomType

class TestHotelSystem(unittest.TestCase):

    def setUp(self):
        # სატესტო გარემოს მომზადება ყოველი ტესტის წინ
        self.room1 = Room(101, RoomType.SINGLE, 100.0, True, 1)
        self.room2 = Room(102, RoomType.DOUBLE, 150.0, False, 2)  # წინასწარ დაკავებული
        self.hotel = Hotel("Sheraton", [self.room1, self.room2])
        self.customer = Customer("გიორგი", 500.0)

    def test_pay_for_booking_success(self):
        # ტესტი 1: წარმატებული გადახდა
        initial_budget = self.customer.budget
        total_price = 200.0
        
        success = self.customer.pay_for_booking(total_price)
        
        self.assertTrue(success)
        self.assertEqual(self.customer.budget, initial_budget - total_price)
        self.assertEqual(self.customer.reward_points, 20)  # 200 / 10 = 20 ქულა

    def test_pay_for_booking_insufficient_budget(self):
        # ტესტი 2: გადახდა როცა ფული არ გვყოფნის
        success = self.customer.pay_for_booking(1000.0)
        
        self.assertFalse(success)
        self.assertEqual(self.customer.budget, 500.0)  # ბიუჯეტი არ შეცვლილა
        self.assertEqual(self.customer.reward_points, 0)

    def test_book_free_room_success(self):
        # ტესტი 3: თავისუფალი ოთახის წარმატებული დაჯავშნა
        success = self.hotel.book_room_for_customer(self.customer, 101, nights=2) # ფასი: 200₾
        
        self.assertTrue(success)
        self.assertFalse(self.room1.is_available)  # ოთახი დაკავდა
        self.assertIn(self.room1, self.customer.booked_rooms)  # დაემატა მომხმარებლის სიას
        self.assertEqual(self.customer.budget, 300.0)  # 500 - 200 = 300

    def test_book_already_occupied_room(self):
        # ტესტი 4: დაკავებული ოთახის დაჯავშნის მცდელობა
        success = self.hotel.book_room_for_customer(self.customer, 102, nights=1)
        
        self.assertFalse(success)
        self.assertEqual(self.customer.budget, 500.0)  # ფული არ ჩამოჭრილა

if __name__ == "__main__":
    unittest.main()