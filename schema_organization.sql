USE factory;

SELECT * FROM finance;

/* Formatting*/

ALTER TABLE calendar
DROP COLUMN `index`;

ALTER TABLE week_proportion
DROP COLUMN `index`;

ALTER TABLE human_resources
RENAME COLUMN `index` to hr_id;

ALTER TABLE productivity
RENAME COLUMN `index` to hr_id;

ALTER TABLE production
RENAME COLUMN `index` to hr_id;

ALTER TABLE finance
RENAME COLUMN `index` to hr_id;

/* Setting Primary Keys */

ALTER TABLE calendar
ADD CONSTRAINT PK_calendar PRIMARY KEY (calendar_id);

ALTER TABLE week_proportion
ADD CONSTRAINT PK_week_proportion PRIMARY KEY (week_id);

ALTER TABLE productivity
ADD productivity_id SERIAL;
ALTER TABLE productivity
ADD CONSTRAINT PK_productivity PRIMARY KEY (productivity_id);

ALTER TABLE production
ADD production_id SERIAL;
ALTER TABLE production
ADD CONSTRAINT PK_production PRIMARY KEY (production_id);

ALTER TABLE finance
ADD finance_id SERIAL;
ALTER TABLE finance
ADD CONSTRAINT PK_finance PRIMARY KEY (finance_id);

ALTER TABLE human_resources
ADD CONSTRAINT PK_human_resources PRIMARY KEY (`index`);


/* Setting the Foreign Keys */

ALTER TABLE productivity
ADD CONSTRAINT PK_productivity
FOREIGN KEY (hr_id) REFERENCES human_resources(hr_id);

ALTER TABLE production
ADD CONSTRAINT PK_production
FOREIGN KEY (hr_id) REFERENCES human_resources(hr_id);

ALTER TABLE finance
ADD CONSTRAINT FK_finance 
FOREIGN KEY (hr_id) REFERENCES human_resources(hr_id);

ALTER TABLE finance
ADD CONSTRAINT FK_finance1
FOREIGN KEY (calendar_id) REFERENCES calendar(calendar_id);

ALTER TABLE human_resources
ADD CONSTRAINT FK_human_resources
FOREIGN KEY (calendar_id) REFERENCES calendar(calendar_id);

ALTER TABLE production
ADD CONSTRAINT FK_production
FOREIGN KEY (week_id) REFERENCES week_proportion(week_id);

ALTER TABLE calendar
ADD CONSTRAINT FK_calendar
FOREIGN KEY (week_id) REFERENCES week_proportion(week_id);