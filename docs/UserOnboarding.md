# Introduction

Project Prototype - Low Fidelity

Project Name: Samanvaya
Maintainers: 
Version: 0.1.0
Last Revision: 29 June 2026

# Authentication

The user may login or register and be redirected to the login page, from where the authentication phase of completed and the user moves on to the dashboard or the next page depending on context.

The retreived token is stored at the user and and is included with every request subsequent to the registration/login.

If the requests are not accompanied by an authorization header, the request should only return Not Authorized.

The type of user shall be inferred from the login site itself, possibly within the login modal, by using the field such as 'Im looking to provide service' or 'Im seeking service'

# Profile

Upon login/ navigating to the dashboard, a request to fetch the profile data will be propagated from the user side and this verifies that the user has completed the profile or not. If the profile has not been completed, redirect the user to the profile page. In case the profile is completed, the user is redirected to the dashboard.

# Profile Types

Based on the user type the profile completion modals(or pages) are displayed.
The defined user types are customer and vendor.

## Customer

Customer is the one who is seeking service from the platform and aims to contact with vendors, or is just a user of the platform. There are no additional fields to be filled in case of a customer.

In addition, the details such as phone number and email id are to be received from the user inorder to check the legitimacy of the user and to reduce spams and unneccessary incidents. 

And keeping contact and connection in view, the user AKA customer is also liable to provide the platform with any kind of id proof or something that can be held credible against the customer in case of fraud or mischief. 

only then the customer gets the verified status and only those customers shall have a verfied badge in their profile or contact. and that badge should be visible for the vendors.

Customer to customer interaction and enumeration is strictly prohibited and should not be implemented in the platform.

Customer can initiate and close communication with a vendor.

## Vendor

Vendor is the one who aims to provide service or seeks customers to the services they provide.
Additional information required to verify the service provider's legitiacy should be received from the user and it should be verfieid internally and set verified status to the vendor.

Keeping the business view, considering there may be organisers, vendor to vendor communication is enabled. 

Vendors shall be able to contact with customers who initiated the communication with them, and only be allowed in that context, no vendor can initiate a chat or any form of communication through the platform unless initiated by the customer.

Vendors can view past customers and can view details of the transaction, both financial and conversational.

Even if communication initiated by customer, after the transaction has been closed at the customer end, the vendor should not be able to communcate with the customer.

<!-- Further negotiable on how to handle situation where payments and spams are handled -->
