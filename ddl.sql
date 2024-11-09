CREATE SCHEMA IF NOT EXISTS app_main AUTHORIZATION postgres;

CREATE TABLE IF NOT EXISTS app_main.prescription_attributes (
	id bigserial primary key,
	prescription_id character varying(256),
	prescription_date character varying(50),
	doctor_name character varying(256),
	doctor_address text,
	diagnoses text
);

CREATE TABLE IF NOT EXISTS app_main.prescription_schedule (
	id bigserial primary key,
	prescription_id character varying(256),
	medicine_name text,
	frequency text
);

CREATE TABLE IF NOT EXISTS app_main.document_parsing (
	document_id character varying(256) primary key,
	raw_data text,
	ocr_cost numeric,
	json_dump text,
	json_cost numeric
);

CREATE TABLE IF NOT EXISTS app_main.report_attributes (
	id bigserial primary key,
	report_id character varying(256),
	patient_name character varying(256),
	patient_age numeric,
	report_date character varying(50),
	sample_collection_date character varying(50),
	lab_name text
);

CREATE TABLE IF NOT EXISTS app_main.report_tests (
	id bigserial primary key,
	report_id character varying(256),
	test_name text,
	test_value text,
	unit text,
	bio_ref_interval text
);