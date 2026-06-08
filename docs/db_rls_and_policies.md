# Row Level Security (RLS) Policies Documentation

## Overview

Row Level Security (RLS) has been implemented in the Samanvaya backend database using Supabase PostgreSQL policies.

The purpose of RLS is to:
- Secure sensitive user data
- Restrict unauthorized access
- Ensure users can only modify their own resources
- Allow public access to non-sensitive marketplace data

---

# RLS Strategy

The following access model is used:

| Resource Type | Access Level |
|---|---|
| User Profiles | Owner Only |
| Vendor Profiles | Public Read, Owner Write |
| Categories | Public Read |
| Vendor Images | Public Read, Owner Manage |
| Reviews | Public Read, Owner Manage |

---

# 1. Users Table Policies

## Purpose
Restricts users to accessing and modifying only their own account information.

---

## Read Own Profile

```sql
CREATE POLICY "Users can read own profile"
ON public.users
FOR SELECT
USING (auth.uid() = id);
```

### Description
Allows authenticated users to view only their own profile data.

---

## Update Own Profile

```sql
CREATE POLICY "Users can update own profile"
ON public.users
FOR UPDATE
USING (auth.uid() = id);
```

### Description
Allows users to update only their own profile information.

---

# 2. Vendors Table Policies

## Purpose
Allows public viewing of vendor profiles while restricting modifications to the vendor owner.

---

## Public Vendor Viewing

```sql
CREATE POLICY "Public can view vendors"
ON vendors
FOR SELECT
USING (true);
```

### Description
Allows anyone to browse vendor profiles publicly.

---

## Vendor Profile Creation

```sql
CREATE POLICY "User can create vendor profile"
ON vendors
FOR INSERT
WITH CHECK (auth.uid() = user_id);
```

### Description
Allows authenticated users to create vendor profiles linked to their own account.

---

## Vendor Profile Update

```sql
CREATE POLICY "Vendor owner can update profile"
ON vendors
FOR UPDATE
USING (auth.uid() = user_id);
```

### Description
Restricts vendor profile editing to the profile owner.

---

## Vendor Profile Deletion

```sql
CREATE POLICY "Vendor owner can delete profile"
ON vendors
FOR DELETE
USING (auth.uid() = user_id);
```

### Description
Allows only the vendor owner to delete their vendor profile.

---

# 3. Categories Table Policies

## Purpose
Allows public access to vendor service categories.

---

## Public Category Viewing
```sql
CREATE POLICY "Public can view categories"
ON categories
FOR SELECT
USING (true);
```

### Description
Allows all users to view service categories publicly.

---

# 4. Vendor Categories Table Policies

## Purpose
Controls vendor-category relationships while allowing public viewing.

---

## Public Read Access

```sql
CREATE POLICY "Public read vendor categories"
ON vendor_categories
FOR SELECT
USING (true);
```

### Description
Allows public viewing of vendor-category mappings.

---

## Vendor Category Management

```sql
CREATE POLICY "Vendor owner manages categories"
ON vendor_categories
FOR ALL
USING (
    EXISTS (
        SELECT 1 FROM vendors
        WHERE vendors.id = vendor_categories.vendor_id
        AND vendors.user_id = auth.uid()
    )
);
```

### Description
Allows vendors to manage category mappings only for their own vendor profile.

---

# 5. Vendor Images Table Policies

## Purpose
Allows public viewing of vendor portfolio images while restricting image management to vendor owners.

---

## Public Image Viewing

```sql
CREATE POLICY "Public read vendor images"
ON vendor_images
FOR SELECT
USING (true);
```

### Description
Allows public access to vendor portfolio images.

---

## Vendor Image Management

```sql
CREATE POLICY "Vendor owner manages images"
ON vendor_images
FOR ALL
USING (
    EXISTS (
        SELECT 1 FROM vendors
        WHERE vendors.id = vendor_images.vendor_id
        AND vendors.user_id = auth.uid()
    )
);
```

### Description
Restricts image upload, update, and deletion to the vendor owner.

---

# 6. Reviews Table Policies

## Purpose
Allows public viewing of reviews while ensuring users can manage only their own reviews.

---

## Public Review Viewing

```sql
CREATE POLICY "Public read reviews"
ON reviews
FOR SELECT
USING (true);
```

### Description
Allows all users to read vendor reviews publicly.

---

## Review Creation

```sql
CREATE POLICY "Users create reviews"
ON reviews
FOR INSERT
WITH CHECK (auth.uid() = user_id);
```

### Description
Allows authenticated users to create reviews using their own user ID.

---

## Review Update

```sql
CREATE POLICY "Users update own review"
ON reviews
FOR UPDATE
USING (auth.uid() = user_id);
```

### Description
Restricts review editing to the review owner.

---

## Review Deletion

```sql
CREATE POLICY "Users delete own review"
ON reviews
FOR DELETE
USING (auth.uid() = user_id);
```

### Description
Restricts review deletion to the review owner.

---

# Security Benefits

The implemented RLS policies provide:

- Secure user-specific data access
- Prevention of unauthorized data modification
- Public marketplace discoverability
- Controlled vendor resource management
- Secure review ownership validation
- Protection against unauthorized access and manipulation

---
