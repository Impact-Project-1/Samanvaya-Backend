# Endpoint Documentation (Summary)

Describes the expected payloads, return statuses and reposponses from each endpoint, with their corresponding methods and header parameters.

Sorted by category,

All requests are accompanied by the required identification through the tokens(Authentication Bearer Token). And routes return data based on two roles, namely the customer and vendor.

## Authentication

Purpose: Handle authentication and authorization related proceccesses and token related operations
Prefix: /auth

1. POST /login
Payload: consist of the username(email/phone) and the password, any extra fields are ignored.
Response:
- token string [String]
- status code [Integer]
- error message [String]
- success status [Bool]

2. POST /register
Payload: Consists of username(email or phone or both), role(customer/vendor/admin), password, confirm password, additional fields will be ignored.
Reponse:
- token string [String]
- status code [Integer]
- error message [String]
- success status [Bool]

## Token Structure and Specifications

Token String conststs of the following parameters embedded in it.
- role [customer/vendor]
- verfied [Bool]
- uuid [UUID]

## Customer

Purpose: Handle customer operations including the chat initiation by the customer to the vendor, vendor querying and transaction processing, chat actions etc.
Prefix: /cust

1. POST /query
Purpose: When the customer wants to initiate a chat with a vendor or do some query with a selected vendor.
Payload: Vendor identification details, the query text content(the query text)
Reponse: The payload initiates a chat with the particular vendor and return the chat identification string, which then can be used with conncurrent chat based operations.

2. GET /chats
Purpose: View past conversations and transaction history with vendors.
Payload: None
Reponse: List of chat identification (chat_ids)

3. GET /me
Purpose: View the customer's profile and past interactions
Payload: None
Response: JSON object with customer profile and past interactions with vendors(chats and transactions)

4. UPDATE /me
Purpose: Update customer profile
Payload: Profile details schema
Response: Acknowledgement with message and status code

## Transactions

Purpose: Handle user transactions in the platform and deduct a fee for it to the platform.
Prefix: /pay

## Vendor

Purpose: Handle vendor operations including chat query insepction, query reply and chat initialisation and vendor specific business actions.

1. 

## Chat

Purpose: Handle chat and user to user (both customer-vendor and vendor-vendor) interactions.
Prefix: /chat

1. POST /chats/{chat_id}/send
Purpose: Send a message to the vendor
Payload: Message content
Response: An acknowledgement

2. GET /chats/{chat_id}
Purpose: Retrieve messages in the chat.
Payload: Msg offset marked by date and limit marked by date, (date range)
Reponse: array of Json time tagged message strings, with additional metadata for each msg

## Admin

Purpose: Handle admin operations including user management, vendor management, transaction management, chat management, category management, price range management, rating management, review management, tag management, transaction management, user management, vendor management, chat management, category management, price range management, rating management, review management, tag management


## Review

Purpose: Handle review and rating operations of vendors, here the data is manpipulated by the customer and only viewed by the vendor.
Prefix: /rev

1. 

## Images

Purpose: Handle image upload for any kind of purposes, including vendor image showcasing(business), profile picture settings, profile picture viewing, secure transaction of user verfification details.
Prefix: /img

1. POST /profile
Purpose: upload profile picture
Payload: Multipart form data, prossibly in jpeg fromat (or jpg)
Response: Acknowledgement with message and status code and url

2. POST /secure
Purpose: Upload verfication details, secure endpoint.
Payload: Multipart form data, prossibly in jpeg fromat (or jpg), contains user verification details
Response: Acknowledgement with message and status code and url, with pending verification status

3. GET /verify-status
Purpose: Get user verification status
Payload: The particular user's identification
Response: Verification status with message and status code, status could be pending/verified/not-verified (pending only if the system has started processing it and is awaiting result)

4. GET /profile
Purpose: Get user's profile picture
Payload: The particular user's identification
Response: User profile picture with message and status code

5. POST /vendor
Purpose: For vendors to upload business showcase images
Payload: Multipart form data, prossibly in jpeg fromat (or jpg), contains vendor business showcase images
Response: Acknowlegement with message and status code and url

6. GET /vendor
Purpose: Get vendor business showcase images
Payload: The particular vendor's identification
Response: Array of image json, with urls and alt texts

7. POST /review
Purpose: Upload images for feedbacks and reviews
Payload: Multipart form data, possibly in jpeg format(or jpg), contains the feedback image, for feedback, along with the review id.
Response: Acknowledge and return the url.

8. GET /review
Purpose: Get the image when inspecting feedback and reviews.
Payload: The review id
Response: the image url and acknowledgement, multipart form data

## 