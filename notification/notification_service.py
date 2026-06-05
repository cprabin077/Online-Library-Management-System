from notification.models import Notification


class NotificationService:
    # 🔔 Generic method (CORE REUSABLE FUNCTION)
    @staticmethod
    def create_notification(user, title, message, type):
        return Notification.objects.create(
            user=user,
            title=title,
            message=message,
            type=type
        )

    # 📚 BOOK BORROWED
    @staticmethod
    def book_borrowed(user, book):
        return NotificationService.create_notification(
            user=user,
            title="Book Borrowed",
            message=f"You have borrowed '{book.title}'",
            type="borrow"
        )

    # 📖 BOOK RETURNED
    @staticmethod
    def book_returned(user, book):
        return NotificationService.create_notification(
            user=user,
            title="Book Returned",
            message=f"You have returned '{book.title}'",
            type="return"
        )

    # ⛔ OVERDUE
    @staticmethod
    def book_overdue(user, book):
        return NotificationService.create_notification(
            user=user,
            title="Book Overdue",
            message=f"'{book.title}' is overdue. Please return it.",
            type="overdue"
        )

    # 📌 RESERVATION CONFIRMED
    @staticmethod
    def reservation_confirmed(user, book):
        return NotificationService.create_notification(
            user=user,
            title="Reservation Confirmed",
            message=f"You reserved '{book.title}'",
            type="reservation"
        )

    # 📚 NEW BOOK ADDED
    @staticmethod
    def new_book_added(user, book):
        return NotificationService.create_notification(
            user=user,
            title="New Book Added",
            message=f"New book '{book.title}' is now available",
            type="new_book"
        )

    # 📢 ANNOUNCEMENT
    @staticmethod
    def announcement(user, title):
        return NotificationService.create_notification(
            user=user,
            title="Announcement",
            message=title,
            type="announcement"
        )

    # 💰 FINE APPLIED
    @staticmethod
    def fine_applied(user, amount):
        return NotificationService.create_notification(
            user=user,
            title="Fine Applied",
            message=f"A fine of Rs. {amount} has been applied.",
            type="fine"
        )

    # 💳 PAYMENT SUCCESS
    @staticmethod
    def payment_success(user, amount):
        return NotificationService.create_notification(
            user=user,
            title="Payment Successful",
            message=f"Payment of Rs. {amount} successful.",
            type="payment_success"
        )

    # ❌ PAYMENT FAILED
    @staticmethod
    def payment_failed(user, amount):
        return NotificationService.create_notification(
            user=user,
            title="Payment Failed",
            message=f"Payment of Rs. {amount} failed.",
            type="payment_failed"
        )