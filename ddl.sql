CREATE TABLE prescription_attributes (
	id bigserial primary key,
	prescription_id character varying(256),
	prescription_date character varying(50),
	doctor_name character varying(256),
	doctor_address text,
	diagnoses text
);

CREATE TABLE prescription_schedule (
	id bigserial primary key,
	prescription_id character varying(256),
	medicine_name text,
	frequency text
);