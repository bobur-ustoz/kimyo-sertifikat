-- STEP 2: run this only AFTER the site code that reads topic_example_analogs is deployed.
-- It removes the publicly readable copies of the analogs.
alter table topic_examples drop column if exists analog_savol;
alter table topic_examples drop column if exists analog_yechim;
alter table topic_examples drop column if exists analog_javob;
