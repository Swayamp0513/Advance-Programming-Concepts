from books.catalog import get_book_title
from members.member_info import get_member
from transactions.checkout import issue_book

print(get_book_title("BK100"))
print(get_member("MEM01"))
print(issue_book("BK100", "MEM01"))
