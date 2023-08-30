create table labevents_transform (
  id serial not null,
  row_key varchar(255) not null unique,
  subject_id integer not null,
  hadm_id integer,
  charttime timestamp not null,
  item_values jsonb not null,
  primary key (id)
);
CREATE INDEX labevents_transform_charttime_idx ON labevents_transform (charttime);