### PROCESS GUIDE FOR BUILDING OUR APPLICATION
At the high level, the design is divided into three flows: product digital sales and stock management
• Product Digital Sales : Vendors upload the product they have for sale and these products will be available for individudals to purchase
. Stock Management


- #### What specific features are we going to build?
Vendor Features
- Vendors can upload products images and description etc
- Admin Features to track customer's order and export features etc
- Track customer order shipping process

Individual Features

- Shopping Cart Features
- Tracking Customer Orders
- Background task for sending emails to users with Invoice details
- Payment Options 
- Add Coupon features
- Serve multiple users from different countries and languages
- Add Recommendation with smart Machine learning models and optimized formulas


Inventory Management Features
- Demand Forcasting using smart Machine learning models , helps the vendors not to overstock or   understock
- Product Analytics - Check top performing products and inform vendors on better product stocking
- Product Tracking, track products with closer expiry products
- Inventory Alerting - Alert vendors on products with small safety stock
- Give vendors option to add different users with seperate roles for inventory management action
- Barcoding and Tagging



• How many users does the product have?
The product should be able to serve multiple users such as 1000 vendors and 10,000 customers looking to buy product from the application.

• How fast does the company anticipate to scale up? What are the anticipated scales in 3
months, 6 months, and a year?
We intend to take 50 vendors in first 3 months, and more in upcoming months.

• What is the company’s technology stack? What existing services you might leverage to
simplify the design?
We are going to use Flask for the backend and React for frontend
#### Why Flask
- With Flask, our simple application can be later changed to add more functionality and make it complex. It provides flexibility to expand the application quickly.