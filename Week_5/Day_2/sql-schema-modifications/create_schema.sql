-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.

-- Modify this code to update the DB schema diagram.
-- To reset the sample schema, replace everything with
-- two dots ('..' - without quotes).

-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.

-- Modify this code to update the DB schema diagram.
-- To reset the sample schema, replace everything with
-- two dots ('..' - without quotes).
-- BlueApron

-- DROP TABLE IF EXISTS "Users" cascade;
-- DROP TABLE IF EXISTS "Deliveries" cascade;
-- DROP TABLE IF EXISTS "Recipes" cascade;
-- DROP TABLE IF EXISTS "Ingredients" cascade;

-- CREATE TABLE "Users" (
--     "id" serial UNIQUE NOT NULL,
--     "password" varchar(255)   NOT NULL,
--     "email" varchar(255)   NOT NULL,
--     "phone" int   NOT NULL,
--     "address" varchar(255) UNIQUE NOT NULL,
--     "payment_info" varchar(255)   NOT NULL,
--     "service_plan" varchar(255) UNIQUE  NOT NULL,
--     CONSTRAINT "pk_Users" PRIMARY KEY (
--         "id"
--      )
-- );

-- CREATE TABLE "Deliveries" (
--     "id" serial   NOT NULL,
--     "user" int UNIQUE  NOT NULL,
--     "service_id" varchar(255)   NOT NULL,
--     "user_address" varchar(255)   NOT NULL,
--     "recipes_id" int UNIQUE NOT NULL,
--     CONSTRAINT "pk_Deliveries" PRIMARY KEY (
--         "id"
--      )
-- );

-- CREATE TABLE "Recipes" (
--     "id" serial   NOT NULL,
--     "ingredient_id" int UNIQUE NOT NULL,
--     CONSTRAINT "pk_Recipes" PRIMARY KEY (
--         "id"
--      )
-- );

-- CREATE TABLE "Ingredients" (
--     "id" serial   NOT NULL,
--     "food_name" varchar(255)   NOT NULL,
--     CONSTRAINT "pk_Ingredients" PRIMARY KEY (
--         "id"
--      )
-- );

-- ALTER TABLE "Deliveries" ADD CONSTRAINT "fk_Deliveries_user_service_id_user_address" FOREIGN KEY("user", "service_id", "user_address")
-- REFERENCES "Users" ("id", "service_plan", "address");

-- ALTER TABLE "Recipes" ADD CONSTRAINT "fk_Recipes_id" FOREIGN KEY("id")
-- REFERENCES "Deliveries" ("recipes_id");

-- ALTER TABLE "Ingredients" ADD CONSTRAINT "fk_Ingredients_id" FOREIGN KEY("id")
-- REFERENCES "Recipes" ("ingredient_id");




-- GrubHub App
-- DROP TABLE IF EXISTS "Users" cascade;
-- DROP TABLE IF EXISTS "Orders" cascade;
-- DROP TABLE IF EXISTS "Restaurants" cascade;
-- DROP TABLE IF EXISTS "Menu_Items" cascade;
-- DROP TABLE IF EXISTS "Shopping_Cart" cascade;



-- CREATE TABLE "Users" (
--     "id" serial   NOT NULL,
--     "email" varchar(255)   NOT NULL,
--     "phone" int   NOT NULL,
--     "password" varchar(255)   NOT NULL,
--     "user_age" int   NOT NULL,
--     "shopping_cart_id" int   NOT NULL,
--     CONSTRAINT "pk_Users" PRIMARY KEY (
--         "id"
--      ),
--     CONSTRAINT "uc_Users_shopping_cart_id" UNIQUE (
--         "shopping_cart_id"
--     )
-- );

-- CREATE TABLE "Orders" (
--     "id" serial   NOT NULL,
--     "user_id" int   NOT NULL,
--     "rest_id" int   NOT NULL,
--     "price" int   NOT NULL,
--     CONSTRAINT "pk_Orders" PRIMARY KEY (
--         "id"
--      )
-- );

-- CREATE TABLE "Restaurants" (
--     "id" serial   NOT NULL,
--     "menu_id" int   NOT NULL,
--     "available" boolean   NOT NULL,
--     "location" varchar(255)   NOT NULL,
--     "phone" int   NOT NULL,
--     CONSTRAINT "pk_Restaurants" PRIMARY KEY (
--         "id"
--      )
-- );

-- CREATE TABLE "Menu_Items" (
--     "id" serial   NOT NULL,
--     "menu_item" varchar(255)   NOT NULL,
--     "food_price" int   NOT NULL,
--     "available" boolean   NOT NULL,
--     "is_alcohol" boolean   NOT NULL,
--     CONSTRAINT "pk_Menu_Items" PRIMARY KEY (
--         "id"
--      )
-- );

-- CREATE TABLE "Shopping_Cart" (
--     "id" serial   NOT NULL,
--     "order_id" int   NOT NULL,
--     "price" int   NOT NULL,
--     CONSTRAINT "pk_Shopping_Cart" PRIMARY KEY (
--         "id"
--      )
-- );

-- ALTER TABLE "Users" ADD CONSTRAINT "fk_Users_shopping_cart_id" FOREIGN KEY("shopping_cart_id")
-- REFERENCES "Shopping_Cart" ("id");

-- ALTER TABLE "Orders" ADD CONSTRAINT "fk_Orders_user_id" FOREIGN KEY("user_id")
-- REFERENCES "Users" ("id");

-- ALTER TABLE "Orders" ADD CONSTRAINT "fk_Orders_rest_id" FOREIGN KEY("rest_id")
-- REFERENCES "Restaurants" ("id");

-- ALTER TABLE "Menu_Items" ADD CONSTRAINT "fk_Menu_Items_id" FOREIGN KEY("id")
-- REFERENCES "Restaurants" ("menu_id");

-- ALTER TABLE "Shopping_Cart" ADD CONSTRAINT "fk_Shopping_Cart_order_id" FOREIGN KEY("order_id")
-- REFERENCES "Orders" ("id");

DROP TABLE IF EXISTS customers CASCADE;
DROP TABLE IF EXISTS bills CASCADE;


CREATE TABLE customers(
    id SERIAL PRIMARY KEY,
    first text,
    last text,
    social varchar(255),
    account_number varchar(255),
    line_1 varchar(255),
    city varchar(255),
    state varchar(255),
    zip varchar(255),
    current_bill_cents integer
);

CREATE TABLE bills(
    id SERIAL PRIMARY KEY,
    customer_id integer,
    gallons_used integer,
    cents_per_gallon integer,
    start_date date,
    end_date date,
    status varchar(255),
    payment_date date,
    due_date date,
    amount_due_cents integer,
    min_amount_due_cents integer
);
-- --1
ALTER TABLE customers RENAME COLUMN first TO first_name;
ALTER TABLE customers RENAME COLUMN last TO last_name;
--2
-- ALTER TABLE customers ALTER COLUMN first_names TYPE varchar(255) USING SUBSTRING(first_names FROM 1 FOR 255);
-- ALTER TABLE customers ALTER COLUMN first_names SET NOT NULL;
-- ALTER TABLE customers ALTER COLUMN first_names TYPE varchar(255);

ALTER TABLE customers ALTER COLUMN first_name TYPE varchar(255);
ALTER TABLE customers ALTER COLUMN last_name TYPE varchar(255);

--3
ALTER TABLE customers ALTER COLUMN social TYPE char(9);
--4
ALTER TABLE customers ALTER COLUMN account_number TYPE char(14);
--5
ALTER TABLE customers ADD COLUMN line_2 varchar(255);
--6
ALTER TABLE customers ALTER COLUMN zip TYPE char(5);
--7
ALTER TABLE customers DROP COLUMN current_bill_cents;

--Statements
--1
ALTER TABLE bills ALTER COLUMN customer_id SET NOT NULL;
--2
ALTER TABLE bills ALTER COLUMN gallons_used TYPE NUMERIC(16,2);
--3
ALTER TABLE bills ALTER status SET DEFAULT 'In Debt LMAO';