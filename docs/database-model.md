# Samanvaya Database Model

## Overview

The Samanvaya database is designed to support an event-services marketplace platform connecting customers with vendors such as photographers, decorators, caterers, and venues.

---

# Entity Relationship Overview

## Core Tables

- users
- vendors
- categories
- vendor_categories
- vendor_images
- reviews

---

# 1. Users Table

## Purpose

Stores application users including customers and vendors.

## Table Name

```sql
users
```

## Fields

| Field | Type | Description |
|---|---|---|
| id | UUID | Primary key linked with `auth.users.id` |
| name | TEXT | Full name of the user |
| email | TEXT | User email address |
| role | TEXT | User role (`customer` or `vendor`) |
| created_at | TIMESTAMP | Account creation timestamp |

## Relationships

- One user can own one vendor profile
- One user can write multiple reviews

---

# 2. Vendors Table

## Purpose

Stores vendor business profile information.

## Table Name

```sql
vendors
```

## Fields

| Field | Type | Description |
|---|---|---|
| vendor_id | UUID | Primary key |
| business_name | TEXT | Vendor business name |
| about | TEXT | Vendor/business description |
| city | TEXT | Vendor city |
| state | TEXT | Vendor state |
| phone | TEXT | Contact number |
| whatsapp | TEXT | WhatsApp contact |
| website | TEXT | Vendor website |
| price_range_high | INT4 | Maximum service price |
| price_range_low | INT4 | Minimum service price |
| verified | BOOLEAN | Vendor verification status |
| created_at | TIMESTAMP | Profile creation timestamp |
| rating_avg | FLOAT4 | Average vendor rating |
| rating_count | INT4 | Total review count |
| links | TEXT[] | Social media or external links |

## Relationships

- Belongs to one user
- Has many reviews
- Has many images
- Belongs to many categories

---

# 3. Categories Table

## Purpose

Stores available event service categories.

## Table Name

```sql
categories
```

## Fields

| Field | Type | Description |
|---|---|---|
| category_id | INT4 | Primary key |
| name | TEXT | Category name |
| slug | TEXT | URL-friendly category identifier |

## Example Categories

- Photography
- Catering
- Decoration
- Makeup
- Venue
- DJ Services

## Relationships

- Connected to vendors through `vendor_categories`

---

# 4. Vendor Categories Table

## Purpose

Acts as a junction table for the many-to-many relationship between vendors and categories.

## Table Name

```sql
vendor_categories
```

## Fields

| Field | Type | Description |
|---|---|---|
| vendor_id | UUID | Linked vendor |
| category_id | INT4 | Linked category |

## Relationships

- Many vendors can belong to many categories
- Connects `vendors` and `categories`

---

# 5. Vendor Images Table

## Purpose

Stores vendor portfolio and gallery images.

## Table Name

```sql
vendor_images
```

## Fields

| Field | Type | Description |
|---|---|---|
| vendor_id | UUID | Linked vendor |
| image_url | TEXT | Vendor image URL |

## Relationships

- One vendor can have multiple images

---

# 6. Reviews Table

## Purpose

Stores customer reviews and ratings for vendors.

## Table Name

```sql
reviews
```

## Fields

| Field | Type | Description |
|---|---|---|
| vendor_id | UUID | Reviewed vendor |
| user_id | UUID | User who submitted review |
| rating | INT4 | Rating value |
| comment | TEXT | Review content |
| created_at | TIMESTAMP | Review creation timestamp |

## Relationships

- One vendor can have multiple reviews
- One user can submit multiple reviews

---

# Relationship Summary

| Relationship | Type |
|---|---|
| User → Vendor | One-to-One |
| Vendor → Reviews | One-to-Many |
| Vendor → Images | One-to-Many |
| Vendor ↔ Categories | Many-to-Many |
| User → Reviews | One-to-Many |

---

# Constraints & Rules

## Users
- `email` should be unique
- `role` should contain valid user roles

## Vendors
- `verified` defaults to `false`
- `rating_avg` is calculated from reviews
- `rating_count` stores total number of reviews

## Reviews
- `rating` should be between 1 and 5

## Vendor Categories
- Prevent duplicate vendor-category mappings

---
