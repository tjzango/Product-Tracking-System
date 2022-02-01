# Product-Tracking-System
Uses dimensional barcodes and QR codes for product from 3 using the zbar library to track items of items

Used by busness to keep record of their basic sales and more importantly, provide utitlity for customer to ensure the orginality of their products


***scenario
Mr A sells 100 computer hard drive daily, he testes and verify the usability of each hard drive before processing the order. The issue is Mr received a return order of almost 20 non-working hard drives from his customer. He implied some of his customers are using the opportunity to bring back hard drive other than his. Mr A cannon test all the hard drives in the customers' presence and wishes to use this system to track the unique created ID of each product. 


USAGE:
install requirement
generate secret key
create .env 
configure environment variables

./manage.py makemigrations
./manage.py migrate
./manage.py runserver

