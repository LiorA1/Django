BEGIN;
--
-- Create model Contact
--
CREATE TABLE "contact" 
(	"id" integer NOT NULL PRIMARY KEY,
	"last_name" varchar(15) NOT NULL,
	"first_name" varchar(15) NOT NULL,
	"title" varchar(2) NOT NULL,
	"street" varchar(30) NOT NULL,
	"city" varchar(20) NOT NULL,
	"state" varchar(2) NOT NULL,
	"zip_code" varchar(5) NOT NULL,
	"phone" varchar(10) NOT NULL,
	"fax" varchar(10) NOT NULL);
	
--
-- Create model Customer
--
CREATE TABLE "customer" (
	"id" integer NOT NULL PRIMARY KEY,
	"fname" varchar(15) NOT NULL,
	"lname" varchar(20) NOT NULL,
	"address" varchar(35) NOT NULL,
	"city" varchar(20) NOT NULL,
	"state" varchar(2) NOT NULL,
	"zip_code" varchar(5) NOT NULL,
	"phone" varchar(12) NOT NULL,
	"company_name" varchar(35) NOT NULL);
--
-- Create model Employee
--
CREATE TABLE "employee" (
	"emp_id" integer NOT NULL PRIMARY KEY,
	"manager_id" integer NOT NULL,
	"emp_fname" varchar(20) NOT NULL,
	"emp_lname" varchar(20) NOT NULL,
	"street" varchar(40) NOT NULL,
	"city" varchar(20) NOT NULL,
	"state" varchar(4) NOT NULL,
	"zip_code" varchar(9) NOT NULL,
	"phone" varchar(10) NOT NULL,
	"status" varchar(1) NOT NULL,
	"ss_number" varchar(11) NOT NULL,
	"salary" real NOT NULL,
	"start_date" date NOT NULL,
	"termination_date" date NOT NULL,
	"birth_date" date NOT NULL,
	"bene_health_ins" varchar(1) NOT NULL,
	"bene_life_ins" varchar(1) NOT NULL,
	"bene_day_care" varchar(1) NOT NULL,
	"sex" varchar(1) NOT NULL,
	"dept_id_id" integer NOT NULL REFERENCES "employee" ("emp_id") DEFERRABLE INITIALLY DEFERRED);
	
--
-- Create model FinCode
--
CREATE TABLE "fin_code" (
	"code" varchar(2) NOT NULL PRIMARY KEY,
	"typeOf" varchar(10) NOT NULL,
	"description" varchar(50) NOT NULL);
	
--
-- Create model Product
--
CREATE TABLE "product" (
	"id" integer NOT NULL PRIMARY KEY,
	"name" varchar(15) NOT NULL,
	"description" varchar(30) NOT NULL,
	"size" varchar(18) NOT NULL,
	"color" varchar(6) NOT NULL,
	"quantity" integer NOT NULL,
	"unit_price" real NOT NULL);
	
--
-- Create model SalesOrder
--
CREATE TABLE "sales_order" (
	"id" integer NOT NULL PRIMARY KEY,
	"order_date" date NOT NULL,
	"region" varchar(7) NOT NULL,
	"cust_id_id" integer NOT NULL REFERENCES "customer" ("id") DEFERRABLE INITIALLY DEFERRED,
	"fin_code_id_id" varchar(2) NOT NULL REFERENCES "fin_code" ("code") DEFERRABLE INITIALLY DEFERRED,
	"sales_rep_id" integer NOT NULL REFERENCES "employee" ("emp_id") DEFERRABLE INITIALLY DEFERRED);
	
--
-- Create model SalesOrderItems
--
CREATE TABLE "sales_order_items" (
	"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"line_id" integer NOT NULL,
	"quantity" integer NOT NULL,
	"ship_date" date NOT NULL,
	"prod_id_id" integer NOT NULL REFERENCES "product" ("id") DEFERRABLE INITIALLY DEFERRED,
	"sale_order_id_id" integer NOT NULL REFERENCES "sales_order" ("id") DEFERRABLE INITIALLY DEFERRED);
	
--
-- Create model FinData
--
CREATE TABLE "fin_data" (
	"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"year" varchar(4) NOT NULL,
	"quarter" varchar(2) NOT NULL,
	"amount" real NOT NULL,
	"code_id" varchar(2) NOT NULL REFERENCES "fin_code" ("code") DEFERRABLE INITIALLY DEFERRED);
	
	
--
-- Create model Department
--
CREATE TABLE "department" (
	"dept_id" integer NOT NULL PRIMARY KEY,
	"dept_name" varchar(40) NOT NULL,
	"dept_head_id_id" integer NOT NULL REFERENCES "employee" ("emp_id") DEFERRABLE INITIALLY DEFERRED);
	
--
-- Create constraint sales_order_items_pk on model salesorderitems
--
CREATE TABLE "new__sales_order_items" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "line_id" integer NOT NULL, "quantity" integer NOT NULL, "ship_date" date NOT NULL, "prod_id_id" integer NOT NULL REFERENCES "product" ("id") DEFERRABLE INITIALLY DEFERRED, "sale_order_id_id" integer NOT NULL REFERENCES "sales_order" ("id") DEFERRABLE INITIALLY DEFERRED, CONSTRAINT "sales_order_items_pk" UNIQUE ("sale_order_id_id", "line_id"));
INSERT INTO "new__sales_order_items" ("id", "line_id", "quantity", "ship_date", "prod_id_id", "sale_order_id_id") SELECT "id", "line_id", "quantity", "ship_date", "prod_id_id", "sale_order_id_id" FROM "sales_order_items";
DROP TABLE "sales_order_items";
ALTER TABLE "new__sales_order_items" RENAME TO "sales_order_items";
CREATE INDEX "employee_dept_id_id_12bb5a1f" ON "employee" ("dept_id_id");
CREATE INDEX "sales_order_cust_id_id_9faf5ef9" ON "sales_order" ("cust_id_id");
CREATE INDEX "sales_order_fin_code_id_id_a4730f54" ON "sales_order" ("fin_code_id_id");
CREATE INDEX "sales_order_sales_rep_id_e8d38d2a" ON "sales_order" ("sales_rep_id");
CREATE INDEX "fin_data_code_id_b0e37346" ON "fin_data" ("code_id");
CREATE INDEX "department_dept_head_id_id_060f581c" ON "department" ("dept_head_id_id");
CREATE INDEX "sales_order_items_prod_id_id_58e476b2" ON "sales_order_items" ("prod_id_id");
CREATE INDEX "sales_order_items_sale_order_id_id_29f0cecc" ON "sales_order_items" ("sale_order_id_id");

--
-- Create constraint fin_data_pk on model findata
--
CREATE TABLE "new__fin_data" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "year" varchar(4) NOT NULL, "quarter" varchar(2) NOT NULL, "amount" real NOT NULL, "code_id" varchar(2) NOT NULL REFERENCES "fin_code" ("code") DEFERRABLE INITIALLY DEFERRED, CONSTRAINT "fin_data_pk" UNIQUE ("year", "quarter", "code_id"));
INSERT INTO "new__fin_data" ("id", "year", "quarter", "amount", "code_id") SELECT "id", "year", "quarter", "amount", "code_id" FROM "fin_data";
DROP TABLE "fin_data";
ALTER TABLE "new__fin_data" RENAME TO "fin_data";
CREATE INDEX "fin_data_code_id_b0e37346" ON "fin_data" ("code_id");
COMMIT;
